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
    # A banner too long for one line wraps, and the tail carries no "SUBPART"
    # to match on. These five are every wrapped tail in the document; none of
    # them ever occurs as body prose. Without them, 211 header fragments are
    # injected into paragraph bodies -- "AND CONSTRUCTION" lands twice inside
    # CS-E 510(a). The Subpart F banner wraps at two different points
    # depending on the page, so both of its tails are listed.
    r"|(?-i:SUBSTANTIATION|AND CONSTRUCTION"
    r"|ENVIRONMENTAL AND OPERATIONAL|AND OPERATIONAL DESIGN REQUIREMENTS"
    r"|DESIGN REQUIREMENTS)\s*$"
    r"|Annex to ED Decision"
    r"|Page\s+\d+\s+of\s+\d+)",
    re.IGNORECASE,
)
ID = r"(?:AMC to CS-E|CS-E|AMC E|GM E)\s*\d{1,4}(?:\([^)\s]{1,6}\))*"
HEAD_ID = re.compile(rf"^({ID})\s*(.*)$")


APPENDIX = re.compile(r"^(Appendix\s+[A-Z])\b")


def paragraph_id(heading: str, match) -> str:
    """The id of a paragraph, from its banner.

    A CS-E or AMC banner yields its number. An appendix banner does not match
    that pattern, and falling back to the whole heading gives an id 77
    characters long -- "Appendix A Certification Standard Atmospheric
    Concentrations of Rain and Hail" -- which then becomes the note filename and
    the prefix of every figure crop. classification.py already calls it
    "Appendix A", so the banner is cut to the same thing.
    """
    if match:
        return " ".join(match.group(1).split())
    m = APPENDIX.match(heading.strip())
    if m:
        return m.group(1)
    return heading.split("  ")[0].strip()


def slug(pid: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", pid).strip("_")


def banner_positions(page: pymupdf.Page) -> list[tuple[float, float, str]]:
    """(top y, bottom y, text) per banner on the page.

    Both y values matter and they are not interchangeable. The top orders the
    banner against the previous paragraph and fixes where that paragraph ends.
    The bottom is where this paragraph's body starts: slicing from the top
    leaves a wrapped banner's own tail sitting in the body, which put
    "Components" at the head of AMC E 70 and "OEI Power Ratings" at the head of
    AMC E 20(f).
    """
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
    merged: list[tuple[float, float, str]] = []
    prev_y = None
    for y, text in out:
        # Compare against the PREVIOUS LINE, not the group's first line: a banner
        # wrapped over three lines spans more than the 25 pt gap from its top.
        if prev_y is not None and (y - prev_y) < 25:
            merged[-1] = (merged[-1][0], y, f"{merged[-1][2]} {text}")
        else:
            merged.append((y, y, text))
        prev_y = y
    return merged


def logo_xrefs(doc: pymupdf.Document) -> set[int]:
    """The EASA logo is one image repeated on every page. Find it by frequency."""
    counts: Counter[int] = Counter()
    for i in range(len(doc)):
        for img in doc[i].get_images(full=True):
            counts[img[0]] += 1
    return {x for x, n in counts.items() if n > len(doc) * 0.8}


def fraction_bars(page) -> list:
    """Horizontal rules that are division bars in a formula.

    A displayed formula survives extraction as nonsense: the text layer gives
    "Pc = Po x 1013.25" and "B" on separate lines, with nothing to say that B is
    the denominator. The division bar is the only reliable marker, and it is
    drawn, not written. It is short (a fraction is narrower than the column),
    thin (well under a point), and it sits in the body band, which separates it
    from the full-width header and footer rules.

    An underline meets every one of those tests, and the document underlines
    freely -- a cross-reference in AMC E 920, a run-in heading in AMC E 660.
    What separates the two is vertical position: an underline is drawn just
    below its own baseline and therefore falls INSIDE the bounding box of the
    text line it belongs to, while a division bar sits in the gap between the
    numerator line and the denominator line. Table cell borders are free of
    any line box too, and stay -- a table is a figure for cropping purposes.

    Returns the rule rectangles, not the formula: a caller that wants to crop
    must grow them to reach the numerator and denominator.
    """
    boxes = [line["bbox"]
             for block in page.get_text("dict")["blocks"] if block["type"] == 0
             for line in block["lines"]]
    out = []
    for drawing in page.get_drawings():
        r = drawing["rect"]
        if not (5 < r.width < 120 and r.height < 1.0 and 90 < r.y0 < 770):
            continue
        if any(y0 <= r.y0 <= y1 and x0 < r.x1 and r.x0 < x1
               for x0, y0, x1, y1 in boxes):
            continue                      # an underline, not a division bar
        out.append(r)
    return out


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
    for rect in fraction_bars(page):
        if y_from <= rect.y0 < y_to:
            return True
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
    lines: list[tuple[float, float, str]] = []
    for block in page.get_text("dict")["blocks"]:
        if block["type"] != 0:
            continue
        for line in block["lines"]:
            y = round(line["bbox"][1], 1)
            if y < y_from or y >= y_to:
                continue
            text = " ".join(" ".join(s["text"] for s in line["spans"]).split())
            if text and not RUNNING.match(text):
                # x breaks a tie on y, and it must: CS-E 520 lays "(c)", "(1)"
                # and the sub-point text on one line at y 360.3. Sorting the
                # tie on the text instead put "(1)" before "(c)", because "1"
                # sorts before "c".
                lines.append((y, round(line["bbox"][0], 1), text))
    return [t for _, _, t in sorted(lines)]


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
    banners: list[tuple[int, float, float, str]] = []
    for i in range(len(doc)):
        for y, y_last, text in banner_positions(doc[i]):
            banners.append((i + 1, y, y_last, text))

    written = 0
    spans: list[dict] = []
    for idx, (pno, y, y_last, heading) in enumerate(banners):
        if idx + 1 < len(banners):
            end_page, end_y = banners[idx + 1][0], banners[idx + 1][1]
        else:
            end_page, end_y = len(doc), 10_000.0

        chunks: list[str] = []
        for n in range(pno, end_page + 1):
            page = doc[n - 1]
            lo = y_last + 1 if n == pno else 0.0  # 0.0: header filtered by pattern
            hi = end_y if n == end_page else 10_000.0
            chunks += body_lines(page, lo, hi)

        m = HEAD_ID.match(heading)
        pid = paragraph_id(heading, m)
        name = f"{slug(pid)}.txt"
        # True last page: the last one this paragraph actually puts body text on.
        # Not next_banner_page - 1: a banner part-way down a page leaves the
        # previous paragraph occupying the top of that same page, as CS-E 40(e)-(h)
        # do on page 30 before the AMC E 40 banner. This is computed BEFORE the
        # file is written, because the file's own page header must carry the same
        # span as spans.json — a writer reads the header, a script reads the json,
        # and the two disagreeing is how a note ends up citing a page the
        # paragraph does not reach.
        last = pno
        fig_pages: list[int] = []
        for n in range(pno, end_page + 1):
            lo = y_last + 1 if n == pno else 0.0
            hi = end_y if n == end_page else 10_000.0
            if body_lines(doc[n - 1], lo, hi):
                last = n
            if figures_in(doc[n - 1], lo, hi, logos):
                fig_pages.append(n)
        header = (
            f"# {heading}\n"
            f"# id: {pid}\n"
            f"# subpart: {pages[pno]['subpart']}\n"
            f"# pages: {pno}-{last}\n"
            f"# source: CS-E_Amendment_8.pdf\n\n"
        )
        (OUT / name).write_text(header + "\n".join(chunks) + "\n", encoding="utf-8")
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
