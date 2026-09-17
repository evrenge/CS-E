# CS-E Deck

Working repository for building a briefing deck on **EASA CS-E (Certification
Specifications and Acceptable Means of Compliance for Engines), Amendment 8**,
with per-slide tagging of what changed at Amendment 7 and Amendment 8.

This is a **document/content repository**, not a software project. The only code
is tooling that fetches sources or generates output.

> The repository root *is* the `cs-e-deck/` root from the project sketch — no
> nested `cs-e-deck/` directory. The repo is `evrenge/CS-E`.

## Layout

```
.
├── CLAUDE.md                              # this file
├── source/                                # EASA source PDFs (authoritative, read-only)
│   ├── SOURCES.md                         # what each file is + where it came from
│   ├── CS-E_Amendment_8.pdf
│   ├── Change_Information_CS-E_Amdt_8.pdf
│   ├── Change_Information_CS-E_Amdt_7.pdf
│   └── EN_to_ED_Decision_2025-003-R.pdf
├── template/
│   └── company_template.pptx              # optional TEI deck template
└── scripts/
    └── fetch_sources.py                   # downloads source/ from easa.europa.eu
```

## Source documents

| File | Role |
|---|---|
| `CS-E_Amendment_8.pdf` | Normative baseline. All requirement text quoted on slides comes from here. |
| `Change_Information_CS-E_Amdt_8.pdf` | Redline, Amdt 8 vs. Amdt 7. Drives the "changed at Amdt 8" tag. |
| `Change_Information_CS-E_Amdt_7.pdf` | Redline, Amdt 7 vs. Amdt 6. Drives the "changed at Amdt 7" tag. |
| `EN_to_ED_Decision_2025-003-R.pdf` | Explanatory Note to ED Decision 2025/003/R. Rationale only — never a source of normative text. |

Amendment 8 was issued by ED Decision 2025/003/R; Amendment 7 by ED Decision
2023/020/R. Full provenance, landing pages and a manual-recovery note are in
`source/SOURCES.md`.

### Populating `source/`

```bash
python3 scripts/fetch_sources.py          # fetch anything missing
python3 scripts/fetch_sources.py --check  # status + sha256 of what is present
python3 scripts/fetch_sources.py --force  # re-fetch all four
```

Standard library only, no dependencies. The script resolves each PDF by scraping
its EASA landing page, because EASA rotates the numeric IDs behind
`/en/downloads/<id>/en` on republication. It downloads nothing unless the payload
starts with `%PDF`.

**Known constraint:** `www.easa.europa.eu` is blocked by the egress policy of the
Claude Code remote sandbox (gateway returns 403 to CONNECT, for both the container
proxy and WebFetch). Sources must therefore be fetched from a machine with
ordinary internet access and pushed, or the block lifted for that host. A remote
session will not be able to populate `source/` on its own.

## Working rules

- `source/` is **read-only input**. Never edit, re-save, rewrite or "clean up" a
  PDF in that directory. If a file looks wrong, re-fetch it.
- Every normative claim on a slide must be traceable to a CS-E paragraph number
  (e.g. `CS-E 740`) in `CS-E_Amendment_8.pdf`. Cite the paragraph, not a page number
   — EASA pagination shifts between amendments.
- Amendment tags are derived from the Change Information PDFs, never inferred by
  diffing prose or by recollection.
- Keep EASA text verbatim when quoted. Paraphrase only in clearly-marked
  commentary, and never paraphrase a requirement into a slide bullet that reads
  as normative.
- Generated decks belong in `output/` (gitignored). Regenerate rather than
  hand-edit; hand edits to a generated deck are lost on the next run.
- `template/company_template.pptx` is optional. Tooling must fall back to a plain
  default layout when it is absent.

## Environment

Python 3.11, no third-party dependencies required for `scripts/`. Any deck
generation that needs `python-pptx` or a PDF parser should declare it in a
`requirements.txt` added at that time.

## Status

Scaffolding only. The deck specification — scope, slide taxonomy, tagging scheme
and output format — has not been defined yet and will be added here once it is.
