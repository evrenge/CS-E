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
from collections import Counter
from pathlib import Path

try:
    import pymupdf
except ImportError:
    sys.exit("pymupdf is required: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "source" / "CS-E_Amendment_8.pdf"
SIDECAR = ROOT / "work" / "pages.json"
OUT = ROOT / "work" / "paragraphs"
SPANS = ROOT / "work" / "spans.json"

WHITE = 16777215
HEADING_MIN_SIZE = 14.0

# The running header and footer are removed by MATCHING THEM, not by vertical
# position. A y-window cannot work here: header lines run y 37.9-107.7 while body
# lines start at y 48.8, so the two ranges overlap. An earlier 95.0 cutoff
# silently dropped 294 body lines - among them the opening of CS-E 40(e), whose
# first line sits at y 92.7 on page 30.
CAPTION = re.compile(r"^\s*(Figure|Table)\s+[0-9IVX]+[.:]?", re.IGNORECASE)

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


def logo_xrefs(doc: pymupdf.Document) -> set[int]:
    """The EASA logo is one image repeated on every page. Find it by frequency."""
    counts: Counter[int] = Counter()
    for i in range(len(doc)):
        for img in doc[i].get_images(full=True):
            counts[img[0]] += 1
    return {x for x, n in counts.items() if n > len(doc) * 0.8}


def figures_in(page: pymupdf.Page, y_from: float, y_to: float,
               logos: set[int]) -> bool:
    """Does a real figure, table or caption fall inside this vertical band?

    Ownership is positional, not per-page. A boundary page carries the tail of
    one paragraph and the start of the next: page 29 holds AMC E 30's table at
    y 92-213 and CS-E 40's banner at y 302, so that table is not CS-E 40's.
    """
    for info in page.get_image_info(xrefs=True):
        if info.get("xref") in logos:
            continue
        if info["bbox"][3] > y_from and info["bbox"][1] < y_to:
            return True
    try:
        for table in page.find_tables().tables:
            if table.bbox[3] > y_from and table.bbox[1] < y_to:
                return True
    except Exception:
        pass
    for block in page.get_text("dict")["blocks"]:
        if block["type"] != 0:
            continue
        for line in block["lines"]:
            y = line["bbox"][1]
            if not (y_from <= y < y_to):
                continue
            text = " ".join(" ".join(sp["text"] for sp in line["spans"]).split())
            if CAPTION.match(text):
                return True
    return False


def body_lines(page: pymupdf.Page, y_from: float, y_to: float) -> list[str]:
    """Text lines on one page within the paragraph's vertical span.

    y_from / y_to bound the paragraph (below its own banner, above the next).
    The running header and footer are removed by pattern, never by position.
    """
    lines: list[tuple[float, str]] = []
    for block in page.get_text("dict")["blocks"]:
        if block["type"] != 0:
            continue
        for line in block["lines"]:
            y = round(line["bbox"][1], 1)
            if y < y_from or y >= y_to:
                continue
            text = " ".join(" ".join(s["text"] for s in line["spans"]).split())
            if text and not RUNNING.match(text):
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
    logos = logo_xrefs(doc)

    # Global ordered banner list: (page, y, heading text).
    banners: list[tuple[int, float, str]] = []
    for i in range(len(doc)):
        for y, text in banner_positions(doc[i]):
            banners.append((i + 1, y, text))

    written = 0
    spans: list[dict] = []
    for idx, (pno, y, heading) in enumerate(banners):
        if idx + 1 < len(banners):
            end_page, end_y = banners[idx + 1][0], banners[idx + 1][1]
        else:
            end_page, end_y = len(doc), 10_000.0

        chunks: list[str] = []
        for n in range(pno, end_page + 1):
            page = doc[n - 1]
            lo = y + 1 if n == pno else 0.0  # 0.0: header is filtered by pattern
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
        # True last page: the last one this paragraph actually puts body text on.
        # Not next_banner_page - 1: a banner part-way down a page leaves the
        # previous paragraph occupying the top of that same page, as CS-E 40(e)-(h)
        # do on page 30 before the AMC E 40 banner.
        last = pno
        fig_pages: list[int] = []
        for n in range(pno, end_page + 1):
            lo = y + 1 if n == pno else 0.0
            hi = end_y if n == end_page else 10_000.0
            if body_lines(doc[n - 1], lo, hi):
                last = n
            if figures_in(doc[n - 1], lo, hi, logos):
                fig_pages.append(n)
        spans.append({
            "id": pid, "title": heading[len(pid):].strip() if heading.startswith(pid) else heading,
            "subpart": pages[pno]["subpart"], "start_page": pno, "end_page": last,
            "has_figure_or_table": "yes" if fig_pages else "no",
            "figure_pages": [n for n in fig_pages if n <= last],
        })
        written += 1

    SPANS.write_text(json.dumps(spans, indent=1), encoding="utf-8")
    print(f"wrote {written} paragraph files to {OUT.relative_to(ROOT)}")
    print(f"wrote {SPANS.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
