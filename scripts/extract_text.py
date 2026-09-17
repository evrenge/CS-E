#!/usr/bin/env python3
"""Phase 1a — extract CS-E Amendment 8 page by page.

Writes work/text/page_NNN.txt (one file per PDF page, 1-based, zero-padded to 3)
and work/pages.json, a per-page sidecar carrying what the index builder and the
extraction-health report need:

    page, subpart, chars, words, images, tables, captions, headings

`subpart` comes from the running page header ("... SUBPART E - TURBINE ENGINES
..."), which every body page carries, not from the section title page — so a
paragraph that spans a subpart boundary still resolves per page.

Usage:
    python3 scripts/extract_text.py
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
OUT_DIR = ROOT / "work" / "text"
SIDECAR = ROOT / "work" / "pages.json"

WHITE = 16777215          # banner heading text colour
HEADING_MIN_SIZE = 14.0   # paragraph banners are 16 pt; subpart titles 20 pt
SUBPART_RE = re.compile(r"SUBPART\s+([A-F])\b")
CAPTION_RE = re.compile(r"^\s*(Figure|Table)\s+[0-9IVX]+[.:]?", re.IGNORECASE | re.MULTILINE)
# Front matter: cover, table of contents, preamble. Body starts at the first
# subpart title page.
FRONT_MATTER_LAST = 14


def line_text(line: dict) -> str:
    return " ".join(" ".join(s["text"] for s in line["spans"]).split())


def page_headings(page: pymupdf.Page) -> list[str]:
    """Merge consecutive white banner lines into whole headings.

    EASA wraps a long banner over two lines; the continuation carries no
    'CS-E'/'AMC' prefix, so joining by vertical adjacency is what recovers
    e.g. 'AMC E 20(f) Power Assurance Data for Engines with One or More OEI
    Power Ratings'.
    """
    banners: list[tuple[float, str]] = []
    for block in page.get_text("dict")["blocks"]:
        if block["type"] != 0:
            continue
        for line in block["lines"]:
            text = line_text(line)
            if not text:
                continue
            span = line["spans"][0]
            if round(span["size"], 1) >= HEADING_MIN_SIZE and span["color"] == WHITE:
                banners.append((round(line["bbox"][1], 1), text))

    banners.sort()
    merged: list[str] = []
    prev_y = None
    for y, text in banners:
        if prev_y is not None and (y - prev_y) < 25:
            merged[-1] = f"{merged[-1]} {text}"
        else:
            merged.append(text)
        prev_y = y
    return merged


def main() -> int:
    if not PDF.exists():
        sys.exit(f"missing {PDF}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    doc = pymupdf.open(PDF)
    pages: list[dict] = []
    current_subpart = ""

    for i, page in enumerate(doc):
        pno = i + 1
        text = page.get_text("text")
        (OUT_DIR / f"page_{pno:03d}.txt").write_text(text, encoding="utf-8")

        # Running header gives the subpart; carry the last seen one forward for
        # pages that omit it (subpart title pages, some full-width tables).
        header = " ".join(text[:400].split())
        match = SUBPART_RE.search(header)
        if match:
            current_subpart = match.group(1)
        subpart = "" if pno <= FRONT_MATTER_LAST else current_subpart

        try:
            tables = len(page.find_tables().tables)
        except Exception:
            tables = 0

        pages.append({
            "page": pno,
            "subpart": subpart,
            "chars": len(text),
            "words": len(text.split()),
            "images": len(page.get_images(full=True)),
            "tables": tables,
            "captions": sorted({" ".join(m.group(0).split()) for m in CAPTION_RE.finditer(text)}),
            "headings": page_headings(page),
        })
        if pno % 40 == 0:
            print(f"  ... {pno}/{len(doc)} pages")

    SIDECAR.write_text(json.dumps(pages, indent=1), encoding="utf-8")
    total = sum(p["chars"] for p in pages)
    print(f"wrote {len(pages)} page files to {OUT_DIR.relative_to(ROOT)}  ({total:,} chars)")
    print(f"wrote {SIDECAR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
