#!/usr/bin/env python3
"""Whole-document audit: every body line reaches the paragraph that owns it.

The slicer's failure modes are silent. A vertical cutoff that clips a line, a
span boundary off by a page, a merge rule that swallows a heading - none raise
an error. They leave a paragraph file quietly missing text, and a note written
from that file reads as authoritative while being wrong.

This resolves ownership independently of the slicer. Every body line on a page
belongs to the last heading banner at or above it, in reading order. The audit
then checks that the line is actually present in that paragraph's file.

    lost     the owning paragraph's file does not contain the line
    orphan   a line before the first banner (front matter) - expected, reported
             only as a count

Running header and footer lines are excluded, as are the banner lines
themselves, which the slicer stores in the file header rather than the body.

Usage:
    python3 scripts/audit_coverage.py [--show N]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:
    sys.exit("pymupdf is required: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "source" / "CS-E_Amendment_8.pdf"
PARAS = ROOT / "work" / "paragraphs"

WHITE = 16777215
HEADING_MIN_SIZE = 14.0
RUNNING = re.compile(
    r"^(?:CS-E\s*[—-]\s*Amendment\s*\d+"
    # Case-sensitive, and the dash is mandatory: every real banner is
    # "SUBPART A - GENERAL". Matching "subpart C or E" case-insensitively
    # ate a body line of CS-E 80(b), and it did so in both this filter and
    # the audit that is meant to catch exactly that loss.
    r"|(?-i:SUBPART)\s+[A-F]\s*[–—-]"
    r"|Annex to ED Decision"
    r"|Page\s+\d+\s+of\s+\d+)",
    re.IGNORECASE,
)
ID = r"(?:AMC to CS-E|CS-E|AMC E|GM E)\s*\d{1,4}(?:\([^)\s]{1,6}\))*"
HEAD_ID = re.compile(rf"^({ID})\s*(.*)$")


def norm(text: str) -> str:
    return " ".join(text.split())


def slug(pid: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", pid).strip("_")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--show", type=int, default=15)
    args = ap.parse_args()

    doc = pymupdf.open(PDF)
    banners: list[tuple[int, float, str]] = []
    lines: list[tuple[int, float, str]] = []

    for i in range(len(doc)):
        raw: list[tuple[float, str, float, int]] = []
        for block in doc[i].get_text("dict")["blocks"]:
            if block["type"] != 0:
                continue
            for line in block["lines"]:
                text = norm(" ".join(s["text"] for s in line["spans"]))
                if not text:
                    continue
                span = line["spans"][0]
                raw.append((round(line["bbox"][1], 1), text,
                            round(span["size"], 1), span["color"]))
        raw.sort()
        prev_y = None
        for y, text, size, color in raw:
            if size >= HEADING_MIN_SIZE and color == WHITE:
                if prev_y is not None and (y - prev_y) < 25 and banners and banners[-1][0] == i + 1:
                    banners[-1] = (i + 1, banners[-1][1], f"{banners[-1][2]} {text}")
                else:
                    banners.append((i + 1, y, text))
                prev_y = y
                continue
            prev_y = None
            if not RUNNING.match(text):
                lines.append((i + 1, y, text))

    # Cache each paragraph's body text, keyed by its id.
    body: dict[str, str] = {}
    for pno, y, heading in banners:
        m = HEAD_ID.match(heading)
        pid = norm(m.group(1)) if m else heading.split("  ")[0].strip()
        f = PARAS / f"{slug(pid)}.txt"
        if f.exists():
            body[pid] = norm(" ".join(
                ln for ln in f.read_text(encoding="utf-8").splitlines()
                if not ln.startswith("#")))

    def owner(page: int, y: float) -> str | None:
        found = None
        for bp, by, heading in banners:
            if bp < page or (bp == page and by < y):
                found = heading
            else:
                break
        if found is None:
            return None
        m = HEAD_ID.match(found)
        return norm(m.group(1)) if m else found.split("  ")[0].strip()

    lost: list[tuple[int, str, str]] = []
    orphans = 0
    checked = 0
    for page, y, text in lines:
        pid = owner(page, y)
        if pid is None:
            orphans += 1
            continue
        checked += 1
        if pid not in body:
            lost.append((page, pid, text))
        elif norm(text) not in body[pid]:
            lost.append((page, pid, text))

    print(f"body lines total            : {len(lines):,}")
    print(f"  before the first banner   : {orphans:,}  (front matter, expected)")
    print(f"  owned by a paragraph      : {checked:,}")
    print(f"banners found               : {len(banners)}")
    print(f"\nLOST — owner's file lacks the line: {len(lost)}")
    if lost:
        print(f"\nfirst {min(args.show, len(lost))}:")
        for page, pid, text in lost[:args.show]:
            print(f"  p{page:<4} {pid:<22} {text[:80]!r}")
    return 1 if lost else 0


if __name__ == "__main__":
    sys.exit(main())
