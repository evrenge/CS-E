---
id: "AMC E 800"
type: AMC
subpart: E
pages: 219-226
changed_in: []
tags: [bird-strike, ingestion, critical-impact-parameter, test-facility, load-device, impact]
---
# AMC E 800 — Bird Strike and Ingestion

> [!summary]
> One AMC serves CS-E 800, structured by test. For the single large bird it
> requires an analysis of the most critical exposed location and states that
> complete power loss afterwards is acceptable. It then covers test facility
> conditions — the critical impact parameter and its 10 % tolerance, inlet
> distortion from the gun arrangement, power measurement accuracy, and the
> turboshaft load device case — followed by definitions of impact, ingestion and
> first stage rotor blades, and general provisions on engine configuration and
> alternative evidence.

## Requirement

### AMC E 800(1)(a) — single large bird

| Ref | Obligation | Strength |
|---|---|---|
| **(1)(a)(i)** | The applicant is required to provide an analysis substantiating the definition of the "most critical exposed location" of CS-E 800(b)(1)(iii). | Required |
| **(1)(a)(i)** | Include in that determination evidence where necessary on: the effect of the bird strike on rotating components, excluding any spinner; the compressor casing strength; the possibility of multiple blade Failures; and the strength of the engine structure and main shafts relative to the unbalance and the excess torque that are likely to occur. | Accepted method |
| **(1)(a)(ii)** | Rig tests may be used to determine whether a bird of a particular size will pass through the inlet, to comply with CS-E 800(b)(1)(ii)(A). | Permitted |
| **(1)(a)(iii)** | The complete loss of power or thrust is acceptable after the ingestion of the single large bird. | Statement |

Point (iii) sets the acceptance boundary for the large bird test, and that
boundary is more permissive than it first appears. The engine may stop producing power entirely; what
[[CS-E 800|CS-E 800(b)(2)]] forbids is a Hazardous Engine Effect as defined in
[[CS-E 510|CS-E 510(g)]].

Point (i) is a design-level analysis, not a test observation. The four items it
names — rotating component damage, casing strength, multiple blade Failure, and
structure and shaft strength against unbalance and excess torque — connect to
[[CS-E 520]] and to the blade containment work of [[CS-E 810]].

### AMC E 800(2) — test facility related conditions

| Ref | Obligation | Strength |
|---|---|---|
| **(2)(a)** | Calibrate the test facility appropriately, so that controlling parameters defined by the analysis of the critical conditions which cannot be accurately controlled, such as bird speed and aiming locations, are within an acceptable tolerance. | Accepted method |
| **(2)(a)** | Derive that tolerance band from an analysis of the sensitivity of the critical impact parameter to variations in the controlling parameters. | Accepted method |
| **(2)(a)** | The critical impact parameter is a parameter used to characterise the state of stress, strain, deflection, twist, or other condition which will result in the maximum impact damage to the engine for the prescribed bird ingestion condition. It is generally a function of bird mass, bird velocity, rotor speed, impact location and blade geometry. | Statement |
| **(2)(a)** | Identify and understand the most limiting parameter prior to any demonstration, since any unplanned variations in controlling test parameters will be evaluated for their effect on the critical impact parameter and the CS-E 800 specifications. | Accepted method |
| **(2)(a)** | For certification tests, the critical impact parameter variation should not be greater than 10 % as a function of any deviation in the controlling parameters of the test. | Accepted method |
| **(2)(b)** | Identify before the test any air distortion in the engine inlet induced by the installation, and especially the gun arrangement, which can artificially reduce the stability margins of the engine. | Accepted method |
| **(2)(c)** | Measure power by a means which can be shown to be accurate throughout the test, to enable power to be set without undue delay and maintained to within ± 3 percentage points of the specified levels. | Accepted method |
| **(2)(c)** | Identify and have approved before the test any inability of an alternative load device to control the power level tolerance band to the desired level, and justify any exceedance of the ± 3 % band in relation to the objectives of CS-E 540(b) or CS-E 800(d). | Accepted method |
| **(2)(d)** | If turboshaft engines are tested using an alternative load device which could induce different engine response characteristics than when the engine is installed in the aircraft, monitor the interface with the test facility and aircraft systems during the test, and use it to determine how the engine would respond in a representative installation and to ensure that the engine would then comply with the specifications. | Accepted method |
| **(2)(e)** | Provide input and output data across the engine interfaces with the aircraft systems in the instructions for installation, regarding the expected interaction of the engine with these systems during ingestion events. Of particular interest would be dynamic interactions such as auto surge recovery. | Accepted method |

Point (2)(a) states which parameter is critical for which engine type: "The CIP
for most modern turbofan Engines is the fan blade leading edge stress… For
turboprop and turbojet Engines, a core feature will most likely be the critical
consideration." [AMC E 800(2)(a)] It does not name a turboshaft. What reaches
this engine is the closing sentence, which is written for every design:
"Regardless of the Engine design, the most limiting parameter should be
identified and understood prior to any demonstration" [AMC E 800(2)(a)].

Point (2)(d) is written for this engine type. It names no load device. It
applies wherever a turboshaft engine is tested on an alternative load device
that "could induce different Engine response characteristics" from the installed
condition, and it then requires the interface with the test facility and aircraft
systems to be monitored during the test and used to predict the installed
behaviour [AMC E 800(2)(d)].

### AMC E 800(3) — impact, ingestion and first stage rotor blades

| Ref | Obligation | Strength |
|---|---|---|
| **(3)(a)** | The front of the engine is any part of the engine which can be struck by a bird. This includes but is not limited to a nose cone or spinner on the compressor rotor, an engine inlet guide vane assembly including the centrebody, any protection device, and inlet-mounted components. | Statement |
| **(3)(b)** | Ingestion is the passage of a bird into the rotating blades. | Statement |
| **(3)(c)** | "First stage rotor blades" in CS-E 800 includes the first stage of any compressor rotor which is susceptible to a bird strike or bird ingestion. These first stage rotor blades are considered to be part of the front of the engine. | Statement |

The three definitions separate what [[CS-E 800|CS-E 800(f)]] evaluates from what
[[CS-E 800|CS-E 800(b)]] tests. A bird that strikes the nose cone, guide vanes or
a protection device without reaching the rotating blades is an impact, not an
ingestion. The first stage rotor blades, however, count as part of the front
of the engine. They therefore appear in both.

### AMC E 800(4) — general

| Ref | Obligation | Strength |
|---|---|---|
| **(4)(a)** | The engine configuration for the test should comply with CS-E 140. | Accepted method |
| **(4)(a)** | The normal functioning of automatic systems that do not require pilot intervention is acceptable, provided that the dispatch criticality is addressed in the appropriate documentation. | Permitted |
| **(4)(a)** | Systems which are not part of the engine should be disabled. | Accepted method |
| **(4)(a)** | Any OEI ratings do not have to be taken into account for compliance with CS-E 800(d). | Relief |
| **(4)(b)** | The minimum engine referred to in CS-E 800(b)(1)(i) is a new engine that exhibits the type design's most limiting operating parameters with respect to the bird ingestion conditions prescribed by CS-E 800. These parameters include, but are not limited to, the power, turbine temperature and rotor speeds. | Statement |
| **(4)(c)** | CS-E 800(g)(1) is intended to allow the certification of design changes or derivative engines without conducting a full engine test. It is not intended, considering the present state of the art, to be used for the certification of new engines. | Statement |
| **(4)(c)** | Any parametric analysis used to substantiate derivative engines should fall within a 10 % variation in the critical impact parameter that was used to substantiate the original base engine. | Accepted method |
| **(4)(c)** | This 10 % variation should not be assumed to be a direct tolerance on the applicant's proposed changes to the take-off power ratings themselves. | Accepted method |
| **(4)(d)** | Any analytical means used in place of a test demonstration, where analysis is permitted, should be validated by evidence based on representative tests, and should have demonstrated its capability to predict engine test results. | Accepted method |
| **(4)(e)** | When reference is made to an "exposed location", this should be understood to be any part of the engine which is not shielded. | Accepted method |
| **(4)(f)** | Where the CS-E 810 test is proposed as an alternative to the single large bird test, under CS-E 800(g)(2), the demonstration should include consideration of unbalance, as well as effects of the axial loading from the bird strike on bearings or other structures. | Accepted method |
| **(4)(g)** | Artificial birds may be used in the tests if they are internationally standardised and are acceptable to the Agency. | Permitted |

The automatic systems allowance in (4)(a) carries the same consequence as the
rain and hail case: normal functioning is acceptable "provided that the dispatch
criticality is addressed in the appropriate documentation". A system relied on to
pass the test becomes something the dispatch analysis must account for.

The minimum engine definition in (4)(b) is the worst-case new engine, not an
average one, and it is why [[CS-E 800|CS-E 800(b)(1)(i)]] requires the hottest-day
account.

Sub-point (4)(f) is the condition set on a waiver this engine may want.
[[CS-E 800|CS-E 800(g)(2)]] allows the single large bird test of CS-E 800(b)(1)
to be waived "if it can be shown by test or analysis that the specifications of
CS-E 810(a) are more severe" [CS-E 800(g)(2)], so the blade Failure test of
[[CS-E 810]] stands in its place. Where that route is taken,
(4)(f) says the demonstration should include consideration of unbalance. It
should also cover the effects of the axial loading from the bird strike on
bearings or other structures [AMC E 800(4)(f)]. The axial loading is the item a
blade Failure test does not itself impose; the unbalance is already the subject
of the out-of-balance run of [[AMC E 810|AMC E 810(3)]].

## Compliance

- Analysis of the most critical exposed location, covering rotating component effects, compressor casing strength, multiple blade Failures, and structure and shaft strength against unbalance and excess torque [AMC E 800(1)(a)(i)].
- Rig test evidence on whether a given bird size passes through the inlet, where used [AMC E 800(1)(a)(ii)].
- Identification of the critical impact parameter for this engine, with the sensitivity analysis that sets the facility tolerance band and the 10 % variation limit [AMC E 800(2)(a)].
- Pre-test identification of any inlet air distortion induced by the facility or gun arrangement [AMC E 800(2)(b)].
- Power measurement accuracy evidence to ± 3 percentage points, with any load device limitation identified and approved before the test [AMC E 800(2)(c)].
- Monitoring of the test facility interface for the alternative load device, and its use to determine the installed response [AMC E 800(2)(d)].
- Engine and aircraft system interface data on ingestion event interactions, in the instructions for installation of [[CS-E 20|CS-E 20(d)]] [AMC E 800(2)(e)].
- Test engine configuration conforming to [[CS-E 140]], with non-engine systems disabled and the dispatch criticality of any automatic system documented [AMC E 800(4)(a)].
- Minimum engine definition, identifying the type design's most limiting power, turbine temperature and rotor speeds [AMC E 800(4)(b)].
- Validation evidence for any analytical means used in place of a test [AMC E 800(4)(d)].

## Application to this engine

The general, facility, impact and definitional sections apply. The sections
serving CS-E 800(c), (d) and (e) do not, and are recorded below.

**The critical impact parameter must be identified before any test.**
AMC E 800(2)(a) names fan blade leading edge stress for most modern turbofans and
a core feature for turboprop and turbojet engines. It says nothing about a
turboshaft. The obligation that does reach this engine is the one that applies
"regardless of the Engine design": the most limiting parameter is identified
and understood prior to any demonstration. The AMC makes this a precondition
rather than a result.

[VERIFY: which feature is the critical impact parameter for this engine.
AMC E 800(2)(a) assigns one to turbofan, turboprop and turbojet engines and not
to a turboshaft, so it follows from the engine's own design rather than from the
AMC.]

**The load device provision is written for this engine type.**
AMC E 800(2)(d) addresses turboshaft engines tested on an
alternative load device. The bed cannot reproduce a rotor system's inertia and
response, so the interface must be monitored and used to predict the installed
behaviour. This connects to [[CS-E 140|CS-E 140(d)]] on accessory drive loading
and to [[CS-E 520|CS-E 520(c)(2)]] on the data provided to the aircraft
constructor.

**Automatic systems become dispatch-critical.** The same consequence appears in
[[AMC E 790|AMC E 790(a)(2)(5)(c)(vi)]] for rain and hail. If an auto surge
recovery or continuous ignition system is relied on to pass a bird ingestion
test, its availability has to be addressed in the dispatch documentation. This
feeds the safety analysis of [[CS-E 510]] and the manuals of [[CS-E 25]].

**The OEI relief in (4)(a) confirms the reading of the tests.** Any OEI ratings
do not have to be taken into account for CS-E 800(d) compliance. That sub-point
is relieved for this engine by [[CS-E 800|CS-E 800(g)(7)]] in any case. The
statement nonetheless confirms that the bird tests are run against the
all-engines-operating ratings rather than the OEI ones.

## Not applicable

- **(1)(b)**, including **(1)(b)(i)** to **(1)(b)(vii)** — the large flocking bird advisory material, serving CS-E 800(c), which applies to engines with an inlet throat area equal to or greater than 2.5 m². This includes the blade span target location figure at page 220, which is therefore not embedded here, the 20-minute run-on guidance, the momentary thrust drop allowances, and the component test provisions of CS-E 800(g)(3)(ii).
- **(1)(c)**, including **(1)(c)(i)** to **(1)(c)(iv)** — the medium and small flocking bird advisory material, serving CS-E 800(d). That sub-point is relieved for this engine by CS-E 800(g)(7), which excuses an engine to be installed in a multi-engine rotorcraft from the medium and small bird specifications.
- **(1)(d)**, including **(1)(d)(i)** to **(1)(d)(vi)** — the core engine flocking bird ingestion test material, serving CS-E 800(e), which applies to turbofan engines. This covers climb rotor speed determination, target selection, run-on sequence requirements and core ingestion prediction analyses.
- **(2)(e)**, in part — propeller autofeather, named as a dynamic interaction of interest. A turboshaft driving a rotorcraft transmission has no propeller.
- **(3)(a)**, **(3)(c)**, in part — the fan cases: a nose cone or spinner on the fan, ducted, unducted and aft fan designs, and blades on two different rotors for aft fan designs. The compressor rotor cases in the same sentences apply.
- **(4)(a)**, in part — the propeller autofeather system, named as an example of a system not part of the engine that should be disabled.
- **(2)(a)**, in part — three paragraphs of turbofan-specific critical impact parameter discussion: slice mass and the shift from leading-edge to blade-root stress, part-span-shroud shingling, and unshrouded wide-chord blade twist. The turbofan and turboprop critical impact parameter sentence before them is kept, because it defines the parameter itself.
- **(2)(c)**, in part — the ± 3 % power band allowance for a sustained high vibratory condition after the first 2 minutes of the CS-E 800(d) test. That test is relieved for this engine by CS-E 800(g)(7).
- **(2)(d)**, in part — the turboprop and propeller cases among the dynamic interactions, including the coupled propeller case.
- **(4)(b)**, in part — the reference to CS-E 800(d)(1)(i) alongside CS-E 800(b)(1)(i). CS-E 800(d) is relieved for this engine.

## References

Specification: [[CS-E 800]]
Related: [[CS-E 540]] · [[CS-E 510]] · [[CS-E 520]] · [[CS-E 700]] · [[CS-E 810]] · [[CS-E 140]] · [[CS-E 25]] · [[CS-E 20]] · [[CS-E 790]] · [[AMC E 790]] · [[AMC E 540]]
