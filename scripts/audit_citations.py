"""Does every citation reach a note, and does every number come from the source?

Two invariants that no other validator covers. `lint_vault.py` checks the form of
a `[[wikilink]]`; nothing checked the `[CS-E 740(c)(3)]` citations, and nothing
checked numbers at all.

1. **Every citation resolves to a note this vault contains.** A citation is
   notation, not a link, so Obsidian never reports a broken one and a reader only
   finds out by looking. Resolving one is not a filename lookup: the vault holds
   **one AMC note per CS-E number**, so `[AMC E 740(c)(3)]` belongs to
   `AMC E 740.md` while `work/paragraphs/` splits it into its own banner file.
   `vault_map.note_name` is the authority, and going around it produces a hundred
   false alarms.

   A citation to an EXCLUDED paragraph is reported separately rather than as an
   error. CS-E 780 cites AMC E 780(1.7) precisely to record why that AMC is
   excluded, which is the legitimate case CLAUDE.md allows: an out-of-scope
   sub-point is kept when it changes what we must do.

2. **Every number carrying a unit appears in the source.** Accuracy rule 3 says
   to copy numbers exactly, with units, and a wrong limit is the defect a
   certification engineer is least able to catch by reading. Only numbers with a
   unit or a percent sign are tested: a bare "three" is prose, and sub-point
   labels like (2) would drown the signal.

   Normalisation matters more than the comparison. The PDF text layer writes
   "2 1/2" where the note writes the vulgar fraction, splits thousands with a thin
   space ("1 500 ft"), and spaces degree signs inconsistently. Both sides are put
   through the same `norm()`, so a real mismatch stays just as visible.

   A number is accepted if it appears in the note's own paragraphs, or anywhere in
   the corpus -- a note may quote a paragraph it links to, which rule 8 encourages
   over duplicating it. A note that declares `imports:` may also take a number
   from `work/external/`, because an imported obligation carries the other
   document's figures; a note that declares no import may not, so a CS-29 number
   cannot drift into a CS-E note unannounced.

An `[ext ...]` citation is not matched against the notes at all -- it names a
paragraph of another document, and `lint_vault.py` owns its resolution. What is
checked here is that its id reaches a slice in `work/external/`, so a citation
the verbatim check cannot follow is reported rather than silently trusted.

The notes in `vault/external/` are audited too: their `[CS-E ...]` citations
resolve like any other, and their numbers are checked against the document they
are about.

Exit status is non-zero if either invariant is broken.
"""
from __future__ import annotations

import collections
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from classification import CLASSIFICATION
from vault_map import expected_notes, note_name

ROOT = pathlib.Path(__file__).resolve().parent.parent
VAULT = ROOT / "vault"
VAULT_EXT = VAULT / "external"
PARA = ROOT / "work" / "paragraphs"
EXTERNAL = ROOT / "work" / "external"

# "AMC to CS-E 50(l)" is a paragraph id in its own right, not a typo for
# "AMC E 50(l)": vault_map resolves it to the AMC E 50 note. Three citations
# use that form and went unchecked while the pattern only knew the other two.
CITE = re.compile(r"\[((?:AMC to CS-E|CS-E|AMC E) \d+[A-Za-z]?)((?:\([^)\]]{1,8}\))*)\]")

# An imported obligation. The id names a paragraph of another document, so it
# resolves to a slice in work/external/, never to a note.
EXT_CITE = re.compile(r"\[ext ([^\]]+)\]")

# A value plus the unit it is measured in. Rule 3 is about these, not about
# every integer on the page.
NUM = re.compile(
    r"\b(\d+(?:\.\d+)?(?: 1/2| 1/4| 3/4)?)\s?"
    r"(%|percent|°c|°f|kg|m2|m²|mm|litre|litres|kw|knots|seconds|second|"
    r"minutes|minute|hours|hour|ft|m/s|bar|hz|g\b)",
    re.I,
)


def norm(text: str) -> str:
    """Flatten the spellings that differ between the PDF text layer and a note."""
    text = (text.replace("½", " 1/2").replace("¼", " 1/4")
                .replace("¾", " 3/4").replace(" ", " ")
                .replace(" ", " ").replace("–", "-")
                .replace("−", "-").replace("’", "'"))
    # "1 500" and "12,285" are one number, however the typesetter split them.
    text = re.sub(r"(?<=\d)[  ,](?=\d\d\d\b)", "", text)
    return re.sub(r"\s+", " ", text).lower()


def paragraph_file(pid: str) -> pathlib.Path:
    return PARA / (re.sub(r"[^A-Za-z0-9]+", "_", pid).strip("_") + ".txt")


def ext_slices() -> dict[str, str]:
    """Every sliced external paragraph: id -> its normalised text."""
    out = {}
    for f in sorted(EXTERNAL.glob("*.txt")):
        lines = f.read_text(encoding="utf-8").splitlines()
        pid = next((ln[6:].strip() for ln in lines[:6] if ln.startswith("# id: ")), "")
        if pid:
            out[pid] = norm(" ".join(ln for ln in lines if not ln.startswith("#")))
    return out


def source_of(ids: list[str]) -> str:
    out = []
    for pid in ids:
        f = paragraph_file(pid)
        if f.exists():
            out.append(f.read_text(encoding="utf-8"))
    return norm(" ".join(out))


def main() -> int:
    verdict = {i: s for i, s, _ in CLASSIFICATION}
    expected = expected_notes(verdict)
    whole = norm(" ".join(p.read_text(encoding="utf-8")
                          for p in sorted(PARA.glob("*.txt"))))

    slices = ext_slices()
    ext_whole = norm(" ".join(slices.values()))

    unresolved: list[tuple[str, str, str]] = []
    to_excluded: list[tuple[str, str]] = []
    unsliced: list[tuple[str, str]] = []
    bad_numbers: dict[str, set[str]] = collections.defaultdict(set)
    n_cites = n_numbers = n_ext = 0

    def check_ext(where: str, text: str) -> None:
        nonlocal n_ext
        for m in EXT_CITE.finditer(text):
            n_ext += 1
            cid = m.group(1).strip()
            if not any(cid == pid or cid.startswith(pid) for pid in slices):
                unsliced.append((where, m.group(0)))

    for note in sorted(VAULT.glob("*.md")):
        name = note.stem
        if name not in expected:
            continue                      # lint_vault.py owns that complaint
        text = note.read_text(encoding="utf-8")

        for m in CITE.finditer(text):
            n_cites += 1
            pid = m.group(1)
            target = note_name(pid)
            if target in expected:
                continue
            if verdict.get(pid) == "EXCLUDED":
                to_excluded.append((note.name, m.group(0)))
            else:
                unresolved.append((note.name, m.group(0),
                                   verdict.get(pid, "not in the index")))

        # Amendment history quotes wording that Amendment 8 no longer carries.
        body = norm(text.split("---\n", 2)[-1].split("## Amendment history")[0])
        own = source_of(expected[name]["ids"])
        check_ext(note.name, text)
        # An imported obligation carries the other document's figures, so a
        # note that declares an import may take a number from work/external/.
        # A note that declares none may not: that is what keeps a CS-29 number
        # from drifting into a CS-E note unannounced.
        imported = ext_whole if re.search(r"^imports:", text, re.M) else ""
        for m in NUM.finditer(body):
            n_numbers += 1
            value, unit = m.group(1), m.group(2)
            if value in own or f"{value} {unit}" in own or value in whole:
                continue
            if imported and (value in imported or f"{value} {unit}" in imported):
                continue
            bad_numbers[note.name].add(f"{value} {unit}")

    # --- the external notes, against the document each one is about
    n_ext_notes = 0
    for note in sorted(VAULT_EXT.glob("*.md")) if VAULT_EXT.exists() else []:
        n_ext_notes += 1
        where = f"external/{note.name}"
        text = note.read_text(encoding="utf-8")
        for m in CITE.finditer(text):
            n_cites += 1
            pid = m.group(1)
            if note_name(pid) in expected:
                continue
            if verdict.get(pid) == "EXCLUDED":
                to_excluded.append((where, m.group(0)))
            else:
                unresolved.append((where, m.group(0),
                                   verdict.get(pid, "not in the index")))
        check_ext(where, text)
        own = slices.get(note.stem, "")
        body = norm(text.split("---\n", 2)[-1])
        for m in NUM.finditer(body):
            n_numbers += 1
            value, unit = m.group(1), m.group(2)
            if value in own or f"{value} {unit}" in own or value in ext_whole:
                continue
            bad_numbers[where].add(f"{value} {unit}")

    print(f"{n_cites} citation(s), {n_ext} import(s) and {n_numbers} number(s) "
          f"checked across {len(expected)} notes"
          + (f" and {n_ext_notes} external note(s)" if n_ext_notes else ""))

    if to_excluded:
        print(f"\n{len(to_excluded)} citation(s) to an EXCLUDED paragraph — "
              "legitimate only where the exclusion itself is the point:")
        for n, c in sorted(set(to_excluded)):
            print(f"   {n}: {c}")

    problems = (len(unresolved) + len(unsliced)
                + sum(len(v) for v in bad_numbers.values()))
    if unsliced:
        print(f"\n{len(unsliced)} import(s) reaching no slice in "
              "work/external/ — add the point to WANTED in "
              "external_paragraphs.py:")
        for n, c in sorted(set(unsliced)):
            print(f"   {n}: {c}")
    if unresolved:
        print(f"\n{len(unresolved)} citation(s) reaching no note:")
        for n, c, v in sorted(set(unresolved)):
            print(f"   {n}: {c}   [{v}]")
    if bad_numbers:
        print(f"\n{sum(len(v) for v in bad_numbers.values())} number(s) absent "
              "from the source:")
        for n, vals in sorted(bad_numbers.items()):
            print(f"   {n}: {sorted(vals)}")

    print(f"\n{problems} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
