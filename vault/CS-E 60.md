---
id: "CS-E 60"
type: CS
subpart: A
pages: 38-39
changed_in: []
tags: [instruments, oei, monitoring, installation]
---
# CS-E 60 — Provision for Instruments

> [!summary]
> The engine must make provision for the instruments needed for operation within
> its limitations, and must tell the installer which ones are mandatory and how
> accurate they must be. Instrumentation and control paths must be segregated so
> that the probability of a Fault propagating between them is consistent with
> its Failure effect. A rotorcraft engine with 30-Second and 2-Minute OEI
> ratings must also alert the pilot, record every use by a means which cannot be
> reset in flight, and permit retrieval of the record.

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| **(a)** | Make provision for installing the instrumentation necessary to ensure operation within the engine operating limitations. | Required |
| **(a)** | Where the safety analysis or any other compliance demonstration depends on instrumentation that is not otherwise mandatory in the assumed aircraft installation, specify that instrumentation in the engine instructions for installation and declare it mandatory in the engine approval documentation. | Required |
| **(b)** | Provide a list of the instruments necessary for control of the engine in the engine instructions for installation. | Required |
| **(b)** | State the overall limits of accuracy and transient response required of those instruments, so the suitability of the instruments as installed may be assessed. | Required |
| **(c)** | Segregate the sensors, their wiring and their signal conditioning, physically and electrically, to the extent necessary to keep the probability of a Fault propagating between instrumentation and monitoring functions and control functions consistent with the Failure effect of the Fault. | Required |
| **(d)(1)** | Have means, or provision for means, to alert the pilot when the engine is at the 30-Second OEI and the 2-Minute OEI Power levels, when the event begins, and when the time interval expires. | Required if claimed |
| **(d)(2)(i)** | Have means, or provision for means, which cannot be reset in flight, to automatically record each usage and duration of power at the 30-Second and 2-Minute OEI Power levels. | Required if claimed |
| **(d)(2)(ii)** | Have means, or provision for means, which cannot be reset in flight, to alert maintenance personnel in a positive manner that the engine has been operated at either or both of those levels, and to permit retrieval of recorded data. | Required if claimed |
| **(d)(3)** | Have means, or provision for means, to enable routine verification of the proper operation of the means required by (d)(1) and (d)(2). | Required if claimed |
| **(e)** | Provide instrumentation enabling the flight crew to monitor the functioning of the turbine cooling system, unless evidence shows one of (e)(1), (e)(2) or (e)(3). | Required |
| **(e)(1)** | Exemption from (e) where other existing instrumentation provides adequate warning of Failure or impending Failure. | Relief |
| **(e)(2)** | Exemption from (e) where Failure of the cooling system would not lead to Hazardous Engine Effects before detection. | Relief |
| **(e)(3)** | Exemption from (e) where the probability of Failure of the cooling system is Extremely Remote. | Relief |
| **(e)** | Promulgate appropriate inspections in the relevant manuals. | Required |

Sub-point (d) applies to "Rotorcraft turbine Engines having 30-Second and
2-Minute OEI Power Ratings" [CS-E 60(d)]. Those ratings are elective under
[[CS-E 40|CS-E 40(b)(3)]], so the strength is Required if claimed. Once claimed,
every duty in (d) is mandatory.

The phrase "means, or provision for means" runs through all of (d). The engine
applicant may supply the function itself, or supply only the provision for it
and leave the function to the rotorcraft. Either path satisfies the
specification [CS-E 60(d)]; see [[AMC E 60|AMC E 60(d)(3)]] for the case where
the recording or retrieval system is not part of the engine.

The inspections sentence closes (e) and is not conditional on the relief. Where
the applicant takes (e)(1), (e)(2) or (e)(3), the inspections are still required
[CS-E 60(e)].

## Compliance

- Engine instructions for installation identifying the instrumentation needed for operation within the limitations, and the engine approval documentation declaring the non-standard instrumentation mandatory [CS-E 60(a)]. Accepted means: [[AMC E 60|AMC E 60(1)]].
- List of instruments necessary for control of the engine, with their overall limits of accuracy and transient response [CS-E 60(b)]. These limits are the ones [[CS-E 40|CS-E 40(g)]] requires the ratings to account for.
- Segregation evidence for sensors, wiring and signal conditioning, referenced to the Fault's Failure effect [CS-E 60(c)]. The Failure effect classification comes from the safety analysis of [[CS-E 510]].
- Sensing-position justification for parameters such as oil pressure [CS-E 60(a)]. Accepted means: [[AMC E 60|AMC E 60(2)]].
- OEI alerting, recording, retrieval and verification means, or the provision for them, with the associated development assurance level [CS-E 60(d)]. Accepted means: [[AMC E 60|AMC E 60(d)]].
- Turbine cooling system instrumentation, or evidence supporting one of the three exemptions [CS-E 60(e)].
- Inspections promulgated in the relevant manuals [CS-E 60(e)].

## Application to this engine

Sub-point (d) is triggered. `engine_profile.md` declares 30-Second OEI and
2-Minute OEI, which are exactly the two ratings named in (d) [CS-E 60(d)].
Continuous OEI is also declared but does not trigger (d); the sub-point names
only the 30-Second and 2-Minute levels.

The recording means must not be resettable in flight [CS-E 60(d)(2)]. If the
recording or retrieval system sits in the rotorcraft rather than the engine, the
applicant supplies the provision and states the interface in the instructions
for installation [AMC E 60(d)(3)]. That makes the system a component outside the
engine type design, so [[CS-E 30|CS-E 30(b)]] requires its interface conditions
and reliability specifications as well [CS-E 30(b)].

Sub-point (c) is load-bearing for a full-authority EECS. Monitoring and control
may share sensors and wiring in an integrated control system, so the segregation
argument must be explicit rather than assumed [CS-E 60(c)]. The acceptable
propagation probability is set by the Failure effect of the Fault, which links
this paragraph to [[CS-E 510]] and to [[CS-E 50|CS-E 50(d)]].

## References

Accepted means: [[AMC E 60]]
Related: [[CS-E 40]] · [[CS-E 50]] · [[CS-E 30]] · [[CS-E 510]] · [[CS-E 20]]
External: [[CS 29.45]] · [[CS 29.1305]] · [[CS 27.45]] · [[CS 27.1305]]

## Amendment history

Unchanged at Amendments 7 and 8. The paragraph carries `[Amdt. No.: E/1]`.
[[AMC E 60]] was amended at Amendment 7.
