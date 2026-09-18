---
id: "AMC E 520"
type: AMC
subpart: D
pages: 106-108
changed_in: [Amdt7]
tags: [strength, high-cycle-fatigue, containment, blade-loss, engine-model, casing, crack-growth]
covers: ["AMC E 520(a)", "AMC E 520(c)(1)", "AMC E 520(c)(2)", "AMC E 520(d)"]
---
# AMC E 520 — Strength

> [!summary]
> Four AMC paragraphs serve CS-E 520. AMC E 520(a) recommends a fatigue strength
> ordering for the blade and disc so that an unpredicted high cycle fatigue
> failure occurs at the least damaging location. AMC E 520(c)(1) covers blade
> containment, including the observation that failed blades do not leave in the
> plane of rotation. AMC E 520(c)(2) is the longest: what the validated engine
> model must contain and how it is correlated against the CS-E 810 blade loss
> test. AMC E 520(d) covers casings designed to tolerate residual crack growth.

## Requirement

### AMC E 520(a) — high cycle fatigue

| Ref | Obligation | Strength |
|---|---|---|
| **(a)** | In order to minimise the adverse consequences of Failures due to unpredicted high cycle fatigue, it is recommended that the relative fatigue strengths of the blade and disc are normally graded in ascending order: blade form, blade root, disc blade attachment, disc rim. | Accepted method |

The ordering puts the weakest link furthest from the disc. An unpredicted high
cycle fatigue failure then occurs in the blade form, which [[CS-E 520|CS-E 520(c)(1)]]
requires to be radially contained, rather than in the disc rim, whose Failure is
treated as uncontained high-energy debris under
[[AMC E 510|AMC E 510(3)(d)(iii)]].

### AMC E 520(c)(1) — shedding of blades

| Ref | Obligation | Strength |
|---|---|---|
| **(c)(1)(1)** | To reduce the risk of a single blade Failure leading to a multiple blade Failure and possible non-containment, pay particular attention to blade material, blade root fixing and the design of casing joints in vulnerable areas. | Accepted method |
| **(c)(1)(2)** | In providing containment for compressor and turbine blades, take account of the possibility that the final trajectory of a failed blade may not be directly in the plane of its rotation. | Accepted method |
| **(c)(1)(2)** | This AMC does not impose an obligation on the engine constructor to provide containment in the direction of the intake and exhaust, provided the limits of the angles to which containment is assured are made available to the aircraft constructor installing the engine. | Relief |

The non-planar trajectory is quantified from service experience: "impact points
on the aircraft structure of failed blades have been experienced at angles up to
± 30° from the point of intersection of the Engine centre line and the plane of
rotation" [AMC E 520(c)(1)(2)].

The AMC names two cases where this matters most: where the final containment
provisions are external to the engine casing and lie some distance from it, and
where the casing containment capability is reduced adjacent to the plane of
rotation — by cut-outs for adjacent stator roots, bleed ports and similar.

The relief has a price attached. Containment fore and aft is not required, but
only if the assured containment angles are given to the aircraft constructor. The
obligation converts from a design duty into an installation-information duty.

### AMC E 520(c)(2) — engine model validation

| Ref | Obligation | Strength |
|---|---|---|
| **(c)(2)(1)** | Validated data specifically for blade loss analysis typically includes: finite element model; out-of-balance; component Failure; rubs, both blade-to-casing and intershaft; resulting stiffness changes; aerodynamic effects such as thrust loss and engine surge; variations with time of the rotational speeds of the engine's main rotating systems after Failure; and dynamic displacement of interface features between engine and aircraft. | Statement |
| **(c)(2)(2)** | Manufacturers whose engines fail the rotor support structure by design during the blade loss event should also evaluate the effect of the loss of support on engine structural response. | Accepted method |
| **(c)(2)(2)** | Evaluate the effect of the most severe blade Failure which would not cause the Failure of the rotor structural support, including the effect on the engine and on the loads transmitted to the aircraft. | Accepted method |
| **(c)(2)(3)** | Validate the model on vibration tests and the results of the blade loss test required for compliance with CS-E 810, allowing for the effects of the test mount structure and any other differences between the test configuration and the aircraft installation. | Accepted method |
| **(c)(2)(3)** | Make the model capable of accurately predicting the transient loads from blade release through run-down to steady state. | Accepted method |
| **(c)(2)(3)** | Where compliance with CS-E 810 is granted by similarity instead of test, correlate the model to prior experience. | Accepted method |
| **(c)(2)(3)** | Document assumptions about the engine installation configuration in the Manuals required by CS-E 20(d). | Accepted method |
| **(c)(2)(4)** | Achieve validation of the engine model static structure by a combination of engine and component tests including structural tests on major load path components, or by analysis, or both. | Accepted method |
| **(c)(2)(4)** | Verify the adequacy of the engine model to predict rotor critical speeds and forced response behaviour by measuring engine vibratory response when imbalances are added to the rotors. | Accepted method |
| **(c)(2)(5)** | Correlate the model against the CS-E 810 blade loss engine test to demonstrate that it accurately represents: initial blade release event loads; any rundown resonant response behaviour; frequencies; Failure sequences; and general engine movements and displacements, including interface features between engine and aircraft. | Accepted method |
| **(c)(2)(6)** | Instrument the blade loss engine test to enable that correlation — for example high-speed cinema and video cameras, accelerometers, strain gauges, continuity wires and shaft speed tachometers — and make the instrumentation capable of measuring loads on the engine attachment structure. | Accepted method |
| **(c)(2)(7)** | The aircraft and engine manufacturers should mutually agree upon the definition of the model, based on test and experience. | Accepted method |

Two items in (c)(2)(2) are easy to conflate. The first applies only where the
rotor support structure is *designed* to fail during blade loss. The second
applies to every engine: the most severe blade Failure that does **not** fail the
rotor support must also be evaluated, because it can produce a longer period of
out-of-balance running.

The mutual agreement in (c)(2)(7) makes the model a joint artefact. It is not
delivered to the installer as a finished product; its definition is agreed
between engine and aircraft manufacturer.

### AMC E 520(d) — local failures

| Ref | Obligation | Strength |
|---|---|---|
| **(d)** | Local Failures of the engine casing may include localised cracking. | Statement |
| **(d)(a)** | For any casing design that allows for residual crack growth, demonstrate that the condition of the casing, including the maximum predicted crack size, will not lead to a Hazardous Engine Effect. | Accepted method |
| **(d)(b)** | If the Failure of the casing, for instance as the result of ultimate crack growth, could result in a Hazardous Engine Effect, classify the part as a Critical Part in accordance with CS-E 510(a)(2) and comply with the Integrity Specifications of CS-E 515. | Accepted method |

Sub-point (d)(b) is a classification trigger, not merely advice. A casing whose
ultimate crack growth could cause a Hazardous Engine Effect enters the Engine
Critical Part regime, which brings the three plans of [[CS-E 515]] with it. The
static pressure loaded part lifing method of
[[AMC E 515|AMC E 515(3)(e)]] is written for exactly this case.

## Compliance

- Blade and disc fatigue strength grading, or justification for departing from the recommended order [AMC E 520(a)].
- Blade material, root fixing and casing joint design substantiation against multiple blade Failure [AMC E 520(c)(1)(1)].
- Containment analysis accounting for non-planar blade trajectories, with the assured containment angle limits declared to the aircraft constructor where fore and aft containment is not provided [AMC E 520(c)(1)(2)], within the manuals of [[CS-E 20|CS-E 20(d)]].
- Validated engine model covering the eight data items of (c)(2)(1) [AMC E 520(c)(2)(1)].
- Evaluation of the most severe blade Failure not causing rotor support Failure, and of loss of rotor support where the structure is designed to fail [AMC E 520(c)(2)(2)].
- Model validation against vibration tests and the [[CS-E 810]] blade loss test, or correlation to prior experience where CS-E 810 compliance is by similarity [AMC E 520(c)(2)(3)].
- Static structure validation by engine and component tests, analysis, or both, with rotor critical speed and forced response verification by added imbalance [AMC E 520(c)(2)(4)], linked to [[CS-E 650]].
- Blade loss test instrumentation capable of measuring loads on the engine attachment structure [AMC E 520(c)(2)(6)].
- Agreed model definition with the aircraft manufacturer [AMC E 520(c)(2)(7)].
- Residual crack growth demonstration for any casing designed to tolerate it, with the maximum predicted crack size [AMC E 520(d)(a)].
- Critical Part classification and [[CS-E 515]] compliance for a casing whose ultimate crack growth could cause a Hazardous Engine Effect [AMC E 520(d)(b)].

## Application to this engine

All four AMC paragraphs apply. None is restricted by rating or control system.

**Containment angles are an installation deliverable.** The ± 30° service
experience figure in (c)(1)(2) and the relief for fore and aft containment both
resolve into information the rotorcraft manufacturer needs. For a rotorcraft
installation the engine sits close to the airframe and to the transmission, so
the assured containment angles carry real weight in the installation assessment
under [[CS-E 30]].

**The engine model is shared work.** (c)(2)(7) requires mutual agreement on the
model definition between the aircraft and engine manufacturers, and (c)(2)(3)
requires installation configuration assumptions to be documented in the manuals
of [[CS-E 20|CS-E 20(d)]]. Because the rotorcraft installation target is not
fixed, those assumptions should be treated as open.

**Aerodynamic effects listed in (c)(2)(1) include "thrust loss and engine surge".**
For a turboshaft the thrust term reads as shaft power loss; surge applies
directly and links to [[CS-E 500|CS-E 500(a)]].

**Rotor imbalance verification.** (c)(2)(4) refers to adding imbalances to "the
fan and other rotors". A turboshaft has no fan, so the compressor, turbine and
power turbine rotors carry the verification, cross-referenced by the AMC to
[[CS-E 650]].

## References

Specification: [[CS-E 520]]
Related: [[CS-E 510]] · [[CS-E 515]] · [[CS-E 500]] · [[CS-E 525]] · [[CS-E 650]] · [[CS-E 810]] · [[CS-E 840]] · [[CS-E 20]] · [[CS-E 30]] · [[AMC E 510]] · [[AMC E 515]]

## Amendment history

AMC E 520(c)(2) was amended at Amendment 7. The validated data list gained an
item and the evaluation duties gained a case.

Before the amendment the list ended at "variations with time of the rotational
speed(s) of the Engine's main rotating system(s) after failure". Amendment 7
appended one further item: "dynamic displacement of interface features between
Engine and aircraft" [AMC E 520(c)(2)(1)].

Amendment 7 also inserted into (c)(2)(2) the sentence requiring evaluation of
"the most severe blade Failure which would not cause the Failure of the rotor
structural support", with the effect on the engine and on the loads transmitted
to the aircraft. Before the amendment, (c)(2)(2) addressed only engines that fail
the rotor support structure by design.

Both changes add work, and both point the same way: towards what the aircraft
sees at the interface. The new data item and the new evaluation case are the
model-side counterpart of the CS-E 520(c)(1) rewrite at the same amendment, which
moved the blade shedding specification from a consequence test to a radial
containment test.

AMC E 520(a) and AMC E 520(c)(1) are unchanged at Amendments 7 and 8 and carry
`[Amdt. No.: E/1]`. AMC E 520(c)(2) carries `[Amdt No: E/2]` and
`[Amdt No: E/7]`. AMC E 520(d) carries `[Amdt No: E/5]`.
