# Phase 2 — Turboshaft applicability matrix

Every paragraph of Subparts A, D, E and F of CS-E Amendment 8, classified for a
**rotorcraft turboshaft** application. Subparts B and C (piston engines) are out of
scope per CS-E 10(c)–(d) and CLAUDE.md.

Each reason quotes or names the Amendment 8 text that decides the verdict. Where a
paragraph's core requirement applies but one sub-point does not, the verdict is
APPLIES and the sub-point is named. Where the whole paragraph exists only when an
engine variable is true, the verdict is CONDITIONAL.

## Summary

| Verdict | Count | Share |
|---|---:|---:|
| APPLIES | 128 | 88% |
| CONDITIONAL | 0 | 0% |
| EXCLUDED | 17 | 12% |
| **Total in scope** | **145** | |

33 of the 145 carry an amendment tag (see `changed_in` in `work/paragraph_index.csv`).

### Engine variables

All five variables in CLAUDE.md are still blank. Per that file, paragraphs that
depend on them are classified CONDITIONAL. Filling them in converts most of the
CONDITIONAL rows to APPLIES or EXCLUDED — the verdicts below name which variable
each row waits on.

| Variable | CONDITIONAL rows waiting on it |
|---|---:|

## Subpart A — General

45 paragraphs — 40 APPLIES, 0 CONDITIONAL, 5 EXCLUDED

| Paragraph | Title | Pages | Fig/Tab | Changed | Verdict | Reason |
|---|---|---|:--:|---|---|---|
| `AMC General` | — | 15 | — | — | **APPLIES** | General AMC pointer: 'AMC-20 may also provide acceptable means of compliance to the specifications in Book 1 of this CS-E.' No engine-type limit. |
| `CS-E 10` | Applicability | 15 | — | Amdt7 | **APPLIES** | '(d) The specifications of subparts A, D, E and F apply to Turbine Engines.' Sub-point (b), thrust-reverser approval, is not sought for a turboshaft. |
| `AMC E 10(b)` | Thrust Reversers | 15–16 | — | Amdt7 | **EXCLUDED** | Wholly about thrust reversers: 'If a thrust reverser is declared as being part of the Engine type design under CS-E 20(a), it should comply with all appropriate CS-E specifications.' A rotorcraft turboshaft has no thrust reverser. |
| `CS-E 15` | Terminology | 16–18 | — | — | **APPLIES** | Defines terms for '(b) All Engines' and '(c) Turbine Engines'; both cover a turboshaft. |
| `CS-E 20` | Engine Configuration and Interfaces | 18 | — | — | **APPLIES** | Engine configuration and interface declarations apply to every Engine; '(f) For Engines having one or more OEI Ratings' is OEI-conditional. |
| `AMC E 20` | Engine Configuration and Interfaces | 19 | — | — | **APPLIES** | Interface guidance for all Engines, and expressly cites 'recording of rotorcraft One Engine Inoperative data' as an aircraft-supplied resource. |
| `AMC E 20(f)` | Power Assurance Data for Engines with One or More OEI Powe | 20–21 | — | Amdt8 | **APPLIES** | OEI ratings are claimed (30-Second, 2-Minute, Continuous OEI), so '(1) For Engines having one or more OEI ratings, the applicant should provide in the instructions for installation the necessary Engine data' is live. |
| `CS-E 25` | Instructions for Continued Airworthiness | 21–22 | — | Amdt7 | **APPLIES** | ICA required for every Engine; '(b)(2) For Engines having 30-Second OEI and 2-Minute OEI power ratings' adds OEI-conditional content. |
| `AMC E 25` | Instructions for continued airworthiness | 22–27 | — | Amdt8 | **APPLIES** | ICA guidance for all Engines; its 30-Second/2-Minute OEI and 30-Minute Power passages are conditional on those ratings. |
| `CS-E 30` | Assumptions | 27 | — | — | **APPLIES** | States the assumptions underlying compliance; no engine-type restriction. |
| `AMC E 30` | Assumptions | 27–29 | yes | Amdt7 | **APPLIES** | Tabulates assumptions for all Engines; the listed 'Propeller or thrust reverser effects' row does not arise for a turboshaft. |
| `CS-E 40` | Ratings | 29–30 | — | Amdt7 | **APPLIES** | Ratings apply to every Engine; '(b)(3) Turbine Engines for multi-engined Rotorcraft' lists the rotorcraft OEI ratings, while '(b)(2) Turbine Engines for multi-engined aeroplanes' does not apply. |
| `AMC E 40` | Ratings | 30 | — | — | **APPLIES** | Short rating guidance with no engine-type restriction. |
| `AMC E 40(b)(3)` | and (b)(4) 30-Second OEI, 2-Minute OEI and 30- minute Powe | 30–31 | — | — | **APPLIES** | 30-Second and 2-Minute OEI are claimed: 'The 30-Second and 2-Minute OEI Power ratings are two separate ratings. However, they are associated in a combined structure of 2.5 minutes duration.' The 30-Minute Power provision at (7) also applies. 2½-Minute OEI and 30-Minute OEI are not claimed. |
| `AMC E 40(d)` | Operating Limitations | 31–33 | — | — | **APPLIES** | Operating-limitation list for all Engines; '(s) Maximum refrigerant flow rate (if applicable)' and the Reversible Pitch Propeller row are self-limiting. |
| `CS-E 50` | Engine Control System | 33–36 | — | — | **APPLIES** | Engine Control System specifications apply to every Engine; '(j) Engines having a 30-Second OEI Power Rating must incorporate means…' is rating-conditional. |
| `AMC E 50` | Engine Control System | 36–37 | — | — | **APPLIES** | Control-system guidance spanning hydromechanical through full-authority EECS architectures. |
| `AMC E 50(e)` | Rotor integrity | 37 | — | — | **APPLIES** | Rotor integrity guidance under CS-E 50; no engine-type restriction. |
| `AMC E 50(j)` | Controls - Engines having a 30-Second OEI Power Rating | 37–38 | — | — | **APPLIES** | 30-Second OEI is claimed — '(1) The 30-Second OEI rating is intended to provide a rotorcraft with a power reserve in the event of one Engine becoming inoperative', and CS-E 50(j) requires automatic availability and control of that rating. |
| `AMC to CS-E 50(l)` | Information system security protection | 38 | — | — | **APPLIES** | Information system security protection; no engine-type restriction. |
| `CS-E 60` | Provision for Instruments | 38–39 | — | — | **APPLIES** | Instrument provisions apply to every Engine; '(d) Rotorcraft turbine Engines having 30-Second and 2-Minute OEI Power Ratings must…' is rating-conditional but rotorcraft-specific. |
| `AMC E 60` | Provision for instruments | 39–40 | — | Amdt7 | **APPLIES** | Instrument guidance for all Engines; the thrust-reverser position indication case is cited only as an example. |
| `AMC E 60(d)` | Provision for instruments | 40–41 | — | — | **APPLIES** | 30-Second and 2-Minute OEI are claimed, so the usage-recording and alerting provisions apply: 'the 30-Second OEI power level is considered to be used whenever one or more of the operating limitations applicable to the 2-Minute OEI power…'. |
| `CS-E 70` | Materials and Manufacturing Methods | 41 | — | — | **APPLIES** | Materials and manufacturing methods; no engine-type restriction. |
| `AMC E 70` | Castings, Forgings, Welded Structures and Welded Component | 41–43 | — | — | **APPLIES** | Castings, forgings and welded structures; no engine-type restriction. |
| `CS-E 80` | Equipment | 43–44 | — | — | **APPLIES** | Equipment specifications; no engine-type restriction. |
| `AMC E 80` | Equipment | 44–50 | yes | — | **APPLIES** | Equipment guidance; no engine-type restriction. |
| `CS-E 90` | Prevention of Corrosion and Deterioration | 50 | — | — | **APPLIES** | Prevention of corrosion and deterioration; no engine-type restriction. |
| `CS-E 100` | Strength | 50 | — | — | **APPLIES** | Strength; no engine-type restriction. |
| `CS-E 110` | Drawings and Marking of Parts – Assembly of Parts | 50–51 | — | — | **APPLIES** | Drawings, marking and assembly of parts; no engine-type restriction. |
| `CS-E 120` | Identification | 51 | — | Amdt7 | **APPLIES** | Identification; no engine-type restriction. |
| `CS-E 130` | Fire Protection | 51–52 | — | — | **APPLIES** | Fire protection; no engine-type restriction. |
| `AMC E 130` | Fire Protection | 53–59 | — | Amdt8 | **APPLIES** | Fire-protection guidance for all Engines; the propeller-feathering mention is one illustrative case. |
| `CS-E 135` | Electrical Bonding | 59 | — | — | **APPLIES** | Electrical bonding; no engine-type restriction. |
| `AMC E 135` | Electrical Bonding | 59–60 | — | — | **APPLIES** | Electrical bonding guidance; no engine-type restriction. |
| `CS-E 140` | Tests - Engine Configuration | 60 | — | — | **APPLIES** | Test engine configuration applies to every Engine; '(f) … the combined Engine and Propeller tests required by CS-E 180' does not arise for a turboshaft. |
| `AMC E 140` | Test - Engine configuration | 60–61 | — | — | **APPLIES** | Test configuration guidance; no engine-type restriction. |
| `CS-E 150` | Tests - General Conduct of Tests | 61 | — | — | **APPLIES** | General conduct of tests; no engine-type restriction. |
| `AMC E 150(a)` | Tests - General conduct of tests | 61 | — | — | **EXCLUDED** | Piston only. The whole body is one sentence, "For piston Engines, where the operating conditions of a test represent Maximum Continuous Power at altitude, a higher grade fuel or any other approved anti-detonant may be used". A turboshaft does not detonate, so nothing in it reaches this engine. CS-E 150(a) therefore has no applicable AMC. |
| `CS-E 160` | Tests - History | 61 | — | Amdt7 | **APPLIES** | Test history recording; no engine-type restriction. |
| `CS-E 170` | Engine Systems and Component Verification | 61–62 | — | — | **APPLIES** | Engine systems and component verification; no engine-type restriction. |
| `AMC E 170` | Engine systems and component verification | 62–63 | — | — | **APPLIES** | Systems and component verification guidance, including the EECS mechanical back-up case. |
| `CS-E 180` | Propeller Functioning Tests | 63–64 | — | — | **EXCLUDED** | Propeller-only: '(a) If approval of the Engine for use with a Variable Pitch Propeller is sought by the Applicant, a sufficient portion of the tests prescribed in CS-P must be made'. A rotorcraft turboshaft drives a rotor, so no propeller approval is sought. |
| `AMC E 180` | Propeller Functioning Tests | 64 | — | — | **EXCLUDED** | Serves CS-E 180: 'For Propeller approval the remaining tests of CS-P may be conducted on another Engine of the same type.' Not applicable without a propeller. |
| `CS-E 190` | Engines for Aerobatic Use | 64–65 | — | — | **EXCLUDED** | Aeroplane-only: 'Where approval is sought for an Engine intended for use in an aeroplane for which the Flight Manual will approve aerobatics or semi-aerobatic flight'. |

## Subpart D — Turbine Engines: Design and Construction

21 paragraphs — 20 APPLIES, 0 CONDITIONAL, 1 EXCLUDED

| Paragraph | Title | Pages | Fig/Tab | Changed | Verdict | Reason |
|---|---|---|:--:|---|---|---|
| `CS-E 500` | Functioning | 81 | — | — | **APPLIES** | Functioning specifications for turbine Engines; no engine-type restriction. |
| `AMC E 500` | Functioning - Control of Engines (Turbine Engines for Aero | 81 | — | — | **EXCLUDED** | Aeroplane-only by its own title: 'Functioning - Control of Engines (Turbine Engines for Aeroplanes)'. |
| `CS-E 510` | Safety Analysis | 81–83 | — | — | **APPLIES** | Safety analysis required for every turbine Engine; the refrigerant-injection and propeller items are listed only 'where applicable'. |
| `AMC E 510` | Safety analysis | 83–91 | — | Amdt7 | **APPLIES** | Safety-analysis guidance, expressly contemplating rotorcraft: 'this assumption may be revisited during aircraft certification, particularly multi-Engine rotorcraft certification.' |
| `CS-E 515` | Engine Critical Parts | 91 | — | — | **APPLIES** | Engine Critical Parts integrity specifications; no engine-type restriction. |
| `AMC E 515` | Engine Critical Parts | 91–106 | yes | Amdt7 | **APPLIES** | Critical-parts guidance with an explicit rotorcraft provision: 'For Rotorcraft turbine Engines, the representative usage of the 30-minute Power rating should be considered in the Engine Flight Cycle when establishing the Approved Life'. |
| `CS-E 520` | Strength | 106 | — | Amdt7 | **APPLIES** | Strength specifications; no engine-type restriction. |
| `AMC E 520(a)` | Strength - High Cycle Fatigue | 106 | — | — | **APPLIES** | High cycle fatigue guidance; no engine-type restriction. |
| `AMC E 520(c)(1)` | Strength - Shedding of Blades | 107 | — | — | **APPLIES** | Shedding of blades guidance; no engine-type restriction. |
| `AMC E 520(c)(2)` | Engine Model Validation | 107–108 | — | Amdt7 | **APPLIES** | Engine model validation guidance; no engine-type restriction. |
| `AMC E 520(d)` | Strength – Local Failures | 108 | — | — | **APPLIES** | Local failures guidance; no engine-type restriction. |
| `CS-E 525` | Continued Rotation | 108 | — | — | **APPLIES** | Continued rotation specifications; no engine-type restriction. |
| `AMC E 525` | Continued rotation | 109 | — | — | **APPLIES** | Expressly rotorcraft-relevant: 'Continued rotation can be either due to windmilling or due to mechanical effects such as clutch drag in the case of a multi-engined rotorcraft.' |
| `CS-E 540` | Strike and Ingestion of Foreign Matter | 109 | — | — | **APPLIES** | Strike and ingestion of foreign matter; no engine-type restriction. |
| `AMC E 540` | Strike and ingestion of foreign matter | 109–110 | — | — | **APPLIES** | Foreign-matter guidance; no engine-type restriction. |
| `CS-E 560` | Fuel System | 110–111 | — | — | **APPLIES** | Fuel system specifications; no engine-type restriction. |
| `AMC E 560` | Fuel System | 111–112 | — | — | **APPLIES** | Fuel system guidance; no engine-type restriction. |
| `CS-E 570` | Oil System | 112–114 | — | — | **APPLIES** | Oil system specifications apply to every turbine Engine; the propeller-feathering oil supply clause is prefixed 'When applicable'. |
| `AMC E 570` | Oil system | 114 | — | — | **APPLIES** | Oil system guidance; no engine-type restriction. |
| `CS-E 580` | Air Systems | 114 | — | — | **APPLIES** | Air systems; no engine-type restriction. |
| `CS-E 590` | Starter Systems | 114 | — | — | **APPLIES** | Starter systems; no engine-type restriction. |

## Subpart E — Turbine Engines: Type Substantiation

69 paragraphs — 61 APPLIES, 0 CONDITIONAL, 8 EXCLUDED

| Paragraph | Title | Pages | Fig/Tab | Changed | Verdict | Reason |
|---|---|---|:--:|---|---|---|
| `CS-E 600` | Tests - General | 115 | — | — | **APPLIES** | Test general specifications include a dedicated rotorcraft clause: '(e) Engines for Rotorcraft.' |
| `AMC E 600(e)` | Test - General | 115 | — | — | **APPLIES** | Rotorcraft-specific: 'The applicant should justify any difference between the Engine attitude during the tests and the Engine attitude in the intended rotorcraft installations.' |
| `CS-E 620` | Performance Correction | 115 | — | — | **APPLIES** | Performance correction; no engine-type restriction. |
| `AMC E 620` | Performance: Formulae | 116–117 | yes | — | **APPLIES** | Performance formulae; no engine-type restriction. |
| `CS-E 640` | Pressure Loads | 117–118 | — | — | **APPLIES** | Pressure loads; no engine-type restriction. |
| `AMC E 640` | Pressure Loads | 118–119 | — | — | **APPLIES** | Pressure-load guidance covering conditions 'likely to be encountered in service' including use of OEI ratings where claimed. |
| `CS-E 650` | Vibration Surveys | 119–120 | — | — | **APPLIES** | Vibration surveys required for every turbine Engine; no engine-type restriction. |
| `AMC E 650` | Vibration Surveys | 120–130 | yes | Amdt7 + Amdt8 | **APPLIES** | Vibration-survey guidance for all Engine architectures; the propeller and thrust-reverser installation features are listed 'Where appropriate'. |
| `CS-E 660` | Fuel Pressure and Temperature | 130 | — | — | **APPLIES** | Fuel pressure and temperature specifications; no engine-type restriction. |
| `AMC E 660` | Fuel Pump Tests (Turbine Engines for Aeroplanes) | 131 | — | — | **EXCLUDED** | Aeroplane-only by its own title: 'Fuel Pump Tests (Turbine Engines for Aeroplanes)'. |
| `CS-E 670` | Contaminated Fuel | 131 | — | — | **APPLIES** | Contaminated fuel specifications; no engine-type restriction. |
| `AMC E 670` | Contaminated Fuel Testing | 131–133 | yes | — | **APPLIES** | Contaminated fuel testing guidance; no engine-type restriction. |
| `CS-E 680` | Inclination and Gyroscopic Load Effects | 133 | — | — | **APPLIES** | Inclination and gyroscopic load effects; no engine-type restriction, and directly relevant to rotorcraft attitudes. |
| `AMC E 680` | Inclination and Gyroscopic Load Effects | 133 | — | — | **APPLIES** | Inclination and gyroscopic load guidance; no engine-type restriction. |
| `CS-E 690` | Engine Bleed | 133–134 | — | Amdt8 | **APPLIES** | Engine bleed specifications; no engine-type restriction. |
| `AMC E 690` | Engine bleed | 134 | — | Amdt8 | **APPLIES** | Engine bleed guidance; no engine-type restriction. |
| `CS-E 700` | Excess Operating Conditions | 134 | — | — | **APPLIES** | Excess operating conditions specifications; no engine-type restriction. |
| `AMC E 700` | Excess Operating Conditions (Turbine Engines for Aeroplane | 135 | — | — | **EXCLUDED** | Aeroplane-only by its own title: 'Excess Operating Conditions (Turbine Engines for Aeroplanes)', and its method is written around VMO / VNE. |
| `CS-E 710` | Rotor Locking Tests | 136 | — | — | **APPLIES** | Rotor locking tests; no engine-type restriction. |
| `AMC E 710` | Rotor locking tests | 136 | — | — | **APPLIES** | Rotor locking test guidance; no engine-type restriction. |
| `CS-E 720` | Continuous Ignition | 136–137 | — | — | **APPLIES** | Continuous ignition; no engine-type restriction. |
| `AMC E 720(a)` | Continuous Ignition | 137 | — | — | **APPLIES** | Continuous ignition guidance; no engine-type restriction. |
| `CS-E 730` | Engine Calibration Test | 137 | — | Amdt8 | **APPLIES** | Calibration test applies to every turbine Engine: 'thrust or power calibration curves of the test Engine must be established… up to the highest rated powers except for 30-Second and 2-Minute OEI Power ratings.' |
| `AMC E 730` | Calibration Tests | 137 | — | — | **APPLIES** | Calibration guidance; the 30-Second / 2-Minute OEI carve-out applies only where those ratings are claimed. |
| `CS-E 740` | Endurance Tests | 138–150 | — | Amdt8 | **APPLIES** | Endurance test applies, but per sub-paragraph: '(2)(i) Schedule for Standard Ratings with 2½-Minute OEI and/or Continuous OEI Rating and/or 30-Minute OEI Rating and/or 30-Minute Power' is the rotorcraft path, while '(c)(4) Alternate Endurance Testing – Turbofan Engine' is EXCLUDED and the turbo-propeller flight-propeller clause does not arise. |
| `AMC E 740(c)(2)(i)` | Endurance Tests – 30-Minute Power Rating | 150 | — | Amdt8 | **APPLIES** | 30-Minute Power is claimed: 'For Rotorcraft turbine Engines to be approved with a 30-Minute Power rating: (a) An applicant may propose either to include the required additional 25 hours within the…'. [VERIFY: the AMC offers a choice - include the additional 25 hours within the endurance test, or run them separately - and the selected option should be agreed with EASA.] |
| `AMC E 740(c)(3)` | Endurance Tests | 150–151 | — | Amdt8 | **APPLIES** | 30-Second and 2-Minute OEI are claimed, so CS-E 740(c)(3) and this AMC apply: '(2) Per CS-E 50(j), the Engine control should prevent exceedance of the speed limitation associated with the 30-Second OEI Power rating.' |
| `AMC E 740(c)(4)` | Alternate Endurance Testing – Turbofan Engine | 151–172 | yes | Amdt8 | **EXCLUDED** | Turbofan-only: 'The alternate endurance test is intended to address a problem faced by turbofan-Engine designs disadvantaged by the classic endurance test.' Excluded by the CLAUDE.md scope rule. |
| `AMC E 740(f)(1)` | Multi-spool Engines | 172–173 | — | — | **APPLIES** | Multi-spool engine endurance guidance; a free power-turbine turboshaft is multi-spool. |
| `AMC E 740(g)(1)` | Endurance Tests - Incremental Periods | 173 | — | — | **APPLIES** | Incremental endurance periods; no engine-type restriction. |
| `AMC E 740(i)(2)` | Endurance tests - Inspection checks | 173–174 | — | Amdt8 | **APPLIES** | Endurance inspection checks; no engine-type restriction. Renamed from AMC E 740(h)(2) and amended at Amendment 8. |
| `CS-E 745` | Engine Acceleration | 174–175 | — | — | **APPLIES** | Contains the rotorcraft acceleration case directly: '(2) For rotorcraft Engines, the power increases to rated Take-off when the power demand is increased from minimum test bed idle to rated Take-off'. |
| `AMC E 745` | Engine Acceleration | 175 | — | — | **APPLIES** | Defines the rotorcraft term: "The 'minimum test bed idle' which is referenced for rotorcraft Engines in CS-E 745(a)". |
| `CS-E 750` | Starting Tests | 175–176 | — | — | **APPLIES** | Contains a rotorcraft-specific clause: '(d) In the case of a free power-turbine Engine for Rotorcraft, each normal start must be made with the free power-turbine locked'. |
| `AMC E 750(b)` | Starting tests | 176 | — | — | **APPLIES** | Starting test guidance; no engine-type restriction. |
| `CS-E 770` | Low Temperature Starting Tests | 176 | — | — | **APPLIES** | Low temperature starting tests; no engine-type restriction. |
| `AMC E 770` | Low Temperature Starting Tests | 176 | — | — | **APPLIES** | Low temperature starting guidance; no engine-type restriction. |
| `CS-E 780` | Icing Conditions | 176–178 | — | Amdt7 | **APPLIES** | Icing specifications reference the rotorcraft certification bases directly: 'CS 27.1093(b), CS 29.1093(b)'. |
| `AMC E 780` | Icing Conditions | 178–194 | yes | Amdt7 | **EXCLUDED** | The AMC excludes itself: '(1.7) Compliance of Rotorcraft Engines with Icing Conditions — Specific provisions for rotorcraft Engines are currently not included in this AMC. Until guidance has been established, the necessary compliance method required for rotorcraft Engines should be agreed by the Agency.' [VERIFY: general sections may still be usable by agreement with EASA; confirm scope of the agreed method.] |
| `CS-E 790` | Ingestion of Rain and Hail | 194–196 | — | — | **APPLIES** | Provides a rotorcraft-only alternative: '(b) Engines for Rotorcraft – As an alternative to the specifications specified in CS-E 790(a)(2), but for rotorcraft turbine Engines only'. '(c) Engines for Supersonic Aeroplanes' does not apply. |
| `AMC E 790` | Rain and Hail Ingestion | 196 | — | — | **APPLIES** | Rain and hail ingestion guidance; no engine-type restriction. |
| `AMC E 790(a)(1)` | Rain and Hail Ingestion Certification for Design Changes a | 196 | — | — | **APPLIES** | Design change and derivative engine guidance; no engine-type restriction. |
| `AMC E 790(a)(2)` | Rain and Hail Ingestion – Turbine Engine Power/ Thrust Los | 196–209 | yes | — | **APPLIES** | Carries a dedicated rotorcraft section: '(d) Rotorcraft Turbine Engines — For rotorcraft applications, testing to the specifications of CS-E 790(a)(2) may be…'. The turbofan/turbojet aeroplane sub-cases do not apply. |
| `Appendix A` | Certification Standard Atmospheric Concentrations of Rain  | 210–212 | yes | — | **APPLIES** | Certification standard atmospheric concentrations of rain and hail, referenced by CS-E 790; no engine-type restriction. |
| `CS-E 800` | Bird Strike and Ingestion | 212–219 | yes | — | **APPLIES** | Bird ingestion sets a rotorcraft speed directly: '(iv) A bird speed of 200 knots for Engines to be installed on aeroplanes or the maximum airspeed for normal flight operations for Engines to be installed on Rotorcraft'. |
| `AMC E 800` | Bird Strike and Ingestion | 219–226 | yes | — | **APPLIES** | Names turboshaft explicitly: '(d) If turboprop or turboshaft Engines are tested using an alternative load device which could induce different Engine response characteristics'. |
| `CS-E 810` | Compressor and Turbine Blade Failure | 226 | — | Amdt7 | **APPLIES** | Compressor and turbine blade failure applies to every turbine Engine; the composite fan blade clause '(c)' applies only if such blades are fitted. |
| `AMC E 810` | Compressor and Turbine Blade Failure | 226–229 | — | Amdt7 | **APPLIES** | Blade failure guidance; the composite fan blade release method is one case within it. |
| `CS-E 820` | Over-torque Test | 229–230 | — | — | **APPLIES** | Over-torque test is written around power-turbine torque, which is the turboshaft load path; no engine-type restriction. |
| `AMC E 820(a)(2)` | Over-torque Test | 230 | — | — | **APPLIES** | 30-Second and 2-Minute OEI are claimed: 'it should be shown that an over-torque event does not compromise the ability of the Engine to reach its Rated 30-Second/2-Minute OEI Power.' |
| `CS-E 830` | Maximum Engine Over-speed | 230 | — | — | **APPLIES** | Maximum engine over-speed test; no engine-type restriction. |
| `AMC E 830(c)` | Maximum Engine Over-speed | 230–231 | — | — | **APPLIES** | 30-Second and 2-Minute OEI are claimed: 'it should be shown that an over-speed event does not compromise the ability of the Engine to reach its Rated 30-Second/2-Minute OEI Power.' |
| `CS-E 840` | Rotor Integrity | 231–232 | — | — | **APPLIES** | Rotor integrity; no engine-type restriction. |
| `AMC E 840` | Rotor Integrity | 232–235 | — | — | **APPLIES** | Rotor integrity guidance; no engine-type restriction. |
| `CS-E 850` | Compressor, Fan and Turbine Shafts | 235–236 | — | — | **APPLIES** | Compressor, fan and turbine shafts; directly relevant to a power-turbine shaft. |
| `AMC E 850` | Compressor, Fan and Turbine Shafts | 236–239 | — | — | **APPLIES** | Shaft guidance; no engine-type restriction. |
| `CS-E 860` | Turbine Rotor Over-temperature | 239 | — | — | **APPLIES** | Turbine rotor over-temperature; no engine-type restriction. |
| `CS-E 870` | Exhaust Gas Over-temperature Test | 239–240 | — | — | **APPLIES** | Exhaust gas over-temperature test; no engine-type restriction. |
| `AMC E 870(a)(3)` | Exhaust Gas Over-temperature Test | 240 | — | — | **APPLIES** | 30-Second and 2-Minute OEI are claimed: 'it should be shown that an over-temperature event does not compromise the ability of the Engine to reach its Rated 30-Second/2-Minute OEI Power.' |
| `CS-E 880` | Tests with Refrigerant Injection for Take-Off and/or 2½- M | 240–241 | — | — | **EXCLUDED** | Refrigerant injection is not used. The paragraph covers power augmentation only — '(b) … Refrigerant Injection Used to Increase ISA Take-off and/or 2½-Minute OEI Performance' and '(c) … Used to Restore ISA Take-off … at Higher Ambient Temperature'. This is not water ingestion, which is CS-E 790. 2½-Minute OEI is also not claimed. |
| `CS-E 890` | Thrust Reverser Tests | 241–242 | — | Amdt8 | **EXCLUDED** | Thrust reverser only: 'CS-E 890 is applicable to thrust reversers intended to be installed on turbine Engines.' A rotorcraft turboshaft has none. |
| `AMC E 890` | Thrust Reverser Tests | 242–243 | — | — | **EXCLUDED** | Serves CS-E 890 and is written around the thrust reverser used in the CS-E 740 test. Not applicable without a thrust reverser. |
| `CS-E 900` | Propeller Parking Brake | 243 | — | — | **EXCLUDED** | Propeller-only: 'If a Propeller parking brake is provided it must be operated 100 times during the endurance test.' |
| `CS-E 910` | Relighting In Flight | 243 | — | — | **APPLIES** | Relighting in flight; no engine-type restriction. |
| `AMC E 910` | Relighting In Flight | 244 | — | — | **APPLIES** | Relighting guidance; no engine-type restriction. |
| `CS-E 920` | Over-temperature Test | 244 | — | Amdt8 | **APPLIES** | Over-temperature test applies to every turbine Engine; the OEI-linked rotor speed values apply where those ratings are claimed. |
| `AMC E 920` | Over-temperature test | 245 | yes | Amdt8 | **APPLIES** | Over-temperature guidance; its '"Maximum power-on rotor speed" is normally the steady state rotor speed associated with the 30-Second OEI Power rating' applies where that rating is claimed. |
| `CS-E 930` | Initial Maintenance Programme Test | 245 | — | Amdt8 | **APPLIES** | Initial Maintenance Programme test, new at Amendment 8; no engine-type restriction. |
| `AMC E 930` | Initial Maintenance Programme Test | 245–251 | — | Amdt8 | **APPLIES** | IMP test guidance; the turbopropeller and thrust-reverser passages are case-specific, and the OEI cumulative-usage passage applies where OEI ratings are claimed. |

## Subpart F — Turbine Engines — Environmental and Operational Design Requirements

10 paragraphs — 7 APPLIES, 0 CONDITIONAL, 3 EXCLUDED

| Paragraph | Title | Pages | Fig/Tab | Changed | Verdict | Reason |
|---|---|---|:--:|---|---|---|
| `CS-E 1000` | General | 252 | — | — | **APPLIES** | Subpart F general specifications; no engine-type restriction. |
| `AMC E 1000` | Environmental and Operational Design Specifications - Gene | 252 | — | — | **APPLIES** | Explains that Subpart F defines design specifications required for particular aircraft approvals; no engine-type restriction. |
| `CS-E 1010` | Fuel Venting | 252 | — | — | **APPLIES** | Fuel venting; no engine-type restriction. |
| `CS-E 1020` | Engine Emissions | 252 | — | — | **APPLIES** | 'It must be demonstrated… that the Engine type design complies with the emission specifications of CS 34.2 in effect at date of Engine certification.' No engine-type carve-out in CS-E. |
| `AMC E 1020` | Engine emissions | 252–253 | — | — | **APPLIES** | Emissions note format and CS-34 assessment guidance; no engine-type restriction. |
| `CS-E 1030` | Time Limited Dispatch | 253 | — | — | **EXCLUDED** | Time-limited dispatch is not claimed. The paragraph is optional by its own wording: '(a) If approval is sought for dispatch with Faults present in an Electronic Engine Control System (EECS)…'. Re-openable later without affecting any other paragraph. |
| `AMC E 1030` | Time limited dispatch | 253–261 | yes | — | **EXCLUDED** | Serves CS-E 1030, which is not claimed. 'This AMC provides guidance for obtaining type design approval of engines with EECS in a degraded condition with respect to redundancy.' |
| `CS-E 1040` | ETOPS | 261 | — | — | **EXCLUDED** | ETOPS, excluded by the CLAUDE.md scope rule: 'In order to be approved for ETOPS capability, the engine shall achieve an IFSD rate that is compatible with the safety target associated to the maximum flight d[iversion time]'. ETOPS is an aeroplane operation. |
| `CS-E 1050` | Exposure to volcanic cloud hazards | 261 | — | — | **APPLIES** | Exposure to volcanic cloud hazards; no engine-type restriction. |
| `AMC E 1050` | Exposure to volcanic cloud hazards | 262 | — | — | **APPLIES** | Volcanic cloud guidance; no engine-type restriction. |

## Excluded paragraphs, grouped by reason

| Reason | Paragraphs |
|---|---|
| Aeroplane-only | `AMC E 500`, `AMC E 660`, `AMC E 700`, `CS-E 190` |
| ETOPS | `CS-E 1040` |
| No rotorcraft provisions in the AMC | `AMC E 1030`, `AMC E 150(a)`, `AMC E 780`, `CS-E 1030`, `CS-E 880` |
| Propeller | `AMC E 180`, `CS-E 180`, `CS-E 900` |
| Thrust reverser | `AMC E 10(b)`, `AMC E 890`, `CS-E 890` |
| Turbofan-only | `AMC E 740(c)(4)` |

## Topic grouping (reading order / MOC basis)

**58 topics.** Grouping rule: one or two CS paragraphs plus their AMCs
per topic. Each paragraph still gets its own note; this grouping drives the
map-of-content notes and the reading order. Every APPLIES paragraph appears in
exactly one topic — checked by this script. EXCLUDED paragraphs get no note;
they are listed in the exclusions MOC.

| Section | Topics |
|---|---:|
| Intro | 6 |
| A | 15 |
| D | 7 |
| E | 25 |
| F | 2 |
| Closing | 3 |
| **Total** | **58** |

| # | Section | Topic | Paragraphs | Note |
|---:|:--:|---|---|---|
| 1 | Intro | CS-E Amendment 8 for turboshaft engines — what this deck covers | — | Scope statement: Subparts A, D, E, F; rotorcraft turboshaft; 145 paragraphs; 13 excluded. |
| 2 | Intro | How CS-E is built: Book 1 and Book 2, Subparts A–F | `CS-E 10`, `AMC General` | Document map. CS = specification, AMC = accepted means. CS-E 10(d) is the scope anchor. |
| 3 | Intro | Glossary 1 — regulatory terms | `CS-E 15` | Extremely Remote, Remote, Reasonably Probable with their probability ranges; Hazardous / Major / Minor Engine Effect. |
| 4 | Intro | Glossary 2 — ratings for rotorcraft engines | `CS-E 40`, `AMC E 40` | Take-off, Maximum Continuous, and the rotorcraft OEI family. Defines every rating used later. |
| 5 | Intro | What changed at Amendment 7 — 16 in-scope paragraphs | — | Summary table only, from work/paragraph_index.csv. No requirement content. |
| 6 | Intro | What changed at Amendment 8 — 16 in-scope paragraphs | — | Summary table. Flag CS-E 930 and AMC E 930 as wholly new, and AMC E 740(c)(4) as new but out of scope. |
| 7 | A | Engine configuration and interfaces with the aircraft | `CS-E 20`, `AMC E 20` | Declared type design, interfaces, manuals. |
| 8 | A | Power assurance data for OEI engines | `AMC E 20(f)` | CONDITIONAL on OEI ratings. Changed at Amdt 8. |
| 9 | A | Instructions for Continued Airworthiness — the basics | `CS-E 25` | Airworthiness limitations section, mandatory actions. Changed at Amdt 7. |
| 10 | A | ICA — OEI post-flight actions and usage limits | `AMC E 25` | Split 1 of 1 of AMC E 25's OEI content. Point (6) added at Amdt 8. |
| 11 | A | Assumptions behind compliance | `CS-E 30`, `AMC E 30` | The interface assumptions table. Changed at Amdt 7. |
| 12 | A | OEI and 30-Minute Power ratings in detail | `AMC E 40(b)(3)` | CONDITIONAL on OEI ratings and 30-Minute Power. Rotorcraft-specific ratings. |
| 13 | A | Operating limitations to be declared | `AMC E 40(d)` | The limitation list, including refrigerant flow rate where fitted. |
| 14 | A | Engine Control System | `CS-E 50`, `AMC E 50`, `AMC E 50(e)`, `AMC to CS-E 50(l)` | Control modes, back-up, rotor integrity, information security. |
| 15 | A | 30-Second OEI control and instrument provisions | `AMC E 50(j)`, `CS-E 60`, `AMC E 60`, `AMC E 60(d)` | CONDITIONAL parts on 30-Second / 2-Minute OEI. CS-E 60(d) is rotorcraft-specific. AMC E 60 changed at Amdt 7. |
| 16 | A | Materials, corrosion, strength, marking and identification | `CS-E 70`, `AMC E 70`, `CS-E 90`, `CS-E 100`, `CS-E 110`, `CS-E 120` | Low-content paragraphs grouped. CS-E 120 changed at Amdt 7. |
| 17 | A | Equipment | `CS-E 80`, `AMC E 80` | Equipment specifications and their AMC. |
| 18 | A | Fire protection 1 — fire zones and materials | `CS-E 130`, `AMC E 130` | Split 1 of 2 of AMC E 130 (3,055 words). Changed at Amdt 8. |
| 19 | A | Fire protection 2 — flammable fluids, shut-off, fireproof test | `AMC E 130` | Split 2 of 2. Changed at Amdt 8. |
| 20 | A | Electrical bonding and test engine configuration | `CS-E 135`, `AMC E 135`, `CS-E 140`, `AMC E 140` | Note that CS-E 140(f) propeller joint tests do not apply. |
| 21 | A | Conduct of tests, test history, systems verification | `CS-E 150`, `CS-E 160`, `CS-E 170`, `AMC E 170` | CS-E 160 changed at Amdt 7. |
| 22 | D | Functioning | `CS-E 500` | Note that AMC E 500 is aeroplane-only and excluded. |
| 23 | D | Safety analysis 1 — failure classification and targets | `CS-E 510`, `AMC E 510` | Split 1 of 2 of AMC E 510 (3,482 words). Hazardous / Major / Minor Engine Effect. Changed at Amdt 7. |
| 24 | D | Safety analysis 2 — method, assumptions, multi-engine rotorcraft | `AMC E 510` | Split 2 of 2. Carries the rotorcraft certification assumption. |
| 25 | D | Engine Critical Parts 1 — what they are, integrity plan | `CS-E 515`, `AMC E 515` | Split 1 of 3 of AMC E 515 (5,836 words). Changed at Amdt 7. Figure on p. 93. |
| 26 | D | Engine Critical Parts 2 — Engine Flight Cycle and Approved Life | `AMC E 515` | Split 2 of 3. Carries the rotorcraft 30-Minute Power usage provision. |
| 27 | D | Engine Critical Parts 3 — damage tolerance and in-service management | `AMC E 515` | Split 3 of 3. |
| 28 | D | Strength, continued rotation, foreign matter, fuel, oil, air, starter | `CS-E 520`, `AMC E 520(a)`, `AMC E 520(c)(1)`, `AMC E 520(c)(2)`, `AMC E 520(d)`, `CS-E 525`, `AMC E 525`, `CS-E 540`, `AMC E 540`, `CS-E 560`, `AMC E 560`, `CS-E 570`, `AMC E 570`, `CS-E 580`, `CS-E 590` | Dense grouping of the remaining Subpart D design specifications. CS-E 520 and AMC E 520(c)(2) changed at Amdt 7. May split into two if it runs long. |
| 29 | E | Test general and performance correction | `CS-E 600`, `AMC E 600(e)`, `CS-E 620`, `AMC E 620` | CS-E 600(e) and AMC E 600(e) are the rotorcraft attitude provisions. |
| 30 | E | Pressure loads | `CS-E 640`, `AMC E 640` | Includes OEI rating conditions where claimed. |
| 31 | E | Vibration surveys 1 — what must be surveyed | `CS-E 650`, `AMC E 650` | Split 1 of 2 of AMC E 650 (4,886 words). Changed at BOTH Amdt 7 and Amdt 8 — the only such paragraph. |
| 32 | E | Vibration surveys 2 — domain of applicability and evaluation | `AMC E 650` | Split 2 of 2. Changed at Amdt 7 and Amdt 8. |
| 33 | E | Fuel condition, inclination and gyroscopic loads | `CS-E 660`, `CS-E 670`, `AMC E 670`, `CS-E 680`, `AMC E 680` | CS-E 680 is directly relevant to rotorcraft attitudes. Note AMC E 660 is aeroplane-only and excluded. |
| 34 | E | Engine bleed | `CS-E 690`, `AMC E 690` | Changed at Amdt 8. |
| 35 | E | Excess conditions, rotor locking, continuous ignition | `CS-E 700`, `CS-E 710`, `AMC E 710`, `CS-E 720`, `AMC E 720(a)` | Note AMC E 700 is aeroplane-only and excluded. |
| 36 | E | Engine calibration test | `CS-E 730`, `AMC E 730` | Changed at Amdt 8 — adds the CS-E 740(h) performance-target link. |
| 37 | E | Endurance test 1 — purpose and the rotorcraft schedule | `CS-E 740` | Split 1 of 3 of CS-E 740 (5,703 words). Changed at Amdt 8. |
| 38 | E | Endurance test 2 — OEI and 30-Minute Power schedules | `CS-E 740` | Split 2 of 3. The (c)(2)(i) rotorcraft schedule. Changed at Amdt 8. |
| 39 | E | Endurance test 3 — conduct, multi-spool, inspection checks | `CS-E 740`, `AMC E 740(f)(1)`, `AMC E 740(g)(1)`, `AMC E 740(i)(2)` | Split 3 of 3. AMC E 740(i)(2) renamed from (h)(2) and amended at Amdt 8. Figure on p. 172. |
| 40 | E | Endurance additions for 30-Minute Power and 30-Second OEI | `AMC E 740(c)(2)(i)`, `AMC E 740(c)(3)` | CONDITIONAL. Both changed at Amdt 8. |
| 41 | E | Acceleration and starting | `CS-E 745`, `AMC E 745`, `CS-E 750`, `AMC E 750(b)`, `CS-E 770`, `AMC E 770` | CS-E 745(a)(2), AMC E 745(3) and CS-E 750(d) are the rotorcraft and free power-turbine cases. |
| 42 | E | Icing conditions — and the rotorcraft AMC gap | `CS-E 780` | CS-E 780 applies and cites CS 27.1093(b) / CS 29.1093(b). AMC E 780 states it has no rotorcraft provisions — method must be agreed with EASA. Changed at Amdt 7. |
| 43 | E | Rain and hail 1 — the rotorcraft alternative | `CS-E 790`, `AMC E 790`, `AMC E 790(a)(1)` | CS-E 790(b) is a rotorcraft-only alternative to (a)(2). |
| 44 | E | Rain and hail 2 — test reduction and standard concentrations | `AMC E 790(a)(2)`, `Appendix A` | Split of AMC E 790(a)(2) (4,698 words) — rotorcraft section (d) only. FIGURES on pp. 199–201; render and read. |
| 45 | E | Bird strike 1 — rotorcraft bird speed and test matrix | `CS-E 800`, `AMC E 800` | Split 1 of 2. Rotorcraft speed is the maximum airspeed for normal flight operations, not 200 kt. FIGURE on p. 214. |
| 46 | E | Bird strike 2 — turboshaft load device and acceptance | `CS-E 800`, `AMC E 800` | Split 2 of 2. AMC E 800(d) names turboshaft engines directly. FIGURE on p. 220. |
| 47 | E | Compressor and turbine blade failure | `CS-E 810`, `AMC E 810` | Changed at Amdt 7. Composite fan blade clauses apply only if such blades are fitted. |
| 48 | E | Over-torque, over-speed and rotor integrity | `CS-E 820`, `CS-E 830`, `CS-E 840`, `AMC E 840` | Over-torque is the turboshaft power-turbine load path. |
| 49 | E | Shafts and over-temperature | `CS-E 850`, `AMC E 850`, `CS-E 860`, `CS-E 870` | Compressor, fan and turbine shafts; turbine rotor and exhaust gas over-temperature. |
| 50 | E | OEI capability after an over-limit event | `AMC E 820(a)(2)`, `AMC E 830(c)`, `AMC E 870(a)(3)` | CONDITIONAL on 30-Second / 2-Minute OEI. Three one-sentence AMCs with the same test. |
| 51 | E | Relighting and the over-temperature test | `CS-E 910`, `AMC E 910`, `CS-E 920`, `AMC E 920` | CS-E 920 and AMC E 920 changed at Amdt 8. |
| 52 | E | Initial Maintenance Programme test 1 — what it is | `CS-E 930`, `AMC E 930` | Split 1 of 2. NEW at Amdt 8 — CS-E 930 and AMC E 930 did not exist in Amendment 7. |
| 53 | E | Initial Maintenance Programme test 2 — build, cycle, evidence | `AMC E 930` | Split 2 of 2. NEW at Amdt 8. Covers OEI cumulative usage where those ratings are claimed. |
| 54 | F | Subpart F scope, fuel venting and emissions | `CS-E 1000`, `AMC E 1000`, `CS-E 1010`, `CS-E 1020`, `AMC E 1020` | CS-34 emissions compliance. |
| 55 | F | Volcanic cloud hazards | `CS-E 1050`, `AMC E 1050` | Note CS-E 1040 ETOPS is excluded. FIGURE on p. 261. |
| 56 | Closing | What does not apply, and why | — | The 13 EXCLUDED paragraphs grouped by reason: thrust reverser, propeller, turbofan-only, aeroplane-only, ETOPS, and the AMC E 780 rotorcraft gap. |
| 57 | Closing | Open items and engine variables to confirm | — | The five CLAUDE.md variables, every [VERIFY] raised, and the AMC E 780 / AMC E 1030 items needing EASA agreement. |
| 58 | Closing | Compliance matrix template | — | One row per in-scope paragraph: status, method (test / analysis / similarity), evidence document, owner. Exported as deck/compliance_matrix.xlsx in Phase 5. |

Paragraphs deliberately spread across more than one topic: `AMC E 130`, `AMC E 510`, `AMC E 515`, `AMC E 650`, `AMC E 800`, `AMC E 930`, `CS-E 740`, `CS-E 800`.
