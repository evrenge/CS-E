"""Phase 2 — proposed slide grouping for the turboshaft deck.

(section, title, [paragraph ids], note). Grouping rule from the task: one or two
CS paragraphs plus their AMCs per slide. Large AMCs are split across slides; the
`note` says why a slide exists or what it must carry.

Every APPLIES and CONDITIONAL paragraph appears on exactly one content slide.
EXCLUDED paragraphs are not covered individually — they are listed on the
exclusions slide in the closing section.
"""

PLAN: list[tuple[str, str, list[str], str]] = [
    # ------------------------------------------------------------------- Intro
    ("Intro", "CS-E Amendment 8 for turboshaft engines — what this deck covers", [], "Scope statement: Subparts A, D, E, F; rotorcraft turboshaft; 145 paragraphs; 13 excluded."),
    ("Intro", "How CS-E is built: Book 1 and Book 2, Subparts A–F", ["CS-E 10", "AMC General"], "Document map. CS = specification, AMC = accepted means. CS-E 10(d) is the scope anchor."),
    ("Intro", "Glossary 1 — regulatory terms", ["CS-E 15"], "Extremely Remote, Remote, Reasonably Probable with their probability ranges; Hazardous / Major / Minor Engine Effect."),
    ("Intro", "Glossary 2 — ratings for rotorcraft engines", ["CS-E 40", "AMC E 40"], "Take-off, Maximum Continuous, and the rotorcraft OEI family. Defines every rating used later."),
    ("Intro", "What changed at Amendment 7 — 16 in-scope paragraphs", [], "Summary table only, from work/paragraph_index.csv. No requirement content."),
    ("Intro", "What changed at Amendment 8 — 16 in-scope paragraphs", [], "Summary table. Flag CS-E 930 and AMC E 930 as wholly new, and AMC E 740(c)(4) as new but out of scope."),

    # --------------------------------------------------------------- Subpart A
    ("A", "Engine configuration and interfaces with the aircraft", ["CS-E 20", "AMC E 20"], "Declared type design, interfaces, manuals."),
    ("A", "Power assurance data for OEI engines", ["AMC E 20(f)"], "CONDITIONAL on OEI ratings. Changed at Amdt 8."),
    ("A", "Instructions for Continued Airworthiness — the basics", ["CS-E 25"], "Airworthiness limitations section, mandatory actions. Changed at Amdt 7."),
    ("A", "ICA — OEI post-flight actions and usage limits", ["AMC E 25"], "Split 1 of 1 of AMC E 25's OEI content. Point (6) added at Amdt 8."),
    ("A", "Assumptions behind compliance", ["CS-E 30", "AMC E 30"], "The interface assumptions table. Changed at Amdt 7."),
    ("A", "OEI and 30-Minute Power ratings in detail", ["AMC E 40(b)(3)"], "CONDITIONAL on OEI ratings and 30-Minute Power. Rotorcraft-specific ratings."),
    ("A", "Operating limitations to be declared", ["AMC E 40(d)"], "The limitation list, including refrigerant flow rate where fitted."),
    ("A", "Engine Control System", ["CS-E 50", "AMC E 50", "AMC E 50(e)", "AMC to CS-E 50(l)"], "Control modes, back-up, rotor integrity, information security."),
    ("A", "30-Second OEI control and instrument provisions", ["AMC E 50(j)", "CS-E 60", "AMC E 60", "AMC E 60(d)"], "CONDITIONAL parts on 30-Second / 2-Minute OEI. CS-E 60(d) is rotorcraft-specific. AMC E 60 changed at Amdt 7."),
    ("A", "Materials, corrosion, strength, marking and identification", ["CS-E 70", "AMC E 70", "CS-E 90", "CS-E 100", "CS-E 110", "CS-E 120"], "Low-content paragraphs grouped. CS-E 120 changed at Amdt 7."),
    ("A", "Equipment", ["CS-E 80", "AMC E 80"], "Equipment specifications and their AMC."),
    ("A", "Fire protection 1 — fire zones and materials", ["CS-E 130", "AMC E 130"], "Split 1 of 2 of AMC E 130 (3,055 words). Changed at Amdt 8."),
    ("A", "Fire protection 2 — flammable fluids, shut-off, fireproof test", ["AMC E 130"], "Split 2 of 2. Changed at Amdt 8."),
    ("A", "Electrical bonding and test engine configuration", ["CS-E 135", "AMC E 135", "CS-E 140", "AMC E 140"], "Note that CS-E 140(f) propeller joint tests do not apply."),
    ("A", "Conduct of tests, test history, systems verification", ["CS-E 150", "AMC E 150(a)", "CS-E 160", "CS-E 170", "AMC E 170"], "CS-E 160 changed at Amdt 7."),

    # --------------------------------------------------------------- Subpart D
    ("D", "Functioning", ["CS-E 500"], "Note that AMC E 500 is aeroplane-only and excluded."),
    ("D", "Safety analysis 1 — failure classification and targets", ["CS-E 510", "AMC E 510"], "Split 1 of 2 of AMC E 510 (3,482 words). Hazardous / Major / Minor Engine Effect. Changed at Amdt 7."),
    ("D", "Safety analysis 2 — method, assumptions, multi-engine rotorcraft", ["AMC E 510"], "Split 2 of 2. Carries the rotorcraft certification assumption."),
    ("D", "Engine Critical Parts 1 — what they are, integrity plan", ["CS-E 515", "AMC E 515"], "Split 1 of 3 of AMC E 515 (5,836 words). Changed at Amdt 7. Figure on p. 93."),
    ("D", "Engine Critical Parts 2 — Engine Flight Cycle and Approved Life", ["AMC E 515"], "Split 2 of 3. Carries the rotorcraft 30-Minute Power usage provision."),
    ("D", "Engine Critical Parts 3 — damage tolerance and in-service management", ["AMC E 515"], "Split 3 of 3."),
    ("D", "Strength, continued rotation, foreign matter, fuel, oil, air, starter", ["CS-E 520", "AMC E 520(a)", "AMC E 520(c)(1)", "AMC E 520(c)(2)", "AMC E 520(d)", "CS-E 525", "AMC E 525", "CS-E 540", "AMC E 540", "CS-E 560", "AMC E 560", "CS-E 570", "AMC E 570", "CS-E 580", "CS-E 590"], "Dense grouping of the remaining Subpart D design specifications. CS-E 520 and AMC E 520(c)(2) changed at Amdt 7. May split into two if it runs long."),

    # --------------------------------------------------------------- Subpart E
    ("E", "Test general and performance correction", ["CS-E 600", "AMC E 600(e)", "CS-E 620", "AMC E 620"], "CS-E 600(e) and AMC E 600(e) are the rotorcraft attitude provisions."),
    ("E", "Pressure loads", ["CS-E 640", "AMC E 640"], "Includes OEI rating conditions where claimed."),
    ("E", "Vibration surveys 1 — what must be surveyed", ["CS-E 650", "AMC E 650"], "Split 1 of 2 of AMC E 650 (4,886 words). Changed at BOTH Amdt 7 and Amdt 8 — the only such paragraph."),
    ("E", "Vibration surveys 2 — domain of applicability and evaluation", ["AMC E 650"], "Split 2 of 2. Changed at Amdt 7 and Amdt 8."),
    ("E", "Fuel condition, inclination and gyroscopic loads", ["CS-E 660", "CS-E 670", "AMC E 670", "CS-E 680", "AMC E 680"], "CS-E 680 is directly relevant to rotorcraft attitudes. Note AMC E 660 is aeroplane-only and excluded."),
    ("E", "Engine bleed", ["CS-E 690", "AMC E 690"], "Changed at Amdt 8."),
    ("E", "Excess conditions, rotor locking, continuous ignition", ["CS-E 700", "CS-E 710", "AMC E 710", "CS-E 720", "AMC E 720(a)"], "Note AMC E 700 is aeroplane-only and excluded."),
    ("E", "Engine calibration test", ["CS-E 730", "AMC E 730"], "Changed at Amdt 8 — adds the CS-E 740(h) performance-target link."),
    ("E", "Endurance test 1 — purpose and the rotorcraft schedule", ["CS-E 740"], "Split 1 of 3 of CS-E 740 (5,703 words). Changed at Amdt 8."),
    ("E", "Endurance test 2 — OEI and 30-Minute Power schedules", ["CS-E 740"], "Split 2 of 3. The (c)(2)(i) rotorcraft schedule. Changed at Amdt 8."),
    ("E", "Endurance test 3 — conduct, multi-spool, inspection checks", ["CS-E 740", "AMC E 740(f)(1)", "AMC E 740(g)(1)", "AMC E 740(i)(2)"], "Split 3 of 3. AMC E 740(i)(2) renamed from (h)(2) and amended at Amdt 8. Figure on p. 172."),
    ("E", "Endurance additions for 30-Minute Power and 30-Second OEI", ["AMC E 740(c)(2)(i)", "AMC E 740(c)(3)"], "CONDITIONAL. Both changed at Amdt 8."),
    ("E", "Acceleration and starting", ["CS-E 745", "AMC E 745", "CS-E 750", "AMC E 750(b)", "CS-E 770", "AMC E 770"], "CS-E 745(a)(2), AMC E 745(3) and CS-E 750(d) are the rotorcraft and free power-turbine cases."),
    ("E", "Icing conditions — and the rotorcraft AMC gap", ["CS-E 780"], "CS-E 780 applies and cites CS 27.1093(b) / CS 29.1093(b). AMC E 780 states it has no rotorcraft provisions — method must be agreed with EASA. Changed at Amdt 7."),
    ("E", "Rain and hail 1 — the rotorcraft alternative", ["CS-E 790", "AMC E 790", "AMC E 790(a)(1)"], "CS-E 790(b) is a rotorcraft-only alternative to (a)(2)."),
    ("E", "Rain and hail 2 — test reduction and standard concentrations", ["AMC E 790(a)(2)", "Appendix A"], "Split of AMC E 790(a)(2) (4,698 words) — rotorcraft section (d) only. FIGURES on pp. 199–201; render and read."),
    ("E", "Bird strike 1 — rotorcraft bird speed and test matrix", ["CS-E 800", "AMC E 800"], "Split 1 of 2. Rotorcraft speed is the maximum airspeed for normal flight operations, not 200 kt. FIGURE on p. 214."),
    ("E", "Bird strike 2 — turboshaft load device and acceptance", ["CS-E 800", "AMC E 800"], "Split 2 of 2. AMC E 800(d) names turboshaft engines directly. FIGURE on p. 220."),
    ("E", "Compressor and turbine blade failure", ["CS-E 810", "AMC E 810"], "Changed at Amdt 7. Composite fan blade clauses apply only if such blades are fitted."),
    ("E", "Over-torque, over-speed and rotor integrity", ["CS-E 820", "CS-E 830", "CS-E 840", "AMC E 840"], "Over-torque is the turboshaft power-turbine load path."),
    ("E", "Shafts and over-temperature", ["CS-E 850", "AMC E 850", "CS-E 860", "CS-E 870"], "Compressor, fan and turbine shafts; turbine rotor and exhaust gas over-temperature."),
    ("E", "OEI capability after an over-limit event", ["AMC E 820(a)(2)", "AMC E 830(c)", "AMC E 870(a)(3)"], "CONDITIONAL on 30-Second / 2-Minute OEI. Three one-sentence AMCs with the same test."),
    ("E", "Tests with refrigerant injection", ["CS-E 880"], "CONDITIONAL on refrigerant injection and 2½-Minute OEI. Opens '(a) Engines for Rotorcraft.'"),
    ("E", "Relighting and the over-temperature test", ["CS-E 910", "AMC E 910", "CS-E 920", "AMC E 920"], "CS-E 920 and AMC E 920 changed at Amdt 8."),
    ("E", "Initial Maintenance Programme test 1 — what it is", ["CS-E 930", "AMC E 930"], "Split 1 of 2. NEW at Amdt 8 — CS-E 930 and AMC E 930 did not exist in Amendment 7."),
    ("E", "Initial Maintenance Programme test 2 — build, cycle, evidence", ["AMC E 930"], "Split 2 of 2. NEW at Amdt 8. Covers OEI cumulative usage where those ratings are claimed."),

    # --------------------------------------------------------------- Subpart F
    ("F", "Subpart F scope, fuel venting and emissions", ["CS-E 1000", "AMC E 1000", "CS-E 1010", "CS-E 1020", "AMC E 1020"], "CS-34 emissions compliance."),
    ("F", "Time limited dispatch", ["CS-E 1030", "AMC E 1030"], "CONDITIONAL on TLD claimed and EECS fitted. AMC E 1030 is 3,208 words; split if TLD is claimed. FIGURES on p. 260."),
    ("F", "Volcanic cloud hazards", ["CS-E 1050", "AMC E 1050"], "Note CS-E 1040 ETOPS is excluded. FIGURE on p. 261."),

    # ----------------------------------------------------------------- Closing
    ("Closing", "What does not apply, and why", [], "The 13 EXCLUDED paragraphs grouped by reason: thrust reverser, propeller, turbofan-only, aeroplane-only, ETOPS, and the AMC E 780 rotorcraft gap."),
    ("Closing", "Open items and engine variables to confirm", [], "The five CLAUDE.md variables, every [VERIFY] raised, and the AMC E 780 / AMC E 1030 items needing EASA agreement."),
    ("Closing", "Compliance matrix template", [], "One row per in-scope paragraph: status, method (test / analysis / similarity), evidence document, owner. Exported as deck/compliance_matrix.xlsx in Phase 5."),
]
