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

Two documents are not laid out that way and get their own style.

AMC-20 is a compilation of whole AMCs, each headed "AMC 20-3B Certification of
Engines Equipped with Electronic Engine Control Systems", and each preceded by a
divider line carrying the bare number. The divider has to count as a boundary
too, or the slice ends with the next AMC's number hanging off it.

CS-Definitions is a glossary. Its entries open with the term in single quotes --
"'Fireproof.' means ..." -- so the boundary is the next quoted term, and the id
a note cites is "CS-Definitions, Fireproof". 'Icing Atmospheric Conditions' is
sliced as three entries, because 'Continuous Maximum Icing' and 'Intermittent
Maximum Icing' are separate entries in the source and a note cites whichever one
it means. The glossary also carries different page furniture: no "Page N of M"
line, and a bare page number that lands in the middle of a definition.

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

# (paragraph id, file, human title, search key). The id is what a note cites
# inside [ext ...]. The key is how the heading is written in the document, and is
# given only where it differs -- a glossary entry is headed "'Fireproof.'", not
# "CS-Definitions, Fireproof".
WANTED: list[tuple[str, str, str, str]] = [
    # --- CS-27 / CS-29, the rotorcraft codes
    ("CS 27.45", "CS-27_Amendment_10.pdf", "General (performance)"),
    ("CS 29.45", "CS-29_Amendment_12.pdf", "General (performance)"),
    ("CS 27.927", "CS-27_Amendment_10.pdf", "Additional tests"),
    ("CS 29.927", "CS-29_Amendment_12.pdf", "Additional tests"),
    ("CS 27.1093", "CS-27_Amendment_10.pdf", "Induction system icing protection"),
    ("CS 29.1093", "CS-29_Amendment_12.pdf", "Induction system icing protection"),
    ("CS 27.1305", "CS-27_Amendment_10.pdf", "Powerplant instruments"),
    ("CS 29.1305", "CS-29_Amendment_12.pdf", "Powerplant instruments"),
    ("CS 29.917", "CS-29_Amendment_12.pdf", "Design (rotor drive system)"),
    ("CS 27.917", "CS-27_Amendment_10.pdf", "Design (rotor drive system)"),
    ("CS 29.923", "CS-29_Amendment_12.pdf", "Rotor drive system and control mechanism tests"),
    ("CS 27.923", "CS-27_Amendment_10.pdf", "Rotor drive system and control mechanism tests"),
    ("AMC2 29.917", "CS-29_Amendment_12.pdf", "Rotor drive system design — lubrication systems"),
    # The AMC of the two paragraphs that have a note of their own. A CS and its
    # AMC belong together; that is the whole structure of this vault.
    ("AMC1 27.927", "CS-27_Amendment_10.pdf", "Additional tests"),
    ("AMC1 29.927", "CS-29_Amendment_12.pdf", "Additional tests"),
    ("AMC1 29.927(c)", "CS-29_Amendment_12.pdf", "Additional tests — loss of lubrication"),
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
    ("21.A.7", "Part-21_EAR_Reg-748-2012_Nov-2025.pdf", "Instructions for continued airworthiness"),
    ("21.A.3A", "Part-21_EAR_Reg-748-2012_Nov-2025.pdf", "Reporting system"),
    ("21.A.3B", "Part-21_EAR_Reg-748-2012_Nov-2025.pdf", "Airworthiness directives"),
    ("AMC1 21.A.3B(b)", "Part-21_EAR_Reg-748-2012_Nov-2025.pdf", "Failures, malfunctions and defects"),
    ("21.A.33", "Part-21_EAR_Reg-748-2012_Nov-2025.pdf", "Inspections and tests"),
    ("21.A.41", "Part-21_EAR_Reg-748-2012_Nov-2025.pdf", "Type-certificate"),
    # --- AMC-20. CS-E cites AMC 20-1, AMC 20-3 and AMC 20-115 without their
    # revision letters; Amendment 23 carries 20-1A, 20-3B and 20-115D.
    # AMC 20-6B is not sliced: it is the ETOPS AMC, and ETOPS is out of scope.
    ("AMC 20-1A", "AMC-20_Amendment_23.pdf", "Certification of Aircraft Propulsion Systems Equipped with Electronic Control Systems"),
    ("AMC 20-3B", "AMC-20_Amendment_23.pdf", "Certification of Engines Equipped with Electronic Engine Control Systems"),
    ("AMC 20-42", "AMC-20_Amendment_23.pdf", "Airworthiness information security risk assessment"),
    ("AMC 20-115D", "AMC-20_Amendment_23.pdf", "Airborne Software Development Assurance Using EUROCAE ED-12 and RTCA DO-178"),
    # --- CS-Definitions, a glossary
    ("CS-Definitions, Fireproof", "CS-Definitions_Amendment_2.pdf", "Fireproof", "\u2018Fireproof.\u2019"),
    ("CS-Definitions, Fire-resistant", "CS-Definitions_Amendment_2.pdf", "Fire-resistant", "\u2018Fire-resistant.\u2019"),
    ("CS-Definitions, Icing Atmospheric Conditions", "CS-Definitions_Amendment_2.pdf", "Icing Atmospheric Conditions", "\u2018Icing Atmospheric Conditions\u2019"),
    ("CS-Definitions, Continuous Maximum Icing", "CS-Definitions_Amendment_2.pdf", "Continuous Maximum Icing", "\u2018Continuous Maximum Icing\u2019"),
    ("CS-Definitions, Intermittent Maximum Icing", "CS-Definitions_Amendment_2.pdf", "Intermittent Maximum Icing", "\u2018Intermittent Maximum Icing\u2019"),
    # --- the repeal decision's explanatory note, whole. It is six pages, it has
    # no paragraph numbering worth slicing, and it is the only document that
    # says what became of CS-34 and what a TCDS reference to it is now worth.
    ("ED Decision 2025/005/R", "EN_to_ED_Decision_2025-005-R_CS-34-repeal.pdf", "Repeal of CS-34, CS-36 and CS-CO2", "*"),
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
    #
    # The lookbehind catches the case where the continuation IS capitalised:
    # "...as prescribed in CS 27.927(a). The need for representative test runs"
    # breaks so that the citation starts a line, and "The" then looks like a
    # title. A heading never ends in a full stop, and a citation mid-sentence
    # usually does. Without this, AMC1 27.927 ended mid-sentence.
    r")(?<![.,;:])[ \t]+[A-Z(]", re.M)

# AMC-20 heads each AMC with its number and title, and puts a divider line
# carrying the bare number in front of it. Both are boundaries.
HEADING_AMC20 = re.compile(r"^[ \t]*AMC\s*20-\d+[A-Z]?[ \t]*(?:$|[ \t][ \t]*[A-Z(])", re.M)

# A glossary entry opens with the term in single quotes at the start of a line.
HEADING_DEF = re.compile(r"^[ \t]*\u2018[^\u2019\n]{2,60}\u2019", re.M)

# CS-Definitions has no "Page N of M" line. Its furniture is the running title,
# the decision reference, the amendment number and a bare page number, and the
# page number lands in the middle of a definition.
FURNITURE_DEF = re.compile(
    r"^\s*(?:CS-Definitions|Annex to Decision \d{4}/\d{3}/R|Amendment \d+|\d{1,3})\s*$",
    re.M)

STYLE = {
    "AMC-20_Amendment_23.pdf": ("amc20", HEADING_AMC20),
    "CS-Definitions_Amendment_2.pdf": ("definitions", HEADING_DEF),
}

# Repeated on every page of these documents, and meaningless inside a slice.
FURNITURE = re.compile(
    r"^\s*(?:"
    r"CS-\d\d Amendment \d+|CS-34 Amendment \d+"
    r"|Annex I{1,2}? to ED Decision[^\n]*|Annex to ED Decision[^\n]*"
    r"|Page \d+ of \d+[^\n]*|Powered by EASA eRules[^\n]*"
    r"|Easy Access Rules for[^\n]*|Subpart [A-Z] —[^\n]*|Subpart [A-Z] -[^\n]*"
    r"|Annex I[b]? SECTION [AB][^\n]*|SECTION [AB] —[^\n]*|SECTION [AB] -[^\n]*"
    r"|Table of contents|TE\.RPRO[^\n]*|An agency of the European Union"
    r"|European Union Aviation Safety Agency|Explanatory Note to ED Decision[^\n]*"
    r"|Proprietary document[^\n]*"
    r")\s*$", re.M)


def slug(pid: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", pid).strip("_")


PAGE_NO = re.compile(r"^\s*Page \d+ of \d+")


def body(path: pathlib.Path, style: str = "") -> str:
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
        page_text = FURNITURE.sub("", "\n".join(lines))
        if style == "definitions":
            page_text = FURNITURE_DEF.sub("", page_text)
        pages.append(page_text)
    return "\n".join(pages)


# In the Easy Access Rules the line under a real heading gives its legal
# attribution. Nothing else in the document looks like this, so it is the
# cleanest way to tell a heading from a citation of the same number inside a
# sentence -- "GM1 21.A.3B(b) 'Failures ...' could be used to assist" starts a
# line and is capitalised, so neither of those tests catches it.
ATTRIB = re.compile(r"^[ \t]*(?:Regulation \((?:EU|EC)\)|ED Decision|\(Reserved\))")


def extract(pid: str, text: str, heading: re.Pattern = HEADING,
            key: str = "") -> str | None:
    """The slice from this paragraph's heading to the next heading."""
    if key == "*":
        # The whole document is the slice. Used where a document has no
        # paragraph numbering to cut on.
        return text.strip()
    key = key or pid
    # A glossary term is followed by "means", not by a title starting with a
    # capital, so the trailing \S is all that can be asked of it. The lookahead
    # is not optional: without it "21.A.21" matches the heading of 21.A.211, and
    # the slice is a different point of Part 21 that reads perfectly well. It is
    # applied only where the key ends in a letter or a digit, because a glossary
    # term ends in a closing quote and is followed by a full stop.
    tail = r"(?![A-Za-z0-9])" if key[-1].isalnum() else ""
    # A paragraph heading is the number, a space, and its title. Allowing no
    # space matched "CS 29.1305(a)(18)." -- a cross-reference at the start of a
    # line -- and the slice that followed was the tail of CS 29.1307. A glossary
    # term is the exception: it is followed directly by a full stop.
    sep = r"[ \t]*" if key.endswith("\u2019") else r"[ \t]+"
    candidates = []
    for m in re.finditer(rf"^[ \t]*{re.escape(key)}{tail}{sep}\S", text, re.M):
        # A table-of-contents entry carries dot leaders and a page number. A
        # long one wraps, so the leaders can be on the following line.
        window = text[m.start():m.start() + 400].split("\n")[:4]
        if any(re.search(r"\.{4,}\s*\d+\s*$", ln) for ln in window):
            continue
        # The attribution is not always the line straight after the number: a
        # long title wraps, and "21.A.801 Identification of products and control
        # and monitoring" puts "units (CMUs)" in between. Looking one line down
        # only, the real heading loses to a cross-reference elsewhere.
        following = [ln for ln in window[1:] if ln.strip()][:2]
        candidates.append((any(ATTRIB.match(ln) for ln in following), m.start()))
    if not candidates:
        return None
    # Prefer a candidate with an attribution line under it; else the first.
    attributed = [pos for ok, pos in candidates if ok]
    start = attributed[0] if attributed else candidates[0][1]
    rest = text[start:]
    first_nl = rest.find("\n")
    nxt = heading.search(rest, first_nl if first_nl > 0 else 1)
    return (rest[:nxt.start()] if nxt else rest).strip()


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    cache: dict[str, str] = {}
    written = missing = 0
    for entry in WANTED:
        pid, fname, title = entry[:3]
        key = entry[3] if len(entry) > 3 else ""
        style, heading = STYLE.get(fname, ("", HEADING))
        path = EXT / fname
        if not path.exists():
            print(f"  {pid:44s} SOURCE MISSING: {fname}")
            missing += 1
            continue
        if fname not in cache:
            cache[fname] = body(path, style)
        slice_ = extract(pid, cache[fname], heading, key)
        if slice_ is None:
            print(f"  {pid:44s} NOT FOUND in {fname}")
            missing += 1
            continue
        # The slice must open with the point it claims to be. This is the check
        # that catches a heading regex matching a longer number -- a defect that
        # produces plausible text for the wrong paragraph and fails nothing else.
        first = slice_.split("\n", 1)[0].strip()
        k = key or pid
        ok = first.startswith(k) and (
            k.endswith("\u2019") or first[len(k):len(k) + 1] in (" ", "\t"))
        if key != "*" and not ok:
            print(f"  {pid:44s} WRONG SLICE: starts {first[:40]!r}")
            missing += 1
            continue
        out = OUT / f"{slug(pid)}.txt"
        out.write_text(
            f"# {pid} {title}\n# id: {pid}\n# source: external/{fname}\n"
            f"# chars: {len(slice_)}\n\n{slice_}\n", encoding="utf-8")
        written += 1
        print(f"  {pid:44s} {len(slice_):7,d} chars -> {out.name}")
    print(f"\n{written} paragraph(s) written to work/external/, {missing} missing")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
