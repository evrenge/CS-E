"""Which chapter does a vault note belong to?

The vault is 113 notes. Read in file order they are a flat list; read in CS-E
page order they fall into thirteen blocks, each a single subject a reader can
finish in one sitting. This module is the authority on those blocks.

A chapter never crosses a subpart, and it never splits a CS paragraph from the
AMC note that gives its accepted means. Within those two constraints the blocks
are sized so that no chapter is far larger than the rest, measured in source
words rather than note count: CS-E 740 is two notes and 7,136 words, CS-E 660
to AMC E 730 is fourteen notes and 2,744.

`lint_vault.py` fails if a note the map expects has no chapter, or if a chapter
names a note that does not exist.
"""

from __future__ import annotations

APPENDIX_A = ("Appendix A Certification Standard Atmospheric Concentrations "
              "of Rain and Hail")

# (letter, title, subpart, notes in source order)
CHAPTERS: list[tuple[str, str, str, list[str]]] = [
    ("A", "Scope, Terminology and Continued Airworthiness", "A", [
        "CS-E 10", "AMC General", "CS-E 15", "CS-E 20", "AMC E 20",
        "CS-E 25", "AMC E 25", "CS-E 30", "AMC E 30",
    ]),
    ("B", "Ratings, Control System and Instruments", "A", [
        "CS-E 40", "AMC E 40", "CS-E 50", "AMC E 50", "CS-E 60", "AMC E 60",
    ]),
    ("C", "Materials, Equipment, Strength and Identification", "A", [
        "CS-E 70", "AMC E 70", "CS-E 80", "AMC E 80", "CS-E 90",
        "CS-E 100", "CS-E 110", "CS-E 120",
    ]),
    ("D", "Fire Protection, Bonding and Conduct of Tests", "A", [
        "CS-E 130", "AMC E 130", "CS-E 135", "AMC E 135", "CS-E 140",
        "AMC E 140", "CS-E 150", "AMC E 150", "CS-E 160", "CS-E 170",
        "AMC E 170",
    ]),
    ("E", "Functioning, Safety Analysis and Engine Critical Parts", "D", [
        "CS-E 500", "CS-E 510", "AMC E 510", "CS-E 515", "AMC E 515",
    ]),
    ("F", "Strength, Ingestion and Engine Systems", "D", [
        "CS-E 520", "AMC E 520", "CS-E 525", "AMC E 525", "CS-E 540",
        "AMC E 540", "CS-E 560", "AMC E 560", "CS-E 570", "AMC E 570",
        "CS-E 580", "CS-E 590",
    ]),
    ("G", "General Test Conditions and Vibration Surveys", "E", [
        "CS-E 600", "AMC E 600", "CS-E 620", "AMC E 620", "CS-E 640",
        "AMC E 640", "CS-E 650", "AMC E 650",
    ]),
    ("H", "Fuel, Bleed, Attitude and Operational Tests", "E", [
        "CS-E 660", "CS-E 670", "AMC E 670", "CS-E 680", "AMC E 680",
        "CS-E 690", "AMC E 690", "CS-E 700", "CS-E 710", "AMC E 710",
        "CS-E 720", "AMC E 720", "CS-E 730", "AMC E 730",
    ]),
    ("I", "Endurance Tests", "E", [
        "CS-E 740", "AMC E 740",
    ]),
    ("J", "Acceleration, Starting, Icing and Ingestion of Rain and Hail", "E", [
        "CS-E 745", "AMC E 745", "CS-E 750", "AMC E 750", "CS-E 770",
        "AMC E 770", "CS-E 780", "CS-E 790", "AMC E 790", APPENDIX_A,
    ]),
    ("K", "Bird Strike, Blade Failure and Over-limit Tests", "E", [
        "CS-E 800", "AMC E 800", "CS-E 810", "AMC E 810", "CS-E 820",
        "AMC E 820", "CS-E 830", "AMC E 830",
    ]),
    ("L", "Rotor Integrity, Over-temperature and Relighting", "E", [
        "CS-E 840", "AMC E 840", "CS-E 850", "AMC E 850", "CS-E 860",
        "CS-E 870", "AMC E 870", "CS-E 910", "AMC E 910", "CS-E 920",
        "AMC E 920", "CS-E 930", "AMC E 930",
    ]),
    ("M", "Environmental and Operational Requirements", "F", [
        "CS-E 1000", "AMC E 1000", "CS-E 1010", "CS-E 1020", "AMC E 1020",
        "CS-E 1050", "AMC E 1050",
    ]),
]

TITLES = {letter: title for letter, title, _, _ in CHAPTERS}
SUBPART = {letter: subpart for letter, _, subpart, _ in CHAPTERS}
_OF = {note: letter for letter, _, _, notes in CHAPTERS for note in notes}


def chapter_of(note_name: str) -> str | None:
    """The chapter letter a note belongs to, or None if it is unassigned."""
    return _OF.get(note_name)


def notes_in(letter: str) -> list[str]:
    return next(notes for lt, _, _, notes in CHAPTERS if lt == letter)


def check(expected: dict[str, dict]) -> list[str]:
    """Problems found against the notes vault_map expects. Empty when sound."""
    problems = []
    assigned = set(_OF)
    for note in sorted(set(expected) - assigned):
        problems.append(f"note in no chapter: {note}")
    for note in sorted(assigned - set(expected)):
        problems.append(f"chapter names a note that does not exist: {note}")
    seen: dict[str, str] = {}
    for letter, _, _, notes in CHAPTERS:
        for note in notes:
            if note in seen:
                problems.append(
                    f"{note} is in chapter {seen[note]} and chapter {letter}")
            seen[note] = letter
    for letter, _, subpart, notes in CHAPTERS:
        for note in notes:
            got = expected.get(note, {}).get("subpart")
            if got and got != subpart:
                problems.append(
                    f"chapter {letter} is subpart {subpart} but {note} "
                    f"is subpart {got}")
    return problems


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from classification import CLASSIFICATION
    from paragraph_text import slug
    from vault_map import expected_notes

    root = Path(__file__).resolve().parent.parent
    expected = expected_notes({i: s for i, s, _ in CLASSIFICATION})
    problems = check(expected)

    def words(note: str) -> int:
        return sum(len((root / "work" / "paragraphs" / f"{slug(p)}.txt")
                        .read_text().split())
                   for p in expected[note]["ids"])

    print("| Ch | Title | Subpart | Pages | Notes | Words | Changed |")
    print("|---|---|---|---:|---:|---:|---:|")
    for letter, title, subpart, notes in CHAPTERS:
        lo = min(expected[n]["start"] for n in notes)
        hi = max(expected[n]["end"] for n in notes)
        chg = sum(1 for n in notes if expected[n]["changed_in"])
        print(f"| **{letter}** | {title} | {subpart} | {lo}-{hi} | "
              f"{len(notes)} | {sum(words(n) for n in notes):,} | {chg} |")
    total = sum(len(n) for _, _, _, n in CHAPTERS)
    print(f"| | **Total** | | | **{total}** | "
          f"**{sum(words(n) for n in expected):,}** | "
          f"**{sum(1 for e in expected.values() if e['changed_in'])}** |")

    if problems:
        print("\n" + "\n".join(problems))
        sys.exit(1)
    print(f"\n{total} notes, every one in exactly one chapter.")
