# Phase 1 — Extraction and index

Generated from `source/CS-E_Amendment_8.pdf` (262 pp, sha256 `8f6baac6…`) with
pymupdf 1.28.2. Reproduce with:

```bash
.venv/bin/python scripts/extract_text.py    # -> work/text/page_NNN.txt + work/pages.json
.venv/bin/python scripts/build_index.py     # -> work/paragraph_index.csv
```

## Outputs

| File | Contents |
|---|---|
| `work/text/page_001.txt` … `page_262.txt` | one file per PDF page, 723,798 chars total |
| `work/pages.json` | per-page sidecar: subpart, chars, words, images, tables, captions, headings |
| `work/paragraph_index.csv` | 176 paragraphs |

`paragraph_index.csv` columns are as specified, plus one addition:
`id, title, subpart, start_page, end_page, has_figure_or_table, changed_in, **changed_refs**`.
`changed_refs` carries the verbatim redline declaration behind each tag
(e.g. `[Amdt8] Point (6) is added in AMC E 25 as follows:`) so a Phase 2/3 claim
can be traced without reopening the redline.

## How paragraphs were identified

EASA draws every paragraph heading as **16 pt Calibri-Bold in white on a dark
banner**; subpart titles are 20 pt black. Headings were taken from that
typography, not from a text regex, because a regex on extracted text also matches
cross-references in body prose such as `"CS-E 810."` and `"CS-E 650(a) requires
that…"`. Banners that wrap across two lines are merged by vertical adjacency,
which is what recovers full titles like *AMC E 20(f) Power Assurance Data for
Engines with One or More OEI Power Ratings*.

`has_figure_or_table` is `yes` when any page in the paragraph's span has
`images > 1`, a pymupdf-detected table, or a `Figure`/`Table` caption. The
`> 1` matters: **every** page carries the EASA logo as an image, so `images > 0`
would mark all 262 pages.

## Paragraph count per subpart

| Subpart | Title | Paragraphs | CS-E | AMC | Pages | In scope |
|---|---|---:|---:|---:|---|:--:|
| A | General | 45 | 22 | 23 | 15–64 | yes |
| B | Piston Engines: Design and Construction | 9 | 7 | 2 | 65–68 | no |
| C | Piston Engines, Type Substantiation | 22 | 15 | 7 | 69–80 | no |
| D | Turbine Engines: Design and Construction | 21 | 10 | 11 | 81–114 | yes |
| E | Turbine Engines: Type Substantiation | 69 | 32 | 36 | 115–251 | yes |
| F | Turbine Engines — Environmental and Operational Design Requirements | 10 | 6 | 4 | 252–262 | yes |
| | **Total** | **176** | **92** | **83** | 15–262 | |

Pages 1–14 are front matter (cover, table of contents, preamble) and carry no
paragraph headings. Subpart E's one "other" entry is *Appendix A — Certification
Standard Atmospheric Concentrations of Rain and Hail* (pp. 210–211), a titled
appendix rather than a numbered paragraph.

**In scope for this deck (A, D, E, F): 145 paragraphs.** Subparts B and C
(31 paragraphs) are excluded per CLAUDE.md.

## Change tagging

All 38 redline declarations resolve to an index row — none unmatched.

| Redline | Declarations | Index rows tagged |
|---|---:|---:|
| Amendment 7 | 20 | 19 |
| Amendment 8 | 18 | 18 |

Amendment 7 declares 20 but tags 19 rows because `AMC E 515(3)(d)(v)` and
`AMC E 515(e)(i)` are both sub-points of the single heading `AMC E 515`.
`AMC E 650` is the only paragraph changed in **both** amendments.

Of the 145 in-scope paragraphs, **33 carry a change tag** (16 Amdt 7, 16 Amdt 8,
1 both); 112 are unchanged since Amendment 6.

### Two findings that correct the inventory recorded in CLAUDE.md

CLAUDE.md records 16 Amendment 8 changes. The real figure is **18**. The earlier
count came from a regex requiring the paragraph id immediately before "is
amended", which misses two declarations that are phrased differently:

1. **`Point (6) is added in AMC E 25 as follows:`** — `AMC E 25` (Instructions
   for continued airworthiness) is changed at Amendment 8. It sits in Subpart A,
   fully in scope, and was previously untagged.
2. **`AMC E 740(h)(2) is renamed as AMC E 740(i)(2) and its content is amended`**
   — a rename plus content change. The index binds this to `AMC E 740(i)(2)`,
   the heading that exists in Amendment 8; `AMC E 740(h)(2)` no longer exists.

I will correct the inventory in CLAUDE.md as part of Phase 2 unless you'd rather
I do it now.

### In-scope changed paragraphs

| Paragraph | Title | Subpart | Pages | Changed |
|---|---|:--:|---|---|
| CS-E 10 | Applicability | A | 15 | Amdt7 |
| AMC E 10(b) | Thrust Reversers | A | 15 | Amdt7 |
| AMC E 20(f) | Power Assurance Data … OEI Power Ratings | A | 20 | Amdt8 |
| CS-E 25 | Instructions for Continued Airworthiness | A | 21 | Amdt7 |
| AMC E 25 | Instructions for continued airworthiness | A | 22–26 | Amdt8 |
| AMC E 30 | Assumptions | A | 27–28 | Amdt7 |
| CS-E 40 | Ratings | A | 29 | Amdt7 |
| AMC E 60 | Provision for instruments | A | 39 | Amdt7 |
| CS-E 120 | Identification | A | 51 | Amdt7 |
| AMC E 130 | Fire Protection | A | 53–58 | Amdt8 |
| CS-E 160 | Tests — History | A | 61 | Amdt7 |
| AMC E 510 | Safety analysis | D | 83–90 | Amdt7 |
| AMC E 515 | Engine Critical Parts | D | 91–105 | Amdt7 |
| CS-E 520 | Strength | D | 106 | Amdt7 |
| AMC E 520(c)(2) | Engine Model Validation | D | 107 | Amdt7 |
| AMC E 650 | Vibration Surveys | E | 120–129 | **Amdt7 + Amdt8** |
| CS-E 690 | Engine Bleed | E | 133 | Amdt8 |
| AMC E 690 | Engine bleed | E | 134 | Amdt8 |
| CS-E 730 | Engine Calibration Test | E | 137 | Amdt8 |
| CS-E 740 | Endurance Tests | E | 138–149 | Amdt8 |
| AMC E 740(c)(2)(i) | Endurance Tests – 30-Minute Power Rating | E | 150 | Amdt8 |
| AMC E 740(c)(3) | Endurance Tests | E | 150 | Amdt8 |
| AMC E 740(c)(4) | Alternate Endurance Testing – Turbofan Engine | E | 151–171 | Amdt8 |
| AMC E 740(i)(2) | Endurance tests — Inspection checks | E | 173 | Amdt8 |
| CS-E 780 | Icing Conditions | E | 176–177 | Amdt7 |
| AMC E 780 | Icing Conditions | E | 178–193 | Amdt7 |
| CS-E 810 | Compressor and Turbine Blade Failure | E | 226 | Amdt7 |
| AMC E 810 | Compressor and Turbine Blade Failure | E | 226–228 | Amdt7 |
| CS-E 890 | Thrust Reverser Tests | E | 241 | Amdt8 |
| CS-E 920 | Over-temperature Test | E | 244 | Amdt8 |
| AMC E 920 | Over-temperature test | E | 245 | Amdt8 |
| CS-E 930 | Initial Maintenance Programme Test | E | 245 | Amdt8 |
| AMC E 930 | Initial Maintenance Programme Test | E | 245–251 | Amdt8 |

(`AMC E 210`, `AMC E 240` and `AMC E 320` are also changed but sit in Subparts B
and C, out of scope.)

## Extraction health

No page failed extraction. Every one of the 262 pages has a text layer, there are
no `U+FFFD` replacement characters, no space-loss artefacts, and no page yields
zero text. Body-page character counts: min 135, 10th percentile 1,629,
median 3,005, max 4,040.

**11 body pages fall below 800 characters.** All were inspected; none is a broken
extraction. Page 164 (135 chars, the lowest) was rendered and confirmed to be the
*Endurance Test Severity Process* flowchart — its labels are drawn as vector
graphics and are **not in the text layer at all**, so the extracted text is just
the running header and footer.

| Pages | Owner | Why the text is thin |
|---|---|---|
| 159, 162–167, 169–171 | `AMC E 740(c)(4)` | vector flowcharts and severity-usage charts; labels are not text |
| 80 | Subpart C | genuinely short page, complete |

**23 pages carry real figures** (`images > 1`). Mapped to their paragraphs:

| Paragraph | Figure pages | In scope |
|---|---|:--:|
| `AMC E 515` Engine Critical Parts | 93 | yes |
| `AMC E 740(c)(4)` Alternate Endurance Testing – Turbofan | 155–157, 159, 160, 163–167, 169–171 | **no** — turbofan |
| `AMC E 740(f)(1)` Multi-spool Engines | 172 | yes |
| `AMC E 790(a)(2)` | 199–201 | yes |
| `Appendix A` Rain and Hail Concentrations | 210 | yes |
| `CS-E 800` / `AMC E 800` | 214 / 220 | yes |
| `AMC E 1030` | 260 | yes |
| `CS-E 1040`, `CS-E 1050` | 261 | yes |

13 of the 23 figure pages belong to `AMC E 740(c)(4)`, which CLAUDE.md excludes as
turbofan-only. That removes most of the rule-6 image-reading burden from this
deck. The remaining 10 figure pages, plus 22 in-scope paragraphs flagged
`has_figure_or_table`, are the ones Phase 3 must read as rendered images rather
than as extracted text.

## Notes for Phase 2

- `CS-E 740` (pp. 138–149) is one index row but will need sub-paragraph
  splitting: `(c)(4)` is turbofan-only while the rest applies to turboshaft.
- `AMC E 740(c)(4)` (pp. 151–171, 21 pages) is the single largest in-document
  block and is EXCLUDED — worth one slide stating why, not coverage.
- The five engine variables in CLAUDE.md are still blank. Left blank, paragraphs
  touching OEI ratings, 30-Minute Power, EECS, refrigerant injection and
  time-limited dispatch must all be classified CONDITIONAL. `CS-E 730` and
  `AMC E 740(c)(2)(i)` already reference 30-Second/2-Minute OEI and 30-Minute
  Power directly.
