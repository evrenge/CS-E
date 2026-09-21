#!/usr/bin/env python3
"""Check every vault note against the index and the CLAUDE.md rules.

Catches the mistakes that are invisible when writing one note at a time:

  unexpected     a note whose name is not one the vault should contain
  frontmatter    a missing field, or a value that disagrees with the index
                 (pages, subpart, type, changed_in, covers, imports)
  sections       a required section missing, or 'Not applicable' present but empty
  summary        not exactly one [!summary] callout
  quote          a quoted passage of 40 characters or more that is not verbatim
                 anywhere in CS-E Amendment 8, or -- for an [ext ...] quotation --
                 in work/external/
  strength       a Strength cell outside the seven allowed values
  ref-format     a Ref cell splitting nested sub-points, e.g. "(a) (2)"
  import         an [ext ...] citation in a Requirement row (rule A), an id with
                 no slice in work/external/, or imports: that does not match the
                 documents the note actually cites (rule E)
  link-paren     [[X]](y), which GitHub parses as a link to the path "y"
  ghost-link     a [[wikilink]] to a note the vault will not contain
  missing-image  an ![[embed]] whose file is absent from vault/figures/
  terminology    the note uses "Book 1" or "Book 2", which CLAUDE.md bans

The notes in vault/external/ are checked too, against their own template: they
carry type: EXT and document:, they have no subpart, changed_in, applicability
verdict or cut list, and their quotations are checked against the document they
are about.

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
VAULT_EXT = VAULT / "external"
PARAS = ROOT / "work" / "paragraphs"
EXTERNAL = ROOT / "work" / "external"
SOURCE_EXT = ROOT / "source" / "external"
REDLINE = ROOT / "work" / "redline.json"

REQUIRED = ["## Requirement", "## Compliance", "## Application to this engine",
            "## References"]
# The template's tail, in order. A note carries any subset of these, but never
# out of this sequence.
TAIL_ORDER = ["## Requirement", "## Compliance", "## Application to this engine",
              "## Not applicable", "## References", "## Amendment history"]
# An external note is about another document, so it has no applicability verdict
# and no cut list. See CLAUDE.md, "External notes".
EXT_REQUIRED = ["## Requirement", "## Bearing on this engine", "## References"]
EXT_ORDER = ["## Requirement", "## Bearing on this engine", "## References"]
EXT_BANNED = ["## Application to this engine", "## Not applicable"]
STRENGTHS = {"Required", "Required if claimed", "Recommended",
             "Accepted method", "Permitted", "Relief", "Statement"}

WIKILINK = re.compile(r"(?<!!)\[\[([^\]|#]+)")
EMBED = re.compile(r"!\[\[([^\]|#]+)\]\]")
LINK_PAREN = re.compile(r"\]\]\(")
FM_FIELD = re.compile(r"^(\w+):\s*(.*)$")
SUMMARY = re.compile(r">\s*\[!summary\]")
EXT_CITE = re.compile(r"\[ext ([^\]]+)\]")
# Everything a note legitimately needs beyond ASCII: typography the house style
# uses, and the technical notation the source carries. Anything else is a slip —
# a stray CJK character once landed mid-sentence in CS-E 790 and read as a word.
ALLOWED_NON_ASCII = set("·—–…½°±×−√θ⁻⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉‘’“”")
# Quotation marks are paired by POSITION, not matched by a regex: a regex cannot
# tell an opening quote from a closing one, so it matches the prose BETWEEN two
# separate quotations and reports it as unverifiable.
MIN_QUOTE = 40

# The document an [ext ...] id belongs to, where no slice names it. The keys are
# matched as a prefix of the id, longest first.
DOC_PREFIX = [
    ("CS-Definitions", "CS-Definitions"),
    ("AMC 20", "AMC-20"),
    ("AMC1 20", "AMC-20"),
    ("CS 27.", "CS-27"),
    ("CS 29.", "CS-29"),
    ("CS 34.", "CS-34"),
    ("AMC 27.", "CS-27"), ("AMC1 27.", "CS-27"), ("AMC2 27.", "CS-27"),
    ("AMC 29.", "CS-29"), ("AMC1 29.", "CS-29"), ("AMC2 29.", "CS-29"),
    ("GM1 34.", "CS-34"), ("GM2 34.", "CS-34"),
    ("21.A.", "Part 21"), ("21.B.", "Part 21"),
    ("AMC1 21.", "Part 21"), ("AMC 21.", "Part 21"),
    ("GM1 21.", "Part 21"), ("GM2 21.", "Part 21"), ("GM 21.", "Part 21"),
]
# The documents whose cited paragraphs are sliced into work/external/. An id
# belonging to one of these and matching no slice is a missing slice, not a
# document the vault simply does not hold in that form.
SLICED_DOCS = {"CS-27", "CS-29", "CS-34", "Part 21", "CS-Definitions", "AMC-20"}
# source/external/ filename -> the label a note writes in imports:
DOC_OF_FILE = {
    "CS-27_Amendment_10.pdf": "CS-27",
    "CS-29_Amendment_12.pdf": "CS-29",
    "CS-34_Amendment_4_repealed.pdf": "CS-34",
    "Part-21_EAR_Reg-748-2012_Nov-2025.pdf": "Part 21",
    "CS-Definitions_Amendment_2.pdf": "CS-Definitions",
    "AMC-20_Amendment_23.pdf": "AMC-20",
    "EN_to_ED_Decision_2025-005-R_CS-34-repeal.pdf": "ED Decision 2025/005/R",
}


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


_EXT_SLICES: dict[str, tuple[str, str]] | None = None


def ext_slices() -> dict[str, tuple[str, str]]:
    """Every sliced external paragraph: id -> (document label, its text).

    Built from the headers `external_paragraphs.py` writes, so adding a point to
    its WANTED table is all it takes to make that point quotable.
    """
    global _EXT_SLICES
    if _EXT_SLICES is None:
        _EXT_SLICES = {}
        for f in sorted(EXTERNAL.glob("*.txt")):
            lines = f.read_text(encoding="utf-8").splitlines()
            pid = fname = ""
            for line in lines[:6]:
                if line.startswith("# id: "):
                    pid = line[6:].strip()
                elif line.startswith("# source: "):
                    fname = line[10:].strip().split("/")[-1]
            if not pid:
                continue
            body = norm(" ".join(ln for ln in lines if not ln.startswith("#")))
            _EXT_SLICES[pid] = (DOC_OF_FILE.get(fname, fname), body)
    return _EXT_SLICES


_EXT_WHOLE: str | None = None


def external_document() -> str:
    """Every sliced external paragraph, as one haystack.

    Accuracy rule 4 does not weaken for imported material: a quotation from
    CS-29 or Part 21 is checked word-for-word the way a CS-E quotation is. This
    is the haystack that makes that possible, and the reason
    `external_paragraphs.py` exists.
    """
    global _EXT_WHOLE
    if _EXT_WHOLE is None:
        _EXT_WHOLE = norm(" ".join(t for _, t in ext_slices().values()))
    return _EXT_WHOLE


def ext_document(cid: str) -> tuple[str | None, bool]:
    """(document label, whether a slice covers it) for an [ext ...] id."""
    hits = [pid for pid in ext_slices() if cid == pid or cid.startswith(pid)]
    if hits:
        return ext_slices()[max(hits, key=len)][0], True
    for prefix, doc in sorted(DOC_PREFIX, key=lambda p: -len(p[0])):
        if cid.startswith(prefix):
            return doc, False
    return None, False


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


# --- checks a CS-E note and an external note share ---------------------------

def check_frontmatter(text, say) -> dict[str, str]:
    if not text.startswith("---\n"):
        say("frontmatter missing")
        return {}
    fm = {}
    for line in text.split("---\n", 2)[1].splitlines():
        m = FM_FIELD.match(line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm


def fm_list(value: str) -> list[str]:
    return sorted(c.strip(" '\"") for c in value.strip("[]").split(",")
                  if c.strip())


def check_self_link(text, name, say) -> None:
    """A note that links to itself sends the reader to the page they are on.

    The alias form hides that it does. Ten notes did.
    """
    for m in re.finditer(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", text):
        if m.group(1).strip() == name:
            say(f"links to itself: {m.group(0)}")
            break


def check_heading_spacing(text, say) -> None:
    """A "## " heading needs a blank line before it.

    Obsidian and GitHub both fold it into the preceding paragraph otherwise.
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("## ") and i and lines[i - 1].strip():
            say(f"no blank line before {line!r}")


def check_section_order(text, template, say) -> None:
    """The template fixes the order of the sections.

    Drift here is invisible one note at a time: eleven notes had put Amendment
    history before References before this check existed.
    """
    order = [ln.strip() for ln in text.splitlines() if ln.startswith("## ")]
    tail = [s for s in template if s in order]
    if [s for s in order if s in template] != tail:
        say(f"sections out of template order: expected {' then '.join(tail)}")


def check_summary(text, say) -> None:
    n = len(SUMMARY.findall(text))
    if n != 1:
        say(f"{n} [!summary] callouts, expected exactly 1")


def check_quotes(text, haystacks, say, allow_prior=False) -> None:
    """Every quoted passage of MIN_QUOTE characters or more must be verbatim.

    Flatten first: a quote wrapped over several lines, or sitting inside a
    "> " callout, is still one quotation.
    """
    body_flat = " ".join(
        re.sub(r"^\s*>\s?", "", ln)
        for ln in text.split("---\n", 2)[-1].splitlines())
    # The Amendment history section may quote the pre-amendment wording, which
    # is absent from Amendment 8 by definition. Split the body there.
    history = ""
    if allow_prior and "## Amendment history" in body_flat:
        body_flat, history = body_flat.split("## Amendment history", 1)
    pieces = body_flat.replace("“", '"').replace("”", '"').split('"')
    hist_pieces = history.replace("“", '"').replace("”", '"').split('"')
    for quoted in {q.strip() for q in pieces[1::2] + hist_pieces[1::2]}:
        if len(quoted) < MIN_QUOTE:
            continue
        parts = [f.strip() for f in quoted.split("…") if f.strip()]
        if any(all(norm(part) in hay() for part in parts) for hay in haystacks):
            continue
        # Only the Amendment history section may quote pre-amendment wording.
        if (allow_prior and quoted in history
                and all(norm_stitched(part) in prior_wording() for part in parts)):
            continue
        say(f"quoted passage not verbatim in source: {quoted[:70]!r}...")

    # A quotation inside a quotation defeats the positional pairing above: the
    # inner passage lands in an "outside" slice and is never checked. Its
    # signature is two quote marks with nothing between them.
    if '""' in body_flat.replace("“", '"').replace("”", '"'):
        say('nested quotation (\'""\') — the inner passage escapes the '
            "verbatim check; use an elision or restructure the sentence")


def check_requirement_table(text, say, ban_imports=False) -> None:
    """Strength values, Ref formatting, and rule A.

    A three-column table is not automatically a Requirement table. AMC E 620
    sets out the notation for its formulae as Symbol | Meaning | Unit, and "kW"
    is not an obligation strength. Only a table headed Ref | Obligation |
    Strength is checked, and `in_table` goes false at the blank line that ends
    it.
    """
    if "## Requirement" not in text:
        return
    block = text.split("## Requirement", 1)[1].split("\n## ", 1)[0]
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
        # Rule A: in a CS-E note the Requirement table is the 1:1 map to CS-E,
        # and it is the part a reader trusts without checking. An imported
        # obligation in it destroys exactly that.
        if ban_imports and "[ext " in row:
            say(f"[ext ...] in a Requirement row — rule A puts an imported "
                f"obligation in Compliance or in prose: {row.strip()[:60]!r}")


def check_table_rows(text, say) -> None:
    """A table row with the wrong number of cells.

    It breaks the table on GitHub from that line down, and Obsidian renders it
    anyway, so the damage is invisible in the editor the vault is written in.
    The usual cause is an aliased wikilink in a cell: the "|" in
    [[CS-E 110|CS-E 110(e)]] is read as a column separator. Use the citation
    form, [CS-E 110(e)], in a cell.
    """
    rows = text.splitlines()
    k = 0
    while k < len(rows):
        head = rows[k].strip()
        if (head.startswith("|") and k + 1 < len(rows)
                and re.fullmatch(r"\|[\s\-:|]+\|", rows[k + 1].strip())):
            cols = head.strip("|").count("|") + 1
            m = k + 2
            while m < len(rows) and rows[m].strip().startswith("|"):
                got = rows[m].strip().strip("|").count("|") + 1
                if got != cols:
                    say(f"table row has {got} cells, header has {cols}: "
                        f"{rows[m].strip()[:60]!r}")
                m += 1
            k = m
        else:
            k += 1


def check_links(text, say, targets) -> None:
    if LINK_PAREN.search(text):
        say("link-paren: [[X]](y) renders as a broken hyperlink on GitHub; "
            "use the alias form [[X|X(y)]]")
    body = text.split("---\n", 2)[-1]
    verdict = targets["verdict"]
    known = targets["notes"]
    for target in {t.strip() for t in WIKILINK.findall(body)}:
        if target in known:
            continue
        resolved = note_name(target)
        if resolved in known:
            say(f"[[{target}]] — link to the note {resolved!r} instead")
        elif target in verdict:
            say(f"ghost-link [[{target}]] — that paragraph is {verdict[target]} "
                "and gets no note; use plain text")
        else:
            say(f"bad-link [[{target}]] — not a note this vault contains")
    for img in {i.strip() for i in EMBED.findall(text)}:
        if not (VAULT / "figures" / img).exists():
            say(f"missing-image ![[{img}]] — not in vault/figures/")


def check_imports(text, fm, say, require_field=True) -> set[str]:
    """Rules B and E: every [ext ...] id resolves, and imports: matches them."""
    docs: set[str] = set()
    for cid in {c.strip() for c in EXT_CITE.findall(text)}:
        doc, sliced = ext_document(cid)
        if doc is None:
            say(f"[ext {cid}] — id belongs to no document this vault holds")
            continue
        docs.add(doc)
        if not sliced and doc in SLICED_DOCS:
            say(f"[ext {cid}] — no slice in work/external/; add the point to "
                "WANTED in external_paragraphs.py")
    if not require_field:
        return docs
    declared = set(fm_list(fm.get("imports", "[]")))
    if docs and "imports" not in fm:
        say(f"cites {sorted(docs)} but frontmatter has no imports:")
    elif declared != docs:
        say(f"imports: {sorted(declared)} but the note cites {sorted(docs)}")
    return docs


def check_characters(text, say) -> None:
    for n, line in enumerate(text.splitlines(), 1):
        bad = {c for c in line if ord(c) > 127 and c not in ALLOWED_NON_ASCII}
        if bad:
            chars = ", ".join(f"{c!r} (U+{ord(c):04X})" for c in sorted(bad))
            say(f"line {n}: unexpected character {chars}")


def check_terminology(text, say) -> None:
    for banned in ("Book 1", "Book 2"):
        if banned in text:
            say(f"uses {banned!r} — CLAUDE.md bans it; "
                "CS-E has CS and AMC paragraphs only")


# --- the two passes ----------------------------------------------------------

def check_cse_notes(expected, targets, problems) -> set[str]:
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

        fm = check_frontmatter(text, say)
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
        got = fm_list(fm.get("changed_in", "[]"))
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

        for section in REQUIRED:
            if section not in text:
                say(f"missing section {section!r}")
        if "## Not applicable" in text:
            block = text.split("## Not applicable", 1)[1].split("\n## ", 1)[0]
            if not [ln for ln in block.splitlines() if ln.strip().startswith("-")]:
                say("'Not applicable' present but empty — omit it instead")

        check_self_link(text, name, say)
        check_heading_spacing(text, say)
        check_section_order(text, TAIL_ORDER, say)
        # A changed paragraph must say what changed. The reverse is not
        # required: where changed_in is empty the section is optional, and
        # carried only when it adds something the frontmatter cannot.
        if meta["changed_in"] and "## Amendment history" not in text:
            say(f"changed_in is {meta['changed_in']} but there is no "
                "'## Amendment history' section")
        check_summary(text, say)
        check_quotes(text,
                     [lambda ids=meta["ids"]: source_text(ids),
                      whole_document, external_document],
                     say, allow_prior=True)
        check_requirement_table(text, say, ban_imports=True)
        check_table_rows(text, say)
        check_links(text, say, targets)
        check_imports(text, fm, say)
        check_characters(text, say)
        check_terminology(text, say)
    return seen


def check_external_notes(targets, problems) -> set[str]:
    """The notes in vault/external/, against the external-note template."""
    seen: set[str] = set()
    if not VAULT_EXT.exists():
        return seen
    files = {f.name for f in SOURCE_EXT.glob("*.pdf")}
    for note in sorted(VAULT_EXT.glob("*.md")):
        name = note.stem
        text = note.read_text(encoding="utf-8")
        seen.add(name)
        say = lambda msg: problems.append(f"external/{note.name}: {msg}")  # noqa: E731

        fm = check_frontmatter(text, say)
        for field in ("id", "type", "document", "tags"):
            if field not in fm:
                say(f"frontmatter missing field {field!r}")
        if fm.get("type") != "EXT":
            say(f"type {fm.get('type')!r}, expected 'EXT'")
        if fm.get("id", "").strip("'\"") != name:
            say(f"id {fm.get('id')!r} but the file is named {name!r}")
        doc = fm.get("document", "").strip("'\"")
        if doc and doc not in files:
            say(f"document {doc!r} is not a file in source/external/")
        for field in ("subpart", "changed_in", "pages"):
            if field in fm:
                say(f"frontmatter carries {field!r}, which means nothing "
                    "outside CS-E")

        for section in EXT_REQUIRED:
            if section not in text:
                say(f"missing section {section!r}")
        for section in EXT_BANNED:
            if section in text:
                say(f"carries {section!r} — an external note records what the "
                    "paragraph says, not a CS-E scope verdict")

        check_self_link(text, name, say)
        check_heading_spacing(text, say)
        check_section_order(text, EXT_ORDER, say)
        check_summary(text, say)
        # The note's own paragraph first, then the rest of the external corpus:
        # an external note may quote a point it cross-refers to, exactly as a
        # CS-E note may. CS-E is a haystack here too, because an external note
        # quotes the CS-E paragraph it bears on -- that is its whole subject.
        own = ext_slices().get(name)
        check_quotes(text,
                     [lambda t=own: t[1] if t else "", external_document,
                      whole_document],
                     say)
        if own is None:
            say(f"no slice in work/external/ for {name!r}; add the point to "
                "WANTED in external_paragraphs.py")
        check_requirement_table(text, say)
        check_table_rows(text, say)
        check_links(text, say, targets)
        # `document:` already names the source, so imports: would repeat it.
        check_imports(text, fm, say, require_field=False)
        if "imports" in fm:
            say("imports: repeats document: — omit it in an external note")
        check_characters(text, say)
        check_terminology(text, say)
    return seen


def main() -> int:
    verdict = {i: s for i, s, _ in CLASSIFICATION}
    expected = expected_notes(verdict)
    problems: list[str] = []
    ext_names = {f.stem for f in VAULT_EXT.glob("*.md")} if VAULT_EXT.exists() else set()
    targets = {"verdict": verdict, "notes": set(expected) | ext_names}

    seen = check_cse_notes(expected, targets, problems)
    seen_ext = check_external_notes(targets, problems)

    print(f"{len(seen)} notes checked, {len(expected)} expected in total "
          f"({len(set(expected) - seen)} not yet written)")
    for sp in sorted({e["subpart"] for e in expected.values()}):
        want = {n for n, e in expected.items() if e["subpart"] == sp}
        print(f"  Subpart {sp}: {len(want & seen)}/{len(want)}")
    if seen_ext:
        print(f"  External: {len(seen_ext)} note(s) in vault/external/")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  {p}")
        return 1
    print("all clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
