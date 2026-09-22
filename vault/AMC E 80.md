---
id: "AMC E 80"
type: AMC
subpart: A
pages: 44-50
changed_in: []
imports: [AMC-20]
tags: [equipment, environmental-qualification, do-160, high-energy-rotor, containment, weak-link]
---
# AMC E 80 — Equipment

> [!summary]
> One AMC serves CS-E 80, and most of it is an environmental qualification
> programme. Tables 1 to 4 list the conditions equipment should be shown to
> survive and the test standard accepted for each, and the prose after each of
> those tables states what the demonstration is for. Two further points stand
> apart: a weak link is the normal means of limiting excessive torque but is not
> always adequate, and high-energy rotor compliance is demonstrated against four
> containment categories.

## Requirement

### AMC E 80(1) — scope of the additional specifications

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | Determine the need for additional specifications in the equipment specifications when complying with CS-E 80, or define them on a general basis, for example to cover more than one aircraft installation. | Accepted method |
| **(1)** | Show that all equipment — electronic units, sensors, harnesses, hydromechanical elements and any other relevant elements or units — operates properly in its declared environment. | Accepted method |
| **(1)** | Additional testing may be required to comply with CS-E 80(b), depending on the assumed installation conditions. | Statement |

Considering general conditions such as EUROCAE ED-14 / RTCA/DO-160 "allows the
certification of equipment in a consistent manner, independent from any
installation consideration" [AMC E 80(1)]. That independence is the reason the
tables are written against a standard rather than against an aircraft.

### AMC E 80(2) — how to use the tables

| Ref | Obligation | Strength |
|---|---|---|
| **(2)** | Consider the applicability of the items listed in Tables 1 to 4, which are provided as a guide. | Accepted method |
| **(2)** | The manufacturer may define other acceptable appropriate test and analysis procedures. | Permitted |
| **(2)** | Demonstrate compliance normally by test or analysis, unless the equipment is shown to be sufficiently similar to previously certified equipment and operates in an environment that is the same or less severe. | Accepted method |

The similarity route is the only alternative to test or analysis. It carries
two conditions at once: sufficient similarity of the equipment, **and** an
environment no more severe than the one already certified [AMC E 80(2)].

### AMC E 80(2)(a) — general environmental conditions, all equipment

Table 1 applies to all equipment.

![[AMC_E_80_p45.png]]

| Ref | Obligation | Strength |
|---|---|---|
| **(2)(a)** | High temperature: verify that the equipment functions properly in its maximum temperature environment and identify damage from that exposure that could lead to equipment Failure, taking account of ambient, external and internal fluid temperatures. | Accepted method |
| **(2)(a)** | Low temperature: verify the same in the minimum temperature environment, on the same basis. | Accepted method |
| **(2)(a)** | Room temperature: identify damage caused by extended operation at room temperature that could lead to equipment Failure. The test may be combined with the contaminated fluid tests. | Accepted method |
| **(2)(a)** | Contaminated fluids: verify that the engine systems function properly in a contaminated fluid environment, by system testing or by individual equipment test or analysis. | Accepted method |
| **(2)(a)** | Vibration: verify that exposure to the declared vibration environment causes no structural Failures and that the equipment functions properly under it, by a specific unbalanced engine test or by equipment test. | Accepted method |
| **(2)(a)** | The equipment may be non-operational during equipment vibration testing where the applicant demonstrates by other means that it operates satisfactorily, or does not adversely affect system operation, in the declared vibration environment. | Permitted |
| **(2)(a)** | Operational shock: verify that shocks experienced during normal aircraft operations allow the equipment to continue functioning properly. | Accepted method |
| **(2)(a)** | Crash safety: verify that shocks experienced in crash conditions will not cause Failure of the mounting attachment. Applies where separation of the equipment could lead to a Hazardous Engine Effect. | Accepted method |
| **(2)(a)** | Sand and dust: applicable to all equipment that is not environmentally sealed. | Accepted method |
| **(2)(a)** | Fluid susceptibility: verify proper function after exposure to the fluids likely to be encountered in service, such as fuel, oil, hydraulic fluids and cleaning solvents, and identify damage that could lead to equipment Failure. | Accepted method |
| **(2)(a)** | After the fluid susceptibility test, where the design allows, open and inspect the unit for fluid entry; where fluid entry is detected, provide the rationale for accepting the results based on the criticality of the quantity and location of the entry point. | Accepted method |
| **(2)(a)** | Salt spray: verify proper operation after exposure to a salt spray environment. For environmentally sealed equipment the specification may be substantiated by an analysis showing the external materials are immune to salt spray. | Accepted method |
| **(2)(a)** | Fuel system icing: fuel system equipment normally substantiates its capability to operate in an icing environment through system test or analysis. | Statement |
| **(2)(a)** | Induction icing: equipment exposed to engine gas path or bleed system icing normally substantiates its capability through an engine test or analysis. | Statement |
| **(2)(a)** | Fungus: substantiate by test, or by an analysis showing no materials supporting fungus growth are used in the equipment. | Accepted method |
| **(2)(a)** | Temperature and altitude: verify by test or analysis that the equipment operates per design intent throughout the engine flight envelope. | Accepted method |

Items 4, 10 and 11 of Table 1 are marked "As a reminder" and point to
specifications elsewhere in CS-E rather than to a test standard
[AMC E 80(2)(a)]. The binding duty sits in [[CS-E 560|CS-E 560(e)]],
[[CS-E 570]], [[CS-E 580]] and [[CS-E 780]].

### AMC E 80(2)(b) — electrical and electronic equipment

Table 2 applies to all electrical or electronic equipment, and to equipment with
electrical or electronic sub-components.

![[AMC_E_80_p47.png]]

| Ref | Obligation | Strength |
|---|---|---|
| **(2)(b)** | Thermal cycle: demonstrate that the equipment continues to operate and is neither failed nor damaged by temperature cycles and thermal transients consistent with the declared temperature environment. | Accepted method |
| **(2)(b)** | Where the equipment has electrical sub-components, testing of the sub-components only may be acceptable. | Permitted |
| **(2)(b)** | Explosion proofness: verify that the equipment cannot cause an explosion of flammable fluids or vapours. | Accepted method |
| **(2)(b)** | Humidity: demonstrate that the equipment is not adversely affected, operationally or structurally, by ingress of moisture. | Accepted method |
| **(2)(b)** | Waterproofness: verify proper function after exposure to water and identify damage from water exposure that could lead to equipment Failure; where the design allows, open and inspect for water entry and justify acceptance if entry is detected. | Accepted method |
| **(2)(b)** | EMI, HIRF and lightning: see AMC 20-1 and AMC 20-3. | Accepted method |
| **(2)(b)** | Power input: demonstrate that equipment receiving power directly from the aircraft can accommodate the full range of power inputs declared for the installation. | Accepted method |

The explosion proofness text distinguishes two environments. Environment I
"defines equipment mounted in fuel tanks or within fuel systems", and
Environment II is an atmosphere in which flammable mixtures can be expected to
occur as the result of a Fault causing spillage or leakage [AMC E 80(2)(b)]. For
a Fire zone, which has extinguishing provisions, the Environment II test is
adequate; Flammable Fluid Leakage areas may lack those provisions, so
Environment I may be required for aircraft installation [AMC E 80(2)(b)].

Power input applies only to equipment powered directly by the aircraft, and the
AMC names the electronic engine control (EEC) and the hydromechanical unit (HMU)
fuel shutoff solenoid as examples [AMC E 80(2)(b)].

### AMC E 80(2)(c) — mechanical equipment

Table 3 points to other CS-E specifications rather than to external standards.

![[AMC_E_80_p48.png]]
![[AMC_E_80_p49.png]]

| Ref | Obligation | Strength |
|---|---|---|
| **(2)(c)** | Proof pressure and burst pressure, per CS-E 640(a)(1) and CS-E 640(a)(2). | Accepted method |
| **(2)(c)** | Pressure cycling, per AMC E 515(3)(e). | Accepted method |
| **(2)(c)** | Fire, per CS-E 130; the Engine Control System should also comply with CS-E 130(e). | Accepted method |

The related [[AMC E 130]] and [[AMC E 640]] are therefore relevant
[AMC E 80(2)(c)].

### AMC E 80(2)(d) — specialised equipment testing

![[AMC_E_80_p49_2.png]]

| Ref | Obligation | Strength |
|---|---|---|
| **(2)(d)** | Overheat: verify by test or analysis that the electrical and electronic portions of the Engine Control System, when subjected to an overheat condition leading to Failure, will not cause a Hazardous Engine Effect. | Accepted method |
| **(2)(d)** | Where an overheat test or analysis is not completed, declare this as an installation limitation in the engine instructions for installation, and address the possibility of an overheat at aircraft certification. | Accepted method |

### AMC E 80(3) — limiting excessive torque

| Ref | Obligation | Strength |
|---|---|---|
| **(3)** | A weak link in the drive, or the specification of a weak link in the equipment, will normally be an acceptable means of limiting excessive torque. | Accepted method |
| **(3)** | For some equipment under CS-E 20(c), such as a high output electrical generator, a weak link might not adequately safeguard against damage to the engine from overheating and break-up of the equipment. | Statement |
| **(3)** | In such a case, other means of disconnect would need to be provided or specified, to permit disengagement of the equipment with the engine running. | Required |

[VERIFY: unlisted construction. Row (3) uses "would need to" and carries
Required. The phrasing is neither one of the seven source verbs nor a listed
declaratory form. The vault reads a statement of necessity as Required, as it
reads "is required to". The owner decides each construction once, for every row
in the vault that carries it.]

This is the accepted means for [[CS-E 80|CS-E 80(a)(2)(ii)]], which requires the
mountings and drives to minimise engine shut-down caused by excessive torque.

### AMC E 80(4) — equipment with high-energy rotors

Compliance with [[CS-E 80|CS-E 80(d)]] can be demonstrated by reference to four
containment categories, set out for a turbine starter supplied with air or gas
from an external source. Other equipment is considered on a similar basis, using
the Fault analysis of the whole system to determine the critical speeds that may
result from Failures [AMC E 80(4)].

![[AMC_E_80_p49_3.png]]
![[AMC_E_80_p50.png]]

| Ref | Obligation | Strength |
|---|---|---|
| **(4)** | Demonstrate one of the four containment categories of Table 5, and meet the Table 6 specifications listed against that category. | Accepted method |
| **(4)** | For equipment other than a turbine starter, use the Fault analysis of the whole system to determine the critical speeds that may result from Failures, and proceed on a similar basis. | Accepted method |

Table 5 and Table 6 work as a pair: the category demonstrated determines which
of the specifications a to e apply. Broadly, the stronger the containment
demonstrated, the fewer the additional specifications. Category 1, blade
containment only, and Category 2 carry all five; Category 3 carries a and b; and
Category 4 carries specification a alone [AMC E 80(4)].

The Table 6 specifications route into paragraphs with their own notes:
[[CS-E 590]] for the drive mechanism probability, [[CS-E 515]], [[CS-E 70]] and
[[CS-E 110]] for Approved Life and quality control of rotating Engine Critical
Parts, [[CS-E 840]] for the integrity test of rotating parts, and
[[CS-E 520|CS-E 520(b)]] for clearance between rotating and fixed parts.

## Compliance

- Equipment environmental qualification plan covering Table 1 for all equipment, with each item either tested, analysed, justified by similarity, or recorded as not applicable [AMC E 80(2)(a)].
- Electrical and electronic qualification covering Table 2, including the explosion proofness environment selected and its justification [AMC E 80(2)(b)].
- Mechanical equipment evidence against Table 3, delivered through [[CS-E 640]], [[AMC E 515]] and [[CS-E 130]] rather than as separate tests [AMC E 80(2)(c)].
- Overheat test or analysis for the electrical and electronic portions of the Engine Control System; or, where not completed, the installation limitation stated in the instructions for installation [AMC E 80(2)(d)].
- Similarity justifications, where used, establishing both sufficient similarity and an environment no more severe than previously certified [AMC E 80(2)].
- Torque limitation design: the weak link, or the alternative means of disconnect with the engine running where a weak link is not adequate [AMC E 80(3)].
- High-energy rotor containment demonstration: the category claimed from Table 5, with the Table 6 specifications that follow from it [AMC E 80(4)].
- Fluid and water entry inspection records with acceptance rationale, where entry is detected [AMC E 80(2)(a)], [AMC E 80(2)(b)].

## Application to this engine

The whole AMC applies. Nothing in it is restricted by engine type or rating
[AMC E 80].

Table 1 item 11, induction icing, cites "CS-E 230 & CS-E 780". CS-E 230 is a
Subpart B piston engine paragraph and is outside the scope of this vault, so the
applicable specification for this engine is [[CS-E 780]] alone
[AMC E 80(2)(a)].

Table 2 and Table 4 carry the weight for a full-authority EECS. Power input
applies to the EEC directly. It depends on the aircraft-supplied power range
declared for the installation. That range is an installation assumption under
[[CS-E 30|CS-E 30(a)]] and a control system specification under
[[CS-E 50|CS-E 50(h)]]. The Table 4 overheat item is specific to engine
electronic control systems. If the overheat test or analysis is not completed,
the engine carries an installation limitation instead, and the overheat case
should be addressed at aircraft certification [AMC E 80(2)(d)].

Table 2 item 18 and Table 4 item 24 name AMC 20-1 and AMC 20-3 as the acceptable
tests or procedures for EMI, HIRF and lightning, and for control system overheat
[AMC E 80(2)(b)], [AMC E 80(2)(d)].

Both are now held. What they contribute for those two items is the EMI, HIRF and
lightning method of [[AMC 20-3B]], recorded in that note: testing of the
installed control system including representative engine-aircraft interface
cables, system-level tests on open-loop or closed-loop set-ups at the most
sensitive operating point, and a pass criterion of no adverse effect. The
criterion is defined by what counts as adverse, including a change of Take-off
Power greater than 3 % lasting more than 2 seconds, a transfer to an Alternate
Channel or Back-up System, component damage, a false annunciation, or erroneous
operation of a protection system [ext AMC 20-3B(6)(e)(iii)].

AMC 20-3B also confirms what this table leaves implicit: EMI procedures and
levels to MIL-STD-461 or ED-14 and DO-160 have been considered acceptable, and
environmental tests to MIL-STD-810 may be accepted in lieu of ED-14 and DO-160
tests where they are equal to or more rigorous [ext AMC 20-3B(6)(e)(ii)]. Those
industry standards remain unheld, so the procedures inside them stay a dead
end.

Environmental sealing decides two Table 1 items. Sand and dust applies to all
equipment that is not environmentally sealed, so the sealing claim is the
decision that removes the test [AMC E 80(2)(a)]. For sealed equipment, salt
spray may be substantiated by an analysis showing that the external materials
are immune to a salt spray environment [AMC E 80(2)(a)].

[VERIFY: whether a turbine starter with an external air or gas supply is fitted.
AMC E 80(4) sets the containment and burst provisions for such a starter, and
considers other high-energy rotor equipment on a similar basis. The answer
decides whether Table 5 applies directly or only by analogy. It is not recorded
in `engine_profile.md`.]

## Not applicable

- **(2)(a)** Table 1 item 11, in part — the reference to CS-E 230, a Subpart B piston engine paragraph, alongside CS-E 780. Subpart B is outside this vault by scope.

## References

Specification: [[CS-E 80]]
Related: [[CS-E 20]] · [[CS-E 30]] · [[CS-E 50]] · [[CS-E 130]] · [[CS-E 515]] · [[CS-E 520]] · [[CS-E 560]] · [[CS-E 570]] · [[CS-E 580]] · [[CS-E 590]] · [[CS-E 640]] · [[CS-E 780]] · [[CS-E 840]] · [[CS-E 70]] · [[CS-E 110]] · [[CS-E 90]] · [[AMC E 130]] · [[AMC E 515]] · [[AMC E 640]]
External: [[AMC 20-3B]]

## Amendment history

Unchanged at Amendments 7 and 8. The paragraph carries `[Amdt No: E/1]` and
`[Amdt No: E/5]`.
