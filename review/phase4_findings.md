# Phase 4 verification — findings

Seven independent verification passes over the 112 notes, one per scope, each
reading every note against its source paragraph files in `work/paragraphs/` and
against `engine_profile.md`, `work/redline.json` and `vault/figures/`.

The method is deliberately adversarial: the verifier is told the paragraph text
is the only authority, that general knowledge about CS-E is inadmissible, and
that a statement the source does not make is a finding even if it is true.

| Scope | Notes | BLOCKER | MAJOR | MINOR |
|---|---|---|---|---|
| Subpart A, CS-E 10 – AMC E 50 | 13 | 2 | 6 | 10 |
| Subpart A, CS-E 60 – AMC E 170 | 20 | 0 | 0 | 9 |
| Subpart D | 17 | 6 | 5 | 19 |
| Subpart E, CS-E 600 – AMC E 730 | 22 | 2 | 5 | 13 |
| Subpart E, CS-E 740 – AMC E 800 | 14 | 6 | 9 | 21 |
| Subpart E, CS-E 810 – AMC E 930 | 19 | 1 | 6 | 18 |
| Subpart F | 7 | 1 | 5 | 9 |
| Cross-check on `should` in CS paragraphs | — | 1 | — | — |
| **Total** | **112** | **19** | **36** | **99** |

Severity, as briefed: BLOCKER is a silent omission, a wrong number, a wrong
strength, a misquote, a wrong citation or invented requirement content — anything
that would mislead a certification engineer. MAJOR is an unrecorded cut, a
duplication, an engine-profile conflict. MINOR is register, template and link
defects.

## Defect classes, most to least serious

1. **Silent omission.** Source obligations reaching neither the Requirement table
   nor `## Not applicable`. Worst case: AMC E 790, where most of AMC E 790(a)(2)
   is absent, including the material AMC E 790(2) and (3) route CS-E 790(b)
   compliance to — and CS-E 790(b) is the route this engine elects.
2. **Invented cuts.** `## Not applicable` entries recording the removal of text
   the source never contained. AMC E 510 records a cut of "the fan" from a
   paragraph in which the word does not occur. Several notes record a fan cut
   from a sub-point that has no fan wording and is reproduced in full.
   This is the inverse of silent omission and defeats the same guarantee.
3. **Strength errors.** A `must` rendered Accepted method, a `will` rendered
   Required, a `should` in a CS paragraph rendered Required.
4. **Wrong citations.** A statement attributed to a sub-point that does not carry
   it, or to one that does not exist — CS-E 510(a)(5), where CS-E 510(a) runs
   (1) to (4).
5. **Invented content.** Plausible elaboration from general knowledge: the
   rotor-lock mechanism in AMC E 910, the hot-section damage mechanism in
   AMC E 870.
6. **Engine-profile conflicts.** Three notes state that `engine_profile.md`
   records something as an open item. It records exactly one `[VERIFY]`, about
   the additional 25 hours of AMC E 740(c)(2)(i).
7. **Unrecorded cuts.** Mostly the "thrust or power" prune, explained in
   `## Application to this engine` prose rather than recorded in
   `## Not applicable`. Not silent, but not where the template puts it.

The per-note detail follows, one section per scope, as written by each pass.


---

# Orchestrator cross-check — the ten `should` instances in CS paragraphs

CLAUDE.md states there are 10 instances of `should` inside in-scope **CS**
paragraphs, each of which must carry **Recommended** and never Required. The
matrix export counts only **2** rows labelled Recommended. Audit of all ten:

| # | Paragraph | Line | Verdict |
|---|---|---|---|
| 1 | CS-E 25(c)(5) | "the recommended periods at which it should be cleaned" | Not an obligation verb. The operative verb is in CS-E 25(c). No finding. |
| 2 | CS-E 50(h)(2) | "its capacity should provide sufficient margin" | Correctly marked **Recommended** in the note. Clean. |
| 3 | CS-E 160 | "should a Failure of an Engine" | Conditional "should" meaning "if". Not an obligation verb. No finding. |
| 4 | **CS-E 720(c)** | "and should be agreed by the Agency for individual cases" | **DEFECT — see below.** |
| 5 | CS-E 740 (c)(4) | "Engine hardware modifications should be minimised" | Inside CS-E 740(c)(4), the turbofan alternate endurance test, EXCLUDED by CLAUDE.md. No note content. No finding. |
| 6 | CS-E 740 (c)(4) | "The applicant should therefore decide" | Same sub-point. No finding. |
| 7 | CS-E 740 (c)(4) | "on average should be held within ± 3 %" | Same sub-point. No finding. |
| 8 | CS-E 740 (c)(4) | "for which target conditions should be justified" | Same sub-point. No finding. |
| 9 | CS-E 770(a) | "the temperature indicated for service use should be the oil temperature" | Correctly marked **Recommended** in the note. Clean. |
| 10 | CS-E 800(e)(3) | "subparagraphs (e)(4), (5) and (6) should be applied" | Inside CS-E 800(e), the core engine flocking bird test, dropped and recorded in `## Not applicable`. No finding. |

## Findings

### CS-E 720.md
- **BLOCKER** — obligation strength upgraded. CS-E 720(c) carries two verbs in one
  sentence: "The system **must** be operated during a suitable Engine endurance
  test for periods representative of the duration and frequency of operation of
  the system during likely service usage, and **should** be agreed by the Agency
  for individual cases." The note folds both into a single row —
  "Operate the system during a suitable engine endurance test for periods
  representative of the duration and frequency of operation of the system during
  likely service usage, agreed by the Agency for individual cases." — with
  Strength `Required if claimed`. The Agency-agreement half is a `should` in a
  CS paragraph and must be a separate row at `Recommended`. CLAUDE.md accuracy
  rule 2 forbids the upgrade. [CS-E 720(c)]

## Note on the CLAUDE.md count

CLAUDE.md says "Rare — 10 instances in scope". Ten lines do contain `should`, but
only **four** of them are obligation verbs in a sub-point that reaches a note
(CS-E 50(h)(2), CS-E 720(c), CS-E 770(a), and CS-E 25(c)(5) arguably not). The
rest are a conditional "should", or sit in sub-points that are excluded or
pruned. The figure in CLAUDE.md is a raw string count, not a count of
Recommended obligations, and it is exactly the kind of measured value that file
says should not live there. Worth a one-line correction to the rules file.

---

# Subpart A, first half (13 notes) — verification

## Summary

Thirteen notes checked against their source paragraph files in `work/paragraphs/`
(AMC notes checked against every file listed in the manifest): AMC General,
CS-E 10, CS-E 15, CS-E 20, AMC E 20, CS-E 25, AMC E 25, CS-E 30, AMC E 30,
CS-E 40, AMC E 40, CS-E 50, AMC E 50. Three notes are clean (AMC General,
CS-E 10, CS-E 20). Totals: **2 BLOCKER, 6 MAJOR, 10 MINOR**. All quoted passages
in the thirteen notes were machine-checked against the source files and every one
is verbatim; no misquotes and no wrong numbers were found. The two BLOCKERs are a
strength upgrade in CS-E 40(c) and a rewritten obligation in AMC E 40(b)(3)(3).
The MAJORs are unrecorded cuts (AMC E 20 x2, AMC E 30, CS-E 50), one wrong
amendment-history statement (CS-E 25) and a duplicated-block defect in AMC E 50.

## Findings

### AMC General.md
_clean_

### CS-E 10.md
_clean_ — the Amendment 7 history matches `work/redline.json` (`specific` ->
`defined`, `subparts` -> `Subparts`, `21.A.16` -> `point 21.B.75 of Part 21`).

### CS-E 15.md
- **MINOR** — a short quotation is attributed to all three probability terms but
  matches only two of them. Note says: "CS-E 15(b) attaches each range with
  \"Where numerical values are used this may normally be interpreted as\"". Source
  says, for Remote: "When numerical values are used, this may normally be
  interpreted as a probability in the range 10 -5 to 10 -7 per Engine flight hour."
  (Extremely Remote and Reasonably Probable do use "Where … used this".) The
  quotation is verbatim; "each range" is not. [CS-E 15(b)]

### CS-E 20.md
_clean_ — all of (a)–(f) reach the table, the propeller clause of (d) is recorded
under `Not applicable`, and (f) as "Required if claimed" is consistent with the
elective OEI ratings of CS-E 40(b)(3).

### AMC E 20.md
- **MAJOR** — unrecorded cut. The propeller clause of point (7) is dropped and
  appears nowhere in `Not applicable` (which records only the point (6) propeller
  example). Source says: "…including Back-up or Alternate Modes whether
  dispatchable or not, and including the Propeller when applicable." Note says:
  "…including Back-up or Alternate Modes, whether dispatchable or not."
  [AMC E 20(7)]
- **MAJOR** — omitted obligation inside an applicable sub-point, neither in the
  table nor in `Not applicable`. Source says: "For example, all necessary provision
  should be made in the Engine for the fitment and operation of at least the
  mandatory items of equipment prescribed by the use of the word 'should' in the
  assumed applicable aircraft specifications." The note's (4) row stops after the
  coordination sentence; this example, which carries its own "should", is absent
  from the whole note. [AMC E 20(4)]
- **MINOR** — the post-Amendment 8 title is restated with the wrong
  capitalisation. Source banner: "AMC E 20(f) Power Assurance Data for Engines with
  One or More OEI Power Ratings". Note says: "…One or more OEI Power Ratings".
  (The rest of the Amendment 8 history — title recapitalisation and CS-E 50(f) ->
  CS-E 50(j) — matches `work/redline.json`.)

### CS-E 25.md
- **MAJOR** — wrong statement of what Amendment 8 changed in the AMC, and it
  contradicts the AMC E 25 note. Note says: "[[AMC E 25]] was separately amended at
  Amendment 8, which added point (6) on the initial maintenance programme test."
  Source AMC E 25(6) is: "The applicant for the certification of a piston Engine may
  substantiate a time between overhauls (TBO) or a time between replacements (TBR)."
  The initial maintenance programme test was inserted into point (1), not point (6)
  (`work/redline.json`, `AMC E 25 [Amdt8]`), and `AMC E 25.md` records it correctly.
- **MINOR** — an "and/or" is narrowed to "or". Source says: "The programme must
  include service Engine tests or equivalent service Engine test experience on
  Engines of similar design and/or evaluations of service usage of the 30-Second /
  2-Minute OEI ratings." Note says: "…or equivalent service engine test experience on
  engines of similar design, or evaluations of service usage…" [CS-E 25(b)(2)]

### AMC E 25.md
- **MINOR** — two strength cells do not follow the source verb. (a) The first
  (4)(a) row is marked **Required** in an AMC; the source sentence restates the CS
  ("the airworthiness limitations section … are required to prescribe the mandatory
  post-flight inspections"), which under the seven-term table is a Statement — the
  binding force sits in CS-E 25(b)(2), where the note already carries it. (b) The
  second (1) row is marked **Statement** for "The mandatory inspection and
  maintenance actions considered under CS-E 25(b)(1) may also evolve after entering
  service", a "may" the table maps to Permitted. Coverage of (1)–(6) is otherwise
  complete and the Amendment 8 history is correct.

### CS-E 30.md
- **MINOR** — a statement in `Application to this engine` that the source paragraph
  does not make: "For a rotorcraft engine that code is CS-27 or CS-29." CS-E 30 names
  no aircraft code; the CS-27/CS-29 pairing comes from AMC E 20(f) and CS-E 780. A
  [VERIFY] immediately follows, so the risk is low, but it is presented as fact in a
  CS-E 30 note.

### AMC E 30.md
- **MAJOR** — unrecorded cuts in Table 1. `Not applicable` records the CS-E 180
  propeller rows and the propeller part of the Engine Control System row, but not the
  whole **PISTON ENGINES** block of Table 1 (CS-E 230 de-icing/anti-icing, CS-E 260
  filters, CS-E 340 vibration tests, CS-E 430 water spray tests), and not the thrust
  reverser element of the Vibration Surveys row ("Intake conditions, exhaust
  conditions. Propeller or thrust reverser effects." [CS-E 650]). Having recorded one
  class of cut and not the other, the note leaves a reader unable to tell deliberate
  exclusion from omission. (The Amendment 7 oil-consumption quotation is verbatim and
  matches `work/redline.json`.)

### CS-E 40.md
- **BLOCKER** — strength upgraded from Statement to Required. Source says: "(c) The
  Engine Thrust and/or Power ratings **will** be based on standard atmospheric
  conditions, with no air bleed for aircraft services and with only those accessories
  installed which are essential for Engine functioning, including controls, unless
  otherwise declared in the Engine type certificate data sheet." Note says: "|
  **(c)** | Base ratings on standard atmospheric conditions… | Required |". A
  declaratory "will" maps to **Statement**; the note also converts it into an
  imperative. [CS-E 40(c)]

### AMC E 40.md
- **BLOCKER** — point (3) is restated so the flexibility attaches to the wrong object
  and its condition is dropped. Source says: "Therefore some flexibility is possible
  in defining the mandatory maintenance actions, provided they are appropriately
  validated during certification (see also AMC E 25)." Note says: "Experience has
  shown differing manufacturer capabilities and margins, so some flexibility is
  possible in defining **them**." — "them" reads back to the ratings, and the
  "provided they are appropriately validated during certification" proviso is absent
  from the row and from the rest of the note. [AMC E 40(b)(3)(3)]
- **MINOR** — an item count that does not match the list that follows. Note says: "|
  **(3)** | Turbine engine items: the **twenty-one** limitations listed below." The
  table below holds 18 rows, (a)–(r); (s), (t) and (u) are correctly cut and recorded
  under `Not applicable`. Source AMC E 40(d)(3) does list 21 items, so the count is
  true of the source and false of the note. [AMC E 40(d)(3)]

### CS-E 50.md
- **MAJOR** — unrecorded cut of an in-scope cross-reference. Source says: "(d) System
  Safety Assessment. … together with the predicted frequency of occurrence of these
  Faults or Failures. (See also CS-E 110(e))". The note's (d) row and its Compliance
  bullet both stop at "predicted frequency of occurrence"; CS-E 110(e) appears nowhere
  in the note, and CS-E 110 is APPLIES in `work/applicability.md` (line 68) with its
  own vault note. [CS-E 50(d)]
- **MINOR** — the note has no `## Not applicable` section, yet it cuts the CS-E 390
  reference from (a)(2) and the CS-E 210 reference from (d). Both cuts are explained in
  `Application to this engine` prose instead of one line each in the section the
  template reserves for them.
- **MINOR** — strength of the (g)(2) exception row. Source says: "The specification of
  CS-E 50(g)(2) does not apply to thrust or power command signals from the aircraft."
  The note marks it **Relief**; the wording fixes scope rather than exempting from
  something otherwise required, which the table labels **Statement**. Low confidence,
  but worth one ruling applied consistently across the vault. [CS-E 50(g)(2)]

### AMC E 50.md
- **MAJOR** — the note contains six duplicated blocks, apparently from a botched merge
  of the four source AMCs. Lines 60–83 repeat lines 35–58 verbatim (the "What is inside
  the Engine Control System" body plus a second "### Air signal line precautions [(6)]"
  heading and body); lines 97–99 repeat 93–95 ("The split matters…"); lines 132–151
  repeat 111–130 ("The flight and operating conditions…" through a second copy of "The
  two-sided constraint", the repeat demoted to `####`); lines 164–166 repeat 160–162
  ("The second obligation is the substantive one…"). No requirement content is wrong,
  but the note is about a third longer than its content and has two identically titled
  `###` sections.
- **MINOR** — a `Not applicable` entry names a sub-point that has no such clause. Note
  says: "**AMC E 50(2)**, **AMC E 50(5)** propeller clauses". Source AMC E 50(5)
  contains no propeller wording at all (it is aircraft-supplied power, ending "see AMC
  20-1 and AMC 20-3 for relevant interpretation"); only (2) carries "and the Propeller
  when applicable".

## Checks that produced no findings

- All quotations in the thirteen notes were compared against the manifest's source
  files after normalising quotes, dashes and whitespace: every one is verbatim. The
  only non-matches are redline strings in Amendment-history sections (from
  `work/redline.json`, carrying bold markers) and the term "OEI override", which comes
  from `engine_profile.md`.
- Numbers: the 10-3/10-5/10-7/10-9 probability ranges [CS-E 15(b)], 10 % deterioration
  and the 2-hour additional test [AMC E 40(b)(3)(6)], the 2.5-minute combined structure
  and derated 30-second period [AMC E 40(b)(3)(5)], the 30-minute periods
  [AMC E 40(b)(3)(7)], "three applications of 30 seconds OEI rated power"
  [AMC E 25(4)(d)(ii)], CS-27.45(f)/CS-29.45(f) [AMC E 20(f)(1)], and the 18 piston /
  21 turbine limitation items [AMC E 40(d)] — all correct against source.
- Engine-profile consistency: every `Application to this engine` section matches
  `engine_profile.md` (30-Second OEI, 2-Minute OEI, Continuous OEI and Rated 30-Minute
  Power claimed; 2.5-Minute OEI and 30-Minute OEI not claimed, correctly stated in
  CS-E 40; EECS-FADEC full authority; no refrigerant injection, cut at AMC E 40(d)(3)(s);
  no thrust reverser, cut at CS-E 10(b) and AMC E 40(d)(3)(t); 'OEI override' assessed
  under CS-E 50, not CS-E 40).
- Amendment-history sections of CS-E 10, CS-E 25, CS-E 40, AMC E 20, AMC E 25 and
  AMC E 30 were compared against `work/redline.json`; only the CS-E 25 entry above is
  wrong.

---

# Subpart A, second half (CS-E 60 – AMC E 170) — verification

## Summary

20 notes checked against their source paragraph files in `work/paragraphs/`
(21 source files, since AMC E 60 merges `AMC_E_60.txt` + `AMC_E_60_d.txt`).
Coverage, strength, numbers, citations, quotations, recorded cuts, invention,
duplication and engine-profile consistency were checked note by note.

Result: **0 BLOCKER, 0 MAJOR, 9 MINOR.** 13 notes are clean. No silent
omission, no wrong number, no wrong strength label, no misquote and no invented
requirement content was found in this scope. Every sub-point of every CS-E
paragraph in scope reaches its note's Requirement table or its `## Not
applicable` section, and every short quotation I checked is verbatim in the
source. The nine MINOR findings are all template/consistency issues: a cut
explained in `## Application to this engine` instead of being recorded in
`## Not applicable` (three cases), a table row that folds a `may`-permission
into an `Accepted method`/`Required` row (three cases), table/source items with
no Requirement row (two cases), and one figure loose end.

Numbers spot-checked and correct: `23.7 litres` [CS-E 130(c)], `0.25 litre`
[AMC E 130(1)(e)], `5 minutes` / `10 minutes` / `15 minutes` [AMC E 130(2)(d)(i),
(5)], `3 minutes` twice [CS-E 150(d)], `2 minute time limitation`
[AMC E 60(d)(2)]. Amendment-history before/after blocks in CS-E 120, CS-E 160,
AMC E 60 and AMC E 130 match `work/redline.json` word for word. Engine-profile
claims (30-Second OEI, 2-Minute OEI, Continuous OEI, Rated 30-Minute Power
claimed; 2.5-Minute and 30-Minute OEI not claimed; EECS-FADEC full authority; no
time-limited dispatch) are used correctly wherever they appear.

## Findings

### CS-E 60.md
- **MINOR** — the `[!summary]` callout paraphrases the reset restriction as a
  flight-crew restriction, which is the AMC's wording, not the specification's.
  Source says: "Have means or provision for means, which cannot be reset in
  flight" [CS-E 60(d)(2)]. Note says: "record every use in a way the flight crew
  cannot reset". The Requirement table row itself is exact ("which cannot be
  reset in flight"), so the defect is confined to the summary. The flight-crew
  formulation belongs to [AMC E 60(4)] / [AMC E 60(d)(4)].

Coverage confirmed: (a) two duties, (b) two duties, (c), (d)(1), (d)(2)(i),
(d)(2)(ii), (d)(3), (e) plus (e)(1)–(e)(3) and the closing inspections sentence
— all present. The cross-references [[CS-E 40|CS-E 40(g)]] (accuracy of Engine
Control System and instrumentation as defined in CS-E 60(b)) and
[[CS-E 30|CS-E 30(b)]] (interface conditions and reliability specifications for
components outside the type design) both point at the right sub-points.

### AMC E 60.md
_clean_

Both source files walked. `AMC_E_60.txt` (1), (2)(a), (2)(b), (4) are in the
table; (3) is cut and recorded in `## Not applicable` with its reason (thrust
reverser example). `AMC_E_60_d.txt` (1)–(5) all present, with (5)'s two limbs
split correctly into Permitted ("can be approved") and Relief ("need not be
considered"). The quotation "the aircraft should still comply with
CS-27/29.1305 specifications" is verbatim. The alias
[[AMC E 40|AMC E 40(b)(3)]] used for the source's "paragraph (5) of AMC E 40(b)"
resolves to the right material — `AMC_E_40_b_3.txt` paragraph (5) is the
extension of 2-Minute OEI to 2.5 minutes.

### CS-E 70.md
_clean_

### AMC E 70.md
- **MINOR** — the same source sentence is given two different strengths in three
  places. For castings it gets its own row: "Subsequent relaxation may be
  introduced in quantity production, at the engine constructor's discretion,
  using a system acceptable to the Agency. | **Permitted**". For forgings and
  welds the identical clause is folded into an Accepted method row ("…continue
  it until a satisfactory standard of quality has been established; relaxation
  may follow in quantity production…"). Source wording is the same in all three
  [AMC E 70(1)], [AMC E 70(2)(a)], [AMC E 70(3)]. The `may` permission is
  therefore visible for castings and hidden for forgings and welds.

Coverage otherwise complete: (1), (2)(a), (2)(b), (2)(c), (3), all obligations
present. The two short quotations ("Failure … could hazard the aircraft" and
"Failure or leakage of which could hazard the aircraft") are verbatim, and the
note's observation that welds add leakage as a failure mode is supported by the
source.

### CS-E 80.md
- **MINOR** — a cut is explained in prose but not recorded in a `## Not
  applicable` section (the note has none). Source says: "Unless the
  specifications prescribed in subpart C or E, as appropriate, will subject this
  equipment to such cycles of operation…" [CS-E 80(b)]. Note's table row says:
  "Where the specifications prescribed in Subpart E will not subject the
  equipment to cycles of operation…". The Subpart C limb is dropped. The
  `## Application to this engine` section does explain why ("Subpart C is the
  piston engine type substantiation subpart and is outside the scope of this
  vault"), so this is not a silent omission — but CLAUDE.md puts the record in
  `## Not applicable`, one line with the sub-point reference and the reason.

Coverage otherwise complete: (a)(1)(i), (a)(1)(ii), (a)(2)(i), (a)(2)(ii), (b)
×2, (c)(1), (c)(2), (c)(3), (d)(1), (d)(2), (d)(3). The "will be accepted …
subject to" quotation is verbatim, and so is the AMC E 50 quotation "should be
covered, in addition, under other CS-E paragraphs such as CS-E 80 or CS-E 170,
as appropriate" (checked against `work/paragraphs/AMC_E_50.txt` lines 40-41).

### AMC E 80.md
- **MINOR** — Table 2 item 18, "EMI, HIRF & lightning / See AMC 20-1 and
  AMC 20-3", has no row in the `### AMC E 80(2)(b)` Requirement table, while
  items 14, 15, 16, 17 and 19 all do. It is not a silent omission — the item is
  named in `## Application to this engine` ("Table 2 item 18 and Table 4 item 24
  name AMC 20-1 and AMC 20-3…") and carries a `[VERIFY]` — but the Requirement
  table is the 1:1 map to the source and this entry is missing from it. All 13
  Table 1 items and both Table 4 obligations are present, which makes item 18
  the only gap.
- **MINOR** — a second cut explained in prose rather than recorded. Source says:
  Table 1 item 11 "Induction Icing / As a reminder. See CS-E 230 & CS-E 780"
  [AMC E 80(2)(a)]. Note says (in `## Application to this engine`): "CS-E 230 is
  a Subpart B piston engine paragraph and is outside the scope of this vault, so
  the applicable specification for this engine is [[CS-E 780]] alone." The note
  has no `## Not applicable` section.
- **MINOR** — `work/paragraph_index.csv` records `figure_pages` for AMC E 80 as
  `44 45 47 48 49 50`, and the note embeds `AMC_E_80_p45.png`, `_p47`, `_p48`,
  `_p49`, `_p49_2`, `_p49_3` and `_p50`. There is no `AMC_E_80_p44.png` in
  `vault/figures/` and nothing embedded for page 44. Either the index's page-44
  entry is spurious or a crop is missing; I cannot tell which without the PDF.
  Worth resolving because rule 6 forbids describing a table instead of embedding
  it.

### CS-E 90.md
_clean_

### CS-E 100.md
- **MINOR** — a term is pruned from the Requirement table without a `## Not
  applicable` record (the note has no such section). Source says: "operating
  range of rotational speeds and power/thrust" [CS-E 100(c)]. Note's table row
  says: "operating range of rotational speeds and power". The
  `## Application to this engine` section quotes the full phrase and explains
  ("For a turboshaft the thrust term is inapplicable and the power term
  governs"), so the reader can tell this was deliberate, but the cut is not
  recorded where CLAUDE.md puts it.

Coverage otherwise complete: (a) three duties, (b), (c). The turbine-engine
residual-stress sentence is quoted verbatim.

### CS-E 110.md
_clean_

All five sub-points and their split duties are present: (a) ×3, (b), (c) ×2,
(d), (e) ×2. The short quotations "where this is not practical" and "Except
where otherwise agreed" are verbatim, and the note's reading of (d) as an order
of preference (design first, permanent marking as fallback) follows the source's
"or, where this is not practical".

### CS-E 120.md
_clean_

Amendment history matches `work/redline.json` exactly, including the inserted
tokens "points", "point", "of Part 21". The `[VERIFY]` for the unavailable
Part 21 text is appropriate.

### CS-E 130.md
_clean_

Coverage: (a) ×2, (b) ×2, (c), (d)(1), (d)(2), (d)(3), (e), (f), (g), (g)(1)
×2. Both piston passages are cut and recorded in `## Not applicable` with the
sub-point reference and the reason — the (c) second sentence (integral oil sump
below 23.7 litres) and the whole of (g)(2) with (g)(2)(i)–(iv). The
`## Not applicable` lines record what was removed and why, not what it said, as
required. All three quotations drawn from AMC E 130 are verbatim.

### AMC E 130.md
_clean_

Full walk of a 320-line source: (1)(a)–(e), (2)(a)–(d) including (2)(d)(i)–(v),
(3)(a)–(e), (4)(a)–(d), (5), (6), (7), (8), (9). Every one has a Requirement
row. Two partial cuts are recorded in `## Not applicable`: the propeller
feathering limb of the (2)(b) objective, and thrust augmentation as an example
in (2)(c) — with the note correctly keeping the hydraulic-system example from
the same sentence. Quotations checked verbatim: "a reasonable time period for
the flight crew to recognise a fire condition, shut down the appropriate Engine
and close the appropriate fuel shutoff valve(s)", "might exist for as long as
the continued rotation effects are present or until the oil supply is depleted",
"oil tank fire tests have failed due to high internal pressure and inadequate
venting", "can reduce the susceptibility of Engines to titanium fires", "or
feathering of the Propeller (if the Propeller control system is part of the
Engine design)", "In the absence of a more suitable determination of a hazardous
quantity of flammable fluid". Amendment history matches `work/redline.json`: the
Amdt 8 change is the single `c` → `e` substitution in (4)(d), and the note's
explanation of why it matters is drawn from CS-E 130 itself, not from outside
knowledge.

### CS-E 135.md
_clean_

### AMC E 135.md
_clean_

The note's observation that the AMC scopes the population more widely than the
specification is supported by both texts, and both quotations are verbatim.

### CS-E 140.md
_clean_

Coverage: (a), (b), (c) ×2, (d)(1) ×2, (d)(2) ×2, (e). Both cuts are recorded in
`## Not applicable` with reference and reason — the CS-E 350 limb of (d)(1), and
the whole of (f) (propeller). The (d)(2) relief is correctly split into Relief
("need not be loaded") plus the Required arithmetic that replaces it.

### AMC E 140.md
_clean_

The note flags the source's own citation oddity — AMC E 140 says "as required by
CS-E 140(d)(1)" while the unloading relief sits in CS-E 140(d)(2) — without
silently correcting it. That is the right treatment.

### CS-E 150.md
- **MINOR** — the (b) row folds a `may` permission into a Required row, so the
  permission is not visible in the `Strength` column. Source says: "only
  servicing and minor repairs must be permitted except that major repairs or
  replacement of parts **may be resorted to**, provided that the parts in
  question are subjected to an agreed level of penalty testing" [CS-E 150(b)].
  Note says: one row, "Permit only servicing and minor repairs during all tests,
  except that major repairs or replacement of parts may be resorted to
  provided… | Required". The prose below the table does draw the distinction
  ("Sub-point (b) does not forbid a major repair during testing. It attaches a
  price"), so the substance is not lost.

All six sub-points covered. The claim about AMC E 150(a) in `## Application to
this engine` ("its whole body permits a higher grade fuel or an approved
anti-detonant to suppress detonation during a test representing Maximum
Continuous Power at altitude") was checked against
`work/paragraphs/AMC_E_150_a.txt` and is accurate. The 3-minute exception
reasoning is consistent with `engine_profile.md`.

### CS-E 160.md
_clean_

Amendment history matches `work/redline.json` (deleted "21.A.21(c)(3)",
inserted "point" and "21.A.20(d)2"), and the note is careful to say the CS-E
duty is unchanged while flagging that the cited provision itself changed. The
`[VERIFY]` about whether the two Part 21 provisions impose the same obligation
is exactly the case rule 5 is for.

### CS-E 170.md
_clean_

### AMC E 170.md
- **MINOR** — two closing sentences of the source have no Requirement-table row:
  "Additional means may be found in AMC E 80 or in AMC 20-1 and AMC 20-3 for
  Electronic Engine Control Systems." and "See AMC E 80 for additional specific
  means." Both are referred to in `## Application to this engine` (and carry a
  `[VERIFY]` for the unavailable AMC 20-1 / AMC 20-3), so nothing is silently
  omitted, but the table is the 1:1 map and these pointers are absent from it.

Everything else in this continuous-prose AMC is covered, including all four
"other reasons for testing" examples minus the turbocharger one, which is cut
and recorded in `## Not applicable` together with the CS-E 440 reference and the
reason (piston material in Subpart C). The quotation "not imposed by the rules,
but should be representative of the environments that are expected to be
encountered in the Engine installation" is verbatim. The degraded-dispatch
treatment is correct and careful: the note does not equate "each approved
degraded state" with time-limited dispatch, notes that `engine_profile.md`
records time-limited dispatch as not claimed, and raises a `[VERIFY]` instead of
concluding.

---

# Subpart D (17 notes) — verification

## Summary

All 17 Subpart D notes in `/home/user/CS-E/vault/` were checked against their
source paragraph files in `/home/user/CS-E/work/paragraphs/` (AMC E 520 was
checked against all four of its source files). 8 notes are clean. 30 findings:
**6 BLOCKER**, **5 MAJOR**, **19 MINOR**. All six BLOCKERs and four of the five
MAJORs sit in the two long AMC notes, `AMC E 510.md` and `AMC E 515.md`, and all
six BLOCKERs are silent omissions or an invented statement about source content —
none is a wrong number. Every number, time, percentage and probability in the
seventeen notes was checked against the source and every one is correct.

## Findings

### CS-E 500.md

- **MAJOR** — Compliance bullet attaches continuous ignition to a sub-point that does not carry it. Note says: "Continuous ignition provisions [CS-E 500(c)], covered by [[CS-E 720]]." Source CS-E 500(c) says: "All Engines must be equipped with an igniter system suitable for starting the Engine on the ground and in flight at all altitudes up to a declared altitude." Continuous ignition is a separate, conditional paragraph — CS-E 720(a): "Where approval of an Engine is sought which permits or requires the use of a continuously-operated ignition system…". Nothing in CS-E 500 requires continuous ignition provisions. [CS-E 500(c)]
- **MINOR** — Compliance bullets name supporting tests the source does not cross-reference. Note says: "Surge and instability substantiation across that range [CS-E 500(a)]. The supporting tests are the engine bleed conditions of [[CS-E 690]], the excess operating conditions of [[CS-E 700]], and the ingestion and environmental tests of [[CS-E 780]], [[CS-E 790]] and [[CS-E 800]]." CS-E 500(a) makes no reference to any of these paragraphs. Defensible as a derived compliance route, but it reads as source content. [CS-E 500(a)]
- **MINOR** — Sub-point **(b)** ("[Reserved]") is handled in a prose line under the table rather than in a `## Not applicable` section. Nothing was actually cut, so the omission of the section is arguable, but the template puts recorded exclusions in that section. [CS-E 500(b)]

### CS-E 510.md

- **MINOR** — Strength for **(b)** is Statement. Source: "If significant doubt exists as to the effects of Failures and likely combination of Failures, any assumption **may** be required to be verified by test." The seven-term table maps `may` to Permitted; the note's own Compliance section treats it as an action ("Test verification of any assumption where significant doubt exists [CS-E 510(b)]"), which is inconsistent with a Statement label. [CS-E 510(b)]
- **MINOR** — The four **(g)** rows are labelled Statement, but the source verb is `must` in each ("must be regarded as a Minor Engine Effect", "The following effects **must** be regarded as Hazardous Engine Effects", "must be regarded as a Major Engine Effect"). Statement is defensible for definitional text under CLAUDE.md's own description, but the label is a downgrade against the source verb and should be consistent with how `must`-definitions are handled elsewhere in the vault. [CS-E 510(g)(1)–(g)(3)]

Coverage, numbers (10⁻⁵, 10⁻⁷, 10⁻⁸ per Engine flight hour), the `(f)(4)`/`(f)(8)`/`(f)(9)`/`(g)(2)(vi)` exclusions, and the AMC E 20(f)(2), AMC E 60(d)(3), AMC E 170 and CS-E 50(h) cross-references were all checked and are correct.

### AMC E 510.md

- **BLOCKER** — Silent omission at **(3)(d)(ii)**. Source says: "These specifications are considered to support a design goal that, among other goals, primary LCF (Low Cycle Fatigue) Failure of the component should be Extremely Remote throughout its operational life." The note's two (3)(d)(ii) rows carry the reliance on CS-E 515 and the summation relief, but the LCF design goal — the substance of what meeting CS-E 515 is taken to achieve — appears nowhere in the note (`LCF` does not occur in the file) and is not in `## Not applicable`. [AMC E 510(3)(d)(ii)]
- **BLOCKER** — Silent omission at **(3)(d)(iv)**. Source says: "The intent of CS-E 510(g)(2)(ii) is to address the relative concentration of toxic products in the Engine bleed air delivery. The Hazardous Engine Effect of toxic products relates to significant concentrations of toxic products, with 'significant' defined as concentrations sufficient to incapacitate persons exposed to those concentrations." This is the AMC's definition of the threshold term and it is absent from the note entirely. [AMC E 510(3)(d)(iv)]
- **BLOCKER** — Silent omission at **(3)(e)**. Source says: "The concentration of toxic products in the Engine bleed air may be interpreted as the generation and delivery of toxic products as a result of abnormal Engine operation that would incapacitate the crew or passengers, except that the products are slow-enough acting and/or are readily detectable so as to be stopped by crew action prior to incapacitation. Possible reductions in crew capabilities due to their exposure while acting in identifying and stopping the products **should be considered, if appropriate**." Neither the interpretation nor the accepted-method obligation in the second sentence reaches the note; the note's (3)(e) rows jump from the Major Engine Effects list straight to the installer-information duty. [AMC E 510(3)(e)]
- **BLOCKER** — Invented source content in `## Not applicable`. Note says: "**(3)(d)(iii)**, in part — the fan is named among the rotating components in the general debris discussion. A turboshaft has no fan…". The word "fan" does not occur anywhere in `work/paragraphs/AMC_E_510.txt`. The source names "discs, hubs, impellers, large rotating seals, and other similar large rotating components". The entry records a cut that was never in the source. [AMC E 510(3)(d)(iii)]
- **MAJOR** — Misattribution and dropped clause at **(3)(f)**. Note says: "Both assumptions may be revisited during aircraft certification, particularly multi-engine rotorcraft certification." Source attaches the two qualifiers to different assumptions: the minor-effect assumption "may be revisited during aircraft certification, **where installation effects such as Engine redundancy may be fully taken into consideration**", and only the rating-failure assumption is qualified "particularly multi-Engine rotorcraft certification". The engine-redundancy clause — directly relevant to a multi-engine rotorcraft — is dropped without record, and the same misattribution is repeated in `## Application to this engine`. The source's opening sentence "It is generally recognised that Engine Failures involving complete loss of thrust or power from the affected Engine can be expected to occur in service, and that the aircraft should be capable of controlled flight following such an event" is also absent. [AMC E 510(3)(f)]
- **MAJOR** — Strength at **(3)(c)**. Note says: "Where the applicant cannot determine the detailed Failure sequence, rate of occurrence or dormancy period of Failures of aircraft components, assume a Failure rate for those components for engine certification. | Accepted method". Source says: "In such cases, for Engine certification, the applicant **will** assume a Failure rate for these aircraft components." `will` maps to Statement, not Accepted method. [AMC E 510(3)(c)]
- **MINOR** — Unrecorded cut at **(3)(d)(iii)**. Source: "The integrity specifications of CS-E 515 provide some reliability benefits when applied to a blade (particularly when it forms a part of a blisk (also named integrally bladed rotor))." The note keeps only the negative half of the sentence ("do not provide a valid basis…"); the qualifying benefit and the blisk case are dropped with no `## Not applicable` entry. [AMC E 510(3)(d)(iii)]
- **MINOR** — Unrecorded cut at **(3)(c)**. Source: "CS-E 510(a)(1)(i) requires the applicant to take account of aircraft-level devices in the Engine safety analysis. For example, the effects on the Engine failure of aircraft air ducts might be considered." The worked example is dropped without record. [AMC E 510(3)(c)]
- **MINOR** — Added cross-reference in Compliance. Note says: "Radial containment demonstration for compressor and turbine blade shedding, singly and in likely combinations [AMC E 510(3)(d)(iii)], against [[CS-E 520|CS-E 520(c)(1)]] and [[CS-E 810]]." The source sentence cites only "(see CS-E 520(c)(1))"; CS-E 810 was the reference in the *pre*-Amendment 7 text that this amendment deleted. [AMC E 510(3)(d)(iii)]
- **MINOR** — Frontmatter `covers: ["AMC E 510"]` is a self-reference. CLAUDE.md: "`covers:` … merged AMC notes only; omit otherwise." Nothing is merged here.

The Amendment 7 before/after quotations were checked against `work/redline.json` and both are accurate, including the deleted "The Engine has a containment structure which is designed to withstand the consequences of the release of a single blade (see CS-E 810(a))…" passage.

### CS-E 515.md

_clean_ — the whole paragraph (opening sentence, (a), (b), (c)) reaches the table, the AMC E 515(1) quotation "a closed-loop system which link the assumptions made in the Engineering Plan to how the part is manufactured and maintained in service" is verbatim, and the AMC E 515(3)(d)(i) 30-minute Power and AMC E 515(6)(b) OEI-cycle citations point at the right sub-points.

### AMC E 515.md

- **BLOCKER** — Silent omission at **(3)(d)(iv)**. Source says: "Relevant service experience gained through a successful programme of parts retirement or precautionary sampling inspections, or both, **may be included to adjust the life prediction system**." This is a Permitted provision with real certification value (it is the route by which service experience relieves conservatism in the lifing system). Neither "retirement" nor "sampling" occurs in the note, and there is no `## Not applicable` entry. [AMC E 515(3)(d)(iv)]
- **BLOCKER** — Silent omission at **(3)(d)(iv)**. Source says: "Appropriate analytical and empirical tools should be utilised such that the fatigue life can be adjusted for any differences between the Engine conditions and cyclic test. In the event the test is terminated by burst or complete Failure, crack initiation for this particular test may be defined using the appropriate crack growth calculations and/or fracture surface observations. It may also be possible to utilise the number of cycles at the last crack-free inspection to define the crack initiation point. This approach requires an inspection technique with a high level of detection capability consistent with that used by the Engine industry for rotating parts." None of this — the adjustment obligation, the two ways of defining crack initiation, or the detection-capability condition attached to the second — reaches the note. The note's (3)(d)(iv) rows stop at the scatter-correction and statistical-reduction sentences. [AMC E 515(3)(d)(iv)]
- **MAJOR** — Silent omission at **(3)(e)(i)**. Source final paragraph says: "Manufacturing and in-service inspections are an option to address the potential for fracture. The intervals for each specified in-service inspection should be identified. Engine removal rates and module and piece part availability data could serve as the basis for establishing the inspection interval. The manufacturing inspections should be incorporated into the Manufacturing Plan. Likewise, the assumed in-service inspection procedures and intervals should be integrated into the Service Management Plan and included, as appropriate, in the Airworthiness Limitations Section…". The note carries the equivalent obligations for rotating parts at (3)(d)(v)(4)(a) but not for static pressure loaded parts, and records no cut. [AMC E 515(3)(e)(i)]
- **MAJOR** — Strength at **(3)(d)(v)(5)(a)**. Note says: "Determine the serviceable and repairable damage limits using a process approved by the Agency and summarised in the Service Management Plan … Publish the serviceable and repairable limits in the Instructions for Continued Airworthiness. | Required". The source splits the two: "Determine the serviceable and repairable damage limits using a process approved by the Agency and summarised within the service management plan" is *should*-level material in an AMC (Accepted method), and only "The serviceable and repairable limits **must** be published in the Instructions for Continued Airworthiness" is Required. Merging them into one Required row upgrades the determination duty. [AMC E 515(3)(d)(v)(5)(a)]
- **MINOR** — Asymmetric coverage at **(5)(b)**. The three "The intent is that:" bullets for repair and maintenance processes (developed with appropriate oversight and substantiation programmes agreed up-front; changes visible to all parties and not made without crossfunctional review and approval; suspected non-conformance reviewed with the appropriate skill mix prior to disposition) are dropped, while the identical three bullets at (4)(c) for the Manufacturing Plan are kept in full. [AMC E 515(5)(b)]
- **MINOR** — Unrecorded cuts at **(4)(a)**, **(4)(c)** and **(5)(a)**. The Manufacturing Plan and Service Management Plan introductions have no rows, and (4)(c)'s "The level of detail in the Plan may vary depending on the specific process step being considered, the sensitivity of the particular process step, and the level of control required to achieve the required life capability" is dropped. Rationale text rather than obligation, but nothing records the cut.
- **MINOR** — The alternative burst-margin row at **(3)(d)(iv)** drops a qualifier: source "Typically a 2/3 factor has been applied to the minimum **(1/1000 or alternatively -3 sigma)** burst life"; note "typically a 2/3 factor has been applied to the minimum burst life". The 2/3 figure itself is correct. [AMC E 515(3)(d)(iv)]
- **MINOR** — The cut of "reverse" from the (3)(d)(i) flight-segment list is explained in `## Application to this engine` but the note has no `## Not applicable` section, so the cut is not recorded where the template puts it. [AMC E 515(3)(d)(i)]
- **MINOR** — Frontmatter `covers: ["AMC E 515"]` is a self-reference; nothing is merged.

Numbers all verified correct: 1/1000, −3 sigma, 0.75 mm, 2/3, 3 000 representative flight cycles, 50 %, 0.762 mm × 0.381 mm (0.030 in × 0.015 in), 0.381 mm × 0.381 mm (0.015 in × 0.015 in). The ALS quotation at (6)(a) is verbatim, the figure `AMC_E_515_p93.png` exists, and the Amendment 7 "Before" quotation ("Anomalies for which a common understanding has been reached within the Engine community and the Authorities should be considered in the analysis.") matches `work/redline.json` exactly.

### CS-E 520.md

- **MINOR** — Compliance bullet cites the CS for an AMC-only duty. Note says: "Declared containment angle limits, made available to the aircraft constructor [CS-E 520(c)(1)]." CS-E 520(c)(1) says only that debris from blade shedding "will be radially contained (see AMC E 520(c)(1))". The containment-angle declaration is in AMC E 520(c)(1)(2) ("provided the limits of the angles to which containment is assured are made available to the aircraft constructor installing the Engine"), which the same bullet links as accepted means. [CS-E 520(c)(1)]

Coverage of (a), (b), (b)(1), (b)(2), (c)(1), (c)(2), (d) is complete, the bird-strike carve-out is read correctly, and both Amendment 7 before/after quotations match `work/redline.json`.

### AMC E 520.md

- **MINOR** — Two unrecorded cuts at **(c)(2)(4)**, with no `## Not applicable` section. Source: "…verified by measuring Engine vibratory response when imbalances are added to **the fan and other rotors** (See CS-E 650)"; the note's row says only "added to the rotors". The turboshaft reason is given in `## Application to this engine`, but the cut is not recorded in the template's section. The closing sentence "Vibration data is routinely monitored on a number of Engines during the engine development cycle, thereby providing a solid basis for model correlation" is dropped with no record. [AMC E 520(c)(2)(4)]
- **MINOR** — Amendment history is incomplete. The note says Amendment 7 made two changes ("The validated data list gained an item and the evaluation duties gained a case"). `work/redline.json` shows Amdt 7 also inserted into (c)(2)(3) ", and any other differences between the test configuration and the aircraft installation (e.g. production inlet configuration replaced by test intake configuration)" and "Assumptions about the Engine installation configuration should be documented in the Manuals required by CS-E 20(d).", and into (c)(2)(5) ", including interface features between Engine and aircraft". The CS-E 20(d) documentation duty in particular is a new obligation the history does not mention. [AMC E 520(c)(2)(3), (c)(2)(5)]

The ± 30° quotation at (c)(1)(2) is verbatim; all four source files (AMC E 520(a), (c)(1), (c)(2), (d)) are covered.

### CS-E 525.md

_clean_ — the single unnumbered sentence is carried complete, the AMC E 525(1) clutch-drag quotation is verbatim, and the [VERIFY] on the maximum one-engine-inoperative flight period is properly raised rather than guessed.

### AMC E 525.md

- **MINOR** — The **(1)** row merges two different strengths under Permitted. Source: "Compliance with this specification **may** be established by test or analysis and **should** take into account the conditions imposed on the Engine by a typical aircraft installation." The second limb is an Accepted method, not a permission. [AMC E 525(1)]

The (2)/(3) supersonic and turbopropeller cuts are properly recorded in `## Not applicable`, and the AMC E 130(2)(c) and CS-E 570(e)(1) cross-references were checked and are accurate.

### CS-E 540.md

_clean_ — (a), the Extremely Remote relief, (b) and (b)(1)–(b)(3) all reach the table; the AMC E 540(2) quotations "rain, hail, ice, gravel, sand, small and medium birds" and "are therefore intended to be sufficient for demonstrating compliance with CS-E 540(b) for the considered subject" are verbatim.

### AMC E 540.md

_clean_ — both paragraphs are covered, the 200-knot obligation is quoted accurately and labelled Accepted method, the loose-object provision is correctly labelled Relief, and the bifurcation strut fairing cut is recorded in `## Not applicable`.

### CS-E 560.md

- **MINOR** — Unrecorded pruning at **(b)(2)**. The Requirement row says "any device having a significant function for the control of the power"; the source says "the control of the **thrust or** power". The turboshaft reason is given in `## Application to this engine` with the verbatim quotation, but the note has no `## Not applicable` entry recording the cut. [CS-E 560(b)(2)]

All of (a)(1)–(a)(3), (b)(1)–(b)(2)(ii), (c)–(c)(3), (d), (e), (f), (g) reach the table.

### AMC E 560.md

- **MINOR** — Engine-profile over-claim in `## Not applicable`. Note says: "`engine_profile.md` declares no refrigerant injection **and no boost fluid**, so no such fluid arises on this engine." `engine_profile.md` records "Refrigerant injection | **No**" and nothing at all about water methanol or any other boost fluid. The cut of the (1) water-methanol interpretation is probably right, but the stated basis is not in the profile. [AMC E 560(1)]

All nine points are otherwise covered, including the transient fuel icing definition, which is quoted verbatim.

### CS-E 570.md

_clean_ — (a)(1)–(a)(4), (b)(1)–(b)(2), (c)–(c)(2), (d), (e)(1), (f)(1), (f)(2), (g)(1), (g)(2) all reach the table; the 35 kPa figure is correct; the propeller-feathering cuts at **(e)(2)** and **(f)(3)(i)–(iii)** are recorded in `## Not applicable` with the "When applicable" / conditional qualifier stated.

### AMC E 570.md

_clean_ — all five points covered; the "10 percent of the tank capacity" figure is correct; the onward resolution of "Hazardous quantities" to AMC E 130(1)(e) and the quotation "0.25 litre or more of fuel (or a quantity of flammable material of equivalent heat content)" were both checked against `work/paragraphs/AMC_E_130.txt` and are exact.

### CS-E 580.md

_clean_ — the single sentence is carried complete, the quantity/size distinction is read correctly, and the AMC E 80(2)(a) quotation "to all equipment that is not environmentally sealed" is verbatim.

### CS-E 590.md

_clean_ — all three sentences reach the table; the AMC E 80(4) quotation "Establishment that drive mechanism will prevent the Engine driving the starter to a dangerous speed, unless such a probability is Extremely Remote (see CS-E 590)" is verbatim; CS-E 80(c)/(d) and CS-E 140(e) were checked and are cited correctly; the [VERIFY] on whether the starter is declared as part of the engine is properly raised.

---

# Subpart E, first third (22 notes) — verification

## Summary

All 22 notes in scope were checked note-by-note against their source paragraph
files in `work/paragraphs/`, plus `engine_profile.md`, `work/redline.json` (for
the `Amendment history` sections only) and `vault/figures/` (for the three notes
that embed crops). 11 notes are clean. Findings: **2 BLOCKER, 5 MAJOR,
13 MINOR**.

Coverage was good overall: no whole applicable sub-point was found missing from
any Requirement table, every `Not applicable` entry I checked corresponds to a
real cut, all figure embeds use `![[...]]` syntax and every named file exists,
all numeric values (1013.25 hPa, 288 K, 4 500 m, 1.1/1.33/1.15/1.5 and 35 kPa,
103 %/100 %/2 points, 4.5 g and 0.5 g per 4 500 litres, 500 h, 27 degC, 0.2 ml/l,
25 operations x 5 min, 1000 h, 10 h / half-hour, Stages 3, 7, 13, 17, 23) match
the source, and every `Amendment history` section I cross-checked against
`work/redline.json` is faithful. The defects concentrate in three places:
one `should`-in-a-CS-paragraph upgraded to a mandatory strength, one false
statement about a source table, and a handful of small unrecorded cuts in the
two longest AMC notes.

A note on the recurring **Relief** issue below: CLAUDE.md fixes `Relief` to the
source verb `need not`. Five rows use `Relief` for text whose verb is `may` /
`will be acceptable` / `should be exempt`. Because the direction of the
obligation (non-mandatory) is not inverted, I have graded these MINOR rather
than BLOCKER, but they are strength labels outside the seven-term mapping and
they are inconsistent with the same notes' correct use of `Relief` elsewhere
(e.g. CS-E 650(c), CS-E 690(a)(3)(ii), AMC E 690 — all genuine `need not`).

## Findings

### CS-E 600.md
- **MINOR** — `Relief` used where the source verb is not `need not`. Source
  [CS-E 600(d)]: "it will be acceptable to clean the Engine internally at agreed
  intervals…". Note: row **(d)** … | `Relief`. Per the strength table, "will" /
  declaratory text is `Statement` and an allowance is `Permitted`; `Relief` is
  reserved for `need not`.
- **MINOR** — unrecorded micro-cut. Source [CS-E 600(b)] "jet pipes and / or
  propelling nozzles"; note "other jet pipes or propelling nozzles". Harmless,
  but the note has no `Not applicable` section at all, so nothing records that
  anything was altered. (Same class as the `thrust` cuts listed under CS-E 650,
  CS-E 710 and CS-E 730.)

### AMC E 600.md
_clean_ — single-sentence source, `Accepted method` correct for "should
justify", the CS-E 30(a)/CS-E 20(d) chain asserted in `Application` is supported
by `CS_E_30.txt` ("These assumptions must be included in the Engine instructions
for installation required under CS-E 20(d)").

### CS-E 620.md
_clean_ — all of (a)(1)–(3) and both limbs of (b) are in the table with the
values exact; the AMC E 20(f) power-assurance cross-reference in `Application`
is supported by `AMC_E_20_f.txt`.

### AMC E 620.md
- **MINOR** — sub-point **(2) Notation** has no row in the Requirement table.
  Its content is present (the `### Notation` table below), but the Requirement
  table is the declared 1:1 map and jumps from **(1)** to **(3)**.
- **MINOR** — `covers: ["AMC E 620"]` in frontmatter. CLAUDE.md: "covers:
  merged AMC notes only; omit otherwise". This note has a single source
  paragraph of the same name. (Same on AMC E 640, AMC E 650, AMC E 670,
  AMC E 680, AMC E 710, AMC E 730 — counted once here.)

### CS-E 640.md
_clean_ — (a), (a)(1)(i)–(iii), (a)(2)(i)–(iii), (b)(1)–(4) all reach the note;
every factor and the 35 kPa increments are exact; the AMC E 80(2)(c) claim
("Proof Pressure -> CS-E 640(a)(1)", "Burst Pressure -> CS-E 640(a)(2)") is
verbatim in `AMC_E_80.txt` Table 3.

### AMC E 640.md
- **MINOR** — quotation capitalisation. Source [AMC E 640(1)]: "…(e.g. forward
  speed, altitude, ambient temperature, Engine speed, **use** of OEI ratings)".
  Note (`Application`): `"Use of OEI ratings" is named among…`. The quoted
  fragment is capitalised where the source is lower case.
- **MINOR** — the Maximum Possible Pressure row drops the source's parenthetical
  example list "(e.g. forward speed, altitude, ambient temperature, Engine Speed,
  use of OEI ratings)", which the same note's `Application` section then relies
  on to argue that OEI ratings feed *both* definitions. The Maximum Working
  Pressure row keeps its identical list, so the asymmetry looks accidental.

### CS-E 650.md
- **MINOR** — unrecorded micro-cut, no `Not applicable` section. Source
  [CS-E 650(b)]: "the ranges of power **or thrust** and rotational speed for each
  rotor module". Note row **(b)**: "the ranges of power and rotational speed for
  each rotor module". The cut is correct for a turboshaft but is nowhere
  recorded.

Coverage of (a)–(h), the three (b) candidates, the 2-percentage-point cap and
the `Relief` on (c) ("need not") are all correct, and the rating table in
`Application` matches `engine_profile.md` exactly (30-Second OEI in the
"less than two minutes" tier, 2-Minute OEI on the 103 % side, Rated 30-Minute
Power present, 2.5-Minute and 30-Minute OEI absent).

### AMC E 650.md
- **MAJOR** — unrecorded omission. Source [AMC E 650(14)(b)(ii)] ends with
  "Examples where validated analysis may be used include but are not limited to
  the following:" followed by four bullets (test speeds of CS-E 650(b) and (c)
  not achieved; instrumentation lost; stresses not measured directly at critical
  locations; justifying significant responses whether observed or predicted).
  None of the four appears anywhere in the note (`grep` for "instrumentation has
  been lost", "Examples where" returns nothing), and nothing is recorded in
  `## Not applicable`. Only the first is glancingly covered, under a different
  citation, by the `Compliance` line for [AMC E 650(4)(b)].
- **MAJOR** — unrecorded omission. Source [AMC E 650(8)(d)], final sentence:
  "The provisions of paragraph (4)(b) of this AMC are also applicable." The note
  gives two rows for (8)(d) and neither carries it; it matters because it
  extends the two speed reliefs of (4)(b) to corrected-speed flutter testing —
  a point the note's own `Application` section treats as live for this engine.
- **MINOR** — `Relief` outside the verb mapping, twice.
  (i) Source [AMC E 650(12)]: "…may be waived wholly or in part if the Agency is
  satisfied…" -> note labels the row `Relief`; the verb is `may` -> `Permitted`.
  (ii) Source [AMC E 650(15)]: "…should be exempt from formal Agency approval of
  test plans and reports" -> note labels it `Relief`; `should` in an AMC ->
  `Accepted method`.
- **MINOR** — unverified editorial claim in the `[!summary]`: "The longest AMC in
  Subpart E." `AMC_E_780.txt` (47 932 bytes, Subpart E) and `AMC_E_790_a_2.txt`
  (30 583 bytes) are comparable or larger than `AMC_E_650.txt` (32 762 bytes /
  pages 120–130); AMC E 780 spans roughly pages 178–194.
- **MINOR** — `Amendment history` understates the Amendment 7 before-state of
  (13). `work/redline.json` before: "— mount stiffness ;". Note: "added
  'stiffness and damping of the mount system' … where the previous text named
  only the mount." The previous text named mount *stiffness*; what Amendment 7
  added was the damping.
- **MINOR** — [AMC E 650(4)(b)] final pointer "Refer also to paragraph (5)
  'Altitude and Temperature Effects' and (8) 'Flutter' for complementary guidance
  on affecting speeds" is not carried and not recorded.

Everything else checks out, including both figure embeds
(`AMC_E_650_p120.png`, `AMC_E_650_p121.png` — both present in `vault/figures/`),
the verbatim `fn +/- 2.5 %`, MAC `0.9` and Strouhal `k = w.c/U` quotations, the
three `Not applicable` entries (fan in (3)/(7)/(8)(d)/(8)(f); Propeller and
thrust reverser in (13)), and both `Amendment history` blocks against
`work/redline.json` (the (10) `740(h)` -> `740(i)` change is exactly as
recorded).

### CS-E 660.md
_clean_ — single unnumbered paragraph, both limbs captured; the claim that
AMC E 660 is aeroplane-only is supported by its own banner in
`AMC_E_660.txt`: "AMC E 660 Fuel Pump Tests (Turbine Engines for Aeroplanes)";
the CS-E 560(a)(1) quotation is verbatim.

### CS-E 670.md
- **MAJOR** — the Requirement table, which CLAUDE.md defines as the 1:1 map to
  the regulation, misstates the specification. Source [CS-E 670(b)(2)]: "at least
  half the maximum flight duration of the **aeroplane** in which it is likely to
  be installed". Note row **(b)(2)**: "…half the maximum flight duration of the
  **aircraft** in which it is likely to be installed." The note *does* flag the
  aeroplane/aircraft divergence in a `[VERIFY]` further down (and quotes the
  source correctly there), so this is not a silent change — but a reader working
  from the table alone is given the AMC's word as the specification's.

### AMC E 670.md
- **BLOCKER** — false statement about the source table. Note (`Application`,
  inside the `[VERIFY]`): "The carbon fibre rod entry in the contaminant table
  applies only then, and **it is the largest single solid contaminant quantity in
  the table**." Source [AMC E 670(1)(a)]: carbon fibre rods are
  "0.54 g/1000 litre", while FERRIC iron oxide (Fe2O3) Hematite 0–5 microns is
  "7.13 g/1000 litre" and prepared dirt to ISO 12103-1 A4 is
  "2.11 g/1000 litre". The carbon fibre entry is fourth by quantity, not first.
  (If the intended point was particle size — 2000 microns maximum fibre length —
  the sentence says "quantity", and crushed quartz reaches 1500 microns.)
- **MINOR** — `Relief` outside the verb mapping. Source [AMC E 670(1)(c)]: "the
  objective of this paragraph (c) **may** be considered to have been met" -> note
  labels the row `Relief`; `may` -> `Permitted`.

The three figure embeds (`AMC_E_670_p131.png`, `AMC_E_670_p132.png`,
`AMC_E_670_p132_2.png`) are present and the files exist; 4.5 g / 4 500 litres,
0.5 g / 4 500 litres, 500 hours, 27 degC and 0.2 ml per litre are all exact; the
CS-E 560(c) by-pass summary and the AMC E 560(4) characterisation are both
supported by their source files.

### CS-E 680.md
_clean_ — both limbs of the single sentence captured, CS-E 100(b) and
CS-E 570(a)(1) cross-references verified against their paragraph files.

### AMC E 680.md
_clean_.

### CS-E 690.md
- **MINOR** — `Relief` outside the verb mapping. Source [CS-E 690(b)(2)]: "the
  tests required **may** be modified accordingly" -> note labels the row `Relief`;
  `may` -> `Permitted`. (By contrast (a)(3)(ii), a genuine "need not", is
  correctly `Relief`.)
- **MINOR** — `## Amendment history` follows the `References` line with no blank
  line between them.

Coverage, the elective treatment of (b) as `Required if claimed`, the CS-E
740(c)(4) `Not applicable` entry (both halves: the 25 evenly distributed
intervals in (a)(1)(i) and the one-fifth-of-test provision in (a)(3)(i)), and
the whole `Amendment history` section match `work/redline.json` line for line,
including the deletion of "standard" and the addition of "test" in (a)(2).

### AMC E 690.md
_clean_ — "need not be used" correctly `Relief`; the "is not enhanced",
"speed, temperature and torque" and "gas generator speed to output shaft speed
changes" quotations are verbatim; every punctuation change listed in
`Amendment history` (apostrophe, colon, lower-casing, semicolon, "Engine's",
"(e.g." comma) is confirmed by `work/redline.json`, as is 740(h) -> 740(i).

### CS-E 700.md
- **MAJOR** — altered source content in the Requirement row, unrecorded. Source
  [CS-E 700]: "Where any of the operating conditions (e.g. air or gas pressure,
  **thrust**, gas temperature) substantiated elsewhere in this subpart…". Note:
  "Where any of the operating conditions substantiated elsewhere in Subpart E —
  for example air or gas pressure, **power**, gas temperature — could be
  exceeded…". The source's example list never says power. Cutting "thrust" as
  out of scope would be legitimate if recorded; substituting "power" for it puts
  a word into the specification, and the note has no `Not applicable` section.
  Two lines later the note tells the reader the examples are "introduced by
  'e.g.'", which invites the list to be read as the source's own.

The AMC E 700 aeroplane-only claim is correct — `AMC_E_700.txt` banner: "AMC E
700 Excess Operating Conditions (Turbine Engines for Aeroplanes)".

### CS-E 710.md
- **MINOR** — unrecorded micro-cut. Source: "the Engine must be shut down from
  rated Maximum Continuous **thrust/power**"; note: "rated Maximum Continuous
  power" (summary, table and `Compliance`). Correct pruning, nowhere recorded.

The 25 operations, the five-minute hold and the derived "at least 125 minutes"
are consistent with the source; the AMC E 710(1) and AMC E 710(2) quotations are
verbatim; the AMC E 525(1) clutch-drag claim is supported by `AMC_E_525.txt`.

### AMC E 710.md
_clean_ — all five points (1)–(5) reach the table with strengths that follow the
verbs.

### CS-E 720.md
- **BLOCKER** — `should` in a CS paragraph upgraded to a mandatory strength.
  Source [CS-E 720(c)]: "The system **must** be operated during a suitable Engine
  endurance test for periods representative of the duration and frequency of
  operation of the system during likely service usage, and **should** be agreed
  by the Agency for individual cases." The note merges both verbs into one row —
  "Operate the system during a suitable engine endurance test for periods
  representative … , **agreed by the Agency for individual cases**. |
  `Required if claimed`" — and repeats it in `Compliance` as "Agency agreement on
  the test schedule for the individual case [CS-E 720(c)]". Per CLAUDE.md,
  `should` in a CS paragraph is `Recommended` and must not be rendered as
  Required; this is one of the ten in-scope instances the rulebook warns about.
- **MAJOR** — strength downgrade inside a merged row. Source [CS-E 720(d)]: "It
  is acceptable to conduct an equivalent programme by appropriate rig testing,
  where this is possible, but in this case final confirmation of suitability of
  the equipment in the Engine **must** be obtained by running at least 10 hours…".
  The note puts the permission and the `must` in a single row labelled
  `Permitted`, so the only mandatory element of the alternative route carries a
  non-mandatory strength.
- **MINOR** — short quotation not verbatim. Note: the paragraph "says so
  explicitly — \"(b) together with either (c) or (d)\" [CS-E 720(a)]". Source:
  "the specifications of CS-E 720(b) together with either CS-E 720(c) or (d) must
  be met". The quoted string does not occur in the source in that form.

### AMC E 720.md
_clean_.

### CS-E 730.md
- **MINOR** — `## Amendment history` follows the `References` line with no blank
  line between them.
- **MINOR** — the Requirement rows render "thrust or power calibration curves"
  as "power calibration curves" throughout. The prune is explained in
  `Application` ("**Power, not thrust.** The specification is written as 'thrust
  or power calibration curves'"), which is better than silence, but it is not in
  a `Not applicable` section as CLAUDE.md requires for a cut.

The OEI carve-out, the two alternative routes, the CS-E 740(h) purpose and the
whole `Amendment history` section match `work/redline.json` exactly (single
insertion, nothing deleted).

### AMC E 730.md
_clean_ — (1)–(3) covered, `Relief` correct on "are therefore not required to
comply"; the "more than 2 minutes" versus CS-E 650(b)(1) "two minutes or longer"
comparison is drawn from the two source texts and is correct; the rating
consequences agree with `engine_profile.md`.

## Engine-profile consistency

No conflicts found. Every note that names ratings names 30-Second OEI, 2-Minute
OEI, Continuous OEI and (where relevant) Rated 30-Minute Power, and none claims
2.5-Minute OEI or 30-Minute OEI. The EECS-FADEC full-authority statements in
CS-E 650, AMC E 650 and AMC E 620 are consistent with `engine_profile.md`.
Refrigerant injection and time-limited dispatch are not mentioned in this set.

---

# Subpart E, second third (CS-E 740 – AMC E 800) — verification

## Summary

14 notes checked against their source paragraph files under `work/paragraphs/`:
CS-E 740, AMC E 740, CS-E 745, AMC E 745, CS-E 750, AMC E 750, CS-E 770,
AMC E 770, CS-E 780, CS-E 790, AMC E 790, Appendix A, CS-E 800, AMC E 800.
Two are clean (CS-E 745, AMC E 770). Counts: **6 BLOCKER, 9 MAJOR, 21 MINOR**.

The two scope points named in the task check out in part. AMC E 740(c)(4) is
correctly absent from `covers:` in AMC E 740 and its exclusion is recorded in
`work/applicability.md` and in the `## Not applicable` of CS-E 740 — but **not**
in the AMC E 740 note itself, which instead asserts that only five AMC paragraphs
exist. CS-E 800's retention of the aeroplane 200 kt case and CS-E 790's retention
of (a)(2) alongside (b) are both justified in the text and match the CLAUDE.md
pruning rule; only the bookkeeping around them is defective.

The heaviest defect in scope is AMC E 790, where the bulk of AMC E 790(a)(2) —
including material the general AMC routes CS-E 790(b) compliance to — reaches
neither the Requirement table nor `## Not applicable`.

Figure embeds: all filenames referenced exist in `vault/figures/`
(`AMC_E_790_a_2_p199/200/201.png`, `Appendix_A_p210/210_2/210_3/211/211_2/211_3/212.png`).
CS-E 800 and AMC E 800 embed no images; in both cases the owned crops belong to
excluded sub-points and the omission is recorded (see the notes below for the one
loose end at page 202).

## Findings

### CS-E 740.md

- **MAJOR** — unrecorded cut at **(f)(4)(v)**. Source: "…by running at the required temperature for the first 2 minutes of each prescribed period at Take-off Power conditions in excess of 2 minutes (and for the whole of all the 30-second Take-off Power periods for single-engined rotorcraft)." Note row ends at "…in excess of 2 minutes." The single-engined-rotorcraft clause is dropped with no line in `## Not applicable`. The engine is declared multi-engine, so the cut is probably right, but it is silent. [CS-E 740(f)(4)(v)]
- **MAJOR** — `will` rendered as Required, inconsistently within one sub-point. Source (f)(3): "evidence of additional running **will be required**"; note row: "…provide evidence of additional running. | Required". Source (f)(4)(iii): "The average EGTs **will be reduced**, however, by the amounts necessary…"; note row: "Reduce the average EGTs… | Required". The adjacent (f)(4)(iii) row for "will be utilised" is correctly labelled Statement, so the same verb carries two labels three lines apart. Per the seven-term table `will` → Statement. [CS-E 740(f)(3)], [CS-E 740(f)(4)(iii)]
- **MINOR** — the cut inside the (c)(3)(iii) Part 4 sequence is recorded outside `## Not applicable`. Source Part 4: "Five minutes at whichever is the greatest of, as applicable, 30-Minute OEI Power, Continuous OEI Power and Maximum Continuous Power… However, where the greatest is the 30-Minute OEI Power, that sixty-five minutes period must consist of thirty minutes at 30-Minute OEI Power followed by thirty-five minutes at…". The note's Part 4 row drops both the 30-Minute OEI term and the "However" sentence. It is explained under `## Application to this engine` ("Part 4 of the additional sequence simplifies here") but has no `## Not applicable` line, which is where CLAUDE.md puts every cut.
- **MINOR** — unrecorded cut at **(f)(4)(vii)(C)**: source "…no adverse effect on any system using the oil as a working fluid (e.g. Propeller control)"; the propeller example is dropped without a record, while the note records propeller cuts elsewhere ((b)(4)).
- **MINOR** — unrecorded cut in the **(f)** chapeau: "The EGT limitations may be derived from an analysis when the applicant uses the alternate test specified in CS-E 740(c)(4) (see CS-E 740(f)(4)(ii) below)." The `## Not applicable` list covers (f)(4)(ii) and the "(c)(4) equivalent demonstration" clauses of (e)(1), (e)(2), (f)(2), (g)(1), but not this sentence.
- **MINOR** — mixed strengths in one row at **(e)(2)**: "Run one other stage… During this stage, the oil temperature **need not** be held at its maximum value. | Required". The relief is folded into a Required cell; the following row correctly isolates the "may be omitted" as Permitted.
- **MINOR** — derived arithmetic slightly wrong: "The sixty-five minute first-sequence Part 4 is what carries the sequence total **past** 120 minutes." Four sequences of 15 minutes plus the extra 60 minutes is exactly 120; the source says "not less than 120 minutes".
- **MINOR** — self-link: line 190 writes `[[CS-E 740|CS-E 740(f)]]` inside CS-E 740.md.
- **MINOR** — no blank line between the `## References` block and `## Amendment history` (lines 251–252); same defect in AMC E 740.md and CS-E 780.md.

### AMC E 740.md

- **BLOCKER** — strength downgraded at **AMC E 740(c)(2)(i)(c)**. Source: "The proposal **must** be substantiated and proposed to the Agency for acceptance. These assumptions **will** be recorded in the instructions for installing and operating the Engine, in accordance with CS-E 30(a)." Note: "| **(c)(2)(i)(c)** | Substantiate the proposal and propose it to the Agency for acceptance, and record these assumptions in the instructions for installing and operating the engine in accordance with CS-E 30(a). | **Accepted method** |". A `must` is rendered as Accepted method, and a `will` (Statement) is merged into the same cell. An applicant reading this could propose an alternative to a mandatory step.
- **MAJOR** — AMC E 740(c)(4) is excluded but its exclusion is not recorded in this note, and the note asserts the opposite. Summary line 13: "**Five** AMC paragraphs serve CS-E 740." `work/paragraph_index.csv` lists six AMC E 740 banners; `AMC E 740(c)(4) Alternate Endurance Testing – Turbofan Engine` (pages 151–172) is EXCLUDED in `work/applicability.md`. The note has no `## Not applicable` section, so a reader cannot tell "deliberately excluded" from "forgotten". (Confirmed: (c)(4) is correctly absent from `covers:` and nothing of its content leaks into the note.)
- **MAJOR** — strength at **AMC E 740(c)(3)(3)**. Source: "the interrupted sequence **needs to be repeated** in full or **can be** re-started from the interrupt point if there is a technical justification acceptable to the Agency." Note renders the whole sentence as a single Accepted method row. The mandatory limb ("needs to be repeated") and the permissive limb ("can be re-started") carry different strengths and are collapsed.
- **MINOR** — dropped cross-reference at **(i)(2)(3)**: source "…as required by CS-E 25(b)(2) **and described in the associated AMC material**"; the note stops at CS-E 25(b)(2).
- **MINOR** — the AMC E 740(f)(1) preamble ("supplementary evidence is required to substantiate any rotational speed limitations higher than those covered in that test") is not tabulated and not recorded; it restates CS-E 740(f)(1), which has its own note, so the omission is probably deliberate but is silent.

### CS-E 745.md

_clean_

### AMC E 745.md

- **MINOR** — declaratory sentence labelled Accepted method at **(2)**. Source: "the appropriate adverse combination **is probably** 'maximum bleed air and maximum power extraction'". Note row 26: strength `Accepted method`. The next row, whose source verb is "should probably be", is correctly Accepted method; the two are not the same construction.

### CS-E 750.md

- **BLOCKER** — strength downgraded at **(c)**. Source: "All attempted starts including those prescribed in CS-E 750(b) **must count** towards the total, provided that the normal starting cycle is completed." Note: "| **(c)** | All attempted starts, including those prescribed in CS-E 750(b), count towards the total, provided that the normal starting cycle is completed. | **Statement** |". `must` → Required under the seven-term table; the note's own strength table defines Statement as "Imposes no action".

### AMC E 750.md

- **MINOR** — conjunction changed at **(b)**. Source: "The period is measured from the time at which the starter is switched off **and/or** the Engine fuel cock is closed during a false start." Note: "…the starter is switched off, **or** the engine fuel cock is closed…". The source admits the combined case; the note reads as exclusive.
- **MINOR** — inference presented as reading of the source: "And the clock starts at the shutdown action, **not at the point where the start attempt was abandoned**". The source draws no such contrast; it only names the two measuring events.

### CS-E 770.md

- **MINOR** — no `## Not applicable` section, though (c) is pruned. Source (c): "when the power or thrust control lever is moved from the ground idle position (minimum test bed idle for rotorcraft Engines) to the position appropriate to takeoff". Note (c) row: "when the power control is moved from minimum test bed idle to the position appropriate to take-off". The aeroplane lever wording is dropped silently, where CS-E 745 records the equivalent prune ("**(b)**, in part — the aeroplane wording…").
- **MINOR** — citation attached to the wrong document in Compliance: "Any declared minimum oil temperature for opening up from ground idle for warming up or taxying **[CS-E 770]**." That provision is in AMC E 770, not CS-E 770; CS-E 770 declares only the (b) and (c) temperatures.
- **MINOR** — register: "[[AMC E 770]] gives two **reliefs**". Both AMC provisions are Permitted in the note's own table; "Relief" is a defined strength term in this vault meaning `need not`.

### CS-E 780.md

- **MINOR** — citation attached to a sub-point that does not carry the statement, in Compliance: "Continuous ignition provisions where relied on for icing compliance **[CS-E 780(a)]**, under [[CS-E 720]] and [[AMC E 720]]." Nothing in CS-E 780(a) refers to ignition; the source of that link is AMC E 720.

Verified clean elsewhere: (a)(1)(i)–(iv), (a)(2), (b)–(e) and (f)(1)–(4) all reach
the tables; aeroplane material is not present; the quoted AMC E 780(1.7) passage
("Specific provisions for rotorcraft Engines are currently not included in this
AMC. Until guidance has been established, the necessary compliance method required
for rotorcraft Engines should be agreed by the Agency.") is verbatim against
`work/paragraphs/AMC_E_780.txt` lines 192–194.

### CS-E 790.md

- **BLOCKER** — wrong citation in Compliance: "Further running or other evidence where damage is found **[CS-E 790(b)]**." CS-E 790(b) contains no such provision. The statement comes from AMC E 790(a)(2): "If, after test, it is found that damage has occurred, further running or other evidence may be required to show that subsequent Failures resulting from the damage are unlikely to occur before the damage is rectified" [AMC E 790(a)(2)(5)(c)(vi)]. The adjacent line "Engine performance measured before and after ingestion, normalised, across the full range of engine power [CS-E 790(b)]" has the same problem — that obligation is in the same AMC paragraph, not in CS-E 790(b).
- **MAJOR** — strength at the **(b)** head row. Source: "As an alternative to the specifications specified in CS-E 790(a)(2), but for rotorcraft turbine Engines only, **it must be shown** that each Engine is capable of acceptable operation… of at least 4-percent." Note strength: `Permitted`; the four following (b) rows read `Required if claimed`. The vault's own defined term for an elective provision that is mandatory once elected is "Required if claimed", which is exactly this construction. Marking the substantive obligation Permitted reads as though the 4 % demonstration itself were optional. (The note explains its reasoning at lines 93–95, so this is a labelling decision, not an oversight — but it departs from the fixed seven-term list.)
- **MINOR** — `## Not applicable` records content rather than the cut: "**(c)** — the separate supersonic cruise hailstone test…, **with its 25 millimetres at 10 500 metres to 6 millimetres at 18 000 metres linear diameter variation**." CLAUDE.md: "Record the cut, never the content."
- **MINOR** — citation level inconsistent with the AMC E 790 note. Here: `[[AMC E 790|AMC E 790(a)(2)(d)]]`. The rotorcraft text is at paragraph (2)(d) of AMC E 790(a)(2), which the AMC E 790 note writes as `AMC E 790(a)(2)(2)(d)`. As written, `(a)(2)(d)` points at a sub-point that does not exist.

Checked and correct: all numbers in (a)(1) and (a)(1)(i)/(ii) (0.8 to 0.9 specific
gravity, 4 500 metres, 25 mm, 50 mm, 0.0645 m², 0.0968 m²), the 3-Minute/30-Second
criteria in (a)(2), the 4-percent in (b), and the (d)(1)–(3) waiver conditions.
Retention of (a)(2) alongside (b) is correct and explained ("Sub-point (b) is an
alternative to (a)(2) only. It does not displace (a)(1)").

### AMC E 790.md

- **BLOCKER** — large-scale silent omission from AMC E 790(a)(2). The following source material appears in neither the Requirement tables nor `## Not applicable`:
  - **(1) Definitions** — 7 of the 11 defined terms are absent: Flameout, Hail, Hail water content (HWC), Rain, Rain water content (RWC), Stall, Surge. Only Critical point(s), Rundown, Scoop factor and Sustained power or thrust loss are carried.
  - **(2)(a)** General; the **(2)(c)** and **(2)(c)(ii)** chapeaux; **(2)(e)(i)** Compressor rematch, **(2)(e)(ii)** Engine control response, **(2)(e)(iii)** Combustor response; **(2)(f)** Case contraction — all written for "any turbine Engine".
  - **(3)(a)** General and **(3)(b)(i)–(vii)** Design Features, including (iv) Engine air bleeds, (v) Engine and aircraft accessory loads, (vi) Fuel control and (vii) Variable stator vane, none of which is turbofan- or propeller-specific.
  - **(4)(c)** Critical Point Analysis Procedure — while (4)(a) and (4)(b) are tabulated.
  - **(5)(a)** General, **(5)(b)** Test Point Selection, the **(5)(c)** chapeau, **(5)(c)(i)(A)–(I)** Test Compensation, **(5)(c)(ii)** Engine test facility, **(5)(c)(iii)** Instrumentation, **(5)(c)(iv)(A)–(G)** Test procedure, **(5)(c)(v)** Probable factors, and the HWC/ice-accretion Note following (5)(c)(vi)(B) — while (5)(c)(vi), (A), (B) and (5)(d) are tabulated.
  The `## Not applicable` section has four lines and none of them covers any of the above.
- **BLOCKER** — material the general AMC explicitly routes CS-E 790(b) compliance to is absent from the vault. AMC E 790(3), which the note itself tabulates, says: "For the purposes of interpreting the words 'sudden encounter' in CS-E 790(a)(2) and the words 'suddenly commencing' in CS-E 790(b), see paragraphs (5)(c)(iv)(D) and (G) in AMC E 790(a)(2)." Neither (5)(c)(iv)(D) ("Establish the altitude equivalent rain or hail flow at the proper inlet velocity and size distribution. The maximum rain and hail ingestion rates should occur within 10 seconds.") nor (5)(c)(iv)(G) ("Conduct the thermal shock critical point test by delivering rain for 3 minutes at the critical Power/Thrust condition following a normal stabilisation period without water ingestion. The maximum rain ingestion rate should occur within 10 seconds.") appears anywhere in the note. CS-E 790(b)(1) requires "suddenly commencing ingestion of rain", so the 10-second figure that defines it is a live obligation for the elected route and it is missing. The same applies to AMC E 790(2), which routes "flameout, rundown, continued or non-recoverable surge or stall" in CS-E 790(b) to "paragraphs (1) and (5)(c)(vi)" — paragraph (1) holds the Flameout, Stall and Surge definitions listed as missing above.
- **MINOR** — a `## Not applicable` entry for a sub-point that is in fact covered, and which contradicts itself: "**(a)(2)(1)**, in part — the scoop factor definition is framed on nacelle inlet highlight area. **It is retained above** because AMC E 790(a)(2)(2)(d) reasons from the scoop factor being small for a rotorcraft." The entry records no cut.
- **MINOR** — `## Not applicable` records content rather than the cut at **(a)(2)(2)(c)(ii)(B)**: "…including the Propeller solidity effect, the Propeller spinner redirection of hail, and the conservatism of testing without a Propeller."
- **MINOR** — declaratory sentences labelled Accepted method: row **(a)(2)(4)(a)** "Compliance with CS-E 790(a)(2) is a two-step procedure…" (source "is a two-step procedure") and row **(a)(2)(5)(c)(vi)** "Acceptable engine operation precludes flameout, rundown…" (source "Acceptable Engine operation precludes…"). Both are Statement by the source's verb. Conversely, rows **(a)(1)** ("This 10 % variation… should not be assumed to be a direct tolerance") and **(a)(2)(3)(c)(ii)** ("should not be used by the applicant to show compliance") carry `should` in an AMC and are labelled Statement rather than Accepted method.
- **MINOR** — mixed strengths in one cell at **(a)(2)(5)(d)**: "Analysis **may** be used in lieu of… The analytical methods **should** have a sufficient validation basis…" is a single `Permitted` row.
- **MINOR** — `work/paragraph_index.csv` lists figure pages `199 200 201 202` for AMC E 790(a)(2); the note embeds p199, p200 and p201 and `vault/figures/` holds no `AMC_E_790_a_2_p202.png`. Page 202 carries the end of (2)(d) and the start of (2)(e) in the text layer, so this is most likely a false positive in figure detection — but nothing in the vault records that, and it is the one figure page in this scope with neither a crop nor an explanation.

### Appendix A.md

- **MAJOR** — figure content described rather than embedded, contrary to accuracy rule 6. Note: "And **Figure A1 plots the 1 %, 2 %, 3 % and 4 % water-to-air lines alongside the rain and hail threat curves**, which shows directly how the 4 percent condition relates to the ambient threat across altitude." Nothing in `work/paragraphs/Appendix_A.txt` states what Figure A1 plots beyond "FIGURE A1 - Illustration of Rain and Hail Threats. Certification concentrations are obtained using Tables A1 and A2." The statement cannot be checked against the text layer, which is the reason the rule requires the crop instead of a description. The note makes the point itself two paragraphs earlier ("a transcription could not be checked against the source").

Everything else verified: all seven embeds resolve to files in `vault/figures/`;
the quoted AMC E 790(a)(2)(2)(b) sentence, the ICAO Annex 5 note and the Table A2
extrapolation note are verbatim; 2.66 mm, 16 mm, 46 000 feet and 7 300/29 000 feet
are correct.

### CS-E 800.md

- **MINOR** — unrecorded cut at **(f)**. Source: "…up to 450 m (1 500 ft) above ground level, **but not less than V1 minimum for Engines to be installed on aeroplanes** or higher than the speeds for the ingestion tests." The note keeps the upper bound and drops the aeroplane V1 floor with no `## Not applicable` line, although the note records the analogous 200 kt case in (b)(1)(iv).
- **MINOR** — `## Not applicable` entry misdescribes where the retained text sits: "**(b)(1)(iv)**, in part — the 200-knot aeroplane bird speed. **Retained in the table above** because it defines the rotorcraft case by contrast." The table row carries only the rotorcraft limb; the 200 kt appears in the prose beneath the table, not in the table.
- **MINOR** — Compliance citations pointing at sub-points that do not carry the statement: "Test facility calibration and tolerance analysis against the critical impact parameter **[CS-E 800(b)]**" and "Engine interface data on expected interaction with aircraft systems during ingestion events, in the instructions for installation **[CS-E 800]**". Both obligations are in AMC E 800(2)(a) and (2)(e); CS-E 800(b) is the single large bird test.

Scope point confirmed: the 200 kt aeroplane case is kept once, quoted verbatim
("A bird speed of 200 knots for Engines to be installed on aeroplanes or the
maximum airspeed for normal flight operations for Engines to be installed on
Rotorcraft"), and the retention is argued on exactly the CLAUDE.md ground — the
rotorcraft value is declared rather than fixed, so the aeroplane figure defines
the case by contrast. The (g)(7) multi-engine relief matches `engine_profile.md`
("Rotorcraft turboshaft, multi-engine installation"), and the (c), (d) and (e)
exclusions each carry a reason. The three CS-E 800 figure crops (pages 213, 214,
216) belong to the (c) bird-mass table, the (c) run-on figure and Table A of (d);
all three sub-points are excluded and the tables are named in `## Not applicable`,
so embedding none of them is correct.

### AMC E 800.md

- **BLOCKER** — silent omission of **AMC E 800(4)(f)** and **(4)(g)**. Neither reaches the Requirement table nor `## Not applicable`.
  - (4)(f): "When the CS-E 810 test is proposed as an alternative to the single large bird test (see CS-E 800(g)(2)), the demonstration should include consideration of unbalance, as well as effects of the axial loading from the bird strike on bearings or other structures." This is the accepted means for a waiver the CS-E 800 note carries as a live Relief at (g)(2) and discusses in prose ("The waiver in (g)(2) routes through [[CS-E 810]]"), so the conditions on that waiver exist nowhere in the vault.
  - (4)(g): "Artificial birds may be used in the tests if they are internationally standardised and are acceptable to the Agency." This applies to the single large bird test, which is not relieved for this engine.
- **MAJOR** — strength downgraded at **(1)(a)(i)**. Source: "The applicant **is required to** provide an analysis substantiating the definition of the 'most critical exposed location' (CS-E 800(b)(1)(iii))." Note: "| **(1)(a)(i)** | Provide an analysis substantiating the definition of the "most critical exposed location" of CS-E 800(b)(1)(iii). | **Accepted method** |". "is required to" is mandatory language; Accepted method invites an alternative that the sentence does not offer. (The second row of the same sub-point, source "should include evidence", is correctly Accepted method.)
- **MINOR** — unrecorded cut in **(2)(a)**: three paragraphs of turbofan-specific CIP discussion (slice mass and the shift from leading-edge to blade-root stress; part-span-shroud shingling; unshrouded wide-chord blade twist) are dropped. The turbofan/turboprop CIP sentence immediately before them is quoted in the prose, so the boundary of what was kept is not visible.
- **MINOR** — unrecorded cut in **(2)(c)**: "For the test of CS-E 800(d), if, after the first 2 minutes, operation at the specified power or thrust levels would result in a sustained high vibratory condition, the power or thrust may be varied within the ± 3% band." Serves (d), which is relieved, but the cut is not recorded while other (d)-serving cuts are.
- **MINOR** — unrecorded propeller cuts at **(2)(d)** ("turboprop or", "or propeller", "coupled with a propeller"), although the propeller cuts at (2)(e) and (4)(a) are recorded.
- **MINOR** — unrecorded narrowing at **(4)(b)**: source "referred to in CS-E 800(b)(1)(i) **or (d)(1)(i)**"; the note keeps only (b)(1)(i).

Checked and correct: the 10 % CIP variation appears in both (2)(a) and (4)(c) as
the note has it; ± 3 percentage points and ± 3 % are copied exactly; the quoted
passages at (1)(a)(iii), (2)(a), (3)(a), (3)(b) and (4)(a) are verbatim. The
figure crop `AMC_E_800_p220.png` is deliberately not embedded and the reason is
recorded in `## Not applicable` ("This includes the blade span target location
figure at page 220, which is therefore not embedded here"); page 220 does carry
AMC E 800(1)(b)(ii) and its "(see the figure below)", so the attribution is
consistent with the text layer.

### AMC E 770.md

_clean_

---

# Subpart E, final third (19 notes) — verification

## Summary

19 notes checked against their source paragraph files in `work/paragraphs/`, plus
`work/redline/*.md` and `work/redline.json` for the four `changed_in: [Amdt8]` notes
(CS-E 920, AMC E 920, CS-E 930, AMC E 930) and for the two Amdt7 notes (CS-E 810,
AMC E 810). Coverage of applicable sub-points is complete in every note: no sub-point
of any source file is missing from both the Requirement table and `## Not applicable`.
All numbers, times, temperatures and percentages were checked one by one against the
source and all are correct apart from one rendering change (2½ → 2.5). All quotations
of 20 characters or more were checked verbatim; all are accurate except one attribution
(AMC E 810). Frontmatter `pages` and `changed_in` agree with `work/paragraph_index.csv`
for all 19. No ghost wikilinks, no `[[X]](y)` constructions, no "Book 1/Book 2".
The four Amdt8 before/after accounts are accurate against the redline, and no
pre-amendment wording has leaked into requirement content.

Counts: **1 BLOCKER, 6 MAJOR, 18 MINOR**. Clean notes: 4 (AMC E 820, AMC E 830,
CS-E 910, CS-E 930).

## Findings

### CS-E 810.md
- **MINOR** — hyphenation drift on a defined term. Source `(b)(1)(i)`: "Above the maximum Engine speed to be approved (including the Maximum Engine **Overspeed**)". Note: "including the Maximum Engine **Over-speed**". Not inside quotation marks, so not a misquote, but the source spells the term both ways (CS-E 810 and AMC E 810(2)(b)(ii)(A) unhyphenated; AMC E 810(3)(b)(i) and CS-E 830 hyphenated) and the note silently normalises.
- Amendment history verified: the `Before:` and `After:` strings are word-for-word the `before`/`after` fields of `CS-E 810 [Amdt7]` in `work/redline.json`. The three cross-paragraph claims (CS-E 520(c)(2), CS-E 800(g)(2), AMC E 515(3)(e)(i)) are all present in those source files.

### AMC E 810.md
- **MAJOR** — strength upgrade inside row `(1)(c)`. The source has two verbs: "the threat represented by any blade Failure **must** be addressed. Therefore, the applicant **should** assess other possible blade Failure conditions…". The note merges both into one row obligation ("…must be addressed. **Assess** other possible blade Failure conditions — …") with a single `Strength` of **Required**. The `should assess` half is an AMC `should` and is **Accepted method**; rendering it Required removes the applicant's right to propose an alternative means. Mitigating: the prose immediately below the table does draw the distinction ("Point (1)(c) uses \"must\", not \"should\"… the sub-point then softens only the method"), but the table cell is what a reader maps to. [AMC E 810(1)(c)]
- **MINOR** — quotation attributed to a sub-point whose wording differs. `## Application to this engine`: "Both (2) and (3) run at \"the maximum rotational speed to be approved (other than the Maximum Engine Over-speed)\"." That string is verbatim only in `(3)(b)(i)`. `(2)(b)(ii)(A)` reads "the maximum rotational speed to be approved (other than Maximum Engine Overspeed)" — no "the", and "Overspeed" unhyphenated. The same claim is repeated in `CS-E 830.md` ("Both the containment test and the out-of-balance run of AMC E 810 are conducted at … \"other than the Maximum Engine Over-speed\"").
- **MINOR** — row `(2)(b)(ii)(A)` writes "other than Maximum Engine Over-speed" where the source sub-point writes "Maximum Engine Overspeed" (same drift as above, inside the Requirement table).
- Coverage verified: `(1)(a)(i)–(iii)`, `(1)(b)–(d)`, `(2)(a)–(c)`, `(3)(a)–(c)` all present; the only cut, `(2)(b)(i)(A)` with its conditions (1)–(3) and its NOTE, is recorded in `## Not applicable`. Amendment history matches the deleted runs in `work/redline/AMC_E_810_Amdt7.md` ("without causing", "power Failure", "or the expulsion of blades through the Engine casing or shield;", "hazard to the aircraft", the old intake/exhaust debris NOTE).

### CS-E 820.md
- **MINOR** — duplication of another note's content, shared with CS-E 830, CS-E 870, AMC E 830, AMC E 870 and AMC E 920: each restates the AMC E 60(d)(5) relief (over-torque/over-speed/over-temperature events need not count as OEI usage if the recording system can distinguish them). Six restatements of one sub-point that has its own note. Each does link `[[AMC E 60]]`, and the statements are accurate against `work/paragraphs/AMC_E_60_d.txt`, so this is register rather than error — but it is the pattern rule 8 warns about.
- Everything else verified: 15 minutes, 2½-minutes, 2 minutes, 20 seconds all exact; the two short quotations from (b)(2) and (b)(4) are verbatim; `(b)(4)`'s "unless…" correctly split out as **Relief**; no sub-point cut.

### AMC E 820.md
_clean_ — the single source sentence is rendered once, at **Accepted method**, with the CS-E 820(a)(2) quotation verbatim in the parent note. Cross-claims to CS-E 740(i)(2)(iii) and AMC E 830 check out against their source files.

### CS-E 830.md
- **MINOR** — repeats the AMC E 60(d)(5) relief (see CS-E 820 above).
- **MINOR** — the AMC E 810 quotation attribution problem described under AMC E 810 is repeated here.
- Verified: "2.5 minutes" here matches the source, which writes "2.5 minutes" in CS-E 830(b)(1) (unlike CS-E 820/870, which write "2½-minutes"). The CS-E 650(b)(3) quotation "100 % of any Maximum Engine Over-speeds declared under CS E 830" is verbatim, including the unhyphenated "CS E 830" of the source. The shaft-specific rule in (b)(2) is carried in full.

### AMC E 830.md
_clean_ — but see the "identical wording" MINOR under AMC E 870, which applies to this note's sentence "The wording is identical to [[AMC E 820]]" as well.

### CS-E 840.md
- **MINOR** — `## Not applicable` records a cut that was not made: "**(a)**, **(b)**, **(d)**, in part — the fan rotor". Sub-point (b) contains no reference to a fan ("When determining the operating conditions applicable to each rotor…"); only (a) and (d) name "each fan, compressor, and turbine rotor". The entry names a sub-point that is in fact reproduced in full in the Requirement table.
- **MINOR** — unsourced rationale presented as explanation: "The reason is duration. A rating held for under 2½ minutes exposes the rotor for less time, so the margin above it is smaller." CS-E 840 gives no reason for the 115 %/100 % split, and neither does AMC E 840.
- Verified: 120 %, 115 %, 105 %, 100 %, 2½-minutes, five minutes all exact; `(b)(3)(ii)`'s "except as provided by CS-E 840(c)" preserved; `(d)(1)(i)–(iv)` and `(d)(2)` all present; the CS-E 100(b) and CS-E 510(g)(2)(vii) cross-references are correct (CS-E 510(g)(2)(vii) is "Complete inability to shut the Engine down"). The rating-to-margin table in `## Application to this engine` is consistent with `engine_profile.md`, including the correct placement of Continuous OEI on the ≥2½-minute side.

### AMC E 840.md
- **MINOR** — inconsistent strength labelling inside one list. `(3)` is introduced by "Acceptable means of compliance may include", yet `(3)(a)` is labelled **Accepted method** while `(3)(b)`, `(3)(c)` and `(3)(d)` are labelled **Permitted**. All four are items of the same "may include" list.
- **MINOR** — `(2)(j)` row 2 renders the declaratory "This **would require** determination of the burst speed for each rotor" as **Accepted method**. There is no `should` in that sentence; per the seven-term table it is a **Statement**.
- **MINOR** — `## Not applicable` names "**(1)**, **(2)(j)**, **(2)(k)**, in part — the fan". Correct for (1) and (2)(k), but `(2)(j)` contains no fan reference; that sub-point is reproduced in full in three rows of the table.
- Coverage verified in full: `(1)` three definitions, `(2)(a)`–`(2)(l)`, `(3)(a)`–`(3)(d)`, `(4)(a)(i)`/`(ii)` plus the closing text of (4)(a), `(4)(b)`, `(4)(c)`, `(5)`. The 96 % figure and its two conditions are exact. The AMC E 170 claim ("an over-speed protection system (or a torque limiter)") is present in `work/paragraphs/AMC_E_170.txt`.

### CS-E 850.md
- **MINOR** — inconsistent treatment of the same source verb in one table. `(b)(1)` "a test **will** normally be required" is labelled **Required**, while `(b)(2)` "the Failure rate … **will** be accepted as Extremely Remote, if:" is labelled **Statement**. Per CLAUDE.md `will` maps to **Statement**; the Required label also drops the "normally" qualifier, although the row's obligation text preserves both "normally" and the "unless it is agreed that the consequences are readily predictable" escape.
- Verified: the AMC E 850(3) quotations ("In general, experience has shown that Failures of shafts occur at a rate in excess of Extremely Remote. Consequently, shaft systems should be designed to fail safe as required by CS-E 850(a)(1)." and "but the use of this provision should be strictly limited.") are verbatim. The count "Condition (iii) lists eight environmental factors" is correct. CS-E 510(a)(4) is correctly cited for Remote / less than 10⁻⁵ per Engine flight hour. All five (b)(2) conditions present.

### AMC E 850.md
- **MAJOR** — engine-profile conflict. `## Application to this engine`: "[VERIFY: the maximum oscillatory torque envisaged in the rotorcraft installation … The value depends on the main rotor and transmission dynamics of the target aircraft, which `engine_profile.md` records as an open item.]" `engine_profile.md` records exactly one `[VERIFY]` item — how the additional 25 hours of AMC E 740(c)(2)(i) combine with the CS-E 740(c)(3)(i) schedule. It says nothing about rotor or transmission dynamics. The note asserts a content of the profile that is not there.
- **MAJOR** — strength downgrade in AMC E 850(3), row 2. Source: "However, it is accepted under CS-E 850(a)(3) that, for conventional designs, this is not possible for all parts of a shaft system, but the use of this provision **should** be strictly limited." The note labels the row **Statement**, whose defined meaning is "Imposes no action". The `should` constrains reliance on the CS-E 850(a)(3) route and is **Accepted method**. Row 1 of the same block correctly labels a `should` as Accepted method, so the table contradicts itself.
- **MINOR** — `## Not applicable` records cuts that were not made and invents a phrase. The entry reads: "**(1)(a)**, **(2)(a)**, **(3)** — the fan cases within these sub-points … so \"compressor/fan\", the composite-fan release case and \"a release of the complete fan\" reduce to the compressor." Three problems: (i) `(2)(a)` contains no fan reference at all and is reproduced in full; (ii) the `(3)` row in the Requirement table **keeps** the fan wording — "a release of the complete fan or compressor moving forward" — so nothing was cut there, and the `(1)(a)` verbatim quotation in the prose likewise keeps "compressor/fan"; (iii) "the composite-fan release case" does not exist anywhere in AMC E 850 (it is AMC E 810(2)(b)(i)(A) material).
- Coverage verified: `(1)(a)`, `(1)(b)`, `(2)(a)`–`(2)(c)`, `(3)` including all nine service Failure modes reproduced exactly and in source order, `(4)(a)(i)`–`(vii)`, `(4)(b)(i)`–`(iv)`. The "±5%" floor and all four long quotations are verbatim.

### CS-E 860.md
- **BLOCKER** — wrong citation, twice, to a sub-point that does not exist. The note cites `[[CS-E 510|CS-E 510(a)(5)]]` for the definition of Extremely Remote, in `## Requirement` prose ("as defined in [[CS-E 510|CS-E 510(a)(5)]]") and again in `## Compliance` ("against [[CS-E 510|CS-E 510(a)(5)]]"). `work/paragraphs/CS_E_510.txt` shows CS-E 510(a) runs `(1)` to `(4)` only; there is no `(a)(5)`. Extremely Remote and its probability (less than 10⁻⁷ per Engine flight hour) are defined in **CS-E 510(a)(3)**. (The numbered list `(5) Gas temperature control systems` at that point in the file belongs to CS-E 510(f), not (a).) A certification engineer following this reference lands on nothing, or on the wrong list.
- Otherwise verified: both sub-points and the "need not" relief are correctly rendered; the CS-E 60(e) account ("three escapes") is consistent with the cross-reference it makes.

### CS-E 870.md
- **MINOR** — a number is re-rendered rather than copied. Source `(b)(2)`: "the time of each individual run being no less than **2½-minutes**". Note, in the table and twice more in prose: "**2.5 minutes**". The value is unchanged, but CLAUDE.md rule 3 is copy-exactly, and the sibling note CS-E 820 does copy "2½-minutes" from identical source wording.
- **MINOR** — `## Not applicable` records a cut that was not made: "**(b)(1)** — the fan spool case." CS-E 870(b)(1) says only "with each spool of the Engine which could be significant to the test"; there is no fan wording in the sub-point, and the sub-point is reproduced in full in the table.
- **MINOR** — repeats the AMC E 60(d)(5) relief (see CS-E 820).
- Verified: 15-minute, 2½/2.5-minute, the "(excluding the Maximum Engine Over-speed (20 Second))" condition, and the quotation "with each spool of the Engine which could be significant to the test". The `[VERIFY]` on "Maximum Engine Over-speed (20 Second)" is justified: the term occurs exactly once in `work/paragraphs/` and nowhere in CS-E 15. The declaration item cited as `[AMC E 40(d)(r)]` is correct — "(r) Maximum Over-temperature transient and time limit."

### AMC E 870.md
- **MINOR** — unsourced technical assertion presented as fact: "The hot section damage that would remove 30-Second OEI capability is creep and oxidation of the turbine blades and vanes". AMC E 870(a)(3) is one sentence and says nothing about damage mechanisms; neither does CS-E 870. This is general knowledge in a note.
- **MINOR** — "The wording is **identical** to [[AMC E 820]] and [[AMC E 830]]." The three sentences are parallel, not identical: each names its own CS reference and its own event ("over-torque event" / "over-speed event" / "over-temperature event"). The same claim appears in AMC E 830 ("The wording is identical to [[AMC E 820]]") and, more carefully phrased, in AMC E 820 ("uses the same wording").
- **MINOR** — repeats the AMC E 60(d)(5) relief (see CS-E 820).

### CS-E 910.md
_clean_ — the paragraph has no sub-points; all three obligations are present, the five example conditions are complete and in source order, and the one quotation is verbatim. The `## Application` claims (starter assistance → CS-E 690, control system → CS-E 50) are framed as engine-specific consequences, not as source content.

### AMC E 910.md
- **MAJOR** — invented definition. "**Rotor-lock** is the thermal seizure of a rotor after shutdown, when a hot rotor contracts against a casing that has already cooled or expanded against one that has not." AMC E 910(3)(b) uses the term and lists the assumptions to apply to it ("clearances (taking into account tolerances), the initial conditions, flight effects, thermal effects and the dwell time"), but never defines it and never describes a mechanism. This is a plausible-sounding elaboration from general knowledge, which the source-of-truth rule forbids in a note.
- **MINOR** — `## Not applicable` records a cut that was not made: "**(1)** — the aeroplane origin of AMC 25.903(e)(2) itself." Sub-point (1) is reproduced in full in two rows of the Requirement table, and the entry then explains that the reference is kept. Nothing was dropped.
- **MINOR** — "Active coordination … **is recommended**" is labelled **Accepted method**. The seven-term table fixes **Accepted method** to `should` in an AMC; "is recommended" is not one of the seven listed verbs, so this row has no clean mapping. Worth a house rule rather than a silent choice.
- Verified: the 5-second floor, the five rotor-lock contributors with "include but are not limited to" correctly reported as open, and the flight-test qualification. The note correctly drops "or thrust" from "the previous power or thrust setting" without needing a record, and correctly separates the 5-second delay from the 30-Second OEI rating.

### CS-E 920.md
- **MAJOR** — engine-profile conflict. "[VERIFY: … Both follow from the rating declaration under CS-E 40 and are recorded in `engine_profile.md` as open items.]" `engine_profile.md` does not record the maximum rating's steady-state operating temperature limit or the 30-Second OEI operating temperature limit at all, as open items or otherwise. Its only `[VERIFY]` concerns the additional 25 hours of endurance testing.
- **MINOR** — amendment-history material outside `## Amendment history`. `## Application to this engine` contains "**Amendment 8 added a test this engine must run.** Before Amendment 8 the paragraph contained only the OEI test. An applicant declaring no short OEI ratings ran nothing under CS-E 920." This is a statement about the pre-amendment state, in the section reserved for engine-specific application. It is accurate (the redline `before` confirms it) and it is not quoted pre-amendment wording, so it does not breach the leak rule — but it belongs in the section below.
- **MINOR** — the `Before:` quotation in `## Amendment history` is presented as the whole pre-amendment paragraph ("consisted of a single test… The wording was: …") but stops after the first sentence. The redline `before` continues "Following this test, the turbine assembly may exhibit distress beyond the limits for an over-temperature condition provided the Engine is shown by analysis or test or both to maintain the integrity of the turbine assembly." The quoted sentence itself is accurate word-for-word (the redline's "F or Engines…" is an extraction artefact of the deleted "F" / inserted "f", correctly normalised).
- Redline verified in detail: all three changes in the note's change table match `work/redline/CS_E_920_Amdt8.md` exactly — the whole of (a) inserted, "(b)" plus "In addition to the test requirements in paragraph (a)," inserted with "F"→"f", and "(35 °F)" inserted. 42 °C (75 °F), 5 minutes, 19 °C (35 °F), 4 minutes all exact. No pre-amendment wording in the Requirement table.

### AMC E 920.md
- **MINOR** — an inference stated as fact. `## Amendment history` closes: "What is new is the datum guidance in (1), which now also **governs** the new test of [[CS-E 920|CS-E 920(a)]]." AMC E 920(1) is unscoped ("To establish a datum turbine entry gas temperature…") while (2) is expressly scoped to CS-E 920(b), so the inference is reasonable — but the source never applies (1) to (a), and the note does not mark the step as interpretation or `[VERIFY]`.
- Redline verified: the five rows of the change table match `work/redline/AMC_E_920_Amdt8.md` one-for-one (insert (1); renumber to (2); "(b)" added to the cross-reference; "rpm" deleted / "rotor speed" inserted; "-" inserted in "over-temperature"). The elided `Before:` quotation — "For the purpose of the test of CS-E 920, … is normally the steady state rotor speed associated with the 30-Second OEI Power rating." — matches the `before` field, and the elided term is correctly identified as "Maximum power-on rpm". 3 seconds exact. No pre-amendment wording in requirement content.

### CS-E 930.md
_clean_ — both obligations present, all three quoted fragments verbatim, and the four AMC cross-references (AMC E 930(d)(2)(i), (a)(1), (d)(1), (d)(5)(iii)/(iv)) all say what the note says they say. The "new at Amendment 8" account matches `work/redline/CS_E_930_Amdt8.md` (6 inserted runs, 0 deleted, declared as "The following CS-E 930 is added:").

### AMC E 930.md
- **MAJOR** — engine-profile conflict, third instance. "The rig specification therefore depends on the target rotorcraft transmission, which `engine_profile.md` records as an open item." It does not; see AMC E 850 above.
- **MINOR** — unrecorded omission of source content inside an applicable sub-point. AMC E 930(d)(1)(iii) ends: "…the IMP substantiation may require other test or in-service experience data **(including, if available, comparison of relevant past IMP demonstrations with subsequent successful entry-into-service (EIS) Engine experience)**." The note's row stops at "…other test or in-service experience data." The parenthetical is neither carried nor recorded in `## Not applicable`. It is not a turboshaft-irrelevant cut, so it should have reached the note.
- **MINOR** — wrong count in a `## Not applicable` line: "the **four** conditions of (d)(7)(i)". AMC E 930(d)(7)(i) sets three lettered conditions, (A), (B) and (C); (A) then carries two notes (a) and (b). (The companion count in the same line, "the seven on-wing inspections of (d)(7)(ii)", is correct: (A) to (G).)
- **MINOR** — term drift on the turboshaft sub-point. Source (d)(2)(v): "Potential rotor drive system characteristics include but are not limited to **inertial** and torsional vibration." The Requirement row copies "inertial" correctly, but the prose below ("The two characteristics named, **inertia** and torsional vibration"), the `## Compliance` bullet ("including **inertia** and torsional vibration") and `## Application` ("with **inertia** and torsional vibration named") all change the word. "Inertial vibration" and "inertia" are not the same quantity.
- Pruning verified in full, as the brief asked. The dropped material is: `(d)(7)` in its entirety and the AMC 20-6B paragraph inside `(d)(1)(i)` (the early ETOPS route); `(d)(2)(iv)` Turbopropeller Applications in full; "reverse thrust use" from the `(d)(1)(i)` list; "thrust reverser" from the `(d)(2)(ii)` examples; "size and diameter of the fan" from the `(c)` design-factor list; and "thrust or power" reduced to power throughout. **Every one of these is recorded in `## Not applicable`, one line each, with the sub-point reference and the reason, and none records what the cut text said.** Nothing else in the source was dropped: `(a)(1)`–`(a)(4)`, `(b)` with its three items, `(c)` with both definition lists, `(d)(1)(i)`–`(iii)`, `(d)(2)(i)`–`(iii)` and `(v)`, `(d)(3)`, `(d)(4)` with its Note, `(d)(5)(i)`–`(iv)` including the three-way teardown outcome and the CS-E 25(b)(2) credit, `(d)(6)(i)`–`(iii)`, and `(e)` all reach the Requirement table — apart from the (d)(1)(iii) parenthetical flagged above.
- Other verification: the "1 000-cycle" quotation is verbatim; the (a)(1), (d)(2)(v) and (c) control-system-architecture quotations are verbatim; the CS-E 25(b)(2) characterisation ("an in-service engine evaluation programme with service engine tests or equivalent experience", mandatory post-flight inspections) matches `work/paragraphs/CS_E_25.txt`; the OEI claims match `engine_profile.md`. The "new at Amendment 8" account matches `work/redline/AMC_E_930_Amdt8.md` (260 inserted runs, no deletions, "The following AMC E 930 is added:"), and no pre-amendment wording exists to leak.

---

# Subpart F (all 7 notes) — verification

## Summary

Seven notes checked against their source paragraph files: `CS-E 1000`, `AMC E 1000`,
`CS-E 1010`, `CS-E 1020`, `AMC E 1020`, `CS-E 1050`, `AMC E 1050`. Every line of every
source file was read. One note is clean (`CS-E 1000`). Totals: **1 BLOCKER, 5 MAJOR,
9 MINOR**.

Coverage is good: no sub-point of any applicable paragraph is silently omitted, and no
note needs a `## Not applicable` section because nothing was cut. Frontmatter (`pages`,
`subpart`, `changed_in: []`) agrees with `work/paragraph_index.csv` for all seven, and
no note carries an `## Amendment history` section, correctly, since the index records
`changed_in = none` for every Subpart F paragraph.

**Excluded-paragraph check (explicitly requested).** Clean. `CS-E 1030`, `AMC E 1030`
and `CS-E 1040` appear only as plain text, in `CS-E 1000.md` lines 52-53 and
`AMC E 1000.md` lines 46-48, never as wikilinks. No ghost wikilinks exist anywhere in
the seven notes — every `[[...]]` target resolves to an existing file in `vault/`. No
TLD or ETOPS requirement content is reproduced: a grep for `LOTC`, `LOPC`, `Markov`,
`MMEL`, `dispatch interval`, `entry level`, `mature level`, `IFSD` and `diversion`
across all seven notes returns nothing. The only occurrence of "dispatch deviation" is
in the volcanic-cloud notes and comes from AMC E 1050(3)'s own wording, not from
AMC E 1030.

The dominant defect pattern is not in the Requirement tables — those are accurate — but
in the `Application to this engine` and `Compliance` sections, where cross-references to
other paragraphs are asserted more strongly than their own source text supports, or
attached to the wrong citation.

## Findings

### CS-E 1000.md

_clean_

All three sentences of the source reach the table, all as `Statement` (declaratory
"may be mandatory", "is optional", "will be recorded") — correct. The quoted fragment
"optional, at the request of the applicant" used downstream in `CS-E 1050.md` is
verbatim. `[[CS-E 40]]` in `Related` is justified: CS-E 40 is the paragraph that
mentions the Engine type certificate data sheet.

### AMC E 1000.md

- **MINOR** — `Related:` lists `[[CS-E 50]]`, which is not derivable from this AMC.
  AMC E 1000 is two sentences about the purpose of Subpart F and CS-34; it says nothing
  about engine control systems. The link appears to be reasoning from the excluded TLD
  example to EECS, which the source does not make.
- **MINOR** — `covers: ["AMC E 1000"]` in the frontmatter. CLAUDE.md marks `covers` as
  "merged AMC notes only; omit otherwise", and this note merges nothing: AMC E 1000 is a
  single banner. `scripts/lint_vault.py` line 204 only requires `covers` when a note
  carries more than one id, so nothing enforces it either way.

### CS-E 1010.md

- **MAJOR** — duplication of `CS-E 130`'s content, against CLAUDE.md rule 8. Lines 53-57
  reproduce the whole of CS-E 130(f) rather than linking to it. Source
  [CS-E 130(f)]: "Unintentional accumulation of hazardous quantities of flammable fluid
  within the Engine must be prevented by draining and venting." Note: "unintentional
  accumulation of hazardous quantities of flammable fluid within the engine must be
  prevented by draining and venting". The same lines also restate AMC E 130(6)'s drain
  and vent case ("a drain would flow a hazardous quantity during continued rotation
  after shutdown"), which paraphrases AMC E 130(6) accurately but again reproduces
  rather than links. The characterisations are correct; the objection is that both
  paragraphs have their own notes.
- **MINOR** — line 51-52: "Fuel venting provisions are part of the fuel system, so the
  design work meets [[CS-E 560]]." Neither CS-E 1010 nor CS-E 560 says this. CS-E 1010
  is a single sentence pointing at CS 34.1; CS-E 560 covers fuel specification
  declaration, pump margin and filtration. The claim that CS-E 1010 design work
  discharges CS-E 560 is an inference carrying no citation and no `[VERIFY]`.

### CS-E 1020.md

- **BLOCKER** — wrong citation. Line 43 (`## Compliance`): "Assessment of any further
  type design change for its effect on emissions characteristics and on CS-34 compliance
  **[CS-E 1020]**. Accepted means: [[AMC E 1020|AMC E 1020(2)]]." CS-E 1020's full text
  is: "It must be demonstrated, by test or analysis or combination thereof, that the
  Engine type design complies with the emission specifications of CS 34.2 in effect at
  date of Engine certification. The resulting data must be recorded." It imposes no duty
  concerning later changes to the type design. That duty exists only in AMC E 1020(2)
  ("Any further change to the type design should assess the effect on its engine
  emissions characteristics..."), and it is an `Accepted method`, not a specification.
  The citation upgrades an AMC's accepted means into a CS-E requirement.
- **MAJOR** — unsupported requirement-adjacent claims in `## Application to this engine`,
  lines 50-53. "The declared fuel specifications of [[CS-E 560|CS-E 560(a)(1)]] are an
  input to the emissions demonstration, since emissions depend on the fuel burned and
  each approved fuel type carries its own CS-E 560(a) declaration. The declared ratings
  of [[CS-E 40]] set the operating points." Neither CS-E 1020 nor AMC E 1020 mentions
  fuel specifications, fuel type or ratings; CS-E 560(a)(1) requires fuel specifications
  to be "declared and substantiated" but says nothing about emissions. The second
  sentence also contradicts the note's own `[VERIFY]` eleven lines later, which states
  that "the operating cycle they are measured over" cannot be stated from the sources
  held. Either the claim is general knowledge about emissions certification, which
  CLAUDE.md forbids as requirement content, or it needs its own `[VERIFY]`.
- **MINOR** — `Related:` lists `[[CS-E 730]]` (Engine Calibration Test). Nothing in
  CS-E 1020 or AMC E 1020 connects to calibration, and no other section of the note
  explains the link.

### AMC E 1020.md

- **MAJOR** — overstated cross-reference strength, lines 52-54: "in the same way that
  [[AMC E 515|AMC E 515(3)(g)]] **requires** the Approved Life assumptions to be reviewed
  after certification." AMC E 515(3)(g) says: "A regular review of the assumptions made
  when establishing the Approved Life **may be required, depending on the conservative
  nature of the assumptions** made when determining the Approved Life." That is
  conditional, and AMC E 515 is an AMC, so its strongest reading is `Accepted method`,
  never "requires". The analogy the note draws survives; the word "requires" does not.
- **MINOR** — `covers: ["AMC E 1020"]` on a note that merges nothing (same point as
  AMC E 1000.md).

Coverage, strengths, quotations and numbers in this note are otherwise correct. The
split of AMC E 1020(2) into two `Statement` rows plus one `Accepted method` row matches
the source's verbs exactly ("will be assessed" / "is dependent on" declaratory; "should
assess" accepted method), and the quoted note format ("Note x:", "Engine emissions",
"Engine (type/model) complies with CS-34 amendment (number).") is verbatim.

### CS-E 1050.md

- **MINOR** — strength downgrade on both rows. Source verbs are "must":
  [CS-E 1050(a)] "The susceptibility of turbine Engine features to the effects of
  volcanic cloud hazards **must** be established"; [CS-E 1050(b)] "Information necessary
  for safe operation **must** be provided in the relevant documentation." The table reads
  `Required if claimed` for both. CLAUDE.md fixes `Required if claimed` to the pattern
  "`may` establish/seek, then `must` substantiate", and CS-E 1050 contains no "may". The
  note does justify the choice in the prose under the table, and materially it is right —
  CS-E 1000 makes the paragraph elective — so this is recorded as a deviation from the
  strength rule rather than as a misleading statement. It needs a consistency decision
  across the vault, since `CS-E 1010` and `CS-E 1020`, which are also conditional under
  CS-E 1000, are rendered `Required`.
- **MINOR** — "and/or" dropped, line 41 (`## Compliance`): "Accepted means:
  [[AMC E 1050]] — a combination of experience, studies, analysis and testing of parts,
  sub-assemblies or engines." Source [AMC E 1050]: "should include a combination of
  experience, studies, analysis, **and/or** testing of parts, sub-assemblies or Engines."
  The source allows a combination without testing; the note's wording reads as if testing
  is part of the accepted means in every case. Same defect as the MAJOR in
  `AMC E 1050.md`, in a less prominent position.

Both sub-points are covered, the quotation "optional, at the request of the applicant"
[CS-E 1000] is verbatim, and the observation that the paragraph "requires susceptibility
to be established, not to be absent" is a fair reading of (a). The `[VERIFY]` on whether
the applicant elects the paragraph is correct — `engine_profile.md` does not record it.

### AMC E 1050.md

- **MAJOR** — "and/or" dropped in the Requirement table, row 1: "Establish the
  susceptibility of engine features to the effects of volcanic clouds by a combination of
  experience, studies, analysis, **and** testing of parts, sub-assemblies or engines."
  Source: "Acceptable means of establishing the susceptibility of Engine features to the
  effects of volcanic clouds should include a combination of experience, studies,
  analysis, **and/or** testing of parts, sub-assemblies or Engines." The table is the 1:1
  map to the source, and the change converts an alternative into a conjunction: an
  applicant reading the row concludes that testing of parts, sub-assemblies or engines
  belongs in the accepted means, when the source permits a combination that omits it.
  The `## Compliance` bullet on line 59 repeats the same wording.
- **MAJOR** — unsupported cross-reference and mischaracterisation, lines 83-88: "Inability
  to restart engines is a condition the declared OEI ratings do not cover, because it
  affects all engines exposed to the same cloud — the multi-engine threat case of
  [[CS-E 540|CS-E 540(b)]], where the test is continued safe flight and landing rather
  than absence of a Hazardous Engine Effect." Two problems. (i) Neither AMC E 1050 nor
  CS-E 540 makes this connection, and AMC E 540(2) enumerates what CS-E 540(b) is aimed
  at: "CS-E 540(b) is intended to address for example rain, hail, ice, gravel, sand,
  small and medium birds." Volcanic cloud is not among them, and the note offers no
  `[VERIFY]`. (ii) CS-E 540(b) is misdescribed: it reads "...will not preclude the
  continued safe flight and landing of the aircraft **as a consequence of a Hazardous
  Engine Effect or an unacceptable** (1) Immediate or subsequent loss of performance;
  (2) Deterioration of Engine handling characteristics; (3) Exceedence of any Engine
  operating limitation." A Hazardous Engine Effect is one of the named consequence
  routes inside (b), so "rather than absence of a Hazardous Engine Effect" is not the
  distinction the source draws. The claim about the declared OEI ratings has no source
  at all.
- **MINOR** — one source sentence is absent from the Requirement table and not recorded
  anywhere as a cut: "This information may be used to assist operators in producing
  operational data and instructions for their flight crews when operating in, or
  avoiding, airspace contaminated with volcanic clouds" [AMC E 1050]. Its verb is "may",
  so it belongs in the table as `Permitted`. It is partly reflected in the prose at lines
  49-51 ("it exists so operators can produce operational data and instructions for their
  flight crews"), which is why this is MINOR and not a silent omission — but the prose
  also firms "may be used to assist" into a statement of purpose.
- **MINOR** — `covers: ["AMC E 1050"]` on a note that merges nothing (same point as
  AMC E 1000.md).

Everything else checks out. All six feature categories (1)a-f are present with their
source wording; the lead-in "the following points should be considered" is correctly
rendered as `Accepted method` on (1)-(4); the short quotations "may include but are not
limited to the following", "comprises volcanic ash together with gases and other
chemicals" and "or equivalents" are verbatim and used in their source sense. The
supporting cross-references in `## Application to this engine` were checked individually
against their own paragraph files and are accurate: AMC E 80(2)(a) Table 1 does list
"Sand and Dust" (item 7), "Fluid Susceptibility" (item 8) and "Salt Spray" (item 9);
CS-E 60(e) is the turbine cooling system instrumentation paragraph; CS-E 580 is the
bleed air foreign matter paragraph; CS-E 670 is the contaminated fuel test; CS-E 500(a)
is "free from dangerous surge and instability"; CS-E 910 is relighting in flight;
CS-E 90 is corrosion.

## Numbers and figures

Subpart F in scope contains no numeric values, times, percentages or probabilities — the
only figures in the subpart belong to AMC E 1030, which is excluded, and
`work/paragraph_index.csv` records `has_figure_or_table = no` for all seven notes in
scope. `vault/figures/` correctly holds no image for any of them. Nothing to check under
accuracy rules 3 and 6.

## Engine profile consistency

Consistent. `CS-E 1000.md` and `AMC E 1000.md` state that time limited dispatch is not
claimed, matching `engine_profile.md`. `CS-E 1050.md` and `AMC E 1050.md` refer to
"a full-authority EECS", matching the declared "EECS / FADEC, full authority". No note in
Subpart F makes a claim about OEI ratings other than the unsupported sentence flagged
under `AMC E 1050.md`, and that sentence does not misstate which ratings are declared.
