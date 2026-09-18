# CS-E Amendment 8 — Turboshaft Vault

Turning **EASA CS-E Amendment 8** (262 pages of engine certification
specifications) into a linked Obsidian vault for a **rotorcraft turboshaft**
application, in plain B2-level English, with every statement traceable to a
paragraph number.

Not a summary of the whole document. The point is subtraction: of 176 paragraphs,
31 are piston-engine (out of scope), 16 more do not apply to a turboshaft, and
inside the 129 that remain, sub-points that cannot apply are cut and the cut is
recorded.

## Status

| | |
|---|---|
| Tooling | complete, all validators green |
| Applicability decided | **145 / 145** in-scope paragraphs |
| Before/after wording recovered | **29 / 29** changed paragraphs |
| **Notes written** | **3 / 129** ← the work itself has barely started |

The three notes so far are `vault/CS-E 10.md`, `vault/CS-E 40.md` and
`vault/AMC General.md`. `CS-E 40` is the one worth reading: it exercises every
pruning case.

## Where to look

Start with these five. Everything else is either input or regenerable.

| File | What it answers |
|---|---|
| `CLAUDE.md` | The rules. Audience, scope, accuracy rules, note template |
| `engine_profile.md` | The declared engine: ratings, control system, what is not claimed |
| `work/applicability.md` | Does each paragraph apply to a turboshaft, and why — with the text that decides it |
| `work/paragraph_index.csv` | Every paragraph: pages, figures, which amendment changed it |
| `work/redline.json` | What exactly changed, word by word, at Amdt 7 and Amdt 8 |

## Layout

```
CLAUDE.md          rules — read first
engine_profile.md  the declared engine configuration (project input)
vault/             THE DELIVERABLE. One note per paragraph, Obsidian-linked
source/            the five EASA PDFs, read-only, SHA-256 pinned
scripts/           extraction, classification, validation
work/              generated. 486 files of intermediate output — ignore unless
                   you are checking a specific extraction
```

`work/` is noisy on purpose: `text/` is one file per PDF page and `paragraphs/`
is one per paragraph, both kept so any claim in a note can be traced back without
reopening a PDF. All of it regenerates from `source/` in under a minute.

## Reproducing

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/extract_text.py         # pages     -> work/text/
.venv/bin/python scripts/paragraph_text.py       # paragraphs-> work/paragraphs/
.venv/bin/python scripts/build_index.py          # index     -> work/paragraph_index.csv
.venv/bin/python scripts/scope_evidence.py       # scope keyword evidence
.venv/bin/python scripts/build_applicability.py  # verdicts  -> work/applicability.md
.venv/bin/python scripts/extract_redline.py      # before/after -> work/redline.json
```

Order matters — `paragraph_text.py` establishes each paragraph's true page span
and `build_index.py` consumes it.

### Checks

```bash
.venv/bin/python scripts/verify_sources.py    # the five PDFs are intact and unmodified
.venv/bin/python scripts/audit_coverage.py    # every body line reached its paragraph
.venv/bin/python scripts/lint_vault.py        # notes agree with the index and the rules
```

`audit_coverage.py` is the important one. It re-derives which paragraph owns each
line directly from the PDF, independently of the slicer, and currently reports
**0 lost lines across 11,794**. An earlier version of the slicer silently dropped
294 lines; that is the failure mode this catches.

`lint_vault.py` rejects a note whose `Rule text` quote is not word-for-word in the
source, whose frontmatter contradicts the index, or that links to a paragraph
whose exclusion means it has no note.

## Sources

Five EASA documents, all free, all committed, all checksum-pinned — see
`source/SOURCES.md`. Only **CS-E Amendment 8** supplies requirement content. The
Change Information redlines and Amendment 7 are supporting: they say what changed,
and they are the guard against writing from stale recollection of an earlier
amendment.
