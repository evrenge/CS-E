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

## Engine variables (fill in; if blank, treat related paragraphs as CONDITIONAL)
- OEI ratings claimed: [30-s / 2-min / 2.5-min / 30-min OEI / continuous OEI / none]
- 30-Minute Power rating: [yes/no]
- Control system: [EECS-FADEC / hydromechanical / hybrid]
- Refrigerant injection: [yes/no]
- Time-limited dispatch claimed: [yes/no]

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

Everything below is repository state and tooling. It does not modify the rules above.

## Layout

```
.
├── CLAUDE.md                              # this file
├── requirements.txt                       # pypdf (parsing), pypdfium2 (page -> PNG)
├── source/                                # EASA source PDFs (authoritative, read-only)
│   ├── SOURCES.md                         # provenance, roles, machine-readability notes
│   ├── CHECKSUMS.sha256                   # integrity baseline
│   ├── CS-E_Amendment_8.pdf               # 262 pp — the only authority for requirement content
│   ├── CS-E_Amendment_7.pdf               # 228 pp — previous baseline, verbatim "before" text
│   ├── Change_Information_CS-E_Amdt_8.pdf #  47 pp — change tags, Amdt 8
│   ├── Change_Information_CS-E_Amdt_7.pdf #  30 pp — change tags, Amdt 7
│   └── EN_to_ED_Decision_2025-003-R.pdf   #  11 pp — Explanatory Note, rationale only
├── template/
│   └── company_template.pptx              # optional TEI template (not present yet)
└── scripts/
    ├── fetch_sources.py                   # re-download a source from easa.europa.eu
    └── verify_sources.py                  # integrity + text-layer + change-inventory check
```

Amendment 8 was issued by ED Decision 2025/003/R (8 Apr 2025); Amendment 7 by
ED Decision 2023/020/R (15 Dec 2023). `EN_to_ED_Decision_2025-003-R.pdf` is the
Explanatory Note to the Amdt 8 decision — background for the writer, never slide
content, per the source-of-truth rule above.

`CS-E_Amendment_7.pdf` is the fifth file, beyond the original four. It supplies
the verbatim pre-Amdt-8 text of any paragraph, which is what lets a "Changed in
Amdt 8" slide say what the wording actually was.

## Verified state

All five PDFs are committed and verified: `/Author = EASA`, expected titles,
page counts 262 / 228 / 47 / 30 / 11, a complete text layer on every page
(no OCR needed anywhere), SHA-256 pinned in `source/CHECKSUMS.sha256`.

```bash
pip install -r requirements.txt
python3 scripts/verify_sources.py             # integrity + text layer + change inventory
python3 scripts/verify_sources.py --inventory # list every declared change
python3 scripts/fetch_sources.py --check      # checksum check only, no dependencies
```

Declared change inventory, parsed from the Change Information PDFs — this is the
basis for the **Status: Changed in Amdt 7/8** field:

- **Amdt 8, 16 changes:** CS-E 690, 730, 740, 890, 920 amended; CS-E 930 added;
  AMC E 20(f), 130, 320, 650(10), 690, 740(c)(2)(i), 740(c)(3), 920 amended;
  AMC E 740(c)(4) and AMC E 930 added.
- **Amdt 7, 20 changes:** CS-E 10, 25, 40, 120, 160, 520, 780, 810 amended;
  AMC E 10(b), 30, 60, 210, 240, 510, 515(3)(d)(v), 515(e)(i), 520(c)(2), 650,
  780, 810 amended or created.

Note that `AMC E 740(c)(4)` — the turbofan alternate endurance test — is an
Amdt 8 addition and is EXCLUDED by the scope rule above. The Explanatory Note
gives the alternate endurance test as a headline objective of ED Decision
2025/003/R, so expect a large share of the Amdt 8 redline to fall outside scope,
and expect CS-E 740 itself to need careful APPLIES / EXCLUDED splitting rather
than a single verdict.

## Redline extraction — read before writing any tagging code

Both Change Information PDFs use the same marking scheme, verified by rendering
pages and by reading the content stream:

| Change | How it is drawn | How to detect it |
|---|---|---|
| Inserted text | black text on a **cyan** highlight | filled rectangle with non-stroking colour `0 1 1` behind the run (148 fills in the Amdt 7 CI, 114 in the Amdt 8 CI) |
| Deleted text | **red** text with a strikethrough rule | text fill `1 0 0 rg` (4,118 chars in Amdt 7, 395 in Amdt 8), plus a red rule rectangle |
| Unchanged context | plain black, no fill behind it | neither of the above |

Amendment 8 carries far less red than Amendment 7 because it is predominantly
**additive** — new paragraphs such as CS-E 930 and AMC E 740(c)(4) — not because
it uses a different convention.

Two consequences:

1. `PdfReader.extract_text()` alone is **unsafe** on either redline. It drops both
   markers and concatenates deleted and inserted words into a single run, yielding
   sentences that read as normative but never existed in any amendment. A real
   example from Amdt 7 CI p. 16 extracts as
   `"generate equivalent ice accretion adequately simulate all icing threats"`,
   where `generate equivalent ice accretion` is struck and the rest is new.
   Recover polarity from the content stream (`visitor_operand_before` for fill
   colour and rectangle geometry), or render the page and read the image.
2. Paragraph-level tagging is independent of all this: both files declare their
   changes in prose (`"CS-E 740 is amended as follows"`), which parses cleanly.
   Use those declarations for the **Status** field and the colour/geometry pass
   only when a slide needs to show what specifically changed inside a paragraph.

## Page rendering

Accuracy rule 6 (render figure and table pages to PNG and read the image) needs a
rasteriser. `pypdfium2` is in `requirements.txt` and renders a page with
`PdfDocument(path)[i].render(scale=2).to_pil()`. No poppler or system package is
required.

## Environment

Python 3.11. `scripts/fetch_sources.py` is dependency-free; everything else needs
`pip install -r requirements.txt`. The sandbox image ships a broken system
`cryptography`, so install into a virtualenv rather than with
`pip --break-system-packages`.

**Sandbox egress:** `www.easa.europa.eu` is blocked by the Claude Code remote
sandbox network policy (gateway 403 to CONNECT, for both the container proxy and
WebFetch). A remote session cannot re-fetch a source; it must be supplied from a
machine with ordinary internet access. This does not affect normal work, since all
five files are committed.

## Working rules for `source/`

- `source/` is **read-only input**. Never edit, re-save, rewrite or "clean up" a
  PDF there — re-saving changes the SHA-256 and breaks the provenance chain. If a
  file looks wrong, re-fetch it and update `CHECKSUMS.sha256` deliberately.
- Cite paragraph numbers, never page numbers — EASA pagination shifts between
  amendments.
- Generated output belongs in `output/` (gitignored). Regenerate rather than
  hand-edit.
- `template/company_template.pptx` is optional and currently absent. Tooling must
  fall back to a plain default layout when it is missing.
