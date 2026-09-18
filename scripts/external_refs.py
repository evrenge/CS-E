"""Every reference the vault makes to a document we do not hold.

CS-E does not stand alone. It defers to Part 21 for the certification process,
to CS-27 and CS-29 for what the rotorcraft must do, to CS-34 for emissions, to
CS-Definitions for terms it uses without defining, to the AMC 20 series for
electronic control systems and security, and to industry standards for how each
environmental test is run. None of those are in `source/`, and the five PDFs we
hold are the only authority the vault has.

A reader who follows one of those references leaves the vault and cannot come
back with an answer. This script finds every such exit, in the SOURCE text of
every in-scope paragraph and in the notes, so the list is what EASA actually
cites rather than what a note happened to mention.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARAS = ROOT / "work" / "paragraphs"
VAULT = ROOT / "vault"

sys.path.insert(0, str(ROOT / "scripts"))

# Each pattern names a family of documents outside source/. The CS-E, AMC E and
# GM E families are deliberately absent: those are the vault's own subject.
PATTERNS = [
    ("Part 21",        r"\b(?:point\s+)?21\.A\.\d+[A-Za-z]?(?:\([^)\s]{1,4}\))*\d?"),
    ("Part 21",        r"\bAMC1?\s*21\.A\.\d+[A-Za-z]?(?:\([^)\s]{1,4}\))*"),
    ("AMC 20 series",  r"\bAMC\s*20-\d+[A-Za-z]?"),
    ("CS-Definitions", r"\bCS-Definitions(?:\s+Amendment\s+\d+)?"),
    ("CS-27 / CS-29",  r"\bCS[- ]?2[79](?:\.\d+(?:\([^)\s]{1,4}\))*)?"),
    ("CS-23 / CS-25",  r"\bCS[- ]?2[35](?:\.\d+(?:\([^)\s]{1,4}\))*)?"),
    ("CS-23 / CS-25",  r"\bAMC\s*25\.\d+(?:\([^)\s]{1,4}\))*"),
    ("CS-34",          r"\bCS[- ]?34(?:\.\d+)?"),
    ("FAA",            r"\bFAR\s*\d+\.\d+|\bAC\s*\d+\.\d+-\d+|\b14\s*CFR\b"),
    ("Industry std",   r"\b(?:EUROCAE\s*)?ED-\d+[A-Za-z]?|\bRTCA/?DO-\d+[A-Za-z]?"),
    ("Industry std",   r"\bISO\s*\d+(?:-\d+)?|\bMIL-STD-\d+|\bSAE\s*[A-Z]*\d+"),
    ("Industry std",   r"\bICAO\s+Annex\s+\d+"),
]


def canon(ref: str) -> str:
    """One spelling per document.

    EASA is not consistent with itself: CS-E 780 writes "CS 27.1093(b)" while a
    note writing the same reference may hyphenate it, and "point 21.A.41" and
    "21.A.41" are the same point. Without this, the inventory counts the same
    dead end three times and the reader cannot tell which are real.
    """
    ref = " ".join(ref.split())
    ref = re.sub(r"(?i)^point\s+", "", ref)
    ref = re.sub(r"(?i)^AMC1\s*", "AMC1 ", ref)
    ref = re.sub(r"(?i)^(CS)[- ]?(\d{2})", r"CS-\2", ref)
    ref = re.sub(r"(?i)^CS-(\d{2})\.", r"CS-\1.", ref)
    ref = re.sub(r"(?i)^cs-definitions", "CS-Definitions", ref)
    ref = re.sub(r"(?i)^cs-34", "CS-34", ref)
    ref = re.sub(r"(?i)^EUROCAE\s+", "", ref)
    ref = re.sub(r"(?i)^RTCA/?DO-", "RTCA/DO-", ref)
    return ref


def scan(text: str) -> set[tuple[str, str]]:
    out = set()
    for family, pattern in PATTERNS:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            out.add((family, canon(m.group(0))))
    return out


def slug(pid: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", pid).strip("_")


def main() -> int:
    import csv
    from classification import CLASSIFICATION
    verdict = {i: s for i, s, _ in CLASSIFICATION}
    index = ROOT / "work" / "paragraph_index.csv"
    figures = {r["id"]: r["has_figure_or_table"] == "yes"
               for r in csv.DictReader(index.open(encoding="utf-8"))}

    # family -> reference -> {"source": {paragraph ids}, "notes": {note names}}
    found: dict[str, dict[str, dict[str, set]]] = defaultdict(
        lambda: defaultdict(lambda: {"source": set(), "notes": set()}))

    for pid, status in verdict.items():
        if status != "APPLIES":
            continue
        f = PARAS / f"{slug(pid)}.txt"
        if not f.exists():
            f = next(PARAS.glob(f"{slug(pid)}*.txt"), None)
        if f is None:
            continue
        for family, ref in scan(f.read_text(encoding="utf-8")):
            found[family][ref]["source"].add(pid)

    for note in sorted(VAULT.glob("*.md")):
        for family, ref in scan(note.read_text(encoding="utf-8")):
            found[family][ref]["notes"].add(note.stem)

    total = 0
    for family in sorted(found):
        refs = found[family]
        print(f"\n## {family}  ({len(refs)} distinct)")
        for ref in sorted(refs):
            e = refs[ref]
            total += 1
            src = ", ".join(sorted(e["source"])[:6]) or "—"
            more = "" if len(e["source"]) <= 6 else f" +{len(e['source']) - 6}"
            # A reference that lives inside a table or figure is embedded as a
            # crop under accuracy rule 6, so it is visible to a reader and
            # invisible to a search of the note text. That is by design.
            in_figure = any(figures.get(pid) for pid in e["source"])
            flag = ""
            if not e["notes"]:
                flag = ("   [only inside an embedded table]" if in_figure
                        else "   [NOT MENTIONED IN ANY NOTE]")
            print(f"  {ref:<28} cited by: {src}{more}"
                  f"  | notes: {len(e['notes'])}{flag}")
    print(f"\n{total} distinct external references across {len(found)} families")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
