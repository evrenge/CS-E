#!/usr/bin/env python3
"""Phase 3 — check every vault note against the index and the CLAUDE.md rules.

Catches the mistakes that are invisible when writing one note at a time:

  ghost-link     a [[wikilink]] to a paragraph that gets no note (EXCLUDED, or
                 out of scope). CLAUDE.md requires those as plain text.
  bad-link       a [[wikilink]] to something that is not a paragraph id at all
  frontmatter    missing field, or a value that disagrees with the index
                 (pages, subpart, status, changed_in)
  sections       a required section missing, or Dropped present but empty
  rule-4         not exactly one "Rule text" callout
  orphan         a note whose paragraph is not classified APPLIES

Exit status is 0 only when every note passes.

Usage:
    python3 scripts/lint_vault.py
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from classification import CLASSIFICATION  # noqa: E402

VAULT = ROOT / "vault"
INDEX = ROOT / "work" / "paragraph_index.csv"
REQUIRED = ["## What it means", "## What we must do", "## Turboshaft note",
            "## Related", "## Notes"]
WIKILINK = re.compile(r"\[\[([^\]|#]+)")
FM_FIELD = re.compile(r"^(\w+):\s*(.*)$")


def main() -> int:
    verdict = {i: s for i, s, _ in CLASSIFICATION}
    index = {r["id"]: r for r in csv.DictReader(INDEX.open())}
    # Paragraphs that are entitled to a note.
    expected = {i for i, s in verdict.items() if s == "APPLIES"}

    problems: list[str] = []
    seen: set[str] = set()

    for note in sorted(VAULT.glob("*.md")):
        pid = note.stem
        text = note.read_text(encoding="utf-8")
        seen.add(pid)
        say = lambda msg: problems.append(f"{note.name}: {msg}")  # noqa: E731

        if pid not in expected:
            say(f"orphan — {pid!r} is {verdict.get(pid, 'not classified')}, not APPLIES")

        # --- frontmatter
        if not text.startswith("---\n"):
            say("frontmatter missing")
        else:
            fm_raw = text.split("---\n", 2)[1]
            fm = {}
            for line in fm_raw.splitlines():
                m = FM_FIELD.match(line)
                if m:
                    fm[m.group(1)] = m.group(2).strip()
            for field in ("id", "type", "subpart", "pages", "status", "changed_in", "tags"):
                if field not in fm:
                    say(f"frontmatter missing field {field!r}")
            row = index.get(pid)
            if row:
                want_pages = f"{row['start_page']}-{row['end_page']}"
                if fm.get("pages") != want_pages:
                    say(f"pages {fm.get('pages')!r} but index says {want_pages!r}")
                if fm.get("subpart") != row["subpart"]:
                    say(f"subpart {fm.get('subpart')!r} but index says {row['subpart']!r}")
                want_ch = ([] if row["changed_in"] == "none"
                           else row["changed_in"].split(";"))
                got_ch = [c.strip(" '\"") for c in
                          fm.get("changed_in", "[]").strip("[]").split(",") if c.strip()]
                if sorted(got_ch) != sorted(want_ch):
                    say(f"changed_in {got_ch} but index says {want_ch}")
            if fm.get("status") != "APPLIES":
                say(f"status {fm.get('status')!r}, expected APPLIES")
            want_type = "CS" if pid.startswith("CS-E") else "AMC"
            if fm.get("type") not in (want_type, "AMC" if pid == "AMC General" else want_type):
                say(f"type {fm.get('type')!r}, expected {want_type!r}")

        # --- sections
        for section in REQUIRED:
            if section not in text:
                say(f"missing section {section!r}")
        if "## Dropped" in text:
            block = text.split("## Dropped", 1)[1].split("\n## ", 1)[0]
            if not [ln for ln in block.splitlines() if ln.strip().startswith("-")]:
                say("Dropped section present but empty — omit it instead")

        # --- rule 4: exactly one Rule text callout
        n_quote = text.count("> [!quote] Rule text")
        if n_quote != 1:
            say(f"{n_quote} 'Rule text' callouts, expected exactly 1")

        # --- links
        body = text.split("---\n", 2)[-1]
        for target in {t.strip() for t in WIKILINK.findall(body)}:
            if target in expected:
                continue
            if target in verdict:
                say(f"ghost-link [[{target}]] — that paragraph is "
                    f"{verdict[target]} and gets no note; use plain text")
            elif target in index:
                say(f"ghost-link [[{target}]] — out of scope (subpart "
                    f"{index[target]['subpart']}); use plain text")
            else:
                say(f"bad-link [[{target}]] — not a paragraph id")

    print(f"{len(seen)} notes checked, {len(expected)} expected in total "
          f"({len(expected - seen)} not yet written)")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  {p}")
        return 1
    print("all clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
