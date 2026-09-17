#!/usr/bin/env python3
"""Phase 2a — slice CS-E Amendment 8 into one text file per paragraph.

work/text/page_NNN.txt is page-shaped; classification and drafting need
paragraph-shaped text. This walks the heading banners found in Phase 1 and
writes everything between one banner and the next to work/paragraphs/<slug>.txt,
dropping the running header and footer.

Usage:
    python3 scripts/paragraph_text.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:
    sys.exit("pymupdf is required: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "source" / "CS-E_Amendment_8.pdf"
SIDECAR = ROOT / "work" / "pages.json"
OUT = ROOT / "work" / "paragraphs"

WHITE = 16777215
HEADING_MIN_SIZE = 14.0
HEADER_Y = 95.0    # running header sits above this
FOOTER_Y = 770.0   # running footer below this
ID = r"(?:AMC to CS-E|CS-E|AMC E|GM E)\s*\d{1,4}(?:\([^)\s]{1,6}\))*"
HEAD_ID = re.compile(rf"^({ID})\s*(.*)$")


def slug(pid: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", pid).strip("_")


def banner_positions(page: pymupdf.Page) -> list[tuple[float, str]]:
    out = []
    for block in page.get_text("dict")["blocks"]:
        if block["type"] != 0:
            continue
        for line in block["lines"]:
            text = " ".join(" ".join(s["text"] for s in line["spans"]).split())
            if not text:
                continue
            span = line["spans"][0]
            if round(span["size"], 1) >= HEADING_MIN_SIZE and span["color"] == WHITE:
                out.append((round(line["bbox"][1], 1), text))
    out.sort()
    merged: list[tuple[float, str]] = []
    prev_y = None
    for y, text in out:
        # Compare against the PREVIOUS LINE, not the group's first line: a banner
        # wrapped over three lines spans more than the 25 pt gap from its top.
        if prev_y is not None and (y - prev_y) < 25:
            merged[-1] = (merged[-1][0], f"{merged[-1][1]} {text}")
        else:
            merged.append((y, text))
        prev_y = y
    return merged


def body_lines(page: pymupdf.Page, y_from: float, y_to: float) -> list[str]:
    """Text lines on one page between two vertical bounds, header/footer removed."""
    lines: list[tuple[float, str]] = []
    for block in page.get_text("dict")["blocks"]:
        if block["type"] != 0:
            continue
        for line in block["lines"]:
            y = round(line["bbox"][1], 1)
            if y < max(y_from, HEADER_Y) or y >= min(y_to, FOOTER_Y):
                continue
            text = " ".join(" ".join(s["text"] for s in line["spans"]).split())
            if text:
                lines.append((y, text))
    return [t for _, t in sorted(lines)]


def main() -> int:
    if not SIDECAR.exists():
        sys.exit("run scripts/extract_text.py first")
    OUT.mkdir(parents=True, exist_ok=True)
    for stale in OUT.glob("*.txt"):
        stale.unlink()

    doc = pymupdf.open(PDF)
    pages = {p["page"]: p for p in json.loads(SIDECAR.read_text())}

    # Global ordered banner list: (page, y, heading text).
    banners: list[tuple[int, float, str]] = []
    for i in range(len(doc)):
        for y, text in banner_positions(doc[i]):
            banners.append((i + 1, y, text))

    written = 0
    for idx, (pno, y, heading) in enumerate(banners):
        if idx + 1 < len(banners):
            end_page, end_y = banners[idx + 1][0], banners[idx + 1][1]
        else:
            end_page, end_y = len(doc), 10_000.0

        chunks: list[str] = []
        for n in range(pno, end_page + 1):
            page = doc[n - 1]
            lo = y + 1 if n == pno else 0.0
            hi = end_y if n == end_page else 10_000.0
            chunks += body_lines(page, lo, hi)

        m = HEAD_ID.match(heading)
        pid = " ".join(m.group(1).split()) if m else heading.split("  ")[0].strip()
        name = f"{slug(pid)}.txt"
        header = (
            f"# {heading}\n"
            f"# id: {pid}\n"
            f"# subpart: {pages[pno]['subpart']}\n"
            f"# pages: {pno}-{end_page}\n"
            f"# source: CS-E_Amendment_8.pdf\n\n"
        )
        (OUT / name).write_text(header + "\n".join(chunks) + "\n", encoding="utf-8")
        written += 1

    print(f"wrote {written} paragraph files to {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
