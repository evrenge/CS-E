---
id: "AMC E 910"
type: AMC
subpart: E
pages: 244-244
changed_in: []
tags: [relight, in-flight-restart, rotor-lock, rapid-relight, flight-test]
---
# AMC E 910 — Relighting In Flight

> [!summary]
> Three parts. Part (1) points to an aeroplane certification AMC for the
> objectives and recommends coordination with the aircraft applicant. Part (2)
> names altitude testing and flight testing as acceptable means. Part (3) names
> two specific threats that the demonstration must address: rapid relight after
> an in-flight shutdown, and rotor-lock.

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | AMC 25.903(e)(2) contains guidance that can be used to establish the objectives of the demonstration of compliance of the engine with CS-E 910. | Statement |
| **(1)** | Active coordination between the engine type-certificate applicant and the aircraft type-certificate applicant is recommended. | Accepted method |
| **(2)** | Either engine altitude testing or engine flight testing are considered to be acceptable means of demonstrating compliance. Other appropriate tests or evidence can be proposed by the applicant. | Accepted method |
| **(3)(a)** | Consider rapid relight after an in-flight engine shutdown. Where a functioning engine is shut down and the pilot quickly initiates a restart command, after an initial delay of at least 5 seconds to simulate the pilot response time during an actual in-flight event, the engine design, and in particular the Engine Control System, should not introduce any unnecessary delay in the engine returning to the previous power setting. | Accepted method |
| **(3)(b)** | Determine the potential for rotor-lock and its impact on the capability of the engine to relight in flight. | Accepted method |
| **(3)(b)** | Base any rotor-lock assessment on conservative assumptions that include but are not limited to clearances, taking into account tolerances, the initial conditions, flight effects, thermal effects and the dwell time. All the engine rotors should be considered. | Accepted method |
| **(3)(b)** | Where a demonstration through flight test is proposed, it should represent a set of conservative operating assumptions for the engine in terms of rotor-lock, or it should be supplemented by an analysis that satisfactorily addresses the conservative operating assumptions. | Accepted method |

### The two threats

**Rapid relight** is a control system criterion, not a mechanical one. The
5-second delay is a floor on the simulated pilot response, not a target: the
restart command comes "after an initial delay of at least 5 seconds"
[AMC E 910(3)(a)]. What is then assessed is whether the engine, "and in
particular the Engine Control System", adds any unnecessary delay before the
previous power setting is regained.

**Rotor-lock** is not defined in AMC E 910, nor anywhere else in CS-E
Amendment 8. What the AMC gives instead is the set of assumptions the assessment
must rest on: clearances taking tolerances into account, the initial conditions,
flight effects, thermal effects and the dwell time [AMC E 910(3)(b)]. The list is
open — the source writes "include but are not limited to" — and every engine
rotor is in scope, not only the rotor the relight is initiated on.

[VERIFY: the meaning of rotor-lock is assumed rather than stated. The five named
contributors point at a seizure arising from differential thermal growth between
rotor and casing during the post-shutdown dwell, but the source does not say so,
and the assessment scope should be agreed with the Agency.]

The flight-test route to rotor-lock is qualified. A flight test represents one
set of conditions, so it must either be conservative in itself or be supplemented
by an analysis that covers the conservative assumptions [AMC E 910(3)(b)].

## Compliance

- A relight demonstration plan stating the chosen route: engine altitude testing, engine flight testing, or another proposed means [AMC E 910(2)].
- Evidence of coordination with the aircraft type-certificate applicant on the demonstration objectives [AMC E 910(1)].
- Rapid relight demonstration with a restart command after at least 5 seconds, showing no unnecessary control system delay in returning to the previous power setting [AMC E 910(3)(a)].
- Rotor-lock assessment for all engine rotors, on conservative assumptions covering clearances and tolerances, initial conditions, flight effects, thermal effects and dwell time [AMC E 910(3)(b)].
- Where rotor-lock is shown by flight test, either a conservative test condition set or a supplementary analysis [AMC E 910(3)(b)].

## Application to this engine

The AMC applies. Rotor-lock is the part that bears hardest on a turboshaft: the
gas generator spool and the free power turbine cool at different rates and the
power turbine remains coupled to the rotor drive system, so its dwell condition
after a shutdown differs from anything a turbofan sees.

**The rapid relight case is the OEI case.**
On a multi-engine rotorcraft, a shutdown that is quickly reversed is precisely
the event the OEI ratings cover on the remaining engine. The criterion in
[AMC E 910(3)(a)] is that the returning engine adds no unnecessary delay, which
places the relight schedule inside the control system assessment of
[[CS-E 50]] and alongside the power response requirements of [[CS-E 745]].

**The 5-second delay is not the 30-second rating.**
[AMC E 910(3)(a)] sets 5 seconds as a simulated pilot response time before the
restart command. It has no relationship to the 30-Second OEI rating period. The
two are separate clocks and are not to be conflated.

**All the engine rotors means the power turbine as well.**
The free power turbine is driven by the rotor drive system through the
transmission and may continue to turn after the gas generator has stopped. Its
rotor-lock assessment is therefore made with the installation in view, and the
assumptions are declared under [[CS-E 30]].

[VERIFY: the reference AMC 25.903(e)(2) is aeroplane certification material,
outside CS-E and outside the scope of this vault. AMC E 910(1) offers it for the
objectives of the demonstration only. Whether an equivalent rotorcraft objective
set is agreed with the Agency is an open item.]

## Not applicable

- **(1)** — the aeroplane origin of AMC 25.903(e)(2) itself. The reference is kept because AMC E 910(1) names it as the source of the demonstration objectives; the CS-25 requirement it serves is not a CS-E obligation and is not reproduced.

## References

Specification: [[CS-E 910]]
Related: [[CS-E 50]] · [[CS-E 745]] · [[CS-E 690]] · [[CS-E 30]] · [[CS-E 20]] · [[AMC E 50]] · [[AMC E 690]]
