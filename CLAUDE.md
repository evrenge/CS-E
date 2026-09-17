# Project: CS-E Amendment 8 — Turboshaft Plain-Language Deck

## Audience
Turkish gas turbine engineers. Strong technical background, English is a second language.
Target English level: B2. Short sentences (max ~20 words). Active voice. No legal phrasing.
Define every regulatory term on first use. Keep technical terms (surge, TGT, LCF, OEI) as-is.

## Source of truth
- source/CS-E_Amendment_8.pdf is the ONLY authority for requirement content.
- Change Information PDFs are used ONLY to tag what changed in Amdt 7 / Amdt 8.
- Never use memory or general knowledge for requirement content. If the source does not say it, it does not go on a slide.

## Scope
- Turbine engine rules only: Subparts A, D, E, F (per CS-E 10(d)). Exclude Subparts B and C.
- Turboshaft (rotorcraft) application only. Classify every paragraph as:
  APPLIES / CONDITIONAL (depends on engine variables below) / EXCLUDED (give reason).
- Aeroplane-only AMCs, thrust reverser, propeller, ETOPS, and the turbofan alternate
  endurance test CS-E 740(c)(4) are EXCLUDED unless the text says otherwise.

## Engine variables
Declared in `engine_profile.md`, which also maps the applicant's rating names onto
CS-E terms and records the open [VERIFY] items. Summary:
- OEI ratings claimed: 30-Second OEI, 2-Minute OEI, Continuous OEI.
  NOT claimed: 2.5-Minute OEI, 30-Minute OEI.
- 30-Minute Power rating: yes (CS-E 40(b)(4)) [VERIFY the declared name maps to it]
- Control system: EECS-FADEC, full authority
- Refrigerant injection: no
- Time-limited dispatch claimed: no

## Accuracy rules (non-negotiable)
1. Every statement on a slide carries its paragraph reference, e.g. [CS-E 740(c)(3)].
2. Preserve obligation strength exactly: CS "must" -> "Required"; AMC "should" -> "Accepted method".
   Never upgrade or downgrade.
3. Copy all numbers, times, percentages, probabilities exactly, with units.
4. One short verbatim quote (max 1 sentence) per slide from the key CS text, in a "Rule text" box.
5. If unsure about meaning or applicability, write [VERIFY: reason]. Never guess.
6. For pages with figures or tables, render the page to PNG and read the image. Do not rely on extracted text.

## Slide template (Markdown, one slide per "---")
### <Slide title>
**Paragraphs:** CS-E xxx, AMC E xxx
**Status:** APPLIES | CONDITIONAL (<variable>) | Changed in Amdt 7/8
**Rule text:** "<one original sentence>" [ref]
**What it means:** 2–4 plain sentences.
**What we must do:** bullet list of tasks/evidence (test, analysis, document).
**Turboshaft note:** rotorcraft-specific point, or "None".
**Speaker notes:** longer explanation, AMC detail, examples.

## Working method
- Work subpart by subpart. Write output to files. Do not hold the whole document in context.
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
.venv/bin/python scripts/extract_text.py         # pages  -> work/text/
.venv/bin/python scripts/build_index.py          # index  -> work/paragraph_index.csv
.venv/bin/python scripts/paragraph_text.py       # paras  -> work/paragraphs/
.venv/bin/python scripts/scope_evidence.py       # scope keyword evidence
.venv/bin/python scripts/build_applicability.py  # verdicts -> work/applicability.md
.venv/bin/python scripts/verify_sources.py       # source integrity
```

`build_applicability.py` fails loudly if the classification and the index
disagree, or if the topic grouping misses a paragraph that applies. Trust it over
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
