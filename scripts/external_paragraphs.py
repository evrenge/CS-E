"""Slice the external documents into one file per cited paragraph.

`work/paragraphs/` does this for CS-E. Once a note may carry an imported
obligation, the same discipline has to reach the documents it is imported from,
for one reason: `lint_vault.py` checks a quoted passage word-for-word against a
haystack. Without these files the haystack stops at CS-E, and every quotation
from CS-29 or Part 21 would either fail the check or force it to be switched off
for external material — which is the same as not checking it.

So this is not a convenience. It is what makes accuracy rule 4 hold for the
imported half of a note.

WHAT IS EXTRACTED

Only the points the vault actually cites, listed in `WANTED`. These documents
run to 1,041 pages; slicing all of them would bury the ones that matter and
make the verbatim check slower for no gain. Adding a point means adding a line
to `WANTED`, not changing code.

HOW A SLICE IS FOUND

EASA sets a paragraph heading on its own line: "CS 29.927 Additional tests",
"GM1 21.A.3B(b) Failures, malfunctions and defects". The slice runs from that
line to the next heading of any rank. `HEADING` recognises the four families in
play -- CS-27/29 points, AMC and GM to them, Part 21 points in both Annex I and
Annex Ib, and CS-34.

Page furniture is dropped first. Every page in these files repeats the document
title, the ED Decision, the subpart and a page number, and those lines land in
the middle of a paragraph when the text is concatenated. Leaving them in would
put "Annex to ED Decision 2024/009/R" inside a quotation and break the check it
exists to serve.

Annex Ib (Part 21 Light) is skipped for Part 21 points. Its paragraphs are
numbered 21L.B.45 against Annex I's 21.B.85 and cover a different certification
route; a search that does not exclude it returns the wrong text for the right
number.
"""
from __future__ import annotations

import pathlib
import re
import sys

try:
    import pymupdf
except ImportError:  # pragma: no cover
    sys.exit("pymupdf is required: pip install -r requirements.txt")

ROOT = pathlib.Path(__file__).resolve().parent.parent
EXT = ROOT / "source" / "external"
OUT = ROOT / "work" / "external"

# (paragraph id, file, human title). The id is what a note cites inside [ext ...].
WANTED: list[tuple[str, str, str]] = [
    # --- CS-27 / CS-29, the rotorcraft codes
    ("CS 27.45", "CS-27_Amendment_10.pdf", "General (performance)"),
    ("CS 29.45", "CS-29_Amendment_12.pdf", "General (performance)"),
    ("CS 27.927", "CS-27_Amendment_10.pdf", "Additional tests"),
    ("CS 29.927", "CS-29_Amendment_12.pdf", "Additional tests"),
    ("CS 27.1093", "CS-27_Amendment_10.pdf", "Induction system icing protection"),
    ("CS 29.1093", "CS-29_Amendment_12.pdf", "Induction system icing protection"),
    ("CS 27.1305", "CS-27_Amendment_10.pdf", "Powerplant instruments"),
    ("CS 29.1305", "CS-29_Amendment_12.pdf", "Powerplant instruments"),
    ("CS 29.917", "CS-29_Amendment_12.pdf", "Rotor drive system design"),
    ("CS 27.917", "CS-27_Amendment_10.pdf", "Rotor drive system design"),
    ("CS 29.923", "CS-29_Amendment_12.pdf", "Rotor drive system and control mechanism tests"),
    ("CS 27.923", "CS-27_Amendment_10.pdf", "Rotor drive system and control mechanism tests"),
    ("AMC2 29.917", "CS-29_Amendment_12.pdf", "Rotor drive system design — lubrication systems"),
    # --- CS-34, repealed, kept because CS-E Amendment 8 still cites it
    ("CS 34.1", "CS-34_Amendment_4_repealed.pdf", "Fuel venting"),
    ("CS 34.2", "CS-34_Amendment_4_repealed.pdf", "Aircraft engine emissions"),
    ("GM1 34.1", "CS-34_Amendment_4_repealed.pdf", "Fuel venting"),
    ("GM1 34.2", "CS-34_Amendment_4_repealed.pdf", "Aircraft engine emissions"),
    # --- Part 21, Annex I only
    ("21.A.20", "Part-21_EAR_Reg-748-2012_Nov-2025.pdf", "Compliance with the type-certification basis"),
    ("21.A.21", "Part-21_EAR_Reg-748-2012_Nov-2025.pdf", "Requirements for the issue of a type certificate"),
    # 21.A.61 is deliberately absent. It does not exist in Part 21 any more:
    # the numbering runs 21.A.62 then 21.A.65, and an exact search for
    # "21.A.61" not followed by a digit returns nothing. A substring search
    # appears to find it only because 21.A.601 to 21.A.615 exist.
    ("21.A.801", "Part-21_EAR_Reg-748-2012_Nov-2025.pdf", "Identification of products"),
    ("21.A.805", "Part-21_EAR_Reg-748-2012_Nov-2025.pdf", "Identification of critical parts"),
    ("21.B.85", "Part-21_EAR_Reg-748-2012_Nov-2025.pdf", "Applicable environmental protection requirements"),
    ("GM1 21.A.3B(b)", "Part-21_EAR_Reg-748-2012_Nov-2025.pdf", "Failures, malfunctions and defects"),
    ("GM 21.A.20(d)", "Part-21_EAR_Reg-748-2012_Nov-2025.pdf", "Final statement"),
    ("GM1 21.A.805", "Part-21_EAR_Reg-748-2012_Nov-2025.pdf", "Identification of critical parts"),
    ("GM1 21.B.85(a)", "Part-21_EAR_Reg-748-2012_Nov-2025.pdf", "Content of ICAO Annex 16"),
    ("GM2 21.B.85", "Part-21_EAR_Reg-748-2012_Nov-2025.pdf", "Applicable environmental protection requirements"),
]

# A heading of any rank, in any of the four families.
HEADING = re.compile(
    r"^[ \t]*(?:"
    r"(?:AMC|GM)\s*\d*\s+(?:No\s+\d+\s+to\s+)?(?:CS\s+)?\d{2,3}[A-Z]?\.\d+[A-Za-z0-9().]*"
    r"|CS\s+\d{2,3}[A-Z]?\.\d+[A-Za-z0-9().]*"
    r"|(?:AMC|GM)\s*\d*\s+21L?\.[AB]\.\d+[A-Za-z0-9().]*"
    r"|21L?\.[AB]\.\d+[A-Za-z0-9().]*"
    # A heading is followed by its title, which starts with a capital. A
    # justified PDF breaks lines anywhere, so "...point 21.A.21 of Annex I"
    # puts a paragraph number at the start of a line mid-sentence; the
    # lower-case continuation is what tells the two apart.
    r")[ \t]+[A-Z(]", re.M)

# Repeated on every page of these documents, and meaningless inside a slice.
FURNITURE = re.compile(
    r"^\s*(?:"
    r"CS-\d\d Amendment \d+|CS-34 Amendment \d+"
    r"|Annex I{1,2}? to ED Decision[^\n]*|Annex to ED Decision[^\n]*"
    r"|Page \d+ of \d+[^\n]*|Powered by EASA eRules[^\n]*"
    r"|Easy Access Rules for[^\n]*|Subpart [A-Z] —[^\n]*|Subpart [A-Z] -[^\n]*"
    r"|Annex I[b]? SECTION [AB][^\n]*|SECTION [AB] —[^\n]*|SECTION [AB] -[^\n]*"
    r"|Table of contents|TE\.RPRO[^\n]*"
    r")\s*$", re.M)


def slug(pid: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", pid).strip("_")


PAGE_NO = re.compile(r"^\s*Page \d+ of \d+")


def body(path: pathlib.Path) -> str:
    """Document text with the page header block removed, Annex Ib dropped.

    Every page opens with a header block and closes it with a "Page N of M"
    line. Removing that block whole is the only reliable way: the Easy Access
    Rules header wraps over six lines, so matching furniture line by line
    leaves fragments such as "and Environmental Protection (Regulation" sitting
    inside the next paragraph, where they would end up inside a quotation.
    """
    doc = pymupdf.open(str(path))
    pages = []
    for page in doc:
        text = page.get_text()
        # Annex Ib is Part 21 Light: different numbering, different route.
        if "Annex Ib" in text[:400]:
            continue
        lines = text.split("\n")
        for i, line in enumerate(lines[:12]):
            if PAGE_NO.match(line):
                lines = lines[i + 1:]
                break
        pages.append(FURNITURE.sub("", "\n".join(lines)))
    return "\n".join(pages)


# In the Easy Access Rules the line under a real heading gives its legal
# attribution. Nothing else in the document looks like this, so it is the
# cleanest way to tell a heading from a citation of the same number inside a
# sentence -- "GM1 21.A.3B(b) 'Failures ...' could be used to assist" starts a
# line and is capitalised, so neither of those tests catches it.
ATTRIB = re.compile(r"^[ \t]*(?:Regulation \((?:EU|EC)\)|ED Decision|\(Reserved\))")


def extract(pid: str, text: str) -> str | None:
    """The slice from this paragraph's heading to the next heading."""
    candidates = []
    for m in re.finditer(rf"^[ \t]*{re.escape(pid)}[ \t]+\S", text, re.M):
        # A table-of-contents entry carries dot leaders and a page number. A
        # long one wraps, so the leaders can be on the following line.
        window = text[m.start():m.start() + 320].split("\n")[:3]
        if any(re.search(r"\.{4,}\s*\d+\s*$", ln) for ln in window):
            continue
        following = [ln for ln in window[1:] if ln.strip()]
        candidates.append((bool(following and ATTRIB.match(following[0])), m.start()))
    if not candidates:
        return None
    # Prefer a candidate with an attribution line under it; else the first.
    attributed = [pos for ok, pos in candidates if ok]
    start = attributed[0] if attributed else candidates[0][1]
    rest = text[start:]
    first_nl = rest.find("\n")
    nxt = HEADING.search(rest, first_nl if first_nl > 0 else 1)
    return (rest[:nxt.start()] if nxt else rest).strip()


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    cache: dict[str, str] = {}
    written = missing = 0
    for pid, fname, title in WANTED:
        path = EXT / fname
        if not path.exists():
            print(f"  {pid:18s} SOURCE MISSING: {fname}")
            missing += 1
            continue
        if fname not in cache:
            cache[fname] = body(path)
        slice_ = extract(pid, cache[fname])
        if slice_ is None:
            print(f"  {pid:18s} NOT FOUND in {fname}")
            missing += 1
            continue
        out = OUT / f"{slug(pid)}.txt"
        out.write_text(
            f"# {pid} {title}\n# id: {pid}\n# source: external/{fname}\n"
            f"# chars: {len(slice_)}\n\n{slice_}\n", encoding="utf-8")
        written += 1
        print(f"  {pid:18s} {len(slice_):6,d} chars -> {out.name}")
    print(f"\n{written} paragraph(s) written to work/external/, {missing} missing")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
