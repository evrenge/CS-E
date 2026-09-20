# Source documents

Five EASA documents, all free downloads from easa.europa.eu (no paywall, no login).
All are committed to this repository and verified — see `CHECKSUMS.sha256`.

| File | Pages | Size | Document | PDF title / subject |
|---|---:|---:|---|---|
| `CS-E_Amendment_8.pdf` | 262 | 6.04 MB | CS and AMC for Engines, Amendment 8 — Annex to ED Decision 2025/003/R, 8 Apr 2025 | "CS-E Amendment 8" / "Annex to ED Decision 2025/003/R" |
| `CS-E_Amendment_7.pdf` | 228 | 3.05 MB | CS and AMC for Engines, Amendment 7 — Annex to ED Decision 2023/020/R, 15 Dec 2023 | "CS-E Amendment 7" / "Regular update of CS-E" |
| `Change_Information_CS-E_Amdt_8.pdf` | 47 | 3.48 MB | Change Information, Amendment 8 (vs. Amdt 7) | "Change Information CS-E Amendment 8" |
| `Change_Information_CS-E_Amdt_7.pdf` | 30 | 0.43 MB | Change Information, Amendment 7 (vs. Amdt 6) | "Change information - CS-E Amendment 7" |
| `EN_to_ED_Decision_2025-003-R.pdf` | 11 | 0.36 MB | Explanatory Note to ED Decision 2025/003/R | "Explanatory Note to ED Decision 2025/003/R" |

All five carry `/Author = EASA`. Metadata was checked against the first page of
each file; nothing is a mirror or a third-party reprint.

## Role of each file

- **CS-E Amendment 8** — the normative baseline. Current consolidated CS-E book,
  Subparts A–F plus AMC. Every requirement quoted in a note comes from here.
- **CS-E Amendment 7** — the previous consolidated baseline. Provides verbatim
  "before" text for a changed paragraph, and allows a full-text Amdt 7 → Amdt 8
  diff as a cross-check on the change inventory.
- **Change Information, Amdt 8** — declares which paragraphs Amendment 8 amended,
  added or deleted. Authority for the "changed at Amdt 8" tag.
- **Change Information, Amdt 7** — same, for Amendment 7 against Amendment 6.
  Authority for the "changed at Amdt 7" tag.
- **Explanatory Note to ED Decision 2025/003/R** — rationale, scope and
  comment-response summary for Amendment 8. Never a source of normative text.

## Landing pages

| File | Landing page |
|---|---|
| `CS-E_Amendment_8.pdf`, `Change_Information_CS-E_Amdt_8.pdf` | https://www.easa.europa.eu/en/document-library/certification-specifications/cs-e-amendment-8 |
| `CS-E_Amendment_7.pdf`, `Change_Information_CS-E_Amdt_7.pdf` | https://www.easa.europa.eu/en/document-library/certification-specifications/cs-e-amendment-7 |
| `EN_to_ED_Decision_2025-003-R.pdf` | https://www.easa.europa.eu/en/downloads/141876/en |

Related, not stored here:

- ED Decision 2025/003/R (Amdt 8): https://www.easa.europa.eu/en/document-library/agency-decisions/ed-decision-2025003r
- ED Decision 2023/020/R (Amdt 7): https://www.easa.europa.eu/en/document-library/agency-decisions/ed-decision-2023020r
- CS-E document group: https://www.easa.europa.eu/en/document-library/certification-specifications/group/cs-e-engines

## Machine-readability

Verified with `pypdf` (see `scripts/verify_sources.py`):

- All five have a complete embedded text layer. No OCR is needed anywhere.
- CS-E Amdt 8 yields ~723,000 characters of text, 92 distinct `CS-E NNN`
  paragraph numbers, Subparts A–F.
- Both Change Information PDFs parse into a clean change inventory: 20 declared
  changes at Amdt 7, 16 at Amdt 8.

### Redline markup scheme

Both Change Information PDFs mark changes the same way (verified by rendering
pages and by reading the content stream):

- **Inserted text** — black, on a cyan highlight drawn as a filled rectangle with
  non-stroking colour `0 1 1`. 148 such fills in the Amdt 7 CI, 114 in the Amdt 8 CI.
- **Deleted text** — red (`1 0 0 rg`) with a strikethrough rule. 4,118 red
  characters in the Amdt 7 CI, 395 in the Amdt 8 CI.

Amendment 8 carries less red because it is predominantly additive, not because it
uses a different convention.

`extract_text()` drops both markers and merges deleted and inserted words into one
run — the result reads as normative text that never existed in either amendment.
Recover polarity from the content stream or from a rendered page.

## Provenance rule

Do not substitute a mirrored or third-party copy, and do not re-save these PDFs.
Verify with `sha256sum -c CHECKSUMS.sha256` from this directory. If a file must be
replaced, re-fetch from the EASA landing page above — EASA rotates the numeric
`/en/downloads/<id>/en` IDs when a document is republished.
