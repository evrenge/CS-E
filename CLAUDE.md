# Project: CS-E Amendment 8 — Turboshaft Plain-Language Vault

## Audience
Turkish gas turbine engineers. Strong technical background, English is a second language.
Target English level: B2. Short sentences (max ~20 words). Active voice. No legal phrasing.
Define every regulatory term on first use. Keep technical terms (surge, TGT, LCF, OEI) as-is.

## Source of truth
- source/CS-E_Amendment_8.pdf is the ONLY authority for requirement content.
- Change Information PDFs are used ONLY to tag what changed in Amdt 7 / Amdt 8.
- Never use memory or general knowledge for requirement content. If the source does not say it, it does not go in a note.

## Scope
- Turbine engine rules only: Subparts A, D, E, F (per CS-E 10(d)). Exclude Subparts B and C.
- Turboshaft (rotorcraft) application only. Classify every paragraph as
  APPLIES / EXCLUDED (give reason). A paragraph classified EXCLUDED gets no note.
- Aeroplane-only AMCs, thrust reverser, propeller, ETOPS, and the turbofan alternate
  endurance test CS-E 740(c)(4) are EXCLUDED unless the text says otherwise.

### Pruning inside a note (the point of this vault)
Cutting whole paragraphs is not enough. Most paragraphs that apply still contain
sub-points that are dead ends for a turboshaft — piston ratings, aeroplane-only
schedules, propeller clauses, turbofan cases. Cut them.

- Drop any sub-point that cannot apply to this engine. Do not paraphrase it, do
  not "cover it briefly".
- Keep an out-of-scope sub-point ONLY when it changes what we must do: it sets a
  contrast that defines our case (CS-E 800's aeroplane 200 kt vs the rotorcraft
  speed), or our case is written as an alternative to it (CS-E 790(b) is an
  alternative to CS-E 790(a)(2)).
- Every cut is recorded in the note's `Dropped` section, one line, with the
  sub-point reference and the reason. A reader must always be able to tell
  "deliberately excluded" from "forgotten". Silent omission is a defect.
- Record the cut, never the content: `Dropped` says what was removed and why, not
  what it said.

## Engine variables
Declared in `engine_profile.md`, which also maps the applicant's rating names onto
CS-E terms and records the open [VERIFY] items. Summary:
- OEI ratings claimed: 30-Second OEI, 2-Minute OEI, Continuous OEI.
  NOT claimed: 2.5-Minute OEI, 30-Minute OEI.
- 30-Minute Power rating: yes, CS-E 40(b)(4) Rated 30-Minute Power
- Control system: EECS-FADEC, full authority
- Refrigerant injection: no
- Time-limited dispatch claimed: no
- 'OEI override' is a control-system feature, not a rating: assess under CS-E 50,
  not CS-E 40

## Accuracy rules (non-negotiable)
1. Every statement in a note carries its paragraph reference, e.g. [CS-E 740(c)(3)].
2. Preserve obligation strength exactly: CS "must" -> "Required"; AMC "should" -> "Accepted method".
   Never upgrade or downgrade.
3. Copy all numbers, times, percentages, probabilities exactly, with units.
4. One short verbatim quote (max 1 sentence) per note from the key CS text, in the "Rule text" callout.
5. If unsure about meaning or applicability, write [VERIFY: reason]. Never guess.
6. For pages with figures or tables, render the page to PNG and read the image. Do not rely on extracted text.
7. Never cap a list. Every obligation in an applicable sub-point reaches the note.
   When `What we must do` exceeds ~10 items, group them under `###` sub-headings by
   theme instead of trimming. Dropping an obligation to fit a length target is the
   same defect as silent omission.
8. A note never repeats content that has its own note. Link to it instead. Two
   copies of the same requirement drift apart, and the graph exists precisely so
   that one copy can serve every reader.

## Note template (Obsidian, one file per paragraph, `vault/`)
Filename is the paragraph id: `CS-E 740.md`, `AMC E 740(c)(3).md`.

```markdown
---
id: "CS-E 740"
type: CS                     # CS | AMC
subpart: E
pages: 138-149
status: APPLIES
changed_in: [Amdt8]          # [] when unchanged
tags: [endurance, oei, test]
---
# CS-E 740 — Endurance Tests

> [!quote] Rule text
> "<one original sentence>" — CS-E 740(c)(3)(i)

## What it means
2-4 plain sentences, B2 level, max ~20 words each, active voice.

## What we must do
- test / analysis / document items, each with its [ref]
- over ~10 items, group under `###` sub-headings by theme — never trim (rule 7)

## Turboshaft note
Rotorcraft-specific point, or "None".

## Dropped
- CS-E 740(c)(4) — turbofan alternate endurance test, not applicable.
- CS-E 740(c)(1) Part 1 aeroplane schedule — superseded by the rotorcraft case.

## Accepted means
[[AMC E 740(c)(3)]] · [[AMC E 740(i)(2)]]

## Related
[[CS-E 730]] · [[CS-E 50]]

## Notes
Only what belongs nowhere else: what changed at Amdt 7/8 and why it matters,
worked examples, and [VERIFY] items. Detail that has its own note is linked,
never restated (rule 8).
```

An AMC note carries `## Specification` linking back to its parent CS instead of
`## Accepted means`. A note with nothing cut omits `## Dropped` entirely.

## Working method
- Work subpart by subpart. Write output to files. Do not hold the whole document in context.
- Notes are generated into `vault/`. Out-of-scope cross-references are rendered as
  plain text, never as links, so the graph has no ghost nodes.
- Stop at every checkpoint in the task prompt and wait for my approval.

---

# Repository reference

Rules and invariants only. **Measured or derived values do not belong in this
file** — they go stale and then mislead. Anything a script can recompute lives in
`work/` or in `source/SOURCES.md`.

## Layout

```
.
├── CLAUDE.md                # this file — rules
├── engine_profile.md        # declared engine configuration — project input
├── requirements.txt
├── source/                  # EASA source PDFs, read-only. See source/SOURCES.md
├── scripts/                 # extraction, indexing, classification, rendering
└── work/                    # everything derived. Regenerate, never hand-edit
    ├── text/                # one file per PDF page
    ├── paragraphs/          # one file per CS-E / AMC paragraph
    ├── spans.json           # true page span per paragraph
    ├── paragraph_index.csv  # id, title, subpart, pages, figures, changed_in
    ├── applicability.md     # turboshaft verdict + reason per paragraph
    └── phase1_report.md
```

Where to look instead of trusting a number written here:

| Question | Source of truth |
|---|---|
| Which paragraphs changed, and at which amendment | `work/paragraph_index.csv` (`changed_in`, `changed_refs`) |
| Does a paragraph apply to a turboshaft, and why | `work/applicability.md` |
| Page counts, checksums, provenance | `source/SOURCES.md`, `source/CHECKSUMS.sha256` |
| Declared ratings and systems | `engine_profile.md` |

## Regenerating

```bash
.venv/bin/python scripts/extract_text.py         # pages  -> work/text/, work/pages.json
.venv/bin/python scripts/paragraph_text.py       # paras  -> work/paragraphs/, work/spans.json
.venv/bin/python scripts/build_index.py          # index  -> work/paragraph_index.csv
.venv/bin/python scripts/scope_evidence.py       # scope keyword evidence
.venv/bin/python scripts/build_applicability.py  # verdicts -> work/applicability.md
.venv/bin/python scripts/lint_vault.py           # vault notes vs index and rules
.venv/bin/python scripts/verify_sources.py       # source integrity
```

Order matters: `paragraph_text.py` establishes the true page span of each
paragraph (`work/spans.json`) and `build_index.py` consumes it. Deriving the span
any other way gets it wrong wherever a heading banner sits part-way down a page.

`build_applicability.py` fails loudly if the classification and the index
disagree, or if the topic grouping misses a paragraph that applies.
`lint_vault.py` fails on a ghost wikilink, frontmatter that contradicts the index,
a missing section, or a note for a paragraph that is not APPLIES. Trust them over
any prose.

## Redline marking scheme

Both Change Information PDFs mark changes the same way:

| Change | How it is drawn | How to detect it |
|---|---|---|
| Inserted | black text on a **cyan** highlight | filled rectangle, non-stroking colour `0 1 1`, behind the run |
| Deleted | **red** text with a strikethrough rule | text fill `1 0 0 rg` plus a red rule rectangle |
| Unchanged | plain black, nothing behind it | neither |

`extract_text()` drops both markers and merges deleted and inserted words into one
run, producing sentences that read as normative but exist in no amendment. Read
the content stream (`visitor_operand_before` for fill colour and rectangle
geometry) or render the page. Amendment-level tagging does not need any of this:
both files declare their changes in prose, which parses cleanly.

## Page rendering

Accuracy rule 6 needs a rasteriser. `pypdfium2`:
`PdfDocument(path)[i].render(scale=2).to_pil()`. No system package required.

## Environment

Python 3.11, virtualenv at `.venv`. The sandbox image ships a broken system
`cryptography`, so install into the virtualenv, never with
`pip --break-system-packages`.

`www.easa.europa.eu` is blocked by the sandbox egress policy, so a remote session
cannot re-fetch a source. All five are committed, so this does not affect normal
work.

## Working rules for `source/`

- `source/` is **read-only input**. Never edit or re-save a PDF there — it changes
  the SHA-256 and breaks provenance. Re-fetch and update `CHECKSUMS.sha256`
  deliberately.
- Cite paragraph numbers, never page numbers — pagination shifts between
  amendments.
- `work/` is generated. Regenerate rather than hand-edit.
