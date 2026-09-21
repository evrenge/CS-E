# Project: CS-E Amendment 8 — Turboshaft Plain-Language Vault

## Audience
Turkish gas turbine engineers. Strong technical background, English is a second language.
Target English level: B2. Short sentences (max ~20 words). Active voice. No legal phrasing.
Define every regulatory term on first use. Keep technical terms (surge, TGT, LCF, OEI) as-is.

## Source of truth
- source/CS-E_Amendment_8.pdf is the ONLY authority for **CS-E** requirement content.
- Change Information PDFs are used ONLY to tag what changed in Amdt 7 / Amdt 8.
- Never use memory or general knowledge for requirement content. If the source does not say it, it does not go in a note.
- A document in `source/external/` may answer a question CS-E asks and does not
  answer itself — what CS 29.927 requires of the transmission, what Fireproof
  means, what 21.B.85 designates. That is an **imported obligation**, and it is
  governed by **Imported obligations** below. It never becomes a CS-E
  requirement, and it is never written without the marking that rule sets out.

### Imported obligations
CS-E defers constantly, and until the external documents were held the vault
could only say "this is defined elsewhere". It can now answer. The risk that
creates is precise: a reader who cannot tell a CS-E obligation from a CS-29 one
has lost the only thing this vault guarantees. Five rules prevent that.

**A. An imported obligation never becomes a `## Requirement` row.** In a CS-E
note that table is the 1:1 map to CS-E, and it is the part a reader trusts
without checking. A CS-29 row in it destroys exactly that. Imported material
goes in `## Compliance`, in `## Application to this engine`, or in interpretive
prose.

**B. It is cited as `[ext <id>]`** — `[ext CS 29.927(c)]`, `[ext GM1 21.A.3B(b)]`,
`[ext CS-Definitions, Fireproof]`. The `ext` marker is the point: `CS-E` and
`CS-29` differ by two characters, which is not enough to carry a distinction
this important. `<id>` matches a file in `work/external/` wherever one exists.

**C. In a CS-E note an imported statement gets no `Strength` label.** The seven
terms are keyed to *CS-E's* verbs. Labelling CS-29's `must` as **Required**
tells a reader CS-E imposes it. CS-E does not; CS-29 does, on the rotorcraft.
Write what the other document requires and of whom.

**D. A quotation from an external document follows accuracy rule 4 unchanged**,
and is checked against `work/external/`. Same standard, wider haystack. This is
why `scripts/external_paragraphs.py` exists.

**E. Frontmatter records the dependency: `imports: [CS-29, Part 21]`.** One
entry per document, not per citation. It lets a reader see at a glance that a
note rests on something outside CS-E, and lets `build_matrix.py` carry that to
the applicant.

What an import must never do is let CS-E off. If CS-E states an obligation, the
`## Requirement` row states it whether or not the imported material explains it.
The import adds the answer; it does not replace the question.

## Scope
- Turbine engine rules only: Subparts A, D, E, F (per CS-E 10(d)). Exclude Subparts B and C.
- Turboshaft (rotorcraft) application only. Classify every paragraph as
  APPLIES / EXCLUDED (give reason). A paragraph classified EXCLUDED gets no note.
- Aeroplane-only AMCs, thrust reverser, propeller, ETOPS, and the turbofan alternate
  endurance test CS-E 740(c)(4) are EXCLUDED unless the text says otherwise.
- **A reference chain leaving CS-E is recorded, not followed to its end.**
  CS-E 1010 and CS-E 1020 route through CS 34.1 / CS 34.2 to point 21.A.21, then
  21.A.20, then 21.B.85, and end at the SARPs in ICAO Annex 16. The vault states
  that chain and stops. ICAO Annex 16 is not an EASA document and this is a CS-E
  vault; the applicant follows the last link. Recording where a chain ends is an
  answer, not a gap.

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
- Every cut is recorded in the note's `## Not applicable` section, one line, with
  the sub-point reference and the reason. A reader must always be able to tell
  "deliberately excluded" from "forgotten". Silent omission is a defect.
- Record the cut, never the content: `## Not applicable` says what was removed and
  why, not what it said.

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
   When `## Compliance` exceeds ~10 items, group them under `###` sub-headings by
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
imports: [CS-29]             # documents an [ext ...] citation comes from; omit when none
tags: [endurance, oei, test]
covers: ["AMC E 740(c)(3)", ...]   # see below; omit when it repeats the filename
---
# CS-E 740 — Endurance Tests

> [!summary]
> What this paragraph requires overall, and what it means for this engine.
> About 50 to 90 words. Not a quotation. The budget is words, not sentences:
> the B2 sentence-length rule applies here too, so a summary at the top of that
> range runs to four or five short sentences rather than two long ones. A merged
> AMC note covering several banners may run longer, because it introduces each.

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
Required whenever `changed_in` is non-empty.
```

Where `changed_in` is empty the section is carried only if it says something the
frontmatter does not: that a related AMC changed while the specification did not,
or which amendment the paragraph was last touched at, read from its own
`[Amdt No]` marking. A section whose whole content is "Unchanged at Amendments 7
and 8" restates `changed_in: []` and is noise — omit it.

The distinction a reader needs is between *checked and unchanged* and *not
reviewed*. `changed_in` carries that on its own, which is why the section is
optional here and not a silent omission when it is absent.

### One AMC note per CS-E number
EASA splits its AMC material unevenly: AMC E 40, AMC E 40(b)(3) and AMC E 40(d)
are three separate banners, while AMC E 25 is one. Mirroring that heading for
heading produces a vault that looks arbitrary.

So the vault holds **one AMC note per CS-E number**, named `AMC E 40.md`, with a
`###` section per sub-AMC and a `covers:` list in the frontmatter. CS and AMC stay
in separate files, so the graph keeps its specification-to-means edges.
`scripts/vault_map.py` is the authority on which note a paragraph belongs to, and
`lint_vault.py` rejects a note whose name is not one the map expects.

`covers:` earns its place only when it says something the filename does not. Two
cases qualify, 13 notes in all: a merged note carrying several banners
(`AMC E 740` covers five), and a note named differently from its single banner
(`AMC E 830` covers `AMC E 830(c)`). The other 99 notes are named exactly after
their one banner, and `covers:` there is noise — `lint_vault.py` rejects it.

An AMC note labels its References line `Specification:` and links its parent CS.
A figure or table owned by the paragraph is embedded as an image, not described:
see **Figures** below.

### External notes — `vault/external/`
Some external material is too large to sit inside a CS-E note as an import.
CS 29.927 runs to five printed pages and governs the transmission, not the
engine; quoting it into `CS-E 740` would bury that note and break rule 8 the
moment a second note needed the same text.

Such material gets a note of its own in `vault/external/`, named for the
paragraph: `CS 29.927.md`, `CS 27.927.md`. A CS-E note then links to it —
`[[CS 29.927]]` — exactly as it links a CS-E note.

These are **not** CS-E notes and the differences are deliberate:

- Frontmatter carries `type: EXT` and `document:` naming the source file. There
  is no `subpart:` and no `changed_in:`; neither means anything outside CS-E.
- There is no `## Application to this engine` verdict and no `## Not applicable`
  section. Applicability is a CS-E scope judgement. An external note records
  what the paragraph says and, under `## Bearing on this engine`, what follows
  for a CS-E obligation — which is a different claim.
- The `## Requirement` table **may** use the seven strengths, because the note's
  whole subject is that document and its own verbs. Rule C bars the strength
  vocabulary from an import *inside a CS-E note*, where it would read as CS-E's.
  Here the title, the frontmatter and the folder all say whose obligation it is.
- `## References` labels its CS-E side `Bears on:` and links the CS-E notes that
  depend on it. On the other side of the edge, a CS-E note labels its external
  links `External:`, on a line of its own after `Related:`.

Where a rotorcraft point exists in both codes, **write one note per code**, not a
merged one. `CS 27.927` and `CS 29.927` share a structure and differ in
substance — CS-29 carries the Category A and B loss-of-lubrication regime that
CS-27 states in a single sentence. A merged note would have to caveat every row,
and a reader certifying against one code does not want the other's text in the
same table. Each links the other under `Counterpart:`, and `lint_vault.py`
requires that line wherever the counterpart point is sliced.

**An external note carries its own AMC material inside it**, as a
`### Acceptable means` section under `## Requirement`, and lists it on an
`Accepted means:` line in `## References`. The one AMC note per CS-E number rule
does not extend here: a separate `AMC1 29.927.md` would imply the vault reads
CS-29 as a whole, which it does not. It reads the points it cites.

### CS-27 and CS-29 are read together
The airframe code is not fixed — see the open item in `CS-E 30`. A note that
cites `CS 29.1093` and not `CS 27.1093` reads as though it were. So wherever the
counterpart point is sliced into `work/external/`, a note cites both, and
`lint_vault.py` fails it otherwise. The check is at point level, because the
sub-point labels differ between the codes: the 30-minute power alerting duty is
`CS 29.1305(a)(27)` and `CS 27.1305(w)`.

Where only one code carries something, the note says so in words rather than
falling silent. CS-27 prescribes no rotor drive overspeed test, so the engine
data item behind `CS 29.927(d)` has no CS-27 counterpart, and `CS-E 20` states
that.

### Obligation strength
The `Strength` column takes one of seven values and nothing else. Each is fixed
to the verb the source uses.

| Strength | Source verb | Meaning |
|---|---|---|
| **Required** | `must`, `shall` | Mandatory. CS-E uses both verbs with the same force. |
| **Required if claimed** | `may` establish/seek, then `must` substantiate | Elective provision. Optional to claim; mandatory to substantiate once claimed. |
| **Recommended** | `should`, in a **CS** paragraph | Softer than `must`. Rare. Never render as Required. |
| **Accepted method** | `should`, in an **AMC** | One acceptable way to comply. An alternative may be proposed and justified. |
| **Permitted** | `may` | Allowed, not required. |
| **Relief** | `need not` | Explicit exemption from something otherwise required. |
| **Statement** | `will`, or declaratory text | Fixes scope, a definition or an outcome. Imposes no action. |

#### Declaratory phrasing

CS-E does not always use one of the seven verbs. It states a requirement, a
permission or a relief declaratively, and the label is then chosen by the force
of the sentence, not by hunting for a verb that is not there. These are the forms
in scope, with the label each one takes:

| Source phrasing | Label | Where |
|---|---|---|
| `is required to`, `are required to` | **Required** | AMC E 25(4)(a), AMC E 800(1)(a)(i) |
| `has the option to` | **Permitted** | AMC E 710(1) |
| `it is acceptable to`, `it will be acceptable to` | **Permitted** | CS-E 600(d), CS-E 720(d) |
| `do not have to`, `does not need to comply` | **Relief** | AMC E 800(4)(a), CS-E 800(g)(7) |
| `is an acceptable duration`, `may … provided` where a criterion elsewhere is waived | **Relief** | CS-E 840(a), CS-E 920(b) |
| `is responsible for` | **Statement** | AMC E 20(6) |

`is responsible for` is the one that reads stronger than it is. It allocates a
duty that some **CS** paragraph already imposes; it does not create one. Label it
Statement and say in the prose where the binding duty lives, so the row is not
read as optional.

Do not extend this table by analogy. A phrasing that is not listed and not one of
the seven verbs is a `[VERIFY]`, not a guess.

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

**Never put an aliased wikilink inside a table row.** `[[CS-E 110|CS-E 110(e)]]`
in a table cell puts a `|` inside the row, and GitHub reads it as a column
separator: the row grows a cell and the table breaks from that line down.
Obsidian renders it, so the damage is invisible in the editor. Use the citation
form in a cell — `[CS-E 110(e)]` — which is what the `Requirement` table wants
anyway, since it cites rather than navigates.

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

### Line wrapping
Prose is hard-wrapped at 80 columns. Tables, list bullets, headings and the
`References` link runs stay on one line whatever their length — a wikilink does
not survive a line break, and a wrapped table row is not a table.

The rule exists because splitting a long sentence leaves the paragraph wrapped
at whatever width the join produced. Re-wrap the paragraph you edited, and only
that one: reflowing a file that is merely wrapped at 78 turns a targeted edit
into a whitespace diff that hides it.

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
├── README.md                # what the project is, for a reader arriving cold
├── engine_profile.md        # declared engine configuration — project input
├── requirements.txt
├── source/                  # EASA source PDFs, read-only. See source/SOURCES.md
│   └── external/            # documents CS-E cites and does not contain.
│                            # See source/external/SOURCES.md
├── scripts/                 # extraction, indexing, classification, rendering
├── vault/                   # the notes — one file per paragraph, plus figures/
│   └── external/            # notes on paragraphs of other documents. See
│                            # **External notes** above
├── deck/                    # exports for the certification programme
│   └── compliance_matrix.xlsx   # derived from the vault. Regenerate, never hand-edit
├── review/                  # verification findings and the dead-end inventory
│   ├── phase4_findings.md       # what the two verification passes found
│   └── dead_ends.md             # what the vault cannot answer, and why
└── work/                    # everything derived. Regenerate, never hand-edit
    ├── text/                # one file per PDF page
    ├── paragraphs/          # one file per CS-E / AMC paragraph
    ├── external/            # one file per cited paragraph of an external
    │                        # document — the haystack for an [ext …] quotation
    ├── redline/             # per-paragraph before/after wording
    ├── spans.json           # true page span per paragraph
    ├── pages.json           # page-level extraction metadata
    ├── redline.json         # inserted and deleted wording per paragraph
    ├── scope_evidence.json  # scope keyword hits behind each verdict
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
.venv/bin/python scripts/audit_citations.py     # citations resolve; numbers are the source's
.venv/bin/python scripts/external_paragraphs.py  # cited external paragraphs -> work/external/
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
not APPLIES, or a quoted passage that is not verbatim in the source. Trust them
over any prose.

`audit_cuts.py` checks the one thing `## Not applicable` exists to guarantee:
that a recorded cut is a cut of text the source contains. An entry describing the
removal of something the source never said asserts content into the regulation,
and is worse than a missing entry. It also checks cited sub-point labels against
the labels the target paragraph carries, though only weakly — nesting is not
recoverable from the flat text and the check refuses to guess it.

`audit_citations.py` covers the things nothing else sees. A `[CS-E 740(c)(3)]`
citation is notation, not a link, so Obsidian never reports a broken one and a
reader only finds out by following it. And a number carrying a unit is the defect
a certification engineer is least able to catch by reading, so every one is
matched back to the source, after normalising the spellings that differ between
the PDF text layer and a note — the vulgar fractions, the thin space in
"1 500 ft", the spacing around a degree sign.

It also checks an `[ext …]` citation down to its sub-point: the label must exist
in the slice, written as a label and not in prose. EASA does not number
consistently across documents — AMC 20-3B writes `(7)`, AMC 20-42 writes `5.` —
so a citation mirrors the numbering of the document it names, and the check
reads the raw slice rather than the normalised one, because normalising is what
destroys a label.

`external_paragraphs.py` slices the documents in `source/external/` into one file
per cited paragraph, so an `[ext …]` quotation can be checked word-for-word the
way a CS-E quotation is. Only the points the vault cites are extracted, listed in
its `WANTED` table; adding one means adding a line there. Its docstring records
the extraction defects that had to be fixed to make the slices trustworthy. Every
one of them produced plausible text for the wrong paragraph instead of failing,
which is why each slice is checked to open with the heading it claims.

`external_refs.py` lists every reference the in-scope paragraphs and the notes
make to a document outside `source/` — Part 21, the AMC 20 series, CS-Definitions,
CS-23/25/27/29, CS-34, FAA material and industry standards — and marks each
family **HELD** or **NOT HELD**. A reference into a held family can be followed:
the document is in `source/external/` and the point may be sliced into
`work/external/`. A reference into a family that is not held is a dead end, in
the sense `review/dead_ends.md` uses. A reference that appears only inside an
embedded table is marked as such, because accuracy rule 6 puts it in the crop
rather than the text.

`build_matrix.py` reads the `## Requirement` tables out of the vault and writes one
row per obligation to `deck/compliance_matrix.xlsx`, with sheets for the compliance
items, the open `[VERIFY]` items, the pruned sub-points and the excluded
paragraphs. The four right-hand columns are the applicant's to fill; regenerating
overwrites them, so a working copy of the matrix belongs outside this repository.

### The scripts that are not pipeline steps

These files are not part of the sequence above, and nothing in the sequence
fails if they are never run again.

- `classification.py` — the applicability verdict for every in-scope paragraph, as
  data: one `(id, status, reason)` entry each. `build_applicability.py` renders it
  and `lint_vault.py` enforces it. Editing a verdict means editing this file.
- `vault_map.py` — which note a paragraph belongs to. The authority for the one
  AMC note per CS-E number rule.
- `prune_candidates.py` — proposes sub-points that look like turboshaft dead ends.
  It proposes; the writer decides, and the decision is recorded in the note's
  `## Not applicable` section.
- `fetch_sources.py` — downloads the five source PDFs. It cannot run in a sandbox
  that blocks `www.easa.europa.eu`, and it does not need to: all five are
  committed.
- `slide_plan.py` — the topic grouping and reading order, kept because
  `build_applicability.py` checks its coverage. The deliverable is the vault, not
  a deck; the name is historical.
- `extract_figures.py` — crops a figure or table to `vault/figures/`. Run it when
  a note needs an image it does not yet have; see **Figures**.

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

`source/` holds two tiers, and they are not interchangeable.

**`source/` itself** — the five CS-E documents. `CS-E_Amendment_8.pdf` is the only
authority for requirement content, as stated at the top of this file, and that
does not change because other documents are now present.

**`source/external/`** — documents CS-E cites and does not contain: CS-27, CS-29,
CS-Definitions, AMC-20, the Easy Access Rules edition of Part 21, CS-34 as
repealed, and the repeal's explanatory note. They answer their own questions —
what the rotorcraft code asks, what a deferred term means, what the AMC 20
series accepts — and they are **never** a source of CS-E requirement content.
They are pinned to the version the vault was written against and **not tracked
across amendments**: the amendment machinery exists because CS-E is the
deliverable, and these are not. `source/external/SOURCES.md` records what each
one closes and what is still missing.

Writing note content from one of them is governed by **Imported obligations**
at the top of this file, and by **External notes** where the material warrants a
note of its own.

- `source/` is **read-only input**. Never edit or re-save a PDF there — it changes
  the SHA-256 and breaks provenance. Re-fetch and update `CHECKSUMS.sha256`
  deliberately.
- Cite paragraph numbers, never page numbers — pagination shifts between
  amendments.
- `work/` is generated. Regenerate rather than hand-edit.
