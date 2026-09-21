---
id: "AMC E 850"
type: AMC
subpart: E
pages: 236-239
changed_in: []
tags: [shaft, shaft-failure, over-speed, fatigue, design-assessment, service-experience]
---
# AMC E 850 — Compressor, Fan and Turbine Shafts

> [!summary]
> Four parts. Part (1) defines what counts as a shaft and pulls any engine
> gearbox into that definition. Part (2) gives the two routes for showing a shaft
> Failure is non-hazardous, by test or by validated analysis, and states what
> each route must cover. Part (3) explains why the fail-safe objective is the
> default and lists nine Failure modes seen in service. Part (4) sets the design
> assessment and the investigations and tests that support it.

## Requirement

### AMC E 850(1) — General

| Ref | Obligation | Strength |
|---|---|---|
| **(1)(a)** | A shaft is the system that transmits torque between the power-producing system and the power-using system, and for which the mechanical restraints are mainly torsional. Any engine gearbox in that transmission system is included. | Statement |
| **(1)(a)** | Excluding discs from the shaft definition does not preclude the specification that any Failure of a disc should be Extremely Remote. | Statement |
| **(1)(b)** | Clarification of the terms and probabilities used in CS-E 850 may be found in CS-E 510. The possible shedding of blades is also covered in CS-E 810(b). | Statement |

The definition is quoted in full because the scope of CS-E 850 rests on it:
"A shaft is the system that transmits torque between the disc driving flange or
the shaft attachment member of the system that produces power (e.g. turbine) and
the system that uses this power (e.g. compressor/fan or driving flange), and for
which the mechanical restraints are mainly torsional." [AMC E 850(1)(a)]

Two boundaries follow. An engine gearbox is part of the shaft system; an aircraft
gearbox is treated separately under [AMC E 850(2)(c)]. Discs are outside the
definition, but the AMC states that "The exclusion of discs from this definition
of a shaft does not preclude the specification that any Failure thereof should be
Extremely Remote." [AMC E 850(1)(a)]

### AMC E 850(2) — Non-Hazardous Shaft Failures

| Ref | Obligation | Strength |
|---|---|---|
| **(2)(a)** | Where Hazardous Engine Effects are claimed to be avoided by keeping rotating components substantially in their normal plane of rotation, with over-speed controlled by disc rubbing, blade interference, spragging or shedding, engine surge or stall, or over-speed protection devices, this may be substantiated by either test or validated analysis. | Permitted |
| **(2)(b)** | Where compliance is by test, initiate the shaft Failure under the worst-case operating conditions within the flight envelope, in any dispatchable configuration, that will maximise the rotor over-speed and the subsequent effects. | Accepted method |
| **(2)(b)** | Where the worst case cannot be fully duplicated, the applicant may propose a test under suitably representative conditions. Those test conditions would need to be submitted to the Agency for acceptance. | Permitted |
| **(2)(b)** | Take into account, in addition to the initial rotor speed, the shaft torque and the relevant engine pressures and temperatures. | Accepted method |
| **(2)(b)** | Failures predicted to occur with a probability of Extremely Remote or less do not need to be taken into account if they meet all the requirements of CS-E 850(b)(2). | Relief |
| **(2)(b)** | Where compliance is shown by system or component rig tests rather than a full engine test, show that the tests are sufficiently representative of the way the Failure would occur on a full engine, in terms of the key characteristics of the shaft Failure and its consequences on all the relevant engine parts and on the behaviour of subsystems. | Accepted method |
| **(2)(c)** | Where compliance is by validated analysis, show that all the likely Failure modes have been identified, including the loss of loads caused by a Failure of any gearboxes supplied by the aircraft manufacturer. | Accepted method |
| **(2)(c)** | The Failure analysis should consider the effect of Failures in terms of contact and the loads on the surrounding engine structure, and determine whether the affected rotor components are retained substantially in their rotational plane. | Accepted method |
| **(2)(c)** | Demonstrate that the structural components, when the Failure loads are applied, do not exceed their ultimate stress capability and do not lead to a Hazardous Engine Effect. | Accepted method |
| **(2)(c)** | Validate the analysis against an actual engine, system or component rig tests and/or service events, and show a sufficient degree of similarity with the engine model for which compliance is sought. The similarity argument should be submitted to the Agency for acceptance. | Accepted method |

The four means of over-speed control named in (2)(a) are the mechanisms an
applicant may rely on: disc rubbing, blade interference, spragging or shedding,
engine surge or stall, and over-speed protection devices.

The similarity argument in (2)(c) is not left open. The AMC lists what it must
encompass: "aerodynamics, surge characteristics, engine control logic, rotor
speeds and the associated acceleration characteristics, relevant rotor and stator
design features, materials, clearances, etc." [AMC E 850(2)(c)]

### AMC E 850(3) — Hazardous Shaft Failures

| Ref | Obligation | Strength |
|---|---|---|
| **(3)** | Shaft systems should be designed to fail safe as required by CS-E 850(a)(1), because experience has shown that Failures of shafts occur at a rate in excess of Extremely Remote. | Accepted method |
| **(3)** | It is accepted under CS-E 850(a)(3) that, for conventional designs, fail-safe design is not possible for all parts of a shaft system. | Statement |
| **(3)** | The use of that provision should be strictly limited. | Accepted method |
| **(3)** | Consider particularly two hazardous effects of shaft Failure: a release of the complete fan or compressor moving forward, and an over-speed of the turbine leading to disc burst. | Accepted method |
| **(3)** | Consider industry experience with shaft Failures under CS-E 850(b)(2)(v). Nine Failure modes have caused shaft Failures in service; they are listed below. | Accepted method |
| **(3)** | Show that features such as splines, oil feed holes, couplings, bearing tracks that are integral with the shaft, and sealing fins are well understood and conducive to well-established and validated stressing techniques. | Accepted method |
| **(3)** | Where the assessment under CS-E 850(b)(2)(iii) is that a shaft Failure due to the environment can be discounted, take into account the ability to inspect the critical section of the shaft at the defined intervals and the appropriateness of the inspection method. | Accepted method |

The nine service Failure modes listed in [AMC E 850(3)]:

| # | Failure mode |
|---|---|
| 1 | Degradation of a bearing, leading to shaft orbiting and subsequent contact between the shaft and other rotating or static parts |
| 2 | Blade Failure, resulting in an imbalance and rubbing of the shaft on other parts |
| 3 | Corrosion inside the shaft |
| 4 | Fuel flow instability in the Engine Control System inducing a resonance in the shaft |
| 5 | An oil fire around the shaft |
| 6 | Impingement of hot air on the shaft |
| 7 | A bearing Failure |
| 8 | An HCF Failure from a stress concentration feature |
| 9 | A loss of lubrication of a spline |

The inspectability point carries a worked consequence: "the Failure of a section
of a shaft, which could cause Hazardous Engine Effects, in an area which would
make inspection of the critical section in accordance with the manual difficult,
may not be acceptable." [AMC E 850(3)] Discounting an environmental Failure mode
is therefore tied to whether the maintenance programme can actually reach the
section concerned.

### AMC E 850(4)(a) — Design assessment, causes and probabilities

| Ref | Obligation | Strength |
|---|---|---|
| **(4)(a)(i)** | Include the potential for, and possible effects of, undetected material defects. | Accepted method |
| **(4)(a)(ii)** | Include the effects of manufacturing tolerances allowed by the design. | Accepted method |
| **(4)(a)(iii)** | Include rubbing between any torque-loaded section of the shaft and adjacent surfaces, such as other shafts, oil seals or air seals, to the extent that significant over-heating or reduction in strength could occur. | Accepted method |
| **(4)(a)(iv)** | Include the effect on the shaft of a bearing Failure and the desirability of provision for detecting an incipient bearing Failure, by maintenance techniques and/or flight instrumentation. Consider the possibility of isolating the bearing from the shaft to increase the damage tolerance of the system. | Accepted method |
| **(4)(a)(v)** | Include the effect on the shaft of any likely engine fire and the necessity for provision of an early warning of any internal fires that may occur. | Accepted method |
| **(4)(a)(vi)** | Include the effect on the shaft of loads which could be transmitted by shock loading resulting from bird strikes, blade Failures and similar events. | Accepted method |
| **(4)(a)(vii)** | Include the effect on the shaft of oscillatory loading, for example resulting from fuel system oscillations. | Accepted method |

### AMC E 850(4)(b) — Investigations and testing

| Ref | Obligation | Strength |
|---|---|---|
| **(4)(b)(i)** | Use strain gauge or other suitable means of investigation to satisfy the vibration survey specifications of CS-E 650 and to ensure that shaft whirling is not present to any significant degree at any likely engine operating condition. | Accepted method |
| **(4)(b)(ii)** | Carry out a fatigue evaluation of each shaft in torsional modes to confirm its predicted safe life, with an oscillatory torque superimposed on the steady-state torque. | Accepted method |
| **(4)(b)(iii)** | Where necessary, confirm stress assumptions by static strength tests. | Accepted method |
| **(4)(b)(iv)** | Where necessary, substantiate by test the design considerations detailed in paragraph (4)(a), so as to demonstrate that shaft Failure is acceptably remote. | Accepted method |

The oscillatory torque is fixed by a floor, not by the installation alone. It is
"of a magnitude equal to the maximum envisaged in a representative installation,
but not less than ±5% of the normal maximum steady-state torque"
[AMC E 850(4)(b)(ii)]. The evaluation must also consider any high-frequency
vibrations determined from the survey under (4)(b)(i), and any possible shaft
bending.

## Compliance

- Shaft system definition and boundary, stating which gearboxes are inside the engine shaft system [AMC E 850(1)(a)].
- Test or validated analysis showing that shaft Failure consequences are non-hazardous, with the chosen route justified [AMC E 850(2)(a)].
- Where by test: a worst-case test condition statement covering rotor speed, shaft torque, engine pressures and temperatures, submitted to the Agency where the worst case cannot be duplicated [AMC E 850(2)(b)].
- Where by rig test: a representativeness argument against a full engine Failure [AMC E 850(2)(b)].
- Where by analysis: a Failure mode identification including aircraft-supplied gearbox load loss, a structural load assessment against ultimate stress capability, and a validation and similarity case submitted to the Agency [AMC E 850(2)(c)].
- Service experience assessment against the nine Failure modes, feeding [CS-E 850(b)(2)(v)] [AMC E 850(3)].
- Stressing substantiation for splines, oil feed holes, couplings, integral bearing tracks and sealing fins [AMC E 850(3)].
- Inspectability assessment of the critical shaft section and the inspection method, where an environmental Failure mode is discounted [AMC E 850(3)].
- Design assessment covering the seven causes in [AMC E 850(4)(a)].
- Shaft vibration and whirling survey within [[CS-E 650]] [AMC E 850(4)(b)(i)].
- Torsional fatigue evaluation with at least ± 5 % oscillatory torque, plus high-frequency vibration and shaft bending effects [AMC E 850(4)(b)(ii)].
- Static strength tests and design-consideration tests where necessary [AMC E 850(4)(b)(iii)], [AMC E 850(4)(b)(iv)].

## Application to this engine

The AMC applies in full. Every part of it bears on a turboshaft, and several
parts bear on it more heavily than on a turbofan, particularly where the engine
has a free power turbine.

**Over-speed control by surge or by a protection device.**
[AMC E 850(2)(a)] accepts engine surge or stall and over-speed protection devices
as means of limiting the over-speed after a shaft Failure. For this engine the
protection device is a function of the EECS-FADEC, so the claim is assessed
together with [[CS-E 50]] and the Failure rates established there. Reliance on
surge alone is assessed against the surge behaviour established under
[[CS-E 500]].

**The aircraft gearbox is named.**
[AMC E 850(2)(c)] requires the analysis to include "the loss of loads caused by a
Failure of any gearboxes supplied by the aircraft manufacturer". On a rotorcraft
that is the main transmission, and its Failure is the classic loss-of-load case
for the power turbine. The assumption set crosses the engine boundary and is
declared under [[CS-E 30]].

**Loss of load is the link to rotor integrity.**
[[CS-E 840|CS-E 840(c)]] requires the highest over-speed from a complete loss of
load to be treated as a rotor integrity condition unless it is Extremely Remote
under CS-E 850. [[AMC E 840|AMC E 840(5)]] lists what determines that over-speed:
system inertia, available gas energy, whether the rotor is held in plane, and
over-speed protection devices. The two AMCs are read together for the power
turbine.

**Five of the nine service Failure modes are governed elsewhere in this vault.**
Fuel flow instability inducing shaft resonance connects to [[CS-E 50]] and
[[CS-E 650]]; an oil fire around the shaft to [[CS-E 130]]; bearing degradation
and bearing Failure to [[CS-E 570]]; HCF from a stress concentration feature to
[[CS-E 650|CS-E 650(f)]]. The list in [AMC E 850(3)] is a cross-check on those
paragraphs, not a separate exercise.

**The ± 5 % oscillatory torque floor is a design input.**
It applies to each shaft in torsional modes. On a rotorcraft the representative
installation torque oscillation may exceed 5 % because of rotor dynamics, and
[AMC E 850(4)(b)(ii)] then takes the higher value.

[VERIFY: the maximum oscillatory torque envisaged in the rotorcraft installation,
against the ± 5 % floor of AMC E 850(4)(b)(ii). The value depends on the main
rotor and transmission dynamics of the target aircraft, which are not declared in
engine_profile.md.]

[VERIFY: whether an over-speed protection function of the EECS-FADEC is claimed
as the means of over-speed control under AMC E 850(2)(a). If so, its Failure rate
and its independence from the control channels are assessed under CS-E 50.]

## References

Specification: [[CS-E 850]]
Related: [[CS-E 840]] · [[CS-E 810]] · [[CS-E 515]] · [[CS-E 510]] · [[CS-E 650]] · [[CS-E 570]] · [[CS-E 500]] · [[CS-E 130]] · [[CS-E 50]] · [[CS-E 30]] · [[AMC E 840]] · [[AMC E 810]] · [[AMC E 510]]
