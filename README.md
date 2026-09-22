# CS-E Amendment 8 — Turboshaft Vault

This project turns **EASA CS-E Amendment 8** (262 pages of engine certification
specifications) into a linked Obsidian vault for a **rotorcraft turboshaft**
application. The vault is written in plain B2-level English, and every statement
traces to a paragraph number.

The vault is not a summary of the whole document. Its method is subtraction. Of
176 paragraphs, 31 are piston-engine paragraphs (Subparts B and C, out of
scope), and 17 more do not apply to a turboshaft. Inside the 128 that remain,
sub-points that cannot apply are cut, and each cut is recorded.

## Status

| | |
|---|---|
| Tooling | complete, all validators green |
| Applicability decided | **145 / 145** in-scope paragraphs |
| Before/after wording recovered | **29 / 29** changed paragraphs that apply |
| **Notes written** | **112 / 112** |
| Obligations extracted | **1,516** across the 112 notes |
| Open `[VERIFY]` items | **105** in CS-E notes, **14** in external notes |
| Sub-points cut, each recorded | **129** |
| External notes | **5** in `vault/external/` |
| Imported obligations | **92**, from seven documents outside CS-E |
| Graph | **117 notes, one connected component**, no note without an inbound link |

The vault holds 112 notes rather than 128, because it keeps **one AMC note per
CS-E number**: seven merged notes cover 23 separate AMC banners.
`scripts/vault_map.py` is the authority on which note a paragraph belongs to.

Start with `vault/CS-E 40.md`. It exercises every pruning case.

## Where to look

The files below answer most questions. Everything else in the repository is
either input or can be regenerated.

| File | What it answers |
|---|---|
| `CLAUDE.md` | The rules. Audience, scope, accuracy rules, note template |
| `engine_profile.md` | The declared engine: ratings, control system, what is not claimed |
| `vault/` | The deliverable — one note per paragraph, Obsidian-linked |
| `deck/compliance_matrix.xlsx` | Every obligation, with its strength and its note |
| `review/dead_ends.md` | What the vault cannot answer, and what it blocks |
| `work/applicability.md` | Does each paragraph apply to a turboshaft, and why |
| `work/paragraph_index.csv` | Every paragraph: pages, figures, which amendment changed it |
| `work/redline.json` | What exactly changed, word by word, at Amdt 7 and Amdt 8 |

## Layout

```
CLAUDE.md          rules — read first
engine_profile.md  the declared engine configuration (project input)
vault/             THE DELIVERABLE. One note per paragraph, Obsidian-linked
vault/external/    notes on paragraphs of other documents, where the material
                   is too large to import into a CS-E note
deck/              compliance matrix, derived from the vault
review/            the dead-end inventory
source/            the four EASA CS-E PDFs, read-only, SHA-256 pinned
source/external/   documents CS-E cites and does not contain — CS-27, CS-29,
                   CS-Definitions, AMC-20, Part 21, CS-34. Not requirement
                   content
scripts/           extraction, classification, validation, rendering
work/              generated intermediate output — ignore unless you are
                   checking a specific extraction
```

`work/` is noisy on purpose. `text/` holds one file per PDF page and
`paragraphs/` one file per paragraph. Both are kept so that any claim in a note
can be traced back without reopening a PDF. All of it regenerates from `source/`
in under a minute.

The vault is built for Obsidian. On GitHub the `[[wikilinks]]` show as literal
text, because GitHub supports them only in wikis. That is expected.

## Reproducing

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/extract_text.py         # pages        -> work/text/
.venv/bin/python scripts/paragraph_text.py       # paragraphs   -> work/paragraphs/
.venv/bin/python scripts/build_index.py          # index        -> work/paragraph_index.csv
.venv/bin/python scripts/scope_evidence.py       # scope keyword evidence
.venv/bin/python scripts/build_applicability.py  # verdicts     -> work/applicability.md
.venv/bin/python scripts/extract_redline.py      # before/after -> work/redline.json
.venv/bin/python scripts/external_paragraphs.py  # cited external points -> work/external/
.venv/bin/python scripts/build_matrix.py         # vault        -> deck/compliance_matrix.xlsx
```

Order matters: `paragraph_text.py` establishes the true page span of each
paragraph, and `build_index.py` consumes it.

### Checks

```bash
.venv/bin/python scripts/verify_sources.py       # all source PDFs, CS-E and external, are intact
.venv/bin/python scripts/audit_coverage.py       # every body line reached its paragraph
.venv/bin/python scripts/lint_vault.py           # notes agree with the index and the rules
.venv/bin/python scripts/audit_cuts.py           # every recorded cut is a cut of real text
.venv/bin/python scripts/audit_citations.py      # citations resolve; numbers are the source's
.venv/bin/python scripts/external_refs.py        # every reference out of CS-E, held or not
```

`audit_coverage.py` is the most important check. It re-derives which paragraph
owns each line directly from the PDF, independently of the slicer. It currently
reports **0 lost and 0 injected lines across 12,285**. An earlier version of the
slicer silently dropped 294 lines, and this check catches that failure mode.

`lint_vault.py` rejects a note whose quoted passage is not word-for-word in the
source, whose frontmatter contradicts the index, whose sections are out of
template order, that uses a `Strength` outside the seven allowed values, or that
links to a paragraph whose exclusion means it has no note.

`audit_cuts.py` checks the one thing `## Not applicable` exists to guarantee:
that a recorded cut is a cut of text the source actually contains. An entry that
describes the removal of something the source never said asserts content into
the regulation, and is worse than a missing entry.

## Sources

The vault rests on four EASA documents. All are free, committed and
checksum-pinned; see `source/SOURCES.md`. Only **CS-E Amendment 8** supplies
requirement content. The Change Information redlines and Amendment 7 play a
supporting role: they say what changed, and they guard against writing from
stale recollection of an earlier amendment.

## Limits

`review/dead_ends.md` inventories the dead ends. A dead end is a point where a
reader who follows a reference leaves the vault and cannot come back with an
answer. Dead ends fall into three kinds: documents CS-E cites and this
repository does not hold, terms CS-E uses and defines nowhere, and engine
information the applicant has not yet declared.

`scripts/external_refs.py` derives every reference out of CS-E and marks each
family held or not held. Run it for the current count. At the time of writing,
three quarters of the references point into a document that `source/external/`
holds, and can be followed.

Those references are followed. `source/external/` holds seven documents —
CS-27, CS-29, CS-Definitions, AMC-20, the Easy Access Rules edition of Part 21,
CS-34 as repealed, and the repeal's explanatory note. The points the vault cites
are sliced into `work/external/`. A note cites one as `[ext <id>]` and declares
the document in its `imports:` frontmatter. A quotation from CS-29 or Part 21 is
checked word-for-word, the same way as a CS-E quotation. `CLAUDE.md`, **Imported
obligations**, has the five rules that keep a CS-E obligation distinguishable
from an imported one.

What remains dead is the paywalled and foreign material named inside those
documents: ED-14 and DO-160, ISO 2685, the FAA advisory circulars, the SAE ARP
series, and ICAO Annex 16 at the far end of the emissions chain.

None of these limits is a defect. Together they mark the boundary of what these
notes can answer.
