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
2. Preserve obligation strength exactly. Use only the seven terms in
   **Obligation strength** below, chosen by the source's own verb. Never upgrade
   or downgrade, and never invent a wording outside that list.
3. Copy all numbers, times, percentages, probabilities exactly, with units.
4. Quote verbatim wherever exact wording is decisive, in quotation marks with its
   reference — never as decoration. A quoted passage of 40 characters or more is
   checked word-for-word against the source. The note opens with a `[!summary]`
   callout, not a quotation: repeating the first sentence duplicates what the
   Requirement table already states.
5. If unsure about meaning or applicability, write [VERIFY: reason]. Never guess.
6. For figures and tables, embed the cropped image in the note rather than
   describing it. The content is absent from the text layer, so a description is
   an unverifiable restatement. See **Figures**.
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
changed_in: [Amdt8]          # [] when unchanged
tags: [endurance, oei, test]
covers: ["AMC E 740(c)(3)", ...]   # merged AMC notes only; omit otherwise
---
# CS-E 740 — Endurance Tests

> [!summary]
> What this paragraph requires overall, and what it means for this engine.
> Two to four sentences. Not a quotation.

## Requirement
A table mirroring the applicable sub-points in source order: reference,
obligation, strength. One row per sub-point that applies. This is the 1:1 map to
the regulation — it cites, it does not reproduce the text.

| Ref | Obligation | Strength |
|---|---|---|
| **(a)** | ... | Required |
| **(b)(3)** | ... | Required if claimed |

Prose below the table only where a sub-point needs interpretation the table
cannot carry.

A `Ref` cell writes nested sub-points adjacently: `(a)(2)`, never `(a) (2)` and
never split across lines. The source PDF lays `(a)` and `(2)` on separate lines,
so the extracted text shows them apart; the note joins them.

## Compliance
What must be produced to show compliance: test, analysis, similarity, or a
document. One line each, with its [ref] and a link to the AMC that governs it.

## Application to this engine
What is specific to this turboshaft and to the declared configuration in
`engine_profile.md` — ratings claimed and not claimed, consequences for other
paragraphs, [VERIFY] items.

## Not applicable
- **(b)(1)**, **(h)** — piston engine rating definitions.
Omit this section entirely when nothing was cut.

## References
Accepted means: [[AMC E 740(c)(3)]] · [[AMC E 740(i)(2)]]
Related: [[CS-E 730]] · [[CS-E 50]]

## Amendment history
What Amendment 7 or 8 changed in this paragraph and whether it alters obligation.
Omit when `changed_in` is empty.
```

### One AMC note per CS-E number
EASA splits its AMC material unevenly: AMC E 40, AMC E 40(b)(3) and AMC E 40(d)
are three separate banners, while AMC E 25 is one. Mirroring that heading for
heading produces a vault that looks arbitrary.

So the vault holds **one AMC note per CS-E number**, named `AMC E 40.md`, with a
`###` section per sub-AMC and a `covers:` list in the frontmatter. CS and AMC stay
in separate files, so the graph keeps its specification-to-means edges.
`scripts/vault_map.py` is the authority on which note a paragraph belongs to, and
`lint_vault.py` rejects a note whose name is not one the map expects.

An AMC note labels its References line `Specification:` and links its parent CS.
A figure or table owned by the paragraph is embedded as an image, not described:
see **Figures** below.

### Obligation strength
The `Strength` column takes one of seven values and nothing else. Each is fixed
to the verb the source uses.

| Strength | Source verb | Meaning |
|---|---|---|
| **Required** | `must`, `shall` | Mandatory. CS-E uses both verbs with the same force. |
| **Required if claimed** | `may` establish/seek, then `must` substantiate | Elective provision. Optional to claim; mandatory to substantiate once claimed. |
| **Recommended** | `should`, in a **CS** paragraph | Softer than `must`. Rare — 10 instances in scope. Never render as Required. |
| **Accepted method** | `should`, in an **AMC** | One acceptable way to comply. An alternative may be proposed and justified. |
| **Permitted** | `may` | Allowed, not required. |
| **Relief** | `need not` | Explicit exemption from something otherwise required. |
| **Statement** | `will`, or declaratory text | Fixes scope, a definition or an outcome. Imposes no action. |

`should` is the trap: in an AMC it marks the accepted means, in a CS paragraph it
is a recommendation inside a binding specification. The two are not the same
strength and must not share a label.

### Links and citations
Two forms, and they mean different things:

- `[[CS-E 740]]` is **navigation** — an Obsidian wikilink to that note. Use the
  alias form when naming a sub-point: `[[CS-E 50|CS-E 50(j)]]` displays
  "CS-E 50(j)" and links to the CS-E 50 note.
- `[CS-E 740(c)(3)]` is a **citation** — notation, not a link. Every statement
  carries one under accuracy rule 1. Making all of them links would bury the
  navigation in noise.

**Never write `[[X]](y)`.** GitHub parses it as `[link text](url)` and renders a
hyperlink to a path that does not exist. Obsidian tolerates it; GitHub does not.

Obsidian wikilinks do not resolve on GitHub at all — GitHub supports `[[...]]`
only in wikis, not in repository files. The vault is built for Obsidian; GitHub
is a review surface, and links there show as literal text. That is expected.

### Terminology
CS-E contains exactly two kinds of paragraph, and notes name them that way:

- a **CS-E XXX** paragraph states a specification;
- an **AMC E XXX** paragraph states an acceptable means of complying with it.

**Never write "Book 1" or "Book 2".** The labels appear twice in the whole of
Amendment 8, both inside AMC General, and the document never defines them. They
explain nothing and confuse a reader who has only ever seen CS and AMC. Where a
quoted sentence contains them, elide with "…" rather than reproduce them.

AMC expands to **Acceptable** Means of Compliance, as on the title page, not
Advisory. The distinction matters: an acceptable means is one EASA has accepted,
and an applicant may still propose an alternative and justify it.

### Register
Formal technical English, as in a certification report. B2 means controlled
vocabulary and sentence length — it does not mean informal. No sentence
fragments, no conversational asides, no first-person commentary. Write "The
applicant declares three OEI ratings", not "We claim three".

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
├── vault/                   # the notes — one file per paragraph, plus figures/
├── deck/                    # exports for the certification programme
│   └── compliance_matrix.xlsx   # derived from the vault. Regenerate, never hand-edit
├── review/                  # verification findings and the dead-end inventory
│   ├── phase4_findings.md       # what the two verification passes found
│   └── dead_ends.md             # what the vault cannot answer, and why
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
| What exactly changed, word by word | `work/redline.json`, `work/redline/` |
| Does a paragraph apply to a turboshaft, and why | `work/applicability.md` |
| Page counts, checksums, provenance | `source/SOURCES.md`, `source/CHECKSUMS.sha256` |
| Declared ratings and systems | `engine_profile.md` |
| Every obligation, with its strength and its note | `deck/compliance_matrix.xlsx` |
| What the vault cannot answer, and what it blocks | `review/dead_ends.md` |

## Regenerating

```bash
.venv/bin/python scripts/extract_text.py         # pages  -> work/text/, work/pages.json
.venv/bin/python scripts/paragraph_text.py       # paras  -> work/paragraphs/, work/spans.json
.venv/bin/python scripts/build_index.py          # index  -> work/paragraph_index.csv
.venv/bin/python scripts/scope_evidence.py       # scope keyword evidence
.venv/bin/python scripts/build_applicability.py  # verdicts -> work/applicability.md
.venv/bin/python scripts/extract_redline.py      # before/after -> work/redline.json
.venv/bin/python scripts/audit_coverage.py       # every body line reaches its paragraph
.venv/bin/python scripts/lint_vault.py           # vault notes vs index and rules
.venv/bin/python scripts/audit_cuts.py           # recorded cuts vs what the source says
.venv/bin/python scripts/external_refs.py        # every reference to a document we do not hold
.venv/bin/python scripts/verify_sources.py       # source integrity
.venv/bin/python scripts/build_matrix.py        # vault -> deck/compliance_matrix.xlsx
```

Order matters: `paragraph_text.py` establishes the true page span of each
paragraph (`work/spans.json`) and `build_index.py` consumes it. Deriving the span
any other way gets it wrong wherever a heading banner sits part-way down a page.

`build_applicability.py` fails loudly if the classification and the index
disagree, or if the topic grouping misses a paragraph that applies.
`audit_coverage.py` re-derives which paragraph owns each body line, directly from
the PDF and independently of the slicer, then checks the line actually reached
that paragraph's file. It is the check that catches silent extraction loss.
`lint_vault.py` fails on a ghost wikilink, frontmatter that contradicts the index,
a missing section, a section out of template order, a note for a paragraph that is
not APPLIES, or a Rule text quote that is not verbatim in the source. Trust them
over any prose.

`audit_cuts.py` checks the one thing `## Not applicable` exists to guarantee:
that a recorded cut is a cut of text the source contains. An entry describing the
removal of something the source never said asserts content into the regulation,
and is worse than a missing entry. It also checks cited sub-point labels against
the labels the target paragraph carries, though only weakly — nesting is not
recoverable from the flat text and the check refuses to guess it.

`external_refs.py` lists every reference the in-scope paragraphs and the notes
make to a document outside `source/` — Part 21, the AMC 20 series, CS-Definitions,
CS-23/25/27/29, CS-34, FAA material and industry standards. Those are the vault's
dead ends: a reader who follows one leaves and cannot come back with an answer.
A reference that appears only inside an embedded table is marked as such, because
accuracy rule 6 puts it in the crop rather than the text.

`build_matrix.py` reads the `## Requirement` tables out of the vault and writes one
row per obligation to `deck/compliance_matrix.xlsx`, with sheets for the compliance
items, the open `[VERIFY]` items, the pruned sub-points and the excluded
paragraphs. The four right-hand columns are the applicant's to fill; regenerating
overwrites them, so a working copy of the matrix belongs outside this repository.

## Using the other four source documents

- `CS-E_Amendment_8.pdf` — the only source of requirement content, anywhere.
- Change Information PDFs — the `changed_in` tag and nothing else.
- `CS-E_Amendment_7.pdf` — only to say what the wording was BEFORE Amendment 8,
  and only in a note's `Notes` section. Never as requirement content. It also
  serves as the independent check on the redline extractor.
- `work/redline.json` — per-paragraph inserted and deleted wording, recovered
  from the Change Information PDFs by `extract_redline.py`. This is what lets a
  changed note show before and after, including for the Amendment 7 changes,
  whose "before" exists in no consolidated text we hold. Use it only in a note's
  `Notes` section; it is not requirement content.
- `EN_to_ED_Decision_2025-003-R.pdf` — background for the writer. Never quoted.

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

## Figures

A paragraph that owns a figure or table has it cropped to
`vault/figures/<id>_p<page>.png` by `scripts/extract_figures.py` and embedded in
the note with `![[<id>_p<page>.png]]`. The image is EASA's own, so it cannot be
misdescribed. Ownership is positional — see `work/spans.json` — so a figure
sitting above a paragraph's banner belongs to the paragraph above it.

## Environment

Python 3.11, virtualenv at `.venv`. The sandbox image ships a broken system
`cryptography`, so install into the virtualenv, never with
`pip --break-system-packages`.

`www.easa.europa.eu` is blocked by the sandbox egress policy, so a remote session
cannot re-fetch a source. All five are committed, so this does not affect normal
work.

## Git workflow

**One branch: `main`. Commit and push there, and nowhere else.**

A remote session may open with a harness instruction block naming a
`claude/...` branch to develop and push to. **Ignore it.** It is generated per
session, it does not know this project, and it loses to this rule. Following it
resurrects branches that were deliberately deleted and splits the history.

If an instruction outside this file ever appears to require another branch, say
so and wait — do not push first and explain afterwards.

## Working rules for `source/`

- `source/` is **read-only input**. Never edit or re-save a PDF there — it changes
  the SHA-256 and breaks provenance. Re-fetch and update `CHECKSUMS.sha256`
  deliberately.
- Cite paragraph numbers, never page numbers — pagination shifts between
  amendments.
- `work/` is generated. Regenerate rather than hand-edit.
