#!/usr/bin/env python3
"""Check every vault note against the index and the CLAUDE.md rules.

Catches the mistakes that are invisible when writing one note at a time:

  unexpected     a note whose name is not one the vault should contain
  frontmatter    a missing field, or a value that disagrees with the index
                 (pages, subpart, type, changed_in, covers)
  sections       a required section missing, or 'Not applicable' present but empty
  summary        not exactly one [!summary] callout
  quote          a quoted passage of 40 characters or more that is not verbatim
                 anywhere in CS-E Amendment 8
  strength       a Strength cell outside the seven allowed values
  ref-format     a Ref cell splitting nested sub-points, e.g. "(a) (2)"
  link-paren     [[X]](y), which GitHub parses as a link to the path "y"
  ghost-link     a [[wikilink]] to a note the vault will not contain
  missing-image  an ![[embed]] whose file is absent from vault/figures/
  terminology    the note uses "Book 1" or "Book 2", which CLAUDE.md bans

Exit status is 0 only when every note passes.

Usage:
    python3 scripts/lint_vault.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from classification import CLASSIFICATION  # noqa: E402
from vault_map import expected_notes, note_name  # noqa: E402

VAULT = ROOT / "vault"
PARAS = ROOT / "work" / "paragraphs"
REDLINE = ROOT / "work" / "redline.json"

REQUIRED = ["## Requirement", "## Compliance", "## Application to this engine",
            "## References"]
# The template's tail, in order. A note carries any subset of these, but never
# out of this sequence.
TAIL_ORDER = ["## Requirement", "## Compliance", "## Application to this engine",
              "## Not applicable", "## References", "## Amendment history"]
STRENGTHS = {"Required", "Required if claimed", "Recommended",
             "Accepted method", "Permitted", "Relief", "Statement"}

WIKILINK = re.compile(r"(?<!!)\[\[([^\]|#]+)")
EMBED = re.compile(r"!\[\[([^\]|#]+)\]\]")
LINK_PAREN = re.compile(r"\]\]\(")
FM_FIELD = re.compile(r"^(\w+):\s*(.*)$")
SUMMARY = re.compile(r">\s*\[!summary\]")
# Everything a note legitimately needs beyond ASCII: typography the house style
# uses, and the technical notation the source carries. Anything else is a slip —
# a stray CJK character once landed mid-sentence in CS-E 790 and read as a word.
ALLOWED_NON_ASCII = set("·—–…½°±×−√θ⁻⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉‘’“”")
# Quotation marks are paired by POSITION, not matched by a regex: a regex cannot
# tell an opening quote from a closing one, so it matches the prose BETWEEN two
# separate quotations and reports it as unverifiable.
MIN_QUOTE = 40


def slug(pid: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", pid).strip("_")


def norm(text: str) -> str:
    text = (text.replace("’", "'").replace("‘", "'")
                .replace("“", '"').replace("”", '"')
                .replace("‑", "-").replace("–", "-").replace("—", "-"))
    text = " ".join(text.split())
    # The source typesets a space before punctuation in 68 places, e.g.
    # "Engine Performance Target after Test Completion ." in CS-E 740(h).
    # The spacing carries no meaning, and applying the same normalisation to
    # the quote and to the haystack leaves a real misquote just as detectable.
    text = re.sub(r"\s+([,.;:])", r"\1", text)
    return re.sub(r"-\s+", "-", text)


def source_text(ids: list[str]) -> str:
    """Concatenated source text of every paragraph a note covers."""
    out = []
    for pid in ids:
        f = PARAS / f"{slug(pid)}.txt"
        if f.exists():
            out += [ln for ln in f.read_text(encoding="utf-8").splitlines()
                    if not ln.startswith("#")]
    return norm(" ".join(out))


_WHOLE: str | None = None


def whole_document() -> str:
    """All of CS-E Amendment 8, as the fallback haystack.

    A note may legitimately quote a paragraph it links to rather than one it
    covers — AMC E 50 quoting CS-E 50(a)(3), say. The quotation still has to be
    verbatim, just not necessarily from this note's own paragraphs.
    """
    global _WHOLE
    if _WHOLE is None:
        out = []
        for f in sorted(PARAS.glob("*.txt")):
            body = f.read_text(encoding="utf-8").splitlines()
            out += [ln for ln in body if not ln.startswith("#")]
            # The banner is evidence, not decoration: a note justifies an
            # exclusion by quoting the paragraph's own title, as CS-E 500 does
            # for "Functioning - Control of Engines (Turbine Engines for
            # Aeroplanes)". Strip the "# " and the title becomes quotable.
            if body and body[0].startswith("# "):
                out.append(body[0][2:])
        _WHOLE = norm(" ".join(out))
    return _WHOLE


def norm_stitched(text: str) -> str:
    """norm(), with every space removed.

    The "before" wording is rebuilt by dropping the inserted runs and keeping
    the deleted ones, so a space appears at every run boundary: the amendment's
    "certification," becomes "certification ,", its "CS-E 130(c)" becomes
    "CS-E 130( c )", and a deletion that starts mid-word leaves "T he Engine"
    and "D iscs". Spacing at a stitch boundary carries no information, so the
    comparison ignores spacing altogether rather than chasing each artifact.

    Both sides get the same transform, so identical wording still matches and
    different wording still fails. The only distinction lost is between a
    quotation and the same characters spaced differently.
    """
    return re.sub(r"\s+", "", norm(text))


_PRIOR: str | None = None


def prior_wording() -> str:
    """The pre-amendment wording, from work/redline.json.

    A changed note shows before and after. The "before" is by definition absent
    from Amendment 8, so checking it against the consolidated text always fails.
    It is still a quotation and still verifiable — against the wording the
    redline extractor recovered from the Change Information PDFs, which
    `extract_redline.py` cross-validates against Amendment 7.

    This haystack is admissible only for a note's `Amendment history` section.
    It is not requirement content, and CLAUDE.md bans it everywhere else.
    """
    global _PRIOR
    if _PRIOR is None:
        if not REDLINE.exists():
            _PRIOR = ""
        else:
            data = json.loads(REDLINE.read_text(encoding="utf-8"))
            _PRIOR = norm_stitched(
                " ".join(e.get("before", "") for e in data.values()))
    return _PRIOR


def main() -> int:
    verdict = {i: s for i, s, _ in CLASSIFICATION}
    expected = expected_notes(verdict)
    problems: list[str] = []
    seen: set[str] = set()

    for note in sorted(VAULT.glob("*.md")):
        name = note.stem
        text = note.read_text(encoding="utf-8")
        seen.add(name)
        say = lambda msg: problems.append(f"{note.name}: {msg}")  # noqa: E731

        meta = expected.get(name)
        if meta is None:
            say(f"unexpected note — {name!r} is not a note this vault should contain")
            continue

        # --- frontmatter
        if not text.startswith("---\n"):
            say("frontmatter missing")
            fm = {}
        else:
            fm = {}
            for line in text.split("---\n", 2)[1].splitlines():
                m = FM_FIELD.match(line)
                if m:
                    fm[m.group(1)] = m.group(2).strip()
        for field in ("id", "type", "subpart", "pages", "changed_in", "tags"):
            if field not in fm:
                say(f"frontmatter missing field {field!r}")
        want_pages = f"{meta['start']}-{meta['end']}"
        if fm.get("pages") != want_pages:
            say(f"pages {fm.get('pages')!r} but the index says {want_pages!r}")
        if fm.get("subpart") != meta["subpart"]:
            say(f"subpart {fm.get('subpart')!r} but the index says {meta['subpart']!r}")
        if fm.get("type") != meta["type"]:
            say(f"type {fm.get('type')!r}, expected {meta['type']!r}")
        got = sorted(c.strip(" '\"") for c in
                     fm.get("changed_in", "[]").strip("[]").split(",") if c.strip())
        if got != meta["changed_in"]:
            say(f"changed_in {got} but the index says {meta['changed_in']}")
        if len(meta["ids"]) > 1 and "covers" not in fm:
            say(f"merged note must list covers: {meta['ids']}")
        # covers: earns its place only when it says something the note name does
        # not -- a merge, or a note named differently from its single source
        # banner (AMC E 830 <- AMC E 830(c)). Thirty-three notes carried
        # covers: ["<their own name>"], which is pure noise.
        if "covers" in fm and len(meta["ids"]) == 1 and meta["ids"][0] == name:
            say("covers: repeats the note's own name — omit it")

        # --- sections
        for section in REQUIRED:
            if section not in text:
                say(f"missing section {section!r}")
        if "## Not applicable" in text:
            block = text.split("## Not applicable", 1)[1].split("\n## ", 1)[0]
            if not [ln for ln in block.splitlines() if ln.strip().startswith("-")]:
                say("'Not applicable' present but empty — omit it instead")

        # The template fixes the order of the tail sections, and drift here is
        # invisible one note at a time: eleven notes had put Amendment history
        # before References before this check existed.
        order = [ln.strip() for ln in text.splitlines() if ln.startswith("## ")]
        tail = [s for s in TAIL_ORDER if s in order]
        if [s for s in order if s in TAIL_ORDER] != tail:
            say(f"sections out of template order: expected {' then '.join(tail)}")

        # --- exactly one summary callout
        n = len(SUMMARY.findall(text))
        if n != 1:
            say(f"{n} [!summary] callouts, expected exactly 1")

        # --- every long quoted passage must be verbatim in the source.
        # Flatten first: a quote wrapped over several lines, or sitting inside a
        # "> " callout, is still one quotation.
        body_flat = " ".join(
            re.sub(r"^\s*>\s?", "", ln)
            for ln in text.split("---\n", 2)[-1].splitlines())
        haystack = source_text(meta["ids"])
        # The Amendment history section may quote the pre-amendment wording,
        # which is absent from Amendment 8 by definition. Split the body there.
        history = ""
        if "## Amendment history" in body_flat:
            body_flat, history = body_flat.split("## Amendment history", 1)
        pieces = body_flat.replace("\u201c", '"').replace("\u201d", '"').split('"')
        hist_pieces = history.replace("\u201c", '"').replace("\u201d", '"').split('"')
        for quoted in {q.strip() for q in pieces[1::2] + hist_pieces[1::2]}:
            if len(quoted) < MIN_QUOTE:
                continue
            parts = [f.strip() for f in quoted.split("…") if f.strip()]
            if all(norm(part) in haystack for part in parts):
                continue
            # A note may quote a paragraph it links to rather than one it covers.
            # The quotation must still be verbatim, just not necessarily from
            # this note's own paragraphs.
            if all(norm(part) in whole_document() for part in parts):
                continue
            # Only the Amendment history section may quote pre-amendment wording.
            if (quoted in history
                    and all(norm_stitched(part) in prior_wording()
                            for part in parts)):
                continue
            say(f"quoted passage not verbatim in source: {quoted[:70]!r}...")

        # A quotation inside a quotation defeats the positional pairing above:
        # the inner passage lands in an "outside" slice and is never checked.
        # Its signature is two quote marks with nothing between them.
        if '""' in body_flat.replace("\u201c", '"').replace("\u201d", '"'):
            say('nested quotation (\'""\') — the inner passage escapes the '
                "verbatim check; use an elision or restructure the sentence")

        # --- Requirement table
        if "## Requirement" in text:
            block = text.split("## Requirement", 1)[1].split("\n## ", 1)[0]
            # A three-column table is not automatically a Requirement table.
            # AMC E 620 sets out the notation for its formulae as
            # Symbol | Meaning | Unit, and "kW" is not an obligation strength.
            # Only a table headed Ref | Obligation | Strength is checked, and
            # `in_table` goes false at the blank line that ends it.
            in_table = False
            for row in block.splitlines():
                cells = [c.strip() for c in row.strip().strip("|").split("|")]
                if not row.strip():
                    in_table = False
                    continue
                if len(cells) != 3 or not row.strip().startswith("|"):
                    continue
                header = [c.replace("*", "").strip().lower() for c in cells]
                if header == ["ref", "obligation", "strength"]:
                    in_table = True
                    continue
                if not in_table:
                    continue
                strength = cells[2].replace("*", "").strip()
                if (not strength or strength in ("Strength", "---")
                        or set(strength) <= {"-", ":"}):
                    continue
                if strength not in STRENGTHS:
                    say(f"Strength {strength!r} is not one of the seven allowed values")
                ref = cells[0].replace("*", "").strip()
                if re.search(r"\)\s+\(", ref):
                    say(f"Ref {ref!r} splits nested sub-points — write (a)(2)")

        # --- link form and targets
        if LINK_PAREN.search(text):
            say("link-paren: [[X]](y) renders as a broken hyperlink on GitHub; "
                "use the alias form [[X|X(y)]]")
        body = text.split("---\n", 2)[-1]
        for target in {t.strip() for t in WIKILINK.findall(body)}:
            if target in expected:
                continue
            resolved = note_name(target)
            if resolved in expected:
                say(f"[[{target}]] — link to the note {resolved!r} instead")
            elif target in verdict:
                say(f"ghost-link [[{target}]] — that paragraph is {verdict[target]} "
                    "and gets no note; use plain text")
            else:
                say(f"bad-link [[{target}]] — not a note this vault contains")
        for img in {i.strip() for i in EMBED.findall(text)}:
            if not (VAULT / "figures" / img).exists():
                say(f"missing-image ![[{img}]] — not in vault/figures/")

        # --- stray characters
        for n, line in enumerate(text.splitlines(), 1):
            bad = {c for c in line if ord(c) > 127 and c not in ALLOWED_NON_ASCII}
            if bad:
                chars = ", ".join(f"{c!r} (U+{ord(c):04X})" for c in sorted(bad))
                say(f"line {n}: unexpected character {chars}")

        # --- terminology
        for banned in ("Book 1", "Book 2"):
            if banned in text:
                say(f"uses {banned!r} — CLAUDE.md bans it; "
                    "CS-E has CS and AMC paragraphs only")

    print(f"{len(seen)} notes checked, {len(expected)} expected in total "
          f"({len(set(expected) - seen)} not yet written)")
    for sp in sorted({e["subpart"] for e in expected.values()}):
        want = {n for n, e in expected.items() if e["subpart"] == sp}
        print(f"  Subpart {sp}: {len(want & seen)}/{len(want)}")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  {p}")
        return 1
    print("all clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
