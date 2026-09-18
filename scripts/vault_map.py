"""Which vault note does a CS-E paragraph belong to?

The vault holds one note per CS-E paragraph, and **one AMC note per CS-E
number**. EASA splits its AMC material unevenly — AMC E 40, AMC E 40(b)(3) and
AMC E 40(d) are three separate banners, while AMC E 25 is one — so mirroring the
source heading-for-heading produces a vault that looks arbitrary. Grouping by CS
number makes the rule uniform: every specification has at most one note of
accepted means.

CS and AMC stay in separate files, so the graph keeps its specification-to-means
edges.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "work" / "paragraph_index.csv"

NUM = re.compile(r"^(?:AMC to CS-E|AMC E|GM E|CS-E)\s+(\d{1,4})")


def note_name(paragraph_id: str) -> str:
    """The note a paragraph is written into."""
    if paragraph_id.startswith("CS-E"):
        return paragraph_id
    m = NUM.match(paragraph_id)
    if m and not paragraph_id.startswith("CS-E"):
        return f"AMC E {m.group(1)}"
    return paragraph_id          # AMC General, Appendix A, ...


def verdict_of(paragraph_id: str, verdict: dict[str, str]) -> str | None:
    """The classification of a paragraph, tolerating a spelled-out span id.

    classification.py keys the appendix as "Appendix A"; the banner, and
    therefore spans.json and the index, spell it "Appendix A Certification
    Standard Atmospheric Concentrations of Rain and Hail". A plain dict lookup
    returns None for it, which reads as "not APPLIES" and silently drops the
    paragraph -- that is how three table crops went missing from the appendix.
    """
    if paragraph_id in verdict:
        return verdict[paragraph_id]
    for key, status in verdict.items():
        # The remainder must start at a word boundary. A bare startswith()
        # matches "CS-E 300" against "CS-E 30" and hands back the wrong
        # verdict for a Subpart C paragraph.
        if paragraph_id.startswith(key + " "):
            return status
    return None


def expected_notes(verdict: dict[str, str]) -> dict[str, dict]:
    """{note name: merged metadata} for every note the vault should contain."""
    rows = {r["id"]: r for r in csv.DictReader(INDEX.open())}
    notes: dict[str, dict] = {}
    for pid, status in verdict.items():
        if status != "APPLIES":
            continue
        row = rows.get(pid)
        if row is None:                      # ids the index spells out in full
            row = next((r for r in rows.values() if r["id"].startswith(pid)), None)
        if row is None:
            continue
        name = note_name(row["id"])
        e = notes.setdefault(name, {
            "ids": [], "subpart": row["subpart"],
            "start": int(row["start_page"]), "end": int(row["end_page"]),
            "changed_in": set(), "figure_pages": [],
        })
        e["ids"].append(row["id"])
        e["start"] = min(e["start"], int(row["start_page"]))
        e["end"] = max(e["end"], int(row["end_page"]))
        if row["changed_in"] != "none":
            e["changed_in"].update(row["changed_in"].split(";"))
        e["figure_pages"] += [int(n) for n in row["figure_pages"].split() if n]
    for e in notes.values():
        e["ids"].sort()
        e["changed_in"] = sorted(e["changed_in"])
        e["figure_pages"] = sorted(set(e["figure_pages"]))
        e["type"] = "CS" if e["ids"][0].startswith("CS-E") else "AMC"
    return notes


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(ROOT / "scripts"))
    from classification import CLASSIFICATION
    v = {i: s for i, s, _ in CLASSIFICATION}
    notes = expected_notes(v)
    merged = {k: e for k, e in notes.items() if len(e["ids"]) > 1}
    print(f"{len(notes)} notes expected "
          f"({sum(1 for e in notes.values() if e['type'] == 'CS')} CS, "
          f"{sum(1 for e in notes.values() if e['type'] == 'AMC')} AMC)")
    print(f"{len(merged)} of them merge more than one paragraph:\n")
    for k, e in sorted(merged.items()):
        print(f"  {k:<18} pp{e['start']}-{e['end']:<5} {len(e['ids'])}: {', '.join(e['ids'])}")
