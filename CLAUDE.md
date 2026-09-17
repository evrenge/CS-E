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
