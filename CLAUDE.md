# CS-E Deck

Working repository for building a briefing deck on **EASA CS-E (Certification
Specifications and Acceptable Means of Compliance for Engines), Amendment 8**,
with per-slide tagging of what changed at Amendment 7 and Amendment 8.

This is a **document/content repository**, not a software project. The only code
is tooling that fetches, verifies or renders content.

> The repository root *is* the `cs-e-deck/` root from the project sketch — no
> nested `cs-e-deck/` directory. The repo is `evrenge/CS-E`.

## Layout

```
.
├── CLAUDE.md                              # this file
├── requirements.txt                       # pypdf, for anything that reads a PDF
├── source/                                # EASA source PDFs (authoritative, read-only)
│   ├── SOURCES.md                         # provenance, roles, machine-readability notes
│   ├── CHECKSUMS.sha256                   # integrity baseline for the five PDFs
│   ├── CS-E_Amendment_8.pdf               # 262 pp — normative baseline
│   ├── CS-E_Amendment_7.pdf               # 228 pp — previous baseline, "before" text
│   ├── Change_Information_CS-E_Amdt_8.pdf #  47 pp — redline, Amdt 8 vs 7
│   ├── Change_Information_CS-E_Amdt_7.pdf #  30 pp — redline, Amdt 7 vs 6
│   └── EN_to_ED_Decision_2025-003-R.pdf   #  11 pp — Explanatory Note, rationale only
├── template/
│   └── company_template.pptx              # optional TEI deck template (not present yet)
└── scripts/
    ├── fetch_sources.py                   # downloads source/ from easa.europa.eu
    └── verify_sources.py                  # integrity + machine-readability check
```

## Source documents

| File | Role |
|---|---|
| `CS-E_Amendment_8.pdf` | Normative baseline. All requirement text quoted on slides comes from here. |
| `CS-E_Amendment_7.pdf` | Previous consolidated baseline. Verbatim "before" text, and the other side of an Amdt 7 → Amdt 8 diff. |
| `Change_Information_CS-E_Amdt_8.pdf` | Declares which paragraphs Amendment 8 amended/added. Authority for the "changed at Amdt 8" tag. |
| `Change_Information_CS-E_Amdt_7.pdf` | Same for Amendment 7 vs. Amendment 6. Authority for the "changed at Amdt 7" tag. |
| `EN_to_ED_Decision_2025-003-R.pdf` | Explanatory Note to ED Decision 2025/003/R. Rationale only — never a source of normative text. |

Amendment 8 was issued by ED Decision 2025/003/R (8 Apr 2025); Amendment 7 by
ED Decision 2023/020/R (15 Dec 2023). Full provenance, sizes, page counts and
landing pages are in `source/SOURCES.md`.

### Verified state

All five PDFs are committed and verified: `/Author = EASA`, expected titles and
page counts, complete text layer on every page (no OCR anywhere), SHA-256 pinned
in `source/CHECKSUMS.sha256`.

```bash
pip install -r requirements.txt
python3 scripts/verify_sources.py             # integrity + text layer + change inventory
python3 scripts/verify_sources.py --inventory # also list the declared changes
python3 scripts/fetch_sources.py --check      # checksum check only, no dependencies
```

`scripts/fetch_sources.py` (standard library only) re-downloads a source from its
EASA landing page if one is ever lost. It scrapes the landing page rather than
hardcoding `/en/downloads/<id>/en`, because EASA rotates those numeric IDs on
republication, and writes nothing unless the payload starts with `%PDF`.

**Sandbox constraint:** `www.easa.europa.eu` is blocked by the egress policy of the
Claude Code remote sandbox (gateway 403 to CONNECT, for both the container proxy
and WebFetch). A remote session cannot re-fetch a source; it must be supplied from
a machine with ordinary internet access. This does not affect normal work, since
all five files are in the repository.

## Redline extraction — read before writing any tagging code

The two Change Information PDFs do **not** use the same markup convention:

- **Amdt 7 CI** is a word-level redline. Deletions are drawn in red
  (`1 0 0 rg`, ~6.5% of characters); insertions are black with an underline rule
  drawn as a thin filled rectangle.
- **Amdt 8 CI** is mostly *block replacement* — whole affected paragraphs
  reprinted in black (97% of characters, only 0.48% red). Word-level polarity is
  largely absent.

Two consequences:

1. `PdfReader.extract_text()` alone is **not** safe on the Amdt 7 CI: it
   concatenates deleted and inserted words into one run with no marker, producing
   text that reads as normative but never existed in either amendment. Recover
   polarity from the content stream (fill colour via `visitor_operand_before`,
   underline rules via `re` rectangle geometry), or do not claim polarity at all.
2. A uniform word-level redline cannot be recovered from the Amdt 8 CI. Use the
   CI files as the authority for *which* paragraphs changed, and derive *what*
   changed inside a paragraph from a text diff of Amendment 7 against
   Amendment 8, corroborated against the CI.

Both CI files parse cleanly into a paragraph-level change inventory — 20 declared
changes at Amdt 7, 16 at Amdt 8 — via the `"<paragraph> is amended|added|..."`
declarations. That inventory is the intended basis for the slide tags.

## Working rules

- `source/` is **read-only input**. Never edit, re-save, rewrite or "clean up" a
  PDF there. Re-saving changes the SHA-256 and breaks the provenance chain. If a
  file looks wrong, re-fetch it and update `CHECKSUMS.sha256` deliberately.
- Every normative claim on a slide must be traceable to a CS-E paragraph number
  (e.g. `CS-E 740`) in `CS-E_Amendment_8.pdf`. Cite the paragraph, not a page
  number — EASA pagination shifts between amendments.
- Amendment tags come from the Change Information PDFs. A full-text Amdt 7 → 8
  diff may refine *what* changed inside a tagged paragraph, but never promotes an
  untagged paragraph to "changed" on its own, and recollection never does.
- Keep EASA text verbatim when quoted. Paraphrase only in clearly-marked
  commentary, and never paraphrase a requirement into a slide bullet that reads
  as normative.
- Generated decks belong in `output/` (gitignored). Regenerate rather than
  hand-edit; hand edits to a generated deck are lost on the next run.
- `template/company_template.pptx` is optional and currently absent. Tooling must
  fall back to a plain default layout when it is missing.

## Environment

Python 3.11. `scripts/fetch_sources.py` is dependency-free; everything else needs
`pip install -r requirements.txt` (pypdf). Note that the sandbox image ships a
broken system `cryptography`, so install into a virtualenv rather than with
`pip --break-system-packages`.

## Status

Sources complete and verified. The deck specification — scope, slide taxonomy,
tagging scheme and output format — has not been defined yet and will be added
here once it is.
