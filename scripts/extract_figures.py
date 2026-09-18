#!/usr/bin/env python3
"""Crop each paragraph's own figures and tables to vault/figures/.

Accuracy rule 6 exists because figure content is absent from the text layer:
page 164's flowchart labels are vector graphics and extract to nothing. Writing a
prose description of such a figure produces a claim that cannot be checked
against the source. Embedding EASA's own image removes that risk entirely.

Ownership is positional, from work/spans.json: a figure sitting above a
paragraph's banner belongs to the paragraph above it, not to this one.

Output is vault/figures/<id>_p<page>.png, embedded in a note as
![[<id>_p<page>.png]].

Usage:
    python3 scripts/extract_figures.py [--dpi 200] [--only "CS-E 800"]
"""

from __future__ import annotations

import argparse
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
SPANS = ROOT / "work" / "spans.json"
OUT = ROOT / "vault" / "figures"
sys.path.insert(0, str(ROOT / "scripts"))
from classification import CLASSIFICATION  # noqa: E402

MARGIN = 12.0       # points of whitespace kept around the cropped region
MIN_AREA = 4000.0   # ignore rules, borders and other decoration


def slug(pid: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", pid).strip("_")


def logo_xrefs(doc: pymupdf.Document) -> set[int]:
    from collections import Counter
    counts: Counter[int] = Counter()
    for i in range(len(doc)):
        for img in doc[i].get_images(full=True):
            counts[img[0]] += 1
    return {x for x, n in counts.items() if n > len(doc) * 0.8}


def regions(page: pymupdf.Page, logos: set[int]) -> list[pymupdf.Rect]:
    """Figure and table bounding boxes on one page, merged where they overlap."""
    boxes: list[pymupdf.Rect] = []
    for info in page.get_image_info(xrefs=True):
        if info.get("xref") in logos:
            continue
        boxes.append(pymupdf.Rect(info["bbox"]))
    try:
        for table in page.find_tables().tables:
            boxes.append(pymupdf.Rect(table.bbox))
    except Exception:
        pass
    boxes = [b for b in boxes if b.get_area() >= MIN_AREA]

    merged: list[pymupdf.Rect] = []
    for box in sorted(boxes, key=lambda r: (r.y0, r.x0)):
        for i, done in enumerate(merged):
            if not (box & done).is_empty or abs(box.y0 - done.y1) < 20:
                merged[i] = done | box
                break
        else:
            merged.append(pymupdf.Rect(box))
    return merged


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dpi", type=int, default=200)
    ap.add_argument("--only", help="limit to one paragraph id")
    args = ap.parse_args()

    verdict = {i: s for i, s, _ in CLASSIFICATION}
    spans = json.loads(SPANS.read_text())
    doc = pymupdf.open(PDF)
    logos = logo_xrefs(doc)
    OUT.mkdir(parents=True, exist_ok=True)
    for stale in OUT.glob("*.png"):
        stale.unlink()

    zoom = args.dpi / 72.0
    written: dict[str, list[str]] = {}

    for span in spans:
        pid = span["id"]
        if verdict.get(pid) != "APPLIES":
            continue
        if args.only and pid != args.only:
            continue
        for pno in span.get("figure_pages", []):
            page = doc[pno - 1]
            for n, rect in enumerate(regions(page, logos), 1):
                clip = pymupdf.Rect(rect) + (-MARGIN, -MARGIN, MARGIN, MARGIN)
                clip &= page.rect
                if clip.is_empty:
                    continue
                suffix = "" if n == 1 else f"_{n}"
                name = f"{slug(pid)}_p{pno}{suffix}.png"
                page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom),
                                clip=clip).save(OUT / name)
                written.setdefault(pid, []).append(name)

    total = sum(len(v) for v in written.values())
    print(f"wrote {total} image(s) for {len(written)} paragraph(s) "
          f"to {OUT.relative_to(ROOT)}\n")
    for pid, names in written.items():
        print(f"  {pid:<24} {len(names):>2}  {', '.join(names[:3])}"
              + (" ..." if len(names) > 3 else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
