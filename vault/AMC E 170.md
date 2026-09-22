---
id: "AMC E 170"
type: AMC
subpart: A
pages: 62-63
changed_in: []
imports: [AMC-20]
tags: [test, systems, eecs, hirf, lightning, bonding, installation-limitation, degraded-dispatch]
---
# AMC E 170 — Engine systems and component verification

> [!summary]
> This AMC explains what CS-E 170 is for and then spends most of its length on
> the Engine Control System. It gives examples of what the endurance test misses,
> asks the manufacturer to define the additional testing itself, and sets out
> the electromagnetic case: functional integrity under electric and
> electromagnetic induction, the qualified environment recorded as an installation
> limitation, and the bonding assumptions that a partial HIRF or lightning test
> depends on.

## Requirement

### Intent and scope

| Ref | Obligation | Strength |
|---|---|---|
| — | The intent of CS-E 170 is to define the additional tests or analysis necessary for systems or components not necessarily tested during the endurance test of CS-E 740. | Statement |
| — | The other specifications of CS-E do not always provide sufficient testing to cover all the conditions — pressure, temperature, vibration and others — which could affect the airworthiness of a piece of equipment throughout the declared flight envelope and within all declared installation conditions. | Statement |
| — | The reasons for testing under CS-E 170 "include, but are not limited to" the examples given. | Statement |
| — | Example: testing is required in support of CS-E 50(a) for validation throughout the declared flight envelope and within all declared installation conditions. | Statement |
| — | Example: an over-speed protection system, or a torque limiter, is unlikely to be tested during the scheduled tests of CS-E 740. | Statement |
| — | Example: an Electronic Engine Control System has a mechanical back-up which is not normally used during the endurance test. | Statement |
| — | Example: demonstration that a Failure indicating system, on which dependence is placed in the engine safety analysis, will function satisfactorily when required. | Statement |
| — | Define all necessary testing and analysis for the accessories or systems needing specific substantiation, in addition to the certification tests performed on a complete engine, with attention paid to their location and operating conditions. | Accepted method |
| — | Unless it is necessary to test the functioning of a system itself, substantiation of individual components may be made separately from the system they are part of. | Permitted |

### The Engine Control System in its installed environment

| Ref | Obligation | Strength |
|---|---|---|
| — | The objective of CS-E 50(a), in conjunction with CS-E 80 or CS-E 170, is to demonstrate that the Engine Control System can perform its intended function in its installed environment. | Statement |
| — | Electronic Engine Control Systems are sensitive to lightning and other electromagnetic interference, and these conditions can be common to more than one engine. | Statement |
| — | Maintain the functional integrity of the Engine Control System when subjected to designated levels of electric or electromagnetic induction, including effects from external radiation and lightning. | Accepted method |
| — | Enter the environment to which the Engine Control System and its components are qualified, including radiated and conducted emissions, into the engine instructions for installation. That environment is considered an installation limitation for the installer. | Accepted method |
| — | Where HIRF or lightning tests are carried out on anything other than a representative complete engine, demonstrate that the assumed electrical bonding between the tested elements and the main engine earth is valid, by examination of the type design drawings, electrical continuity checks, or actual inspection of a representative engine. | Accepted method |
| — | Where the installer specifies the environmental conditions of the installation, compliance may be demonstrated by meeting the specified installation specifications. | Permitted |
| — | Where the installation specifications are not specified or not known, environmental conditions of a typical installation may be assumed. | Permitted |
| — | Establish by analysis or test that all components of the Engine Control System — electronics units, sensors, harnesses, hydromechanical elements and any other relevant elements or units — operate properly in their declared environment. | Accepted method |
| — | The environmental limits are not imposed by the rules, but should be representative of the environments expected to be encountered in the engine installation. | Accepted method |
| — | Advisory material for environmental effects other than lightning and electromagnetic effects can be found in AMC E 80. | Statement |
| — | Additional means may be found in AMC E 80, or in AMC 20-1 and AMC 20-3 for Electronic Engine Control Systems. | Permitted |
| — | Give due consideration to dispatching in each approved degraded state when meeting these environmental concerns. | Accepted method |
| — | See AMC E 80 for additional specific means. | Statement |

AMC E 170 is written as continuous prose with no numbered sub-points, so the
`Ref` cells carry no sub-point identifier.

The environmental limits sentence decides who sets the numbers. The limits "are
not imposed by the rules, but should be representative of the environments that
are expected to be encountered in the Engine installation" [AMC E 170]. The
applicant sets the numbers, and the accepted method is that they are
representative. Once declared, they become an installation limitation for the
installer through the instructions for installation [AMC E 170].

The bonding clause creates a dependency. The results of a HIRF or lightning test
on a subset of the engine may depend on the validity of the bonding assumed
between the tested elements and the main engine earth [AMC E 170]. AMC E 170
names three ways to show that bonding. They are the same three routes that
[[AMC E 135]] gives for electrical bonding generally.

## Compliance

- List of systems and components requiring substantiation beyond the complete-engine certification tests, with their location and operating conditions [AMC E 170].
- Additional test or analysis results for each, including protective functions such as over-speed protection or a torque limiter, and any Failure indicating system relied on in the safety analysis of [[CS-E 510]] [AMC E 170].
- Functional integrity evidence for the Engine Control System under electric and electromagnetic induction, external radiation and lightning [AMC E 170].
- Declared qualification environment for the Engine Control System, including radiated and conducted emissions, entered in the instructions for installation as an installation limitation [AMC E 170], within the manuals of [[CS-E 20|CS-E 20(d)]].
- Bonding validity demonstration where HIRF or lightning testing used less than a representative complete engine [AMC E 170], consistent with [[CS-E 135]] and [[AMC E 135]].
- Component-level environmental substantiation for electronics units, sensors, harnesses and hydromechanical elements [AMC E 170], alongside [[AMC E 80|AMC E 80(1)]].
- Assessment of each approved degraded dispatch state against the environmental conditions [AMC E 170].

## Application to this engine

The AMC applies in full, and the Electronic Engine Control System material is
directly on point: `engine_profile.md` declares an EECS-FADEC with full
authority.

Two of the four examples reach this engine specifically. An over-speed protection
system or torque limiter is unlikely to be exercised by the scheduled tests of
[[CS-E 740]]. A Failure indicating system relied on in the safety analysis is a
case for demonstration that it functions when required [AMC E 170]. Where the
safety analysis of [[CS-E 510]] relies on the OEI usage alerting and recording
means of [[CS-E 60|CS-E 60(d)]], those means fall under this example.

The mechanical back-up example does not arise unless the EECS has one.

[VERIFY: whether the EECS has a mechanical back-up. `engine_profile.md` declares
full authority but does not record a back-up. If one exists, AMC E 170 names it
as a case for CS-E 170 testing, because it is not normally used during the
endurance test.]

The degraded dispatch sentence reaches beyond CS-E 1030. `engine_profile.md`
records that time-limited dispatch is not claimed, so there is no time-limited
dispatch regime under CS-E 1030. The AMC's wording is broader than that. It
refers to "each approved degraded state" [AMC E 170]. Any approved degraded
state of the control system is therefore in scope, whether or not time-limited
dispatch is claimed.

[VERIFY: whether any approved degraded state of the Engine Control System exists
for this engine, given that time-limited dispatch is not claimed. The AMC asks
for due consideration of each such state against the environmental conditions.]

AMC E 170 names AMC 20-1 and AMC 20-3 as additional means for Electronic Engine
Control Systems. It also directs the reader to [[AMC E 80]] for environmental
effects other than lightning and electromagnetic effects.

AMC 20-1 and AMC 20-3 are now held, as AMC 20-1A and AMC 20-3B. The additional
means for an EECS is [[AMC 20-3B]], which interprets the pass and fail criteria
of CS-E 170 for HIRF and lightning as no adverse effect on the functionality of
the system, and lists what counts as adverse [ext AMC 20-3B(6)(e)(iii)]. It also
sets the form of the test: the installed control system with representative
engine-aircraft interface cables, tested as a system rather than as components
[ext AMC 20-3B(6)(e)(ii)]. AMC 20-1A is the aircraft-level companion. It
addresses the certification of the installation of propulsion systems with
electronic control systems, which is the installer's task [ext AMC 20-1A 3].

## Not applicable

- The reference to the endurance test of **CS-E 440**, and the worked example of a pressure relief valve in the inlet manifold of a turbocharged engine. Both are piston engine material in Subpart C. For this engine the endurance test is [[CS-E 740]].

## References

Specification: [[CS-E 170]]
Related: [[CS-E 50]] · [[CS-E 80]] · [[CS-E 60]] · [[CS-E 135]] · [[CS-E 510]] · [[CS-E 740]] · [[CS-E 20]] · [[AMC E 80]] · [[AMC E 135]] · [[AMC E 50]]
External: [[AMC 20-3B]]

## Amendment history

Unchanged at Amendments 7 and 8. The paragraph carries `[Amdt. No.: E/1]`.
