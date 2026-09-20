# CS-E Amendment 8 — Turboshaft Vault

Turning **EASA CS-E Amendment 8** (262 pages of engine certification
specifications) into a linked Obsidian vault for a **rotorcraft turboshaft**
application, in plain B2-level English, with every statement traceable to a
paragraph number.

Not a summary of the whole document. The point is subtraction: of 176 paragraphs,
31 are piston-engine (Subparts B and C, out of scope), 17 more do not apply to a
turboshaft, and inside the 128 that remain, sub-points that cannot apply are cut
and the cut is recorded.

## Status

| | |
|---|---|
| Tooling | complete, all validators green |
| Applicability decided | **145 / 145** in-scope paragraphs |
| Before/after wording recovered | **29 / 29** changed paragraphs that apply |
| **Notes written** | **112 / 112** |
| Obligations extracted | **1,492** across the 112 notes |
| Open `[VERIFY]` items | **90** |
| Sub-points cut, each recorded | **121** |

112 notes rather than 128, because the vault holds **one AMC note per CS-E
number**: seven merged notes cover 23 separate AMC banners. `scripts/vault_map.py`
is the authority on which note a paragraph belongs to.

Start with `vault/CS-E 40.md`. It exercises every pruning case.

## Where to look

Everything else is either input or regenerable.

| File | What it answers |
|---|---|
| `CLAUDE.md` | The rules. Audience, scope, accuracy rules, note template |
| `engine_profile.md` | The declared engine: ratings, control system, what is not claimed |
| `vault/` | The deliverable — one note per paragraph, Obsidian-linked |
| `deck/compliance_matrix.xlsx` | Every obligation, with its strength and its note |
| `review/dead_ends.md` | What the vault cannot answer, and what it blocks |
| `review/phase4_findings.md` | What the verification passes found |
| `work/applicability.md` | Does each paragraph apply to a turboshaft, and why |
| `work/paragraph_index.csv` | Every paragraph: pages, figures, which amendment changed it |
| `work/redline.json` | What exactly changed, word by word, at Amdt 7 and Amdt 8 |

## Layout

```
CLAUDE.md          rules — read first
engine_profile.md  the declared engine configuration (project input)
vault/             THE DELIVERABLE. One note per paragraph, Obsidian-linked
deck/              compliance matrix, derived from the vault
review/            verification findings and the dead-end inventory
source/            the five EASA PDFs, read-only, SHA-256 pinned
scripts/           extraction, classification, validation, rendering
work/              generated. 486 files of intermediate output — ignore unless
                   you are checking a specific extraction
```

`work/` is noisy on purpose: `text/` is one file per PDF page and `paragraphs/`
is one per paragraph, both kept so any claim in a note can be traced back without
reopening a PDF. All of it regenerates from `source/` in under a minute.

The vault is built for Obsidian. On GitHub the `[[wikilinks]]` show as literal
text, because GitHub supports them only in wikis. That is expected.

## Reproducing

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/extract_text.py         # pages     -> work/text/
.venv/bin/python scripts/paragraph_text.py       # paragraphs-> work/paragraphs/
.venv/bin/python scripts/build_index.py          # index     -> work/paragraph_index.csv
.venv/bin/python scripts/scope_evidence.py       # scope keyword evidence
.venv/bin/python scripts/build_applicability.py  # verdicts  -> work/applicability.md
.venv/bin/python scripts/extract_redline.py      # before/after -> work/redline.json
.venv/bin/python scripts/build_matrix.py         # vault     -> deck/compliance_matrix.xlsx
```

Order matters — `paragraph_text.py` establishes each paragraph's true page span
and `build_index.py` consumes it.

### Checks

```bash
.venv/bin/python scripts/verify_sources.py    # the five PDFs are intact and unmodified
.venv/bin/python scripts/audit_coverage.py    # every body line reached its paragraph
.venv/bin/python scripts/lint_vault.py        # notes agree with the index and the rules
.venv/bin/python scripts/audit_cuts.py        # every recorded cut is a cut of real text
.venv/bin/python scripts/audit_citations.py   # citations resolve; numbers are the source's
.venv/bin/python scripts/external_refs.py     # every reference to a document we do not hold
```

`audit_coverage.py` is the important one. It re-derives which paragraph owns each
line directly from the PDF, independently of the slicer, and currently reports
**0 lost and 0 injected lines across 12,285**. An earlier version of the slicer
silently dropped 294 lines; that is the failure mode this catches.

`lint_vault.py` rejects a note whose quoted passage is not word-for-word in the
source, whose frontmatter contradicts the index, whose sections are out of
template order, that uses a `Strength` outside the seven allowed values, or that
links to a paragraph whose exclusion means it has no note.

`audit_cuts.py` checks the one thing `## Not applicable` exists to guarantee: that
a recorded cut is a cut of text the source actually contains. An entry describing
the removal of something the source never said asserts content into the
regulation, and is worse than a missing entry.

## Sources

Five EASA documents, all free, all committed, all checksum-pinned — see
`source/SOURCES.md`. Only **CS-E Amendment 8** supplies requirement content. The
Change Information redlines and Amendment 7 are supporting: they say what changed,
and they are the guard against writing from stale recollection of an earlier
amendment.

## Limits

`review/dead_ends.md` inventories the dead ends — points where a reader following
a reference leaves the vault and cannot come back with an answer. They fall into
three kinds: documents EASA cites and this repository does not hold, terms CS-E
uses and defines nowhere, and engine information the applicant has not yet
declared.

Two figures, and they count different things. `scripts/external_refs.py` derives
**45 distinct external references across 8 families** — Part 21, the AMC 20
series, CS-Definitions, CS-23/25/27/29, CS-34, FAA material and industry
standards. That one regenerates. The count of dead ends in `dead_ends.md` is the
reviewer's own deduplication across all three kinds, which is a judgement, not a
derivation; take the document's structure as the authority rather than any single
number.

Neither list is a defect. Both are the boundary of what these notes can answer.
