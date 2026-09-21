# Dead ends — what the vault cannot answer, and why

A **dead end** is a point where the vault stops. Either the answer lives in a
document EASA cites and we do not hold, or it depends on something the applicant
has not yet declared. Neither is a defect. Both are limits on what a reader can
get from these 112 notes, and a certification programme needs the list.

Compiled from seven independent verification passes over the whole vault, one per
scope, each reading the notes AND their source paragraphs. Cross-checked against
`scripts/external_refs.py`, which scans the same corpus mechanically.

> **Status: five of the cited documents are now held.** `source/external/` has
> CS-27 Amendment 10, CS-29 Amendment 12, CS-Definitions Amendment 2, AMC-20
> Amendment 23, and the Easy Access Rules edition of Part 21 — Regulation (EU)
> No 748/2012, which carries the Annex I Regulation text together with its AMC
> and GM. Between them they close the Kind 1 entries for `27.45(f)`, `29.45(f)`,
> `27.1093(b)`, `29.1093(b)`, `Fire-resistant`, `Fireproof`, `Icing Atmospheric
> Conditions`, `AMC 20-1`, `AMC 20-3`, `AMC 20-42`, `AMC 20-115`,
> `AMC 25.1309`, `AMC1 21.A.3B(b)`, `21.A.3`, `21.A.20(d)2`, `21.A.61(a)`,
> `21.A.801` and `21.A.805`.
>
> Holding a document is not the same as having used it. The entries below still
> read as they did when the inventory was compiled, and each is rewritten when
> the answer actually reaches a note — which needs the Source of truth rule in
> CLAUDE.md amended first, with a convention for marking an imported obligation.
> `source/external/SOURCES.md` is the current record of what is held and what
> each one closes.
>
> Still missing: **CS-34**, which is the largest remaining item, and the
> industry standards — EUROCAE ED-14 / RTCA DO-160, ISO 2685, FAA AC 33.70-2
> and -3, SAE ARP4754A / EUROCAE ED-79A.

**145 distinct dead ends.** They fall into three kinds.

## Kind 1 — documents we do not hold

CS-E does not stand alone. It defers to Part 21 for the certification process, to
CS-27 and CS-29 for what the rotorcraft must do, to CS-34 for emissions, to
CS-Definitions for terms it uses without defining, to the AMC 20 series for
electronic control systems, and to industry standards for how each environmental
test is run. `source/` holds five PDFs and none of those is among them.

### Blocking — an obligation cannot be understood or complied with

| Document | Where it bites | What is blocked |
|---|---|---|
| **CS-Definitions** | CS-E 15(a), twice | CS-E 15 defines about twenty terms and says the rest are in CS-Definitions. Every other capitalised term in the vault — Failure, Fault, Control Mode, Fireproof, Engine — is defined there, not here. |
| **CS-Definitions Amendment 2** | CS-E 780(a)(2) | The 'Icing Atmospheric Conditions' the icing test must cover. Without it the test envelope cannot be stated. |
| **CS-34, CS 34.1, CS 34.2** | CS-E 1000, CS-E 1010, CS-E 1020 | Essentially the whole content of two paragraphs: the fuel venting specifications and every emissions limit, operating cycle and measurement method. |
| **CS-27 / CS-29** | The assumed aircraft code, via CS-E 20(b) and CS-E 30 | Which code applies is undecided, and CS-E cites both. It propagates into installation assumptions throughout. |
| **CS-27.45(f) / CS-29.45(f)** | AMC E 20(f)(1) | The power availability specification the engine data must satisfy. |
| **CS 27.1093(b) / CS 29.1093(b)** | CS-E 780(a)(2) | The ice protection specifications that fix which additional icing conditions apply. |
| **AMC 20-1, AMC 20-3** | AMC E 50(2) and (5), AMC E 80 Table 2 item 18, AMC E 170, CS-E 50 banner | The detailed interpretation of CS-E 50 for an EECS. Table 2 item 18 names **no alternative at all** — EMI, HIRF and lightning have no other accepted means in CS-E. |
| **AMC 20-42** | AMC to CS-E 50(l) | The entire security risk assessment method for CS-E 50(l). |
| **AMC1 21.A.3B(b)** | AMC E 510(3)(d)(iii) | The definition of "unsafe condition", which is the trigger for the whole uncontained-debris assessment. |
| **Part 21 points 21.A.801(a), (b), 21.A.805** | CS-E 120(a) | What the marking must contain and where it goes. |
| **point 21.A.3 of Part 21** | AMC E 515 | Occurrence reporting, feeding the Service Management Plan. |
| **EUROCAE ED-14 / RTCA DO-160** | AMC E 80, 15 of 19 items in Table 2 | The test procedure for almost every environmental qualification. |
| **ISO 2685** | AMC E 130 | The fire test standard — flame definition, temperature, duration. |
| **FAA AC 33.70-2** | AMC E 515 | Damage tolerance of hole features in high-energy turbine engine rotors. |

### Limiting — the obligation is clear, a detail is not

Part 21 as a whole and point 21.A.41 (TCDS content); point 21.A.33 (inspection of
type design hardware); AMC 20-115 (named in the CS-E 50 banner and never used
again, so the vault cannot even say what it governs); CS-27/29.1305
(instrumentation, via AMC E 60(d)(3)); AMC 25.903(e)(2) (relight demonstration
objectives); FAA AC 33.70-3; MIL-STD-810, MIL-STD-704, MIL-E-5007 (AMC E 80
tables); the USDA cotton-staple grading standards SRA-AMS 180 and 251
(AMC E 670's contaminant table); "published FAA ACs" as an open class in
AMC E 515; and the unnamed "aircraft certification specifications on oil systems".

### Cosmetic — a pointer only

AMC 25.1309; AMC 20-6B (the early ETOPS route, already excluded by scope);
ISO 12103-1 A4 (quantity and size distribution are given in full in the table);
ICAO Annex 5; FAR 33.87 (the alternative endurance schedule, already cut);
the AIA Propulsion Committee Study PC 338-1 behind Appendix A's tables; SAE
ARP4754A / ED-79A, SAE ARP 926A, SAE ARP 4761 and two reliability textbooks,
all named by AMC E 510 as sources of technique rather than obligation; point
21.B.75, 21.A.16 and 21.A.21(c)(3), which appear only as superseded citations in
Amendment history.

## Kind 2 — terms CS-E uses and defines nowhere

No document can be fetched for these. They are gaps in Amendment 8 itself.

| Term | Where | Why it matters |
|---|---|---|
| **"Maximum Engine Over-speed (20 Second)"** | CS-E 870(b)(1), and nowhere else in the whole document | It bounds the test speed for the exhaust gas over-temperature test. CS-E 830 approves a Maximum Engine Over-speed with no 20-second qualifier, and CS-E 15 does not define the term. **Blocking.** |
| **"rotor-lock"** | AMC E 910(3)(b) | The AMC lists five assumptions to apply to it but never says what it is. The assessment scope depends on a reading the source does not supply. |

## Kind 3 — engine information not yet declared

Not a missing document: a missing decision. `engine_profile.md` declares the
ratings, the control system, refrigerant injection and time-limited dispatch, and
holds exactly one open `[VERIFY]`. Everything below is undeclared.

### The one that blocks most

**The target rotorcraft and its transmission.** It alone blocks at least nine
separate items across the vault: the CS-27-vs-CS-29 code; the maximum airspeed
for normal flight operations (CS-E 800 bird speed); the maximum flight duration
(CS-E 670 filter blockage); the rotor drive system inertial and torsional
characteristics (AMC E 850 oscillatory torque, AMC E 930 IMP test rig); the
installation attitude and inclination range; the maximum period of flight with
one engine inoperative (CS-E 525); and whether the airframe has carbon fibre
composite fuel tanks (AMC E 670 contaminant).

### Blocking, and already flagged in the notes

The declared over-limit ratings — whether a Maximum Engine Over-torque,
Maximum Engine Over-speed or Maximum Exhaust Gas Over-temperature is sought
(CS-E 820, CS-E 830, CS-E 870, and together they decide the AMC E 60(d)(5)
usage-counting relief); the 30-Second OEI and maximum-rating operating
temperature limits (CS-E 920); engine inlet throat area (CS-E 790, CS-E 800);
Maximum Power-turbine Speed for Autorotation (CS-E 740); the declared minimum
engine carcass and oil temperature for starting (CS-E 770); whether a rotor
locking means is incorporated (CS-E 710); whether the starter is part of the
type design (CS-E 590); which shaft elements rely on CS-E 850(a)(3);
whether the CS-E 510 analysis relies on blade shedding for over-speed
protection; the placement of the AMC E 740(c)(2)(i) 25 hours — the single item
`engine_profile.md` does record.

### Blocking, and NOT yet flagged

These are the actionable ones. Each is a question a certification engineer will
hit with nothing in the note to warn them.

| Question | Where it bites |
|---|---|
| **The declared flight envelope** | CS-E 700 states nothing testable without it, and the CS-E 650 vibration survey cannot be bounded. |
| **The "significant response" threshold agreed with the Agency** | AMC E 650(1)'s definition is circular without it, and it triggers dwell testing under CS-E 740(g)(1). |
| **The CS-E 20(a) / CS-E 20(c) equipment split** | Decides, item by item, whether CS-E 80(b) or CS-E 80(c) applies. |
| **Whether a turbine starter with an external air or gas supply is fitted** | Decides the whole AMC E 80(4) containment category. |
| **Over-speed protection technology** | CS-E 50(e)(1) applies to electronic protection, (e)(2) to other, and AMC E 50(1) names a third, blade-shedding case outside the control system. |
| **Relative power levels of the declared ratings** | Which rating produces the maximum fuel demand, for the CS-E 560(a)(3) pump margin. |
| **Whether the engine incorporates a free power turbine** | Five sub-points bind only on that architecture: CS-E 740(f)(3), (g)(3) and (g)(4), CS-E 750(d) and CS-E 820(a). `engine_profile.md` declares the application, the ratings and the systems, not the architecture, and it is now recorded there as undeclared. Those five notes carry a `[VERIFY]`; everywhere else the vault reasons about a free power turbine conditionally. |

### Limiting, not flagged

Maximum rotational speed per rating per rotor module; the most adverse inlet
airflow distortion pattern; maximum declared jet pipe temperature; the declared
vibration environment; the aircraft-supplied power range for the EEC; tank test
parameters for CS-E 130; use of titanium, magnesium and abradable linings;
whether a flammable fluid tank or firewall is part of the engine; whether the
engine supplies bleed air to the cabin; the maximum allowable bleed and power
extraction; the declared drainage period after a false start; whether a 10-minute
Take-off Power rating is sought; engine architecture for the AMC E 1050 feature
map; and whether any boost fluid is used.

## Two structural gaps worth naming

**CS-E 660 and CS-E 700 have no accepted means at all.** AMC E 660 and AMC E 700
are aeroplane-only by their own banners and are excluded. Both specifications
still bind. There is no AMC route for either.

**CS-E 780 has no accepted means for a rotorcraft.** AMC E 780 says so itself:
"Specific provisions for rotorcraft Engines are currently not included in this
AMC. Until guidance has been established, the necessary compliance method
required for rotorcraft Engines should be agreed by the Agency."

**Three references are visible only inside embedded images.** MIL-STD-810,
MIL-STD-704 and ISO 12103-1 live in AMC E 80's four environmental tables and
AMC E 670's contaminant table, which accuracy rule 6 puts in the crop rather than
the text. A reader can see them; a search of the vault cannot find them.

---

The per-scope tables follow, as each verification pass wrote them.


---

# Scope A1

## Dead ends

### External documents

| Reference | Where | What it governs | What is blocked | Flagged? | Severity |
|---|---|---|---|---|---|
| **Part 21** (as a whole) | CS-E 10(a); notes `CS-E 10` (table row (a), Compliance) | The procedure under which the engine type certificate and changes to it are issued | The certification-basis document's own legal frame: what an application contains, who issues, how changes are classified. CS-E states none of it | No | Limiting |
| **point 21.A.41 of Part 21** | CS-E 40(e); notes `CS-E 40` (row (e), Compliance), `AMC E 40` (Compliance) | The engine type certificate data sheet — what a TCDS is and what it must carry | The TCDS content and format cannot be settled. CS-E 40(e) names the ratings and crew limitations plus "all other information found necessary for the safe operation of the Engine"; the boundary of "all other information" lives in 21.A.41 | No | Limiting |
| **point 21.B.75 of Part 21** | CS-E 10(c); note `CS-E 10` (Amendment history) | How variations of Subparts B and C are decided for piston rotorcraft engines | Nothing here — CS-E 10(c) is piston-only and EXCLUDED | No | Cosmetic |
| **21.A.61(a)** | CS-E 25(a) *before* Amendment 7 (`work/redline.json`, `CS-E 25 [Amdt7]`); note `CS-E 25` (Amendment history) | Instructions for continued airworthiness, in the pre-Amendment-7 wording | Nothing — the qualifier was deleted. Recorded only so the history reads correctly | No | Cosmetic |
| **21.A.16** | CS-E 10(c) *before* Amendment 7 (`work/redline.json`); note `CS-E 10` (Amendment history) | Superseded citation, replaced by point 21.B.75 | Nothing | No | Cosmetic |
| **CS-Definitions** | CS-E 15(a) (twice); note `CS-E 15` (row (a), Compliance, [VERIFY]) | Every capitalised term CS-E uses but does not define in CS-E 15 — the initial-capital convention explicitly spans both documents | The meaning of an unknown number of defined terms used throughout the vault. CS-E 15 defines ~20; the rest (Failure, Fault, Control Mode, Hazardous, Fireproof, Engine, Agency…) are assumed to come from CS-Definitions and cannot be checked | **Yes** — `CS-E 15` [VERIFY] at lines 61–64, which also names the issue question | **Blocking** |
| **CS-Definitions, 'Icing Atmospheric Conditions'** | CS-E 780 (out of this scope); cited in note `CS-E 15` [VERIFY] as evidence that "CS-Definitions Amendment 2" is at least contemporaneous | The icing envelope definition | Nothing in this scope; used here only to date the CS-Definitions issue | **Yes** (same [VERIFY]) | Cosmetic *(in this scope)* |
| **CS-27.45(f) / CS-29.45(f)** (also written "CS-27/29.45(f)") | AMC E 20(f)(1) and AMC E 20(f)(4); note `AMC E 20` (row (f)(1), [VERIFY]) | The *rotorcraft* power-availability specification the engine data must let the installer meet | The content and scope of the engine data pack. AMC E 20(f) is written entirely as support for a specification stated elsewhere; without 27/29.45(f) the target of "the necessary Engine data" is undefined | **Yes** — `AMC E 20` [VERIFY] at lines 105–107 | **Blocking** |
| **CS 27.1093(b) / CS 29.1093(b)** | CS-E 780 (out of scope); quoted in note `CS-E 30` [VERIFY] at lines 49–50 | Rotorcraft induction-system icing protection | Nothing in this scope; used as the evidence that CS-E does not itself settle CS-27 vs CS-29 | **Yes** (the same [VERIFY]) | Cosmetic *(in this scope)* |
| **CS-27 / CS-29 as a whole** (the "aircraft certification specification code") | CS-E 20(b), CS-E 30(a), AMC E 20(4), AMC E 30 Table 1 row "Interfaces — Applicable aircraft specifications"; notes `CS-E 20`, `CS-E 30`, `AMC E 20`, `AMC E 30` | The assumed installation code against which every CS-E 30 assumption is judged | The whole assumptions package. AMC E 20(4) requires provision "for… at least the mandatory items of equipment prescribed by the use of the word 'should' in the assumed applicable aircraft specifications" — an obligation whose content is entirely in a document we do not hold | **Partly** — flagged at `CS-E 30` and `AMC E 20`; **not** flagged at `AMC E 20(4)`, where the "mandatory items of equipment" obligation sits | **Blocking** |
| **Aircraft certification specifications on oil systems** (unnamed) | AMC E 30 Table 1, "Oil system" row, the text inserted at Amendment 7; note `AMC E 30` (Amendment history) | The installer's oil-system compliance, which the declared maximum allowable oil consumption exists to support | The value to declare. The AMC gives the assumption to state but not the specification it must satisfy, and does not name the paragraph | No | Limiting |
| **AMC-20** (the series, as a whole) | AMC General; note `AMC General` (Requirement row, Compliance, Application) | A second source of acceptable means for any CS-E specification, alongside the AMC E paragraphs | Completeness of every compliance method in the vault. AMC General creates a standing search obligation against a document we do not hold, so "no acceptable means exists for this specification" can never be concluded | **Yes** — `AMC General` line 39: "AMC-20 is not held in `source/`. Obtain it separately…" | **Blocking** |
| **AMC 20-1** | CS-E 50 banner "(See AMC E 50, AMC 20-1, AMC 20-3, AMC 20-115)"; AMC E 50(2); AMC E 50(5); notes `CS-E 50` (Compliance, [VERIFY]), `AMC E 50` ([VERIFY], `Not applicable`) | "additional and detailed interpretation of CS-E 50" for EECS, with special consideration of aircraft interfaces; and the interpretation for evaluating aircraft-supplied-power dependence under CS-E 50(h) | The EECS compliance method for the longest paragraph in Subpart A. AMC E 50 hands the detail to it twice and supplies none itself | **Yes** — `CS-E 50` lines 127–129 and `AMC E 50` lines 168–169 | **Blocking** |
| **AMC 20-3** | identical to AMC 20-1 — always cited as a pair | as above | as above | **Yes** (same two [VERIFY]s) | **Blocking** |
| **AMC 20-115** | CS-E 50 banner only; note `CS-E 50` (Compliance line 106, [VERIFY]) | Named in the CS-E 50 "(See …)" banner; the paragraph body never returns to it, so CS-E 50 does not say what it governs | Unknown by construction. The vault cannot say what it is for, only that CS-E 50 points at it. `AMC E 50` does not mention it at all | **Yes** — in `CS-E 50` only | Limiting |
| **AMC 20-42** | AMC to CS-E 50(l); note `AMC E 50` (Requirement row, Compliance, [VERIFY]) | The acceptable means, guidance and methods for information system security protection under CS-E 50(l) | The entire CS-E 50(l) compliance method. AMC to CS-E 50(l) is three sentences: it delegates to AMC 20-42 and adds one scoping condition (common-mode IUEIs across all engines). Nothing else is stated | **Yes** — `AMC E 50` lines 215–216 | **Blocking** |

No FAA material (FAR 33.87, AC 33.70-x), no industry standards (EUROCAE ED-14 /
RTCA DO-160, ISO 12103-1, MIL-STD-810, SAE, ASTM), no CS-23/25/34 and no
`AMC1 21.A.3B(b)` occur anywhere in this scope's nineteen source files or thirteen
notes. A token scan for `CS|AMC|AC|FAR|DO|ED|ISO|SAE|ASTM|MIL` over all nineteen
files returns only the references tabulated above.

**Approval dependencies that are not documents.** Three obligations in this scope
are settled by an EASA decision rather than by any text: the in-service engine
evaluation programme "should be provided and be **approved by the Agency prior to
certification**" [AMC E 25(4)(d)(i)]; the TBO/TBR value "should be agreed by EASA"
[AMC E 25(6)(a), piston, EXCLUDED]; and the credit factor for a cyclic durability
test "unless the applicant can justify, and EASA accepts, a higher value"
[AMC E 25(6)(b), piston, EXCLUDED]. Only the first reaches this engine, and
`AMC E 25.md` carries it correctly at lines 105–107.

### Undeclared engine information

| Reference (the quantity) | Where | What it governs | What is blocked | Flagged? | Severity |
|---|---|---|---|---|---|
| **Target rotorcraft, and the assumed aircraft certification specification code (CS-27 or CS-29)** | CS-E 20(b), CS-E 30(a), AMC E 20(4), AMC E 20(f)(1), AMC E 20(f)(4), AMC E 30 Table 1; notes `CS-E 20`, `CS-E 30`, `AMC E 20`, `AMC E 30` | The single assumption on which the whole CS-E 30 package rests | Which power-availability specification the CS-E 20(f) data must support; which "mandatory items of equipment" AMC E 20(4) requires provision for; the content of every Table 1 assumption. `engine_profile.md` says "Rotorcraft turboshaft, multi-engine installation" and stops | **Yes** — `CS-E 30` lines 49–50 and `AMC E 20` lines 105–107 | **Blocking** |
| **Over-speed protection technology: electronic, hydromechanical/mechanical, or blade-shedding** | CS-E 50(e)(1) vs (e)(2), AMC E 50(1), AMC E 50(e); notes `CS-E 50`, `AMC E 50` | Which of two different mandatory demonstrations applies — a BITE/testing design, or a demonstration that the function survives between maintenance periods | The over-speed compliance route. Both notes currently *decide* it from the EECS declaration, which the source does not license (see the CS-E 50 MAJOR above) | **No** — asserted as settled instead | **Blocking** |
| **Whether the EECS depends on aircraft-supplied resources, and which** | AMC E 20(6), CS-E 30(b), AMC E 30 Table 1 "Engine Control System" row; notes `AMC E 20` (lines 89–93), `CS-E 30` (lines 40–43) | Whether the applicant must specify and substantiate EECS requirements on resources the aircraft provides — OEI data recording, aircraft central computers, electrical power, air data | The scope of the CS-E 30(b) interface-conditions statement and of the AMC E 20(6) substantiation. `engine_profile.md` declares the control system's authority but not its external dependencies | **No** — `AMC E 20` states the dependency is "real" | Limiting |
| **Usage-recording design under CS-E 60(d)(2): each usage and duration, or accumulated time only** | AMC E 25(4)(a) final paragraph; note `AMC E 25` (row 4 of the (4)(a) block) | Whether the mandatory post-flight action is driven by the number of applications in a flight or by total recorded duration | The basis of the whole mandatory post-flight maintenance regime, which is the operational cost of the two short OEI ratings | No | Limiting |
| **Whether the applicant elects the 2.5-minute extension of the 2-Minute OEI rating** | AMC E 40(b)(3)(5), AMC E 25(4)(a); notes `AMC E 40` (lines 151–155), `AMC E 25` (lines 117–119) | Whether the additional 30 seconds is treated as a derated 30-Second OEI rating, and which maintenance actions follow | Which of two maintenance-action sets is prescribed, and whether a separate EASA approval is needed for the alternative | No — correctly presented as an open option, but not recorded as an item to close | Limiting |
| **Declared 'Rated 30-Minute Power' level** | AMC E 40(b)(3)(7); note `AMC E 40` (lines 76–80) | The rating may be set anywhere "between the Maximum Continuous up to and including the take-off rating" | The cumulated time limit and ICA instructions of AMC E 25(5), and the AMC E 740(c)(2)(i) additional-25-hours question that `engine_profile.md` already flags | No | Limiting |
| **Declared over-limit values: Maximum Over-torque transient, Over-speed transient(s), Over-temperature transient, Maximum Power Turbine torque and rpm, Autorotation power turbine speed** | AMC E 40(d)(3)(n)–(r); note `AMC E 40` (Turbine engine limitations table, Compliance) | Rows of the operating limitations schedule that AMC E 40(d) says should normally be declared | The limitations schedule and the TCDS entry, and the substantiation routes into CS-E 820, CS-E 830 and CS-E 870 | No | Limiting |
| **Mapping of "Maximum / Intermediate / 30-minute Contingency conditions" onto the declared rating names** | AMC E 40(d)(3)(a); note `AMC E 40` | Which RPM / turbine gas temperature / time rows are entered in the TCDS | Three rows of the limitations schedule. The Contingency names appear in no CS-E 40 sub-point | **Yes** — `AMC E 40` lines 168–172, which routes it to EASA | Limiting |
| **Function and authority of the 'OEI override' feature** | CS-E 50 generally, AMC E 50(1); notes `CS-E 40` (line 55), `CS-E 50` (lines 115–116), `AMC E 50` (lines 163–166) | Whether the feature is part of the Engine Control System, hence in scope of CS-E 50 and the CS-E 510 assessment | Whether CS-E 50's obligations attach to it at all. `engine_profile.md` records what it is *not* (not a rating) but not what it does; `AMC E 50` can only state the test conditionally ("**If** the feature controls, limits or monitors…") | **Partly** — the notes state the condition but open no [VERIFY] | Limiting |
| **Whether an engine-dedicated electrical power source is required for CS-E 50(h)(1)** | CS-E 50(h)(2); note `CS-E 50` (row (h)(2)) | The only **Recommended** obligation in CS-E 50 — a capacity margin for recovery from operation below idle | Whether the recommendation is engaged at all, and what margin is sufficient | No | Limiting |
| **Whether the engine is modular, and its module boundaries** | AMC E 25(3); note `AMC E 25` (row (3), Compliance) | "details of the division of the Engine into modules, giving the nomenclature and clearly defining the boundaries" | An ICA content item — conditioned on "where applicable", which cannot be evaluated | No | Cosmetic |

### Notes on coverage

- **The PDF was not opened**, per the brief. Everything above is checked against
  `work/paragraphs/`, `work/redline.json`, `work/paragraph_index.csv`,
  `engine_profile.md` and the notes themselves.
- **AMC E 30's Table 1 reaches the note only as three page images**
  (`AMC_E_30_p27/28/29.png`). I verified the note's `Not applicable` entries and
  its Amendment-history quotation against the extracted table text, but I did not
  and cannot verify that the three crops actually show the right pages.
- **Two pass-1 strength calls re-examined and left standing.** (a) `AMC E 25`
  row (4)(a) at **Required**: the source reads "the airworthiness limitations
  section… **are required to** prescribe", which carries the force of `must`;
  pass 1 wanted **Statement**. I judge Required defensible and do not re-report
  it. (b) `AMC E 25` row (1) at **Statement** for "may also evolve after entering
  service": this is possibility, not permission, so **Statement** is right and
  pass 1's **Permitted** would have been wrong. One ruling should be written down
  somewhere and applied vault-wide; neither is worth a finding.
- **`2 1/2` vs `2½`.** The source is itself inconsistent: `CS_E_40.txt`,
  `AMC_E_25.txt` and `AMC_E_40_b_3.txt` write "2 1/2" (and AMC E 40(b)(3) also
  writes "2.5 minutes" and "2.5-minute"), while `CS_E_740.txt`, `CS_E_820.txt`,
  `CS_E_840.txt` and others write "2½". The vault normalises to "2½" everywhere
  except where it is quoting AMC E 40(b)(3)'s "2.5 minutes", which it keeps. The
  value is never wrong. I record this rather than reporting thirteen MINORs
  against a source inconsistency, but a one-line ruling in CLAUDE.md would settle
  it.
- **Examples dropped without an entry, where no obligation is lost.** Two cases
  beyond the ones reported: AMC E 20(6)'s second example of an aircraft-supplied
  resource ("aircraft central computers that perform some or all of the Engine
  control functions") reaches no part of `AMC E 20.md`; and the opening rationale
  paragraph of AMC E 25(4)(b) ("The 30-Second and 2-Minute OEI ratings were
  originally intended to allow brief periods of operation close to the limits of
  the Engine design…") reaches no part of `AMC E 25.md`. Both are illustrative,
  neither carries an obligation, and I did not count them as defects — but the
  first is a live FADEC architecture case and is worth a line.
- **`lint_vault.py`, `audit_cuts.py` and `build_matrix.py` were not run.** The
  brief makes the repository read-only and those scripts write into `work/` and
  `deck/`. All template, link and citation checks above were done by hand or with
  throwaway scripts in the scratchpad.

---

# Scope A2

## Dead ends

### External documents

Everything below sits outside the five PDFs in `source/`.

| Reference | Where | What it governs | What is blocked | Flagged? | Severity |
|---|---|---|---|---|---|
| **Part 21, points 21.A.801(a) and (b), and point 21.A.805** | Cited by CS-E 120(a). Note: `CS-E 120.md` (table row, Compliance bullet, `[VERIFY]`, amendment history) | The whole content of engine identification — what must be marked on the engine and how | The entire substance of CS-E 120(a). CS-E adds nothing of its own; the note can state only that the applicant must comply | Yes | **Blocking** |
| **Part 21, point 21.A.20(d)2** | Cited by CS-E 160(a). Note: `CS-E 160.md` (table row, `[VERIFY]`) | The certification-process obligation that CS-E 160(a) exists to enable | Nothing in CS-E 160(a) itself — the CS-E duty (cause, airworthiness effect, corrective action) is stated in full. Only the *reason* for it is unreadable | Yes | **Cosmetic** |
| **Part 21, point 21.A.21(c)(3)** (former text) | The Amdt 7 "before" wording of CS-E 160(a), from `work/redline.json`. Note: `CS-E 160.md` amendment history | The provision that 21.A.20(d)2 replaced | Whether the Amendment 7 substitution changed the underlying obligation or only renumbered it | Yes (second `[VERIFY]` in `CS-E 160.md`) | **Limiting** |
| **CS-27/29.1305** | Cited by AMC E 60(d)(3): "the aircraft should still comply with CS-27/29.1305 specifications". Note: `AMC E 60.md`, `## Application to this engine` | The rotorcraft-level instrument specification the aircraft must meet when the OEI recording or retrieval system is not part of the engine | The aircraft-side content. The engine-side duty (state the objective and assurance level in the instructions for installation) is fully readable. Also blocked: whether CS-27 and CS-29 differ at .1305 — the source names them at one combined number | Partly — discussed in prose, no `[VERIFY]` | **Limiting** |
| **CS-Definitions** ("Fire-resistant", "Fireproof") | Cited by AMC E 130(1)(d); reached generally by CS-E 15(a). Notes: `AMC E 130.md` (table row), `CS-E 130.md` (`[VERIFY]`) | The definitions of the two fire protection levels that CS-E 130 is built on | The definitions themselves. AMC E 130(1)(d) gives only the gloss "the functioning of the part under fire condition should not hazard the aircraft"; the 5-minute and 15-minute exposures come from AMC E 130, not from the definitions | Yes | **Limiting** |
| **EUROCAE ED-14 / RTCA DO-160** (also written "RTCA/DO160"; **DO-160D** in the explosion proofness prose) | AMC E 80(1) prose; **Table 1** items 1, 2, 3 (Section 4), 5 (Section 8), 6 (Sections 7.2 and 7.3.1), 7 (Section 12, Category D), 8 (Section 11, Category F; prose adds paragraph 11.4.1 Spray Test), 9 (Section 14, Category S), 12 (Section 13, Category F), 13 (Section 4); **Table 2** items 14 (Section 5), 15 (Section 9), 16 (Section 6), 17 (Section 10 or MIL-STD-810 (RAIN); prose adds Category S), 19 (Sections 16 and 17). Prose also names DO-160D section 9 Environment I and Environment II. Note: `AMC E 80.md` names it once (l.30); the section/category detail lives only in the embedded crops | The actual test procedure, severity and pass criteria for 15 of the 19 environmental items | Every test condition. The note can say *that* a high-temperature or vibration demonstration is required and *what it is for*, but not what the test is | **No** — no `[VERIFY]` anywhere for ED-14 / DO-160 | **Blocking** |
| **MIL-E-5007** (written "Mil-E-5007" in the tables, "MIL-E-5007" in the prose) | **Table 1** item 1 (paragraph 4.6.2.2.5), item 2 (paragraph 4.6.2.2.7), item 3 (paragraph 4.6.2.2.6), item 4 (paragraph 3.7.3.3.2 Table X, fuel test only). Prose repeats 4.6.2.2.5, 4.6.2.2.7 and 4.6.2.2.6 as "historical specifications" | The alternative (historical) temperature and contaminated-fuel test procedures | Nothing that ED-14 / DO-160 does not already cover; it is offered as an alternative ("or"), and item 4's use is limited to the fuel test | **No** | **Limiting** |
| **MIL-STD-810** | **Table 1** item 7 (Sand and Dust, as alternative to DO-160 Section 12 Category D), item 9 (Salt Spray, as alternative to Section 14 Category S); **Table 2** item 16 (Humidity), item 17 (Waterproofness, "(RAIN)") | Alternative test procedures for sand/dust, salt spray, humidity and rain | The alternative route only. Sand and dust and salt spray matter for a rotorcraft, so the choice between the two standards is a real programme decision that cannot be made here | **No** | **Limiting** |
| **MIL-STD-704** | **Table 2** item 19 (Power Input, as alternative to DO-160 Sections 16 and 17) | The alternative aircraft electrical power characteristics standard for the power input test | The alternative route for the EEC power input qualification | **No** | **Limiting** |
| **AMC 20-1** | AMC E 80(2)(b) header prose; **Table 2** item 18 (EMI, HIRF & lightning); **Table 4** item 24 (Overheat for Engine electronic control systems) and its prose; AMC E 170 ("Additional means may be found in AMC E 80 or in AMC 20-1 and AMC 20-3 for Electronic Engine Control Systems"). Notes: `AMC E 80.md` (table row + `[VERIFY]`), `AMC E 170.md` (table row + `[VERIFY]`) | The *only* named acceptable test procedure for EMI, HIRF and lightning, and for Engine Control System overheat | For a full-authority EECS, the whole EMI/HIRF/lightning qualification and the overheat demonstration. AMC E 80 gives no alternative for item 18 — unlike every other item, it names no DO-160 section | Yes (both notes) | **Blocking** |
| **AMC 20-3** | Identical to AMC 20-1 above — the two are always cited as a pair | Same | Same | Yes (both notes) | **Blocking** |
| **ISO 2685** | AMC E 130(4)(a): "Acceptable procedures for calibration of the relevant burners for the tests, and the standard flame, are defined in the ISO 2685 standard." Notes: `AMC E 130.md` (table row, Compliance bullet, tag `iso-2685`) | Burner calibration and the standard flame for every CS-E 130 fire test | The flame temperature, heat flux and calibration procedure. The AMC requires a pre-test calibration "to verify that the standard flame temperature and heat flux is achieved" but the values live only in ISO 2685 | **No** — stated as a Statement row with no `[VERIFY]` | **Blocking** |
| **Certification Specifications for Propellers** | CS-E 140(f), alongside CS-E 180. Note: `CS-E 140.md`, recorded in `## Not applicable` | Propeller tests that may be run jointly with engine tests | Nothing — the sub-point is correctly cut as propeller material, and this engine drives a rotorcraft transmission | Not applicable (cut, recorded) | **Cosmetic** |

**Not found in this scope.** Several references named in the brief do not occur
anywhere in these 21 source files or 20 notes: AMC 20-6B, AMC 20-42, AMC 20-115,
`AMC1 21.A.3B(b)`, 21.A.33, 21.A.41, 21.A.61, 21.A.20(d) as such (only
21.A.20(d)2), the 'Icing Atmospheric Conditions' definition, CS 27.1093(b) /
CS 29.1093(b) / CS-27.45(f) / CS 29.45(f), CS-23, CS-25, CS-34, any FAA material
(FAR 33.87, AC 33.70-2, AC 33.70-3), ISO 12103-1, SAE and ASTM. The only CS-27/29
citation in scope is the combined **CS-27/29.1305** at AMC E 60(d)(3). The brief
also expected **CS-E 60(e)** to cite CS-27/29.1305; it does not — CS-E 60(e) is
the turbine cooling system instrumentation sub-point and names no other code. The
only ISO reference in scope is **ISO 2685**, not ISO 12103-1.

**In-CS-E but out-of-vault-scope pointers.** These are not external documents,
but they are dead ends for this reader because the target paragraph is excluded
and has no note: **CS-E 230** (AMC E 80 Table 1 item 11, induction icing),
**CS-E 350** (CS-E 140(d)(1), piston calibration test), **CS-E 440**
(AMC E 170, piston endurance test), **CS-E 180** (CS-E 140(f), propeller), and
**AMC E 150(a)** (CS-E 150(a), piston-only). All five are correctly recorded as
cuts or rendered as plain text, and in each case the applicable CS-E paragraph
for this engine is named in its place.

### Undeclared engine information

| Reference | Where | What it governs | What is blocked | Flagged? | Severity |
|---|---|---|---|---|---|
| **Maximum Engine Over-torque / Maximum Engine Over-speed / Maximum Exhaust Gas Over-Temperature — declared or not** | AMC E 60(d)(5), which turns on CS-E 820, CS-E 830 and CS-E 870. Note: `AMC E 60.md` `[VERIFY]` | Whether a genuine over-limit event with all engines operating counts as usage of the 30-Second or 2-Minute OEI rating | Whether the AMC E 60(d)(5) relief is available at all, and therefore whether the OEI recorder needs discrimination logic between an all-engines-operating over-limit event and OEI use. `engine_profile.md` records no over-limit ratings | Yes | **Blocking** |
| **Whether the EECS has a mechanical back-up** | AMC E 170, fourth example. Note: `AMC E 170.md` `[VERIFY]` | Whether an additional CS-E 170 test is needed for a back-up not normally exercised in the endurance test | One item of the CS-E 170 test programme. `engine_profile.md` declares "EECS / FADEC, full authority" but is silent on a back-up | Yes | **Limiting** |
| **Whether any approved degraded state of the Engine Control System exists** | AMC E 170: "due consideration should be given to dispatching in each approved degraded state". Note: `AMC E 170.md` `[VERIFY]` | Assessment of each approved degraded state against the environmental conditions | Whether this obligation has any content for this engine. Time-limited dispatch is not claimed (CS-E 1030 excluded), but the AMC's wording is broader than time-limited dispatch | Yes | **Limiting** |
| **The target rotorcraft / the installation** | CS-E 130(g)(1) (declaration route); AMC E 130(4)(b) (installation-analysis route for flame impingement); AMC E 170 (installer-specified environmental conditions, else "typical installation"); CS-E 100(b) (aircraft flight and ground loads); CS-E 80(b) (assumed installation conditions). Notes: `CS-E 130.md`, `AMC E 130.md`, `AMC E 170.md` all say the installation is not fixed | Several compliance *routes* that are only available once an installation is known | Which route the applicant takes, not whether the obligation exists. Choosing the AMC E 130(4)(b) installation-analysis route now would create a re-evaluation obligation for every future installation | Partly — stated in prose in three notes, no `[VERIFY]` | **Limiting** |
| **Whether a turbine starter with an external air or gas supply is fitted, and whether it is CS-E 20(a) or CS-E 20(c) equipment** | AMC E 80(4) and Table 5, written explicitly "relating to a turbine-starter having air or gas supplied from an external source". Note: `AMC E 80.md` | Which of the four containment categories applies, and therefore which of the Table 6 specifications a–e must be met | The whole high-energy rotor demonstration under CS-E 80(d). It also decides whether CS-E 80(b) or CS-E 80(c) governs the starter | **No** | **Blocking** |
| **The equipment list: which items are declared under CS-E 20(a) and which under CS-E 20(c)** | CS-E 80(a)(2), (b) and (c); AMC E 80(3) (the high output electrical generator example) | The split between equipment approved as an integral part of the engine and equipment accepted subject to the aircraft Type Certificate | Which of CS-E 80(b) and CS-E 80(c) applies to each item, and which items need the weak link or an alternative means of disconnect | **No** | **Blocking** |
| **The declared vibration environment, and whether it correlates to the DO-160 standards** | AMC E 80(2)(a), vibration: "Section 8 tests are appropriate **if** the equipment vibration environment can be correlated to the DO-160 standards" | Whether equipment vibration testing may follow DO-160 Section 8 or needs a specific unbalanced engine test | The choice between the two routes, and the scope of any unbalanced-engine test | **No** | **Limiting** |
| **The aircraft-supplied power range for the EEC** | AMC E 80(2)(b), power input. Note: `AMC E 80.md` names the dependency in `## Application to this engine` | The full range of power inputs the EEC and the HMU fuel shutoff solenoid must accommodate | The power input test specification. It is an installation assumption under CS-E 30(a) and a control system specification under CS-E 50(h) | Partly — named, no `[VERIFY]` | **Limiting** |
| **Whether a flammable fluid tank, and/or a firewall, is part of and attached to the engine** | CS-E 130(c) and AMC E 130(5) (tank fire test); CS-E 130(d) and AMC E 130(8) (firewall). Notes carry the obligations in full | Whether the 15-minute flammable fluid tank fire test and the firewall substantiation are in the programme at all | Two whole test/substantiation items. An engine-mounted oil tank triggers a Fireproof standard and the AMC E 130(5) test conditions; no attached tank removes both | **No** | **Limiting** |
| **Tank test parameters: minimum dispatchable quantity, minimum flight idle flow rate, maximum fluid temperature, normal working pressure** | AMC E 130(5) | The starting conditions of the flammable fluid tank fire test | The test conditions cannot be written down. The AMC gives the rule (no greater than minimum dispatchable quantity, maximum temperature, normal working pressure) but every value is engine data | **No** | **Limiting** |
| **Use of titanium alloys, magnesium alloys and abradable linings** | AMC E 130(3)(a)–(d) | Whether the titanium-fire, magnesium-fire and abradable-lining evaluations are required, and for which stages | Whether these three assessments are in the programme, and the per-stage scope of the abradable lining evaluation ("each fan, compressor and turbine stage which has an abradable lining") | **No** | **Limiting** |

### Notes on coverage

- **Could not check: the AMC E 80 figure crops.** Rule 6 puts the four tables
  into images, so the test standards, sections and categories in Tables 1–6 are
  not in the note's text layer. I read them from `work/paragraphs/AMC_E_80.txt`
  and confirmed the note's prose is consistent with it, but I cannot confirm the
  crops themselves show the right region — including whether anything on page 44
  is missing. That is the open MINOR above.
- **Could not check: DO-160 section numbers against DO-160.** The note does not
  restate them, so nothing to check. `Section 7 2` in the source (Table 1 item 6
  prose) is an extraction artefact of "Section 7.2"; the Table 1 entry itself
  reads "Sections 7.2 and 7.3.1" and the note does not reproduce either.
- **A judgement call I did not raise as a finding.** CLAUDE.md says a
  `## Not applicable` entry should "record the cut, never the content". Two
  entries in `CS-E 130.md` go further than that: the (c) entry names the
  "23.7 litres" threshold, and the (g)(2) entry enumerates "fail-safe mounting
  structure, 5-minute fire load case, shutdown load evaluation and 15-minute
  residual strength provisions". Both describe what the cut passages said. Read
  strictly that is over-recording; read practically, naming the provisions is
  what makes the cut identifiable, and pass 1 examined these same two entries and
  passed them. I am flagging the tension rather than counting it as a defect,
  because it is a rule-reading question for the vault owner, not an accuracy
  failure — nothing in either entry is wrong.
- **Did not run** `lint_vault.py`, `audit_cuts.py` or any other script, to stay
  read-only. Every recorded cut in scope was checked by hand against its source
  paragraph and each one removes text the source actually contains.

---

# Scope D

## Dead ends

### External documents

Twelve distinct external references appear in Subpart D. All of them are in
AMC E 510 and AMC E 515; the other fifteen paragraphs in the subpart defer to
nothing outside the five PDFs we hold. No CS-27/CS-29, CS-23/CS-25 (other than
AMC 25.1309), CS-34, CS-Definitions, AMC 20-series, EUROCAE/RTCA, ISO, MIL-STD or
ASTM reference occurs in a Subpart D source paragraph.

| Reference | Where | What it governs | What is blocked | Flagged? | Severity |
|---|---|---|---|---|---|
| AMC1 21.A.3B(b) | AMC E 510(3)(d)(iii), cited twice (general principle, and the Blades passage). Note: AMC E 510 | The definition of "unsafe condition" that the uncontained-debris criterion turns on | Whether a given release of debris "causes an unsafe condition", and therefore whether it counts as uncontained high-energy debris and a Hazardous Engine Effect. Also the blade-debris probability assessment, which is an assessment of the probability of *that* condition | Yes — `[VERIFY]` in AMC E 510 | **Blocking** |
| Part 21 (general) | AMC E 515(2)(a). Note: AMC E 515 | Establishes that an Engine Critical Part is a Critical Part "by definition, with regard to compliance with Part 21" | The Part 21 obligations that attach to a Critical Part beyond CS-E 515 itself | Partly — the AMC E 515 `[VERIFY]` names Part 21 but is written for point 21.A.3 specifically | **Limiting** |
| point 21.A.3 of Part 21 | AMC E 515(3)(d)(v)(4)(a). Note: AMC E 515 (Requirement row, Compliance bullet, `[VERIFY]`) | The corrective action required when a revised damage-tolerance risk assessment shows the CS-E 510(a)(3) objectives can no longer be met | What that corrective action is, who it is reported to and on what timescale. The trigger is clear and the note labels it `Required`; the action is not | Yes — `[VERIFY]` in AMC E 515 | **Blocking** |
| AMC 25.1309 of CS-25, "System Design and Analysis" | AMC E 510(5). Note: AMC E 510 `[VERIFY]` | Detailed description of safety-analysis technique | Nothing mandatory. Named as a source of detail, not as an obligation | Yes — grouped `[VERIFY]` in AMC E 510 | **Cosmetic** |
| "Systematic Safety", E Lloyd & W Tye, Taylor Young Limited | AMC E 510(5). Note: AMC E 510 `[VERIFY]` | Reliability/safety analysis textbook | Nothing mandatory | Yes — grouped `[VERIFY]` | **Cosmetic** |
| SAE/EUROCAE ARP4754A / EUROCAE ED-79A, "Guidelines for Development of Civil Aircraft and Systems" | AMC E 510(5). Note: AMC E 510 `[VERIFY]` | Development-assurance and system-development process | Nothing mandatory here, though it is the process standard an EECS development assurance argument would normally cite | Yes — grouped `[VERIFY]` | **Cosmetic** |
| SAE ARP 926A, "Fault/Failure Analysis Procedure" | AMC E 510(5). Note: AMC E 510 `[VERIFY]` | FMEA procedure detail | Nothing mandatory | Yes — grouped `[VERIFY]` | **Cosmetic** |
| SAE ARP 4761, "Guidelines and Methods for Conducting the Safety Assessment Process on Civil Airborne Systems and Equipment" | AMC E 510(5). Note: AMC E 510 `[VERIFY]` | FTA / dependence diagram / safety assessment method detail | Nothing mandatory | Yes — grouped `[VERIFY]` | **Cosmetic** |
| Carter, A.D.S., *Mechanical Reliability* (2nd ed.), Macmillan, 1986 | AMC E 510(5). Note: AMC E 510 `[VERIFY]` | Mechanical reliability textbook | Nothing mandatory | Yes — grouped `[VERIFY]` | **Cosmetic** |
| FAA AC 33.70-2, "Damage Tolerance of Hole Features in High Energy Turbine Rotors" | AMC E 515(3)(d)(v)(4)(a), cited twice — as a probabilistic-approach example and as a source of allowable design target risk (DTR) values. Note: AMC E 515 `[VERIFY]` | Worked probabilistic damage-tolerance approach for manufacturing anomalies in hole features, and the numerical DTR values | The allowable DTR value a predicted probability of Failure is compared against. Without it the probabilistic route cannot be closed numerically; the source says "Designs that satisfy the allowable values will be considered to be in compliance with the 'appropriate damage tolerance assessment' required by CS-E 515(a)" | Yes — `[VERIFY]` in AMC E 515 | **Blocking** for the probabilistic route; the deterministic route at (3)(d)(v)(4)(b) is self-contained and remains open |
| FAA AC 33.70-3, "Damage Tolerance for Material Anomalies in Titanium Life-Limited Turbine Engine Rotors" | AMC E 515(3)(d)(v)(4)(a). Note: AMC E 515 `[VERIFY]` | Worked probabilistic approach for hard alpha anomalies in titanium rotor components | The accepted treatment of hard alpha in titanium — one of the three material anomaly types (3)(d)(v)(2) names explicitly | Yes — `[VERIFY]` in AMC E 515 | **Limiting** |
| "published FAA ACs" (unnamed, addressing other specific materials and/or anomaly types) | AMC E 515(3)(d)(v)(4)(a). Note: not named | The allowable DTR values for materials and anomaly types other than the two ACs named | Which further ACs exist and apply to this engine's material set. The source's phrasing is open-ended; only two examples are given | No — the AMC E 515 `[VERIFY]` names the two ACs only, not the open class | **Limiting** |

### Undeclared engine information

| Reference (quantity) | Where | What it governs | What is blocked | Flagged? | Severity |
|---|---|---|---|---|---|
| Maximum period of flight expected with one engine inoperative | CS-E 525; AMC E 525(2). Note: CS-E 525 | The duration over which continued rotation must be shown acceptable — CS-E 525 fixes no number, it says "the maximum period of flight … in the flight conditions expected to occur with that Engine inoperative" | The continued-rotation demonstration cannot be scoped. Oil-out duration and unbalance-running duration both scale with it | Yes — `[VERIFY]` in CS-E 525 | **Blocking** |
| Maximum operating speed of the intended rotorcraft installation | AMC E 540(1). Note: AMC E 540 | Whether "the possibility of aircraft operation at speeds higher than 200 knots" arises at all, for the Extremely Remote bird-strike verification | Whether AMC E 540(1)'s extra consideration applies. CS-E 800 sets the rotorcraft bird speed as "the maximum airspeed for normal flight operations", so the same unknown also sets the CS-E 800 test condition | Yes — `[VERIFY]` in AMC E 540 | **Limiting** |
| Existence of a transient fuel icing threat assessment by the aircraft manufacturer | AMC E 560(4). Notes: AMC E 560, CS-E 560 | Which of the two AMC E 560(4) branches applies: assess the potential threat, or declare that no capability has been demonstrated | The choice is a certification-programme decision with an installation limitation attached; it cannot be made until the installation is known | Yes — `[VERIFY]` in AMC E 560 | **Limiting** |
| Whether any boost fluid (e.g. water methanol) is used | AMC E 560(1). Note: AMC E 560 | Whether "fuel" in CS-E 560 is to be read as covering other fluids | Whether the whole of CS-E 560(a) applies a second time to another fluid. The note has already cut this interpretation on the strength of the refrigerant-injection declaration, which does not cover it | Yes — `[VERIFY]`, but inside the cut record rather than in `## Application` | **Limiting** |
| Whether the starter is declared as part of the engine type design | CS-E 590. Note: CS-E 590 | Whether CS-E 590 binds at all; if not, the starter is equipment under CS-E 80(c) and CS-E 20(c) | The applicability of a whole paragraph | Yes — `[VERIFY]` in CS-E 590 | **Blocking** for CS-E 590 |
| The target rotorcraft / installation configuration | AMC E 520(c)(2)(3) and (c)(2)(7); AMC E 560(4); AMC E 510(3)(c). Notes: AMC E 520, AMC E 560 | Engine-model installation assumptions, the mutually-agreed model definition with the aircraft manufacturer, the transient fuel icing assessment, and the aircraft-component Failure rates the safety analysis assumes | Nothing can be closed with the installer. AMC E 520 says only "Because the rotorcraft installation target is not fixed, those assumptions should be treated as open" | Partly — stated in prose in AMC E 520, `[VERIFY]` only for the fuel-icing instance | **Limiting** |
| Relative power levels of the declared ratings — which rating produces maximum fuel demand | CS-E 560(a)(3). Note: CS-E 560 | The condition at which the fuel pump capacity margin is established | The pump-margin case cannot be identified. `engine_profile.md` gives rating *names* only, and CS-E 40(b)(3) establishes no ordering of power level | **No** — and worse, CS-E 560 asserts the answer ("the 30-Second OEI demand sets the pump capacity case"). See the MAJOR finding above | **Limiting** |
| Whether the engine supplies bleed air to the aircraft cabin | AMC E 510(3)(d)(iv) and (3)(e); CS-E 510(g)(2)(ii). Notes: CS-E 510, AMC E 510 | Whether the toxic-products Hazardous Engine Effect and the matching Major Engine Effect arise, and whether the installer must be given delivery rates and concentrations of toxic products "in the Engine bleed air for the cabin" | Whether an information deliverable to the installer exists. The notes carry the obligation without stating whether the configuration triggers it | **No** | **Limiting** |

### Notes on coverage

- Nesting of sub-point labels is not recoverable from the flat paragraph text, so
  citations such as `AMC E 515(3)(d)(v)(4)(a)` and `AMC E 510(3)(d)(iii)` were
  checked against the source's own internal cross-references (AMC E 515 itself
  writes "paragraph (3)(d)(v)(2) above") and by position within the extracted file.
  Where the source uses an unnumbered banner — AMC E 520's four separate banners,
  merged into one note under a `covers:` list — the note's composite labels
  ((c)(1)(2), (c)(2)(4), (d)(b)) are the note's own construction. They are
  internally consistent and consistent with the citing notes, but they are not
  labels the source prints, so `audit_cuts.py`'s weak label check is the only
  automated guard on them.
- The Amendment 7 before/after text was checked against `work/redline.json` only.
  `CS-E_Amendment_7.pdf` was not opened, per the brief's instruction not to use
  the PDFs. For AMC E 510 and CS-E 520 the reconstruction is unambiguous; for
  AMC E 515 the redline `before` field is empty for the `AMC E 515(3)(d)(v)` entry
  and the check ran against the `deleted` array of the `AMC E 515` entry, which
  contains the quoted sentences intact.
- Two claims rest on engineering classification rather than on source text and
  cannot be checked against `source/`: that a bifurcation strut fairing is a
  bypass-duct structure (AMC E 540's cut record) and that a turboshaft driving a
  rotorcraft transmission has no propeller (CS-E 510, CS-E 570). Both are the kind
  of judgement the applicability classification necessarily rests on, and neither
  is reported as a finding.

---

# Scope E1

## Dead ends

### External documents

Only three references to material outside the five source PDFs occur anywhere in
this scope — two of them inside the AMC E 670 contaminant table, which the note
carries as an image rather than as text.

| Reference | Where | What it governs | What is blocked | Flagged? | Severity |
|---|---|---|---|---|---|
| **point 21.A.33 of Part 21** | Cited in `AMC_E_650.txt` (15); quoted in `AMC E 650.md` — Requirement row **(15)** and `Amendment history` | Inspection of type design hardware. AMC E 650(15) limits that inspection "to only those pertinent Engine components and associated instrumentation that constitute the certification Engine test or the baseline tests supporting the validated analysis" | What the inspection itself consists of, and who performs it. AMC E 650(15) narrows a duty defined entirely in Part 21; the scope of the narrowing is clear, the duty being narrowed is not stated anywhere we hold | No | **Limiting** |
| **ISO 12103-1 A4 (Arizona test dust – coarse)** | `AMC_E_670.txt` (1)(a) contaminant table; in `AMC E 670.md` only inside the embedded image `AMC_E_670_p131.png` | Specifies the "prepared dirt" component of the solid contaminant, 2.11 g/1000 litre. The source reproduces the A4 size distribution (0–5 µm 9.25 %, 5–10 µm 10.25 %, 10–20 µm 14.5 %, 20–40 µm 25 %, 40–80 µm 29.5 %, 80–200 µm 11.5 %) | The material specification and preparation method behind the grade. The size distribution and quantity are given in full in the source, so the test can be specified; procurement and conformity of the dust cannot be settled from CS-E | No | **Cosmetic** |
| **US Dept of Agriculture Grading Standards SRA-AMS 180 and 251** | `AMC_E_670.txt` (1)(a), cotton linters row; in `AMC E 670.md` only inside the embedded image `AMC_E_670_p132.png` | Defines "Below 7 staple" for the cotton linters contaminant, 0.03 g/1000 litre | The physical size of the cotton linters. The quantity is given; the staple grading is not convertible to a length from anything we hold. This is the same gap that makes the note's "longest contaminant" claim unverifiable (see findings) | No | **Limiting** |

None of the reference classes the brief lists as candidates occurs in this
scope: no AMC 20-series document, no CS-Definitions, no CS-23/25/27/29/34, no
FAA material (FAR 33.87, AC 33.70-2/-3), no EUROCAE ED-14 / RTCA DO-160, no
MIL-STD, SAE or ASTM. Verified by pattern scan over all 22 source paragraph
files and all 22 notes.

Three named engineering methods are cited without any document behind them.
They are listed for completeness; none blocks anything, because the source
supplies the parameter it needs on the spot.

| Reference | Where | What it governs | What is blocked | Flagged? | Severity |
|---|---|---|---|---|---|
| **Goodman diagram** | `AMC_E_650.txt` (9)(a); `AMC E 650.md` row **(9)(a)** and `Compliance` | The representation of the endurance limit against combinations of mean and alternating stress | Nothing. The AMC says "usually represented on a Goodman diagram" — the method is named, not mandated | No | Cosmetic |
| **Modal Assurance Criterion (MAC)** | `AMC_E_650.txt` (14)(b)(i); `AMC E 650.md` prose, quoted | Mode-shape similarity within the domain of applicability of a validated analysis | Nothing. The source supplies the threshold itself: "a MAC value greater than 0.9 indicates there is close agreement between measured and calculated mode shapes" | No | Cosmetic |
| **Strouhal number / reduced frequency** | `AMC_E_650.txt` (14)(b)(i); `AMC E 650.md` prose | Aeroelastic characterisation for flutter within the domain of applicability | Nothing. The source gives the formula and every term: "k = ω.c/U, ω = frequency, c = component length in flow direction and U = flow velocity" | No | Cosmetic |

### Undeclared engine information

Every row below is a quantity or a decision that `engine_profile.md` does not
state and that a paragraph in this scope needs. The first eight are already
carried as `[VERIFY]` items in the notes; the last five are not.

| Reference (quantity) | Where | What it governs | What is blocked | Flagged? | Severity |
|---|---|---|---|---|---|
| **Engine installation attitude(s) in the intended rotorcraft** | CS-E 600(e), AMC E 600(e); notes `CS-E 600.md`, `AMC E 600.md` | The attitude in which every Subpart E test is normally run, and the justification owed for any departure | The test attitude cannot be fixed and no difference can be justified. "Installations" is plural, so one comparison per intended installation | Yes (both notes) | **Blocking** |
| **Whether a Maximum Engine Over-speed is declared under CS-E 830** | CS-E 650(b)(3); note `CS-E 650.md` | One of the three candidates for the upper vibration-survey speed | The survey ceiling cannot be computed, because the maximum of the three candidates cannot be taken | Yes | **Blocking** |
| **Maximum flight duration of the intended rotorcraft** | CS-E 670(b)(2), AMC E 670(1)(c); notes `CS-E 670.md`, `AMC E 670.md` | The period the fuel system must keep running after impending filter blockage is indicated — "at least half" of it | The duration of the post-indication demonstration cannot be set. Compounded by the specification saying "aeroplane" where the AMC says "aircraft", which CS-E does not settle | Yes (CS-E 670, referenced from AMC E 670) | **Blocking** |
| **Whether the rotorcraft has carbon fibre composite material fuel tanks** | AMC E 670(1)(a); note `AMC E 670.md` | Whether the carbon fibre rod entry (0.54 g/1000 litre, 0 to 2000 microns) is added to the contaminant batch | The contaminant specification cannot be finalised | Yes | **Limiting** |
| **Inclination range and the normal flight manoeuvre set** | CS-E 680; note `CS-E 680.md` | The bounds of the inclination and gyroscopic demonstrations — the paragraph names no angles and no load factors | Neither limb of CS-E 680 can be scoped; AMC E 680 puts the proof in flight test, which needs the aircraft | Yes | **Blocking** |
| **Whether compressor bleed air is to be declared suitable for direct cabin pressurisation or ventilation** | CS-E 690(b); note `CS-E 690.md` | Whether the purity tests of (b)(1) and the defect analysis of (b)(2) bind | Two elective test programmes cannot be scoped in or out | Yes | **Limiting** |
| **Whether a rotor locking means is incorporated in the type design** | CS-E 710, AMC E 710(1); notes `CS-E 710.md`, `AMC E 710.md` | Whether continued rotation is substantiated under CS-E 710 or under CS-E 525 | Two mutually exclusive evidence routes, one of which (25 locking operations, five-minute holds) is a physical test programme | Yes (CS-E 710, referenced from AMC E 710) | **Blocking** |
| **Whether approval is sought for a continuously operated ignition system** | CS-E 720(a); note `CS-E 720.md` | Whether CS-E 720(b) plus either (c) or (d) binds at all | The whole paragraph, and whether CS-E 780 icing compliance leans on it | Yes | **Limiting** |
| **The declared flight envelope** | CS-E 650(a) and (b), CS-E 700, AMC E 650(1) definition ("all airborne and ground conditions of operation to be approved, including start-up, shutdown and windmilling rotation in flight") | The range over which vibration characteristics must be acceptable, and the reference against which CS-E 700 compares every substantiated operating condition | The vibration survey cannot be bounded and the CS-E 700 excess-condition comparison has no reference. CS-E 700 is a pure comparison paragraph: without the envelope it states nothing testable | **No** | **Blocking** |
| **Maximum rotational speed permitted for each rating, per rotor module** | CS-E 650(b)(1) and (b)(2); note `CS-E 650.md` | The 103 % and 100 % survey speeds. The note maps each declared rating to the right tier, but the speeds themselves are absent | The numeric survey ceiling. The rating-to-tier mapping is settled; the speeds it multiplies are not | **No** | **Limiting** |
| **The most adverse inlet airflow distortion pattern declared by the applicant** | CS-E 650(e), AMC E 650(7); notes `CS-E 650.md`, `AMC E 650.md` | The distortion condition the survey must evaluate, and the test means used to produce it | The distortion part of the survey cannot be specified. AMC E 650(7) ties it to the air intake and crosswinds, which are installation items | **No** | **Limiting** |
| **Maximum declared jet pipe temperature** | CS-E 690(a)(1)(iii); note `CS-E 690.md` | The limit that permits rotational speed to be reduced while bleeds are in operation during the endurance test | Whether the speed reduction is needed, and by how much | **No** | Cosmetic |
| **The "significant response" threshold previously agreed with the Agency** | AMC E 650(1) definition: "a vibratory stress exceeds the level that has been previously agreed by the Agency as providing acceptable margin under CS-E 70 and CS-E 100 for the type of feature concerned" | What counts as a significant response, and therefore what triggers the dwell testing of AMC E 650(10) inside the CS-E 740(g)(1) incremental periods and the CS-E 740(i) strip inspection | The dwell-test trigger. The definition is circular without the agreed level, and the level lives in an agreement, not in any document we hold | **No** | **Blocking** |

Two further items are applicant deliverables rather than declared configuration,
and are named here because a test in this scope is written against them: the
**Engine operating instructions** that specify how the stopping and locking means
is operated (CS-E 710 makes the manual procedure part of the test specification),
and the **normal / maximum working / maximum possible pressures** per part
(AMC E 640(1) defines them but the values are design output, and the maximum
possible pressure depends on a completed CS-E 510 Failure classification).

### Notes on coverage

- **Two AMCs in this scope are excluded, and the CS paragraphs they serve have no
  accepted means left.** `AMC_E_660.txt` is banner-titled "AMC E 660 Fuel Pump
  Tests (Turbine Engines for Aeroplanes)" and `AMC_E_700.txt` "AMC E 700 Excess
  Operating Conditions (Turbine Engines for Aeroplanes)"; both are EXCLUDED in
  `work/applicability.md` and rendered as plain text by `CS-E 660.md` and
  `CS-E 700.md`, which state the consequence explicitly. This is not an external
  dead end — the material is in the Amendment 8 PDF — but it is a real one: for
  CS-E 660 the substantiation method, and for CS-E 700 the comparison method,
  rest on nothing but agreement with the Agency.
- **Four Agency-agreement dead ends** sit inside otherwise complete notes and
  cannot be closed from any document: the "more accurate or additional
  corrections … agreed or required by the Agency" escape in AMC E 620(1); the two
  speed reductions of AMC E 650(4)(b); the instrumentation waiver of
  AMC E 650(12); and the agreed cleaning method and intervals of CS-E 600(d).
  Each is correctly represented in its note as conditional on Agency agreement.
- **Image-carried content was not text-verified.** The contaminant table
  (AMC E 670(1)(a)), the AMC E 650(1) definitions and the AMC E 620 correction
  formulae are embedded as EASA's own crops under accuracy rule 6, so the numbers
  inside them were checked against the extracted text of the paragraph file, not
  against the images themselves. The numeric-coverage scan reports those values
  as absent from the notes; that is expected and correct.
- `AMC E 650(4)(b)`'s "103 %" and the CS-E 650(b) tier numbers do not appear in
  the AMC note. That is rule 8 working as intended — CS-E 650 owns them — and is
  not counted as an omission.
- `scripts/lint_vault.py` and `scripts/audit_cuts.py` were not run, per the
  read-only constraint; all checks above were made by reading and by scans
  against `work/paragraphs/`, `work/redline.json` and `work/applicability.md`.

---

# Scope E2

## Dead ends

### External documents

| Reference | Where | What it governs | What is blocked | Flagged? | Severity |
|---|---|---|---|---|---|
| **CS-Definitions Amendment 2, 'Icing Atmospheric Conditions'** | Source CS-E 780(a)(2); note CS-E 780 lines 15, 31, 80, 101, 159 | Defines the supercooled liquid water conditions the engine must be shown to operate through in flight | The whole in-flight content of CS-E 780(a). No icing envelope, no test points, no analysis conditions can be stated | Yes — CS-E 780 lines 101–106 | **Blocking** |
| **CS 27.1093(b)** | Source CS-E 780(a)(2); note CS-E 780 lines 97, 103 | Rotorcraft (small) air-intake ice protection specification; supplies the *additional* applicable icing conditions | Which of ice crystal, supercooled large drop and snow conditions apply to this installation | Yes — CS-E 780 lines 101–106 | **Blocking** |
| **CS 29.1093(b)** | Source CS-E 780(a)(2); note CS-E 780 lines 97, 103 | Rotorcraft (large) equivalent of the above | Same; and which of CS-27 / CS-29 governs is itself undeclared | Yes — CS-E 780 lines 101–106 | **Blocking** |
| **CS 23.1093(b) (CS-23 until Amdt 4)** | Source CS-E 780(a)(2); note CS-E 780 line 166 | Aeroplane air-intake ice protection specification | Nothing for this engine — aeroplane code, named only because CS-E 780(a)(2) lists all four codes | No (named in `## Amendment history` only) | Cosmetic |
| **CS 23.2415 (CS-23 from Amdt 5)** | Source CS-E 780(a)(2); note CS-E 780 line 167 | The post-Amdt-5 CS-23 replacement for CS 23.1093(b) | Nothing for this engine; recorded because Amendment 7 introduced the distinction | No (Amendment history only) | Cosmetic |
| **CS 25.1093(b)** | Source CS-E 780(a)(2); note CS-E 780 lines 96, 154 | Large aeroplane air-intake ice protection specification | Nothing for this engine | No | Cosmetic |
| **FAR 33.87** | Source CS-E 740(c)(2)(iii); note CS-E 740 line 239 (`## Not applicable`) | Offers the FAA endurance schedule in place of the CS-E 740(c)(2) schedule where an en-route 30-minute OEI rating is sought | Nothing — 30-Minute OEI is not claimed and this engine tests under (c)(3), so the option does not arise. It would become **Blocking** if a 30-Minute OEI rating were later claimed | Recorded as a cut, no `[VERIFY]` | Cosmetic (conditional) |
| **ICAO Annex 5** | Source Appendix A note line 16–17; note Appendix A lines 42–43 | Justifies keeping altitude in feet in Tables A1–A4 | Nothing. A unit-consistency pointer only; the tables carry their own units | No, and none needed | Cosmetic |
| **Aerospace Industries Association Propulsion Committee Study, Project PC 338-1, June 1990** | Source Appendix A; note Appendix A lines 40–41 | The origin of the data in Tables A1 to A4 | Nothing for compliance. It would be needed only to question or extrapolate beyond the published tables — and Table A2 already states its own extrapolation basis | No | Cosmetic |
| **CS-E 810(a)** *(in-source, listed for completeness)* | Source CS-E 800(g)(2), AMC E 800(4)(f); notes CS-E 800 line 84, AMC E 800 lines 96, 108–114 | The blade-failure specification whose greater severity unlocks the single-large-bird waiver | Nothing — CS-E 810 is held, in scope and has its own note. Listed because AMC E 800 misstates the condition (see finding above) | n/a | n/a |

No reference to Part 21, the AMC 20 series, CS-34, FAA advisory circulars,
EUROCAE/RTCA, ISO, MIL-STD, SAE or ASTM occurs anywhere in the twenty source
paragraph files of this scope or in the fourteen notes. This was checked by
pattern search over both sets. The brief's expectation of AMC 20-6B is correct
that it is not here: it belongs to AMC E 930's neighbourhood, not to this scope.

### The in-vault dead end: AMC E 780

Not an external document, but the same kind of blockage and the largest one in
scope. `work/applicability.md` line 157 marks **AMC E 780 EXCLUDED**, on the
AMC's own words: "Specific provisions for rotorcraft Engines are currently not
included in this AMC. Until guidance has been established, the necessary
compliance method required for rotorcraft Engines should be agreed by the
Agency" [AMC E 780(1.7)]. CS-E 780 applies in full and points to "(See
AMC E 780)", so the specification is binding while its accepted means is, by its
own statement, unavailable. CS-E 780 lines 126–143 record this correctly,
including a `[VERIFY]` asking which general sections of AMC E 780 are usable by
agreement. Severity: **Blocking** — the compliance method for the whole of
CS-E 780 must be negotiated with EASA rather than read.

### Undeclared engine information

| Reference (quantity) | Where | What it governs | What is blocked | Flagged? | Severity |
|---|---|---|---|---|---|
| **Engine inlet throat area** | CS-E 790(a)(1)(i)/(ii); CS-E 800(b)(1)(ii), (c), (g)(8); notes CS-E 790 lines 102–104, CS-E 800 lines 131–134 | Selects the hailstone number and size, the large-bird mass tier, whether the CS-E 800(c) 2.5 m² gate is crossed, and becomes a published installation limitation | The hailstone count (one 25 mm stone, or 25 mm + 50 mm pairs per 0.0968 m²), the bird mass (1.85 / 2.75 / 3.65 kg), and the text of the CS-E 800(g)(8) installation limitation | Yes — the same `[VERIFY]` in CS-E 790 and CS-E 800 | **Blocking** |
| **Maximum airspeed for normal flight operations of the target rotorcraft** | CS-E 800(b)(1)(iv) and (f); note CS-E 800 lines 122–129 | The large-bird test speed, in place of the aeroplane's fixed 200 kt, and the upper bound on the impact evaluation speed | The single large bird test cannot be specified. Also decides whether AMC E 540's "above 200 knots" Extremely Remote consideration applies | Yes — CS-E 800 lines 126–129 | **Blocking** |
| **Placement of the additional 25 hours at 30-Minute Power** | AMC E 740(c)(2)(i)(a) with CS-E 740(c)(2)(i) and (c)(3)(i); notes CS-E 740 lines 212–218, AMC E 740 lines 143–147 | Whether the 25 hours sit inside the endurance test or run as a complementary test on the same article | The endurance test programme structure. This is the **single `[VERIFY]` recorded in `engine_profile.md`** | Yes, in both notes and in `engine_profile.md` | **Blocking** |
| **Maximum Power-turbine Speed for Autorotation, and the most critical gas generator conditions for that configuration** | CS-E 740(g)(4); note CS-E 740 lines 207–210 | 10 minutes of Part 4 in each of 25 stages — 250 minutes of running | The Part 4 content of every stage of the endurance schedule | Yes — CS-E 740 lines 207–210 | **Blocking** |
| **Whether each spool's maximum rotational speed can be obtained simultaneously at sea-level test bed conditions** | CS-E 740(f)(1) and AMC E 740(f)(1); note AMC E 740 lines 170–173 | Whether supplementary endurance testing to an agreed schedule is needed to substantiate higher speed limitations | Whether a whole supplementary test programme exists | Yes — AMC E 740 lines 170–173 | Limiting |
| **Whether the installation incorporates or requires an air intake protection device** | CS-E 790(d); CS-E 780(e) and (f)(3); CS-E 800(g)(5); note CS-E 790 lines 118–121 | Three separate provisions: the rain/hail waiver, the icing guard case, and the bird-test configuration | Whether the CS-E 790(d) waiver is available at all, and whether CS-E 800 must be demonstrated with the device functioning | Partly — CS-E 790 flags it and mentions the CS-E 780(e) guard; CS-E 800(g)(5) and CS-E 780(f)(3) carry no `[VERIFY]` | **Blocking** for CS-E 790(d), Limiting elsewhere |
| **Declared minimum engine carcass/oil temperature for starting; declared minimum oil temperature for Take-off Power selection; declared minimum and maximum starting torques** | CS-E 770(b) and (c); note CS-E 770 lines 74–77 | The four inputs to both low-temperature demonstrations | Neither CS-E 770 demonstration can be specified | Yes — CS-E 770 lines 74–77 | **Blocking** |
| **Target rotorcraft, and therefore CS-27 vs CS-29 as the installation code** | CS-E 780(a)(2) via CS-E 20(b); note CS-E 780 lines 95–99, deferring to CS-E 30 | Which ice protection specification supplies the additional icing conditions | Same as the CS 27/29.1093(b) rows above; this is the question that selects between them | Yes, by reference to the open item in CS-E 30 | **Blocking** |
| **Whether the applicant elects CS-E 790(b) or CS-E 790(a)(2)** | CS-E 790(b); AMC E 790(a)(2)(2)(d); note Appendix A lines 111–114 | Which rain and hail compliance route is flown | Whether Appendix A supplies the test input or only the baseline the 4 percent alternative is calibrated against | Yes — Appendix A lines 111–114. Note the mild tension: CS-E 790, AMC E 790 and CS-E 800 all treat (b) as the chosen route, while Appendix A records the choice as open | Limiting |
| **Whether a 10-minute Take-off Power Rating is sought** | CS-E 740(f)(4)(vi); note CS-E 740 line 117, carried as "Required if claimed" | Whether 10 minutes, rather than 5, of each 30-minute Take-off Power period runs at maximum oil temperature | The oil-temperature content of the Take-off Power periods | **No** — carried conditionally with no `[VERIFY]`, and `engine_profile.md` lists no such rating | Limiting |
| **Declared drainage period after a False Start** | CS-E 750(b), AMC E 750(b); note AMC E 750 lines 35–38 | When the normal start following each of the ten False Starts must be attempted | The False Start sequence timing | **No** — treated as an applicant declaration to be produced, no `[VERIFY]` | Limiting |
| **Maximum allowable bleed air and mechanical power extraction for aircraft use, and the approach-representative intermediate value** | CS-E 745(b)(1)–(3), CS-E 780(b); notes CS-E 745 line 55, AMC E 745 lines 64–67 | The three load conditions of the acceleration measurement, and the "most critical" icing bleed setting | The CS-E 745(b) test matrix and the CS-E 780(b) bleed configuration | **No** — CS-E 745 lists the declaration as a compliance item but raises no `[VERIFY]` | Limiting |
| **Whether rain/hail or bird compliance depends on an automatic protection system (continuous ignition, auto-relight, surge recovery)** | AMC E 790(a)(2)(5)(c)(vi); AMC E 800(4)(a); notes AMC E 790 lines 251–257, AMC E 800 lines 149–153, CS-E 790 lines 123–128 | Whether that system's availability becomes dispatch-critical | The dispatch-criticality entries feeding CS-E 510 and the CS-E 25 manuals | Partly — all three notes state the consequence conditionally; none raises a `[VERIFY]` | Limiting |
| **Declared minimum oil temperature for opening up from ground idle (warming up / taxying)** | AMC E 770; notes CS-E 770 lines 67–72, AMC E 770 lines 33–37 | An optional third declared temperature | Nothing mandatory — the declaration is elective. Undeclared, so its value and associated conditions are unknown | No, and none needed | Cosmetic |

### Notes on coverage

- **Not checked against the PDF.** As instructed, only `work/paragraphs/*.txt`
  was used. Figure content was therefore not read; the embeds were checked for
  existence in `vault/figures/` and all eleven in scope resolve.
- **AMC E 740(c)(4)** (503 lines, pages 151–172) was deliberately not walked: it
  is EXCLUDED in `work/applicability.md`, absent from AMC E 740's `covers:`, and
  the exclusion is now recorded. Nothing of its content leaks into any note in
  scope. CS-E 740(c)(4) in the CS paragraph was read only far enough to confirm
  that the note's cut records for (b)(1), (e)(1), (e)(2), (f)(2), (f)(4)(ii) and
  (g)(1) describe text the source really contains. They do.
- **A judgement call, reported as an observation rather than a finding.**
  Three rows in scope render "may be required" as `Statement` rather than
  `Permitted`: CS-E 780 line 35 [CS-E 780(d)] and AMC E 790 line 195
  [AMC E 790(a)(2)(5)(c)(vi)]. The seven-term table maps `may` → Permitted, but
  in these sentences the "may" governs what the Agency may require of the
  applicant, not what the applicant is permitted to do, and `Permitted` would
  read as a licence. The two notes are consistent with each other. Worth a rule
  decision rather than a per-note correction.
- **Ordering inside `## Not applicable`.** CS-E 740's five new cut records are
  appended after the existing entries (lines 246–251 follow the (g)(1) entry at
  245), so the section is no longer in source order. CLAUDE.md does not require
  an order there, so this is noted, not counted.
- `deck/compliance_matrix.xlsx` was not consulted; it is derived from the vault
  and would not be independent evidence.

---

# Scope E3

## Dead ends

### External documents

Two distinct references outside our five PDFs occur anywhere in this scope —
in the notes or in their source paragraphs. Nothing else in these 19 paragraphs
defers to a document we do not hold: there is no Part 21 point, no CS-Definitions
reference, no CS-27/CS-29/CS-23/CS-34 citation, no FAA material and no industry
standard. "The Agency" and "EASA" appear as the authority, not as documents.

| Reference | Where | What it governs | What is blocked | Flagged? | Severity |
|---|---|---|---|---|---|
| **AMC 25.903(e)(2)** | Cited in `AMC E 910(1)`: "AMC 25.903(e)(2) contains guidance that can be used to establish the objectives of the demonstration of compliance of the Engine with CS-E 910." Mentioned in `AMC E 910.md` (Requirement row `(1)`, and a `[VERIFY]`). | The *objectives* of the in-flight relight demonstration — what the relight envelope substantiation has to achieve. | The specific objective set for the CS-E 910 demonstration cannot be stated. The obligation itself is not blocked: `CS-E 910` states it, and `AMC E 910(2)` and `(3)` give an acceptable means (altitude or flight testing) and the two threats to cover. The reference is also aeroplane material, so its transfer to a rotorcraft relight case is itself unsettled. | **Yes** — `AMC E 910.md`: "[VERIFY: the reference AMC 25.903(e)(2) is aeroplane certification material, outside CS-E and outside the scope of this vault. AMC E 910(1) offers it for the objectives of the demonstration only. Whether an equivalent rotorcraft objective set is agreed with the Agency is an open item.]" | **Limiting** |
| **AMC 20-6B** (Appendix 1, Section 2.b) | Cited twice in `AMC E 930`: `(d)(1)(i)` "The applicant may combine the IMP test with the AMC 20-6B early ETOPS test (refer to Appendix 1, Section 2.b)" and `(d)(7)(i)` "The applicant may use a test performed as per AMC 20-6B (Appendix 1, Section 2.b), in lieu of a separate IMP test." Mentioned in `AMC E 930.md` only in `## Not applicable`. | The early ETOPS test that may be run in lieu of, or combined with, the CS-E 930 IMP test, demonstrating CS-E 930 and CS-E 1040 on one engine. | Nothing, for this engine. The route is an option, not an obligation, and it is unavailable here: ETOPS is an aeroplane operation and CS-E 1040 is outside the vault's scope. The IMP test of `AMC E 930(d)` is run on its own. | **No `[VERIFY]`, and correctly so** — the whole route is recorded as a cut in `AMC E 930.md` `## Not applicable`, one line, with the reason. | **Cosmetic** |

**`CS-E 25(b)(2)`, checked as asked, is not a dead end.** It is internal and we
hold it. `CS_E_25.txt` `(b)(2)` requires the airworthiness limitations section to
prescribe the mandatory post-flight inspections and maintenance actions
associated with any use of rated 30-Second or 2-Minute OEI Power, and requires
their adequacy to be validated by an in-service Engine evaluation programme.
`AMC_E_25.txt` `(d)(i)` and `(d)(ii)` then set out that programme in detail — it
is to be "approved by the Agency prior to certification", it compares in-service
hardware condition and power availability against the data from the
`CS-E 740(c)(3)(iii)` two-hour additional endurance test, and it is to include
scheduled or unscheduled service engine tests "imposing three applications of
30 seconds OEI rated power", with equivalent experience on engines of similar
design as an accepted alternative. `AMC E 25` cites no external document at all.
What remains open is not a missing document but the *extent* of the credit
`AMC E 930(d)(5)(iii)` offers: it says the IMP test results "may be used when
showing compliance with CS-E 25(b)(2) **for OEI power availability demonstration
at the end of the fixed Engine overhaul period**", which does not say whether the
in-service programme of `AMC E 25(d)` is displaced in part or only supplemented.
`AMC E 930.md` carries a `[VERIFY]` on whether the credit is claimed, but not on
how far it reaches.

### Terms used in the source and defined nowhere

A third kind of dead end appears twice in this scope: the vault cannot answer
because CS-E Amendment 8 uses a term it never defines. No external document is
named to go to, so there is nothing to fetch — the question can only be settled
with the Agency.

| Term | Where | What it governs | What is blocked | Flagged? | Severity |
|---|---|---|---|---|---|
| **"Maximum Engine Over-speed (20 Second)"** | `CS-E 870(b)(1)`: the 15-minute over-temperature run is made "at the maximum speed to be approved (excluding the Maximum Engine Over-speed (20 Second))". Confirmed to occur **exactly once** in the whole of `work/paragraphs/`, and nowhere in `CS-E 15`. | The upper bound on the speed at which the CS-E 870 test is run. | The test speed cannot be fixed. `CS-E 830` approves a Maximum Engine Over-speed for a rotating system with no 20-second qualifier, and `CS-E 830(b)(2)` uses "periods longer than 20 seconds" for a different purpose (the temperature basis). Whether the excluded quantity is the CS-E 830 over-speed, a 20-second transient of it, or a third thing is undecidable from the source. | **Yes** — `CS-E 870.md` carries a `[VERIFY]` that states the term occurs once, is defined nowhere, and that the relationship to CS-E 830 is to be agreed with the Agency. | **Blocking** |
| **"rotor-lock"** | `AMC E 910(3)(b)`, as the heading and throughout the sub-point. The AMC lists the assumptions the assessment must rest on but never defines the phenomenon. | The scope of the rotor-lock assessment required for the CS-E 910 relight demonstration. | What must be assessed cannot be bounded from the source. The five contributors are given and the list is expressly open ("include but are not limited to"), so the assessment's scope is the applicant's proposal. | **Yes** — `AMC E 910.md` states "**Rotor-lock** is not defined in AMC E 910, nor anywhere else in CS-E Amendment 8" and carries a `[VERIFY]` saying the mechanism it suggests is not in the source and the scope should be agreed with the Agency. | **Limiting** |

### Undeclared engine information

Fourteen quantities or elections that `engine_profile.md` does not state. Where
the note already carries a `[VERIFY]`, its file is named. `engine_profile.md`
holds exactly one `[VERIFY]` — the AMC E 740(c)(2)(i) 25 hours — and **no note in
this scope claims it holds any other**; the three notes that did so in pass 1
(`AMC E 850`, `CS-E 920`, `AMC E 930`) now say the profile does not record the
item.

| Quantity | Where it is needed | What it governs | What is blocked | Flagged? | Severity |
|---|---|---|---|---|---|
| **Target rotorcraft and its transmission** | `AMC E 850(4)(b)(ii)`, `AMC E 930(d)(2)(v)`, `CS-E 930`, `CS-E 910`, `CS-E 840(c)` | The installation the engine is substantiated against | The single largest gap in this third of Subpart E. Without it: the maximum oscillatory torque for the shaft torsional fatigue evaluation (only the ±5% floor is known); the inertial and torsional load specification for the IMP test rig; the predicted Engine flight cycle the whole CS-E 930 test plan rests on; the air-speed boundary of the relight envelope; and whether a complete loss of load on the power turbine is Extremely Remote. | **Yes**, in five notes: `AMC E 850`, `AMC E 930` (twice), `CS-E 930`, `CS-E 910`, `CS-E 840` | **Blocking** |
| **Whether a Maximum Engine Over-torque is sought** | `CS-E 820(a)` | Whether the CS-E 820 test is run at all | The over-torque test programme; and, with the two below, whether the `AMC E 60(d)(5)` usage-counting relief is available | **Yes** — `CS-E 820` | **Blocking** |
| **Whether a Maximum Engine Over-speed is sought, and for which rotating system** | `CS-E 830(a)` | Whether the CS-E 830 test is run | The over-speed test programme; the upper speed of the `CS-E 650(b)(3)` vibration survey; the margin `CS-E 810(b)(1)(i)` requires above it | **Yes** — `CS-E 830` | **Blocking** |
| **Whether a Maximum Exhaust Gas Over-temperature limit is claimed** | `CS-E 870(a)(1)` | Whether the CS-E 870 test is run | The over-temperature test programme and the `AMC E 40(d)(r)` declaration | **Yes** — `CS-E 870` | **Blocking** |
| **The maximum rating's steady-state operating temperature limit** | `CS-E 920(a)` | The datum the 42 °C (75 °F) margin is added to | The absolute temperature of the 5-minute test | **Yes** — `CS-E 920` | **Blocking** |
| **The 30-Second OEI Power rating operating temperature limit** | `CS-E 920(b)` | The datum the 19 °C (35 °F) margin is added to | The absolute temperature of the 4-minute test | **Yes** — `CS-E 920` | **Blocking** |
| **Transient speed stabilisation time on transition to 30-Second OEI power** | `AMC E 920(2)` | Whether "Maximum power-on rotor speed" is the steady-state or the transient rotor speed | The CS-E 920(b) test speed, if the time exceeds 3 seconds | **Yes** — `CS-E 920` | **Limiting** |
| **Whether the CS-E 510 analysis relies on turbine blade shedding for over-speed protection** | `CS-E 810(b)` | Whether the blade-shedding margin tests are required | The whole of CS-E 810(b), and the `AMC E 840(2)(d)` blade-shedding treatment of the (b)(3)/(b)(4) factors | **Yes** — `CS-E 810` | **Blocking** |
| **Engine layout: whether Engine Critical Parts or combustion system components sit outside the compressor or turbine rotor casings** | NOTE under `AMC E 810(2)(b)` | Whether the internal-penetration assessment is needed alongside radial containment | The scope of the containment test assessment | **Yes** — `AMC E 810` | **Limiting** |
| **Whether turbine cooling system instrumentation is provided, or which `CS-E 60(e)` escape is claimed** | `CS-E 860(b)`, `CS-E 60(e)` | Whether the CS-E 860(b) evidence route is exercised | The endurance-running or calculation evidence package, and the cockpit indications declared under CS-E 20(d) | **Yes** — `CS-E 860` | **Limiting** |
| **Which shaft elements, if any, rely on `CS-E 850(a)(3)` rather than the fail-safe objective** | `CS-E 850(a)(3)`, `(b)(2)(i)` | Whether shaft elements become Engine Critical Parts | The CS-E 515 Engineering, Manufacturing and Service Management plans for those elements | **Yes** — `CS-E 850` | **Blocking** |
| **Whether an EECS-FADEC over-speed protection function is claimed as the means of over-speed control** | `AMC E 850(2)(a)`, `AMC E 840(5)` | The over-speed limiting mechanism relied on after a shaft failure or loss of load | The Failure rate and independence case under CS-E 50, and the loss-of-load over-speed value feeding CS-E 840(c) | **Yes** — `AMC E 850` | **Blocking** |
| **Assumed cumulative OEI rating usage between maintenance events** | `AMC E 930(d)(1)(i)` | The OEI content of the IMP test cycle | The IMP test cycle definition, and its consistency with the `CS-E 60(d)` recording provisions and the `CS-E 25(b)(2)` post-flight regime | **Yes** — `AMC E 930`, `CS-E 930` | **Blocking** |
| **The form of the IMP: fixed overhaul period, on-condition, or hard-time — and whether the `CS-E 25(b)(2)` credit is claimed** | `AMC E 930(a)(2)`, `(d)(5)(iii)`, `(e)` | Which route through AMC E 930 is taken | Whether the `AMC E 930(e)` simplified route applies, and whether the OEI power availability demonstration must be planned into the test cycle | **Yes** — `CS-E 930`, `AMC E 930` | **Limiting** |

### Notes on coverage

- **What I could not check.** Nothing in this scope required the PDF. All 19
  paragraphs are plain text with no figure or table:
  `work/paragraph_index.csv` records `has_figure_or_table = no` for all of them,
  and no note in this scope embeds an image. There is therefore no figure
  ownership question here.
- **Excluded paragraphs referenced as plain text.** `CS-E 1040` appears once, in
  `AMC E 930.md` line 261, inside the `## Not applicable` entry, as plain text
  and not as a wikilink — correct, since it has no note. `CS-E 880`, `CS-E 890`,
  `CS-E 900`, `CS-E 1030` are not referenced anywhere in this scope.
- **`work/paragraphs/` completeness.** `AMC E 820`, `AMC E 830` and `AMC E 870`
  each have a single source file covering a single sub-AMC
  (`AMC_E_820_a_2.txt`, `AMC_E_830_c.txt`, `AMC_E_870_a_3.txt`), each one
  sentence long. There is no other AMC material under CS-E 820, 830 or 870 in
  `work/paragraphs/`, so the three notes' claim "the only AMC material under
  CS-E 8x0" is confirmed against what we hold.
- **One cross-cutting pattern, not counted as a separate finding.** Three notes
  (`AMC E 830`, `CS-E 870`, `AMC E 870`) state the same wrong condition for the
  `AMC E 60(d)(5)` relief; the two notes that carry the relief accurately
  (`CS-E 820`, `CS-E 830`) both describe it as "conditioned on the limits
  established under CS-E 820, CS-E 830 and CS-E 870", which is right. The fix is
  the same sentence in three places, and it is worth making once and applying
  three times.

---

# Scope F

## Dead ends

Subpart F is the thinnest scope in the vault for statable content. CS-E 1010 is
one sentence that defers wholly to CS 34.1; CS-E 1020 is two sentences that defer
wholly to CS 34.2 for the thing being demonstrated; CS-E 1000 and AMC E 1000 do
nothing but set the status of those two and point at CS-34. Of the seven notes,
only CS-E 1050 and AMC E 1050 contain requirement substance that can be acted on
from the vault alone — and that pair is elective, and the election is not
declared.

### External documents

| Reference | Where | What it governs | What is blocked | Flagged? | Severity |
|---|---|---|---|---|---|
| **CS-34** (the standard as a whole) | Cited in source by CS-E 1000 ("depending on the specifications referenced under CS-34"), AMC E 1000 ("the specifications necessary at the engine level for compliance with CS-34"), AMC E 1020(1) and (2). Mentioned in notes `CS-E 1000`, `AMC E 1000`, `CS-E 1020`, `AMC E 1020`. | Whether Subpart F's fuel-venting and emissions paragraphs bind at all, and the amendment of the standard the type design is measured against. | Whether CS-E 1010 and CS-E 1020 are mandatory for this certification; whether CS-34 reaches a rotorcraft turboshaft at all; the amendment number that the AMC E 1020(1) TCDS note must name; what "the specifications necessary at the engine level" actually are. | **Yes** — `CS-E 1000` l.57-59, `AMC E 1000` l.56-57, `AMC E 1020` l.59-60. | **Blocking** |
| **CS 34.1** | Source: CS-E 1010, the only reference in the paragraph. Note `CS-E 1010`. | The fuel venting specifications themselves, and which of them are directed at the engine and which at the aircraft. | The entire substantive content of CS-E 1010. The paragraph states no venting limit, no condition, no test and no criterion; it states only *who complies with what is written elsewhere*. Also blocked: the split of the two limbs, hence what has to go into the CS-E 20(d) installation instructions and the CS-E 30 assumptions. | **Yes** — `CS-E 1010` l.57-59, which says so in terms ("This determines the whole content of CS-E 1010 for this engine"). | **Blocking** |
| **CS 34.2** | Source: CS-E 1020, the only reference in the paragraph. Note `CS-E 1020`. | The emission specifications the type design must comply with. | The pollutants, the limits, the operating cycle, the measurement points, the fuel, and the correction basis — none appears in CS-E. What CS-E 1020 does fix and the vault *can* state: the means (test, analysis, or a combination), the reference version ("in effect at date of Engine certification") and the recording duty. | **Yes** — `CS-E 1020` l.50-54 and l.62-65. | **Blocking** |
| **Engine type certificate data sheet (TCDS)** | Source: CS-E 1000 third sentence; AMC E 1020(1) gives the note's format. Notes: `CS-E 1000` l.36/43, `CS-E 1010` l.43, `CS-E 1020` l.42, `AMC E 1020` l.41, `CS-E 1050` l.29/45/68. | The certificate document in which Subpart F compliance is recorded. | Nothing substantive: AMC E 1020(1) supplies the emissions note format verbatim, and no other Subpart F note format is prescribed. The wording of a CS-E 1050 or CS-E 1010 TCDS note is not stated anywhere in the sources held. | No, and none needed for the emissions note. | **Cosmetic** |
| **ETOPS** (named as an example operation; the governing material is not named) | Source: AMC E 1000 ("particular aircraft operations such as ETOPS or Time Limited Dispatch"). Note `AMC E 1000` l.45-48. | An aircraft operational approval that would drive an engine configuration. | Nothing for this engine. ETOPS is an aeroplane operation, excluded by the scope rule, and CS-E 1040 is EXCLUDED with it. Named here only because the example explains why most of Subpart F is elective. | No VERIFY, correctly. | **Cosmetic** |
| **"Dispatch Deviation, or equivalents"** | Source: AMC E 1050(3). Notes `AMC E 1050` row (3) and l.53-55/63, `CS-E 1050` l.43. | Operator-side documents that may need amendment to carry the volcanic-cloud precautions. | Which document is meant, and what an "equivalent" is. The term appears **once in the entire paragraph corpus** (`grep -rn "Dispatch Deviation" work/paragraphs/` → one hit) and CS-E defines it nowhere. The obligation is clear; its target document is not. | No. | **Limiting** |
| **The operator's "overall management system" / safety risk assessment** | Source: AMC E 1050, third sentence of paragraph 2. Note `AMC E 1050` row 4 and l.49-51/65. | The use the operator will put the information to, which sets what "readily usable" means. | What form and granularity make the information "readily usable … in preparing a safety risk assessment". The operating rules that define an operator's management system are outside CS-E entirely and are not named by the source, so the acceptance criterion for this deliverable cannot be derived. | No. | **Limiting** |

Second-order, recorded for completeness and **not counted** in the seven above:
`AMC E 1050` reaches external material through a vault-internal link. Its
l.76/79 point at `AMC E 80(2)(a)` for the sand-and-dust, salt-spray and
fluid-susceptibility qualification; AMC E 80(2)(a) Table 1 gives those items'
acceptable procedures as **EUROCAE ED-14 / RTCA/DO-160** and **Mil-E-5007**,
neither of which we hold. Verified present in `work/paragraphs/AMC_E_80.txt`.
The dead end belongs to AMC E 80's note, not to this scope, but an applicant
following the Subpart F chain arrives at it.

### Undeclared engine information

| Reference (quantity) | Where | What it governs | What is blocked | Flagged? | Severity |
|---|---|---|---|---|---|
| **Whether the applicant elects compliance with CS-E 1050** | `CS-E 1050` l.66-68, `AMC E 1050` l.69-70; CS-E 1000 makes it elective. | Whether the only substantive Subpart F work in scope is done at all. | Everything in CS-E 1050 and AMC E 1050 — two specifications, four AMC points, a susceptibility assessment, an operator-facing documentation package and a TCDS note. `engine_profile.md` records CS-E 1030, CS-E 1040, CS-E 880, CS-E 890, CS-E 180 and CS-E 900 as excluded but is silent on CS-E 1050. | **Yes** — `CS-E 1050` l.66-68. | **Blocking** (for this paragraph pair) |
| **Which other Subpart F paragraphs the applicant elects** | `CS-E 1000` Compliance item 1 ("Statement of which Subpart F paragraphs the applicant elects"). | The scope of the applicant's own Subpart F submission. | Whether any Subpart F declaration beyond the CS-34-driven pair is to be made. Answered for CS-E 1030 and CS-E 1040 by `engine_profile.md`; unanswered for CS-E 1050. | Partly — covered only through the CS-E 1050 VERIFY. | **Limiting** |
| **Target rotorcraft / intended installation** | CS-E 1010 second limb: "incorporate provisions enabling the aircraft in which it is intended to be installed to comply". `engine_profile.md` states only "Rotorcraft turboshaft, multi-engine installation". | Which CS 34.1 specifications are "directed at the aircraft", and what provisions the engine must carry for that aircraft. | The content of the aircraft-directed limb, hence part of the CS-E 20(d) installation instructions and the CS-E 30 assumptions. Even with CS 34.1 in hand, this limb cannot be closed without the installation. | **No.** `CS-E 1010`'s VERIFY covers CS 34.1 only; the installation dependency is not raised. | **Limiting** |
| **Date of engine certification** | CS-E 1020: "the emission specifications of CS 34.2 **in effect at date of Engine certification**"; AMC E 1020(2). | Which version of CS-34 the type design is assessed against, and the amendment number in the TCDS note. | The applicable CS-34 amendment, and therefore the note text of AMC E 1020(1). Distinct from the CS-34 dead end: even holding CS-34, the version is selected by a date that is not declared. | Partly — the notes flag the amendment number (`AMC E 1020` l.59-60), not the date that fixes it. | **Limiting** |
| **Declared fuel specification(s) under CS-E 560(a)(1)** | `CS-E 1020` l.50-54. Verified: CS-E 560(a)(1) requires each fuel specification "to be approved, including any additive … must be declared and substantiated". | Whether the declared fuel is an input to the emissions demonstration. | Whether the emissions work is constrained by, or constrains, the CS-E 560(a)(1) declaration. Neither CS-E 1020 nor AMC E 1020 names a fuel. | **Yes** — `CS-E 1020` l.50-54. | **Limiting** |
| **Whether the emissions demonstration is by test, by analysis or by a combination** | CS-E 1020 offers all three; nothing declares the choice. | The compliance-programme entry for CS-E 1020. | The compliance method and its evidence. Not blocked by any missing document — CS-E 1020 states the choice is the applicant's — only undeclared. | No. | **Limiting** |
| **Engine architecture: cooled turbine blades, bleed air, hydraulic and pneumatic systems** | AMC E 1050(1)(b)–(f): glassy deposits on hot section parts, "clogging of turbine blade cooling channels", "electrical, hydraulic and pneumatic systems". | Which of the six named susceptible-feature categories exist on this engine. | Whether each AMC E 1050(1) category is in play, and therefore the size of the susceptibility assessment. `engine_profile.md` declares ratings and systems relevant to applicability, not engine architecture. | No. | **Limiting** |

### What an applicant can and cannot determine from the vault alone

| Note | Can determine | Cannot determine |
|---|---|---|
| `CS-E 1000` | That Subpart F splits in two tiers; that CS-E 1010 and CS-E 1020 are the CS-34-driven pair; that everything else is elective at the applicant's request; that whatever is complied with appears as a TCDS note. | Whether the CS-34-driven pair is in fact mandatory here — the trigger is "the specifications referenced under CS-34", and CS-34 is not held. This is the hinge of the whole subpart and it is unresolvable from the vault. |
| `AMC E 1000` | Why the subpart exists and where its obligations originate: an aircraft operational approval, or CS-34. That neither named example operation applies to this engine. | What "the specifications necessary at the engine level for compliance with CS-34" are. The AMC asserts they exist and names no single one. |
| `CS-E 1010` | The structure only: two limbs, applied specification by specification, not a choice for the applicant; that the aircraft-directed limb makes its output installation information. | **Everything substantive.** No venting limit, no condition, no test, no acceptance criterion, and no way to sort CS 34.1's specifications into the two limbs. Compounded by the undeclared target rotorcraft. Of the seven notes this is the emptiest: the note is a correct description of a pointer. |
| `CS-E 1020` | Three things CS-E fixes and CS-34 does not: the means (test, analysis, or a combination — analysis alone is a route); the reference version, fixed at the certification date so later CS-34 amendments do not reach back; and that recording the data is a separate obligation from demonstrating compliance. | What is measured, against what limits, over what cycle, on what fuel, at what power settings. The demonstration's entire technical content. |
| `AMC E 1020` | The TCDS note format, in full and verbatim — this is the one deliverable in the CS-34 half of the subpart that the vault can supply complete. That type-design compliance and production-engine compliance are different questions. That a continuing assessment duty runs past certification for every later type-design change. | The amendment number the format needs, which is the one blank in an otherwise complete deliverable. Also, what a type-design change would have to be assessed *against*. |
| `CS-E 1050` | The full obligation: establish susceptibility, and provide the information in the relevant documentation. That the specification requires susceptibility to be *established*, not to be absent — a susceptible engine can comply. That no threshold, ash concentration or exposure duration is set. | Whether the applicant elects it at all. That is the only gap, and it is a declaration, not a document. |
| `AMC E 1050` | The most complete note in the scope. The means (experience, studies, analysis, and/or testing of parts, sub-assemblies or engines); the open-ended six-category feature list; that the assessment extends past ash to the cloud's gases and other chemicals; the four points to be considered; and the operator-facing output. | What "readily usable" means, because that is set by the operator's management system; which document "Dispatch Deviation, or equivalents" names; and which of the six feature categories this engine actually has. None of these blocks the obligation — they limit how far the compliance package can be specified. |

### Notes on coverage

- **Not checked, by instruction:** the PDF. All verification is against
  `work/paragraphs/*.txt`.
- **Change tagging.** All ten Subpart F rows in `work/paragraph_index.csv` carry
  `changed_in=none`, and all seven notes carry `changed_in: []` with no
  `## Amendment history` section — consistent. The `[Amdt. No.: E/1]` and
  `[Amdt. No. E/4]` markers in the source text are CS-E's own historic amendment
  numbering, not Amendment 7 or 8, so they correctly produce no tag. Worth
  recording: **CS-E 1010 carries no amendment marker at all** and no "(See AMC E
  …)" banner — it is the only paragraph in the scope with neither. `CS-E 1010`
  l.28 states both facts and both are correct.
- **Not a dead end, but adjacent to one:** CS-E 1030 / AMC E 1030 (Time Limited
  Dispatch) and CS-E 1040 (ETOPS) are held in `source/` and are simply EXCLUDED,
  so they are absent from the vault by decision rather than by missing document.
  If time-limited dispatch were later claimed, the vault would have no note for
  it, and AMC E 1030 is by far the longest paragraph in the subpart (pages
  253-261, with figures on four pages per the index). That is a scope
  consequence, not a dead end, and `engine_profile.md` already records it as
  "Re-openable later without affecting any other paragraph".
- **Not applicable sections.** None of the seven notes has one, and none should:
  no sub-point in Subpart F is a turboshaft dead end. Check 6 therefore returns
  nothing, and that is the correct result rather than an unchecked area.
- **Figures.** `work/paragraph_index.csv` marks no figure or table for any of the
  seven paragraphs. `work/applicability.md:291` mentions "FIGURE on p. 261" for
  the volcanic-cloud grouping; p. 261 also holds CS-E 1040 and the tail of
  AMC E 1030, which the index credits with figures on 258-261. Ownership is
  positional, so that figure belongs to AMC E 1030 (EXCLUDED), not to CS-E 1050.
  No embed is missing from either CS-E 1050 or AMC E 1050.
