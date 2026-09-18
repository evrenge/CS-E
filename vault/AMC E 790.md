---
id: "AMC E 790"
type: AMC
subpart: E
pages: 196-209
changed_in: []
tags: [rain, hail, ingestion, scoop-factor, critical-point-analysis, acceptance-criteria, rotorcraft]
covers: ["AMC E 790", "AMC E 790(a)(1)", "AMC E 790(a)(2)"]
---
# AMC E 790 — Rain and Hail Ingestion

> [!summary]
> Three AMC paragraphs serve CS-E 790. The short general AMC is a routing table:
> it sends every undefined term in the specification to a paragraph of
> AMC E 790(a)(2). AMC E 790(a)(1) bounds the use of alternative evidence for
> derivative engines. AMC E 790(a)(2) is the substance — the physics of
> concentration amplification, the critical point analysis, and the acceptance
> criteria — and it contains the rotorcraft section that permits the static rain
> test of CS-E 790(b) in place of CS-E 790(a)(2).

## Requirement

### AMC E 790 — where the terms are defined

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | For interpreting "unacceptable mechanical damage" and "unacceptable power or thrust loss" in CS-E 790(a)(1), (a)(2), (b) and (c), see paragraphs (5)(c)(vi), (5)(c)(vi)(A) and (B) in AMC E 790(a)(2). | Statement |
| **(2)** | For interpreting "flameout, rundown, continued or non-recoverable surge or stall" in CS-E 790(a)(2) and (b), see paragraphs (1) and (5)(c)(vi) in AMC E 790(a)(2). | Statement |
| **(3)** | For interpreting "sudden encounter" in CS-E 790(a)(2) and "suddenly commencing" in CS-E 790(b), see paragraphs (5)(c)(iv)(D) and (G) in AMC E 790(a)(2). | Statement |
| **(4)** | "Rapid acceleration" and "rapid deceleration" in CS-E 790(b)(2) and (b)(4) should be interpreted as meaning a throttle movement in not more than one second. | Accepted method |
| **(5)** | If the engine is certified on the assumption that the protection device considered under CS-E 790(d) is provided by the aircraft installation, and compliance with CS-E 790(a) to (c) is waived, the engine approval would be endorsed accordingly, and the engine instructions for installation would need to impose the conditions of CS-E 790(d)(1) to (3) on the installation. | Statement |

Point (4) is the only one that supplies a value rather than a pointer, and it is
the value that makes the CS-E 790(b) test reproducible: the deceleration and
acceleration are one-second movements, the same rate as
[[CS-E 745|CS-E 745(a)(2)]].

Point (5) describes what happens when the protection device belongs to the
aircraft. The waiver does not disappear into the installation: the approval is
endorsed and the conditions become installation obligations.

### AMC E 790(a)(1) — design changes and derivative engines

| Ref | Obligation | Strength |
|---|---|---|
| **(a)(1)** | CS-E 790(a)(1) allows, as an alternative to conducting a full engine test, the certification of design changes or derivative engines based on alternative evidence provided by the applicant. Alternative evidence is not intended to be used for the certification of new engines. | Statement |
| **(a)(1)** | Any parametric analysis used to substantiate design changes or derivative engines should fall within a 10 % variation in the critical impact parameter that was used to substantiate the original base engine. | Accepted method |
| **(a)(1)** | This 10 % variation in the critical impact parameters should not be assumed to be a direct tolerance on the applicant's proposed changes to the Take-off Power or to the thrust ratings themselves. | Statement |

The critical impact parameter is described as often associated with the impact
load at the point of contact between the hail and the rotor blade, generally a
function of impact speed, rotor speed and blade twist angle
[AMC E 790(a)(1)].

The closing sentence forestalls a misreading that would otherwise be natural: the
10 % is a bound on the impact parameter, not a licence to raise the rating by
10 %.

### AMC E 790(a)(2) — definitions and phenomena

| Ref | Obligation | Strength |
|---|---|---|
| **(a)(2)(1)** | Critical points are operating conditions within the engine flight envelope at which an engine's operability margin is reduced to a minimum level. Operability margin includes compressor surge and stall margin, fuel control rundown margin, combustor flameout margin and instrumentation sensing errors. | Statement |
| **(a)(2)(1)** | Rundown is the uncommanded reduction of engine rotor speed that will result from the fuel control steady state operating line coinciding with the fuel control acceleration schedule. | Statement |
| **(a)(2)(1)** | Scoop factor is the ratio of nacelle inlet highlight area to the area of the captured air stream tube. | Statement |
| **(a)(2)(1)** | Sustained power or thrust loss is a permanent reduction in power or thrust at the engine's primary power or thrust set parameter, for example rotor speed, engine pressure ratio, torque or shaft power. | Statement |
| **(a)(2)(2)(b)** | Appendix A to CS-E defines the atmospheric conditions of rain and hail for establishing certification test standards. The water concentrations defined there represent ambient conditions, not test conditions at the engine inlet. | Statement |
| **(a)(2)(2)(c)(i)** | The scoop factor increases with decreasing engine speed and increasing aircraft speed, due to the increase in inlet airflow spillage resulting from a smaller captured air stream tube. The amplification is greatest when high flight speed is combined with low power. | Statement |
| **(a)(2)(2)(e)** | Rain or hail ingested through the engine core can produce compressor surge, power loss and flameout, partly as a result of changes in the thermodynamic cycle caused by the presence of water. | Statement |
| **(a)(2)(3)(c)(i)** | Increasing engine power increases rotor speeds and air intake, which improves centrifuging, decreases the adverse scoop factor effect and improves combustor stability margin. | Statement |
| **(a)(2)(3)(c)(ii)** | Avoidance of throttle transients improves stall and surge tolerance, but should not be used by the applicant to show compliance with the rain and hail ingestion specifications. | Statement |
| **(a)(2)(3)(c)(iii)** | Reduced aircraft speed improves centrifuging while decreasing the adverse scoop factor effect. | Statement |

The AMC illustrates the scoop factor, the velocity vectors and the engine control
characteristics with three figures. They are embedded here rather than described,
because a description of a vector diagram cannot be checked against the source.

![[AMC_E_790_a_2_p199.png]]
![[AMC_E_790_a_2_p200.png]]
![[AMC_E_790_a_2_p201.png]]

### AMC E 790(a)(2)(2)(d) — rotorcraft turbine engines

| Ref | Obligation | Strength |
|---|---|---|
| **(a)(2)(2)(d)** | For rotorcraft applications, testing to the specifications of CS-E 790(a)(2) may be replaced by the static rain ingestion test specified in CS-E 790(b). | Permitted |
| **(a)(2)(2)(d)** | While it may be possible to define in-flight rain and hail concentration amplification and attenuation effects for rotorcraft installations similar to aeroplane installations, these effects are typically small. | Statement |
| **(a)(2)(2)(d)** | When compared to aeroplanes, the proportionately higher engine power during descent and the lower flight speeds of rotorcraft result in a small scoop factor effect. | Statement |
| **(a)(2)(2)(d)** | Rotorcraft turbine engines might not have rotating components that centrifuge rain or hail away from the engine. While differences in centrifuging capability between static test conditions and flight operation are an important consideration for turbofan engines, this typically has no applicability to rotorcraft turbine engines. | Statement |
| **(a)(2)(2)(d)** | Increasing the ambient rain concentration from Appendix A values to 4 percent water droplet flow to airflow, by weight, will usually compensate for any flight effects. | Statement |

This paragraph is the justification for the whole CS-E 790(b) alternative. Two
physical arguments carry it: the scoop factor amplification that dominates the
aeroplane case is small for a rotorcraft, and the centrifuging that a fan
provides is absent, so a static test is not unrepresentative. The 4 percent
concentration is what substitutes for the flight effects.

### AMC E 790(a)(2)(4) — critical point analysis

| Ref | Obligation | Strength |
|---|---|---|
| **(a)(2)(4)(a)** | Compliance with CS-E 790(a)(2) is a two-step procedure: identify by analysis the critical operating points for rain and hail ingestion, then test the engine at selected critical points to validate its capability. | Accepted method |
| **(a)(2)(4)(a)** | Develop a critical point analysis and submit it to the Agency for concurrence, prior to the rain and hail ingestion testing. | Accepted method |
| **(a)(2)(4)(b)(i)** | Use the rain and hail threats identified in Figure A1 and Tables A1 to A4 in Appendix A of CS-E, and consider the effects of nominal as well as extreme levels on all relevant engine components and systems. | Accepted method |
| **(a)(2)(4)(b)(ii)** | Quantify the amount of rain and, separately, the amount of hail ingested into the engine core, including amplification and attenuation effects such as the scoop factor effect and the relative velocity effect. | Accepted method |
| **(a)(2)(4)(b)(ii)** | Establish or conservatively assess rain droplet break-up characteristics, and the trajectories of hail particles after impacting nose cones, spinners, inlet surfaces, blades and vanes. | Accepted method |
| **(a)(2)(4)(b)(iii)** | Analyse the entire envelope of power conditions. Rundown and flameout are predominantly low power anomalies, while compressor stability problems could occur at high power. | Accepted method |
| **(a)(2)(4)(b)(iv)** | Analyse the variability of engine parasitics, such as air bleeds and accessory loads, for their effect on the critical points. | Accepted method |

The critical point analysis belongs to the CS-E 790(a)(2) route. Where the
CS-E 790(b) alternative is elected, its test conditions are fixed by the
specification instead, and the analysis is not the compliance path.

### AMC E 790(a)(2)(5)(c)(vi) — acceptance criteria

| Ref | Obligation | Strength |
|---|---|---|
| **(a)(2)(5)(c)(vi)** | Acceptable engine operation precludes flameout, rundown, continued or non-recoverable surge or stall, or a loss of acceleration and deceleration capability. | Accepted method |
| **(a)(2)(5)(c)(vi)** | A momentary flameout, surge or stall that arrests itself without operational intervention, for example without throttle manipulation, is acceptable. | Permitted |
| **(a)(2)(5)(c)(vi)** | If, after test, it is found that damage has occurred, further running or other evidence may be required to show that subsequent Failures resulting from the damage are unlikely to occur before the damage is rectified. | Statement |
| **(a)(2)(5)(c)(vi)** | Measure engine performance before and after the rain and hail ingestion tests to assess steady-state performance changes, normalise the data according to the applicant's standard practices, and evaluate sustained loss or degradation across the full range of engine power. | Accepted method |
| **(a)(2)(5)(c)(vi)** | If compliance with these criteria is dependent upon the functioning of an automatic protection system, such as continuous ignition, auto-relight or a surge recovery system, then the availability of this system is considered to be critical for dispatch. | Statement |
| **(a)(2)(5)(c)(vi)(A)** | Limit the sustained power loss, as a result of a shift or error in measured power against the primary power set parameters following the ingestion test, to 3 percent. | Accepted method |
| **(a)(2)(5)(c)(vi)(A)** | Measured post-ingestion power losses greater than 3 per cent at any value of the primary setting parameter can only be accepted when supported by appropriate assessments of aircraft performance. | Accepted method |
| **(a)(2)(5)(c)(vi)(B)** | A change in the engine corrected power of up to 10 per cent from rated or pre-test levels, using the applicant's normal performance parameters and excluding the primary power setting parameter, is acceptable, provided the criterion for sustained power loss is met. | Permitted |
| **(a)(2)(5)(d)** | Analysis may be used in lieu of, or in combination with, engine testing. The analytical methods should have a sufficient validation basis to justify the accuracy of the predictions, or be shown to yield conservative results, with validation proportional to the complexity of the methods and the criticality of the calculation. | Permitted |

The two numbers are different quantities and both apply. The 3 percent limit is
on **sustained loss** measured against the primary power setting parameter. The
10 percent allowance is on **degradation** in the other performance parameters,
and it is conditional on the 3 percent criterion already being met.

The self-arresting allowance is precise: a momentary event that recovers without
operational intervention is acceptable, which is why
[[CS-E 790|CS-E 790(a)(2)]] and (b) both forbid "continued or non-recoverable"
surge or stall rather than any surge at all.

## Compliance

- Interpretation of the specification's undefined terms, traced to the AMC E 790(a)(2) paragraphs the general AMC names [AMC E 790(1)] to [AMC E 790(3)].
- One-second throttle movements for the rapid deceleration and acceleration of [[CS-E 790|CS-E 790(b)(2)]] and (b)(4) [AMC E 790(4)].
- Where the protection device is supplied by the aircraft, the endorsed engine approval and the CS-E 790(d) conditions imposed through the instructions for installation of [[CS-E 20|CS-E 20(d)]] [AMC E 790(5)].
- For a derivative engine or design change, a parametric analysis within a 10 % variation of the base engine's critical impact parameter [AMC E 790(a)(1)].
- Pre-test and post-test engine performance measurements, normalised, across the full range of engine power [AMC E 790(a)(2)(5)(c)(vi)].
- Sustained power loss within 3 percent, or supported by aircraft performance assessments [AMC E 790(a)(2)(5)(c)(vi)(A)].
- Power degradation within 10 per cent in the non-primary performance parameters [AMC E 790(a)(2)(5)(c)(vi)(B)].
- Dispatch-critical status recorded for any automatic protection system compliance depends on [AMC E 790(a)(2)(5)(c)(vi)], feeding the safety analysis of [[CS-E 510]] and the manuals of [[CS-E 25]].
- Where the CS-E 790(a)(2) route is taken instead, a critical point analysis submitted to the Agency for concurrence before testing [AMC E 790(a)(2)(4)(a)].

## Application to this engine

**The rotorcraft section decides the compliance route.**
[[AMC E 790|AMC E 790(a)(2)(2)(d)]] permits the CS-E 790(a)(2) testing to be
replaced by the static rain ingestion test of [[CS-E 790|CS-E 790(b)]] for
rotorcraft applications. Two physical arguments support it, and both are
turboshaft properties rather than choices: the scoop factor effect is small
because rotorcraft fly slower and hold proportionately higher engine power during
descent, and the engine has no fan to centrifuge water away from the core.

The consequence is that the critical point analysis of
[[AMC E 790|AMC E 790(a)(2)(4)]] — a two-step procedure requiring Agency
concurrence before testing — is not the compliance path here. The CS-E 790(b)
test conditions are fixed by the specification instead.

**The acceptance criteria still apply.** [[AMC E 790|AMC E 790(1)]] and
[[AMC E 790|AMC E 790(2)]] route the terms used in CS-E 790(b) — "unacceptable
mechanical damage", "unacceptable power loss", "flameout, rundown, continued or
non-recoverable surge or stall" — to AMC E 790(a)(2)(5)(c)(vi). The 3 percent and
10 per cent criteria therefore govern the (b) test as well.

**Continuous ignition would become dispatch-critical.** If compliance with the
rain ingestion criteria depends on an automatic protection system, its
availability "is considered to be critical for dispatch"
[AMC E 790(a)(2)(5)(c)(vi)]. [[AMC E 720]] already names ice ingestion and the
icing specifications as reasons a continuously operated ignition system may be
necessary, so the same system could carry both duties — and the dispatch
consequence with them.

**Avoiding transients is not a compliance argument.**
[[AMC E 790|AMC E 790(a)(2)(3)(c)(ii)]] is explicit that avoidance of throttle
transients "should not be used by the applicant to show compliance with the rain
and hail ingestion specifications". The CS-E 790(b) sequence builds the
transients in for exactly that reason.

## Not applicable

- **(a)(2)(2)(c)(ii)(A)** — the relative velocity centrifuging discussion for turbofan and turbojet aeroplane engines, and its rain and hail velocity vector treatment through the fan.
- **(a)(2)(2)(c)(ii)(B)** — the equivalent treatment for turboprop aeroplane engines, including the Propeller solidity effect, the Propeller spinner redirection of hail, and the conservatism of testing without a Propeller. A turboshaft driving a rotorcraft transmission has no propeller, and propeller material is excluded from this vault by scope.
- **(a)(2)(1)**, in part — the scoop factor definition is framed on nacelle inlet highlight area. It is retained above because AMC E 790(a)(2)(2)(d) reasons from the scoop factor being small for a rotorcraft.
- **(1)**, **(5)**, in part — the references to CS-E 790(c), the supersonic aeroplane hailstone test, which does not apply to this engine.

## References

Specification: [[CS-E 790]]
Related: [[Appendix A]] · [[CS-E 540]] · [[CS-E 780]] · [[CS-E 800]] · [[CS-E 650]] · [[CS-E 720]] · [[CS-E 745]] · [[CS-E 500]] · [[CS-E 510]] · [[CS-E 25]] · [[CS-E 20]] · [[AMC E 650]] · [[AMC E 720]]
