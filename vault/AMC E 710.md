---
id: "AMC E 710"
type: AMC
subpart: E
pages: 136-136
changed_in: []
tags: [rotor-locking, continued-rotation, failure-modes, restart, deterioration]
---
# AMC E 710 — Rotor locking tests

> [!summary]
> Five points serve CS-E 710. The first states what the device is for: it is an
> option that removes the need to comply with CS-E 525. The rest guard against
> the ways that trade can go wrong — the device failing and letting rotation
> continue, deteriorating unnoticed through disuse, or being activated
> inadvertently in flight. The flight crew must also be able to unlock for a
> restart attempt and re-lock if it fails.

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | The applicant has the option to incorporate a rotor-locking device into the type design of the engine in order not to have to comply with CS-E 525. Activation of the device will stop and prevent subsequent continued rotation of the engine rotors during flight when the engine is not operating. | Permitted |
| **(1)** | The device is part of the engine type design and is subject to the same test criteria as other components on the engine. | Statement |
| **(1)** | The rotor-locking device should satisfy the operational and endurance test specifications of CS-E 710 while the engine is subjected to the environmental conditions that result in the maximum rotational torque. | Accepted method |
| **(1)** | The assessment of the maximum rotational torque should consider both damaged and undamaged engine rotors. | Accepted method |
| **(2)** | An engine that is shut down and that has a rotor locking device but continues to rotate due to Failure of the rotor locking device might not satisfy the safety objectives of CS-E 525. | Statement |
| **(2)** | Assess the design of the rotor-locking device for all possible Failure modes under CS-E 510. | Accepted method |
| **(2)** | Consider the effects of an uncommanded or inadvertent activation of the rotor-locking device in flight. | Accepted method |
| **(3)** | Due to the expected infrequency of use, design the device so that under normal engine operating conditions it will not deteriorate beyond serviceable limits to the extent that it fails to perform its intended function when activated during an engine shut down. | Accepted method |
| **(4)** | Design the rotor-locking device so that it is possible for the flight crew to unlock the engine rotors in order to initiate engine restart attempts, and, where those attempts are unsuccessful, to re-lock the engine rotors. | Accepted method |
| **(5)** | Consider the effects of the temperature of the induction air and external surfaces of the engine where relevant to the design. | Accepted method |

Point (1) makes the purpose of CS-E 710 explicit, and the consequence is that a
rotor locking device is never a free substitution. It enters the type design, so
every other engine-level obligation applies to it.

Point (2) is the reason the substitution is not complete. A locking device that
fails leaves the engine rotating with no CS-E 525 case made for it, so the device
must be assessed for **all** possible Failure modes under [[CS-E 510]], including
the opposite failure: activation when it was not commanded.

Point (3) addresses a specific hazard of rarely used equipment. The device sits
unused through normal operation and must still work the one time it is needed,
which is why [[CS-E 510|CS-E 510(e)]] and its dormant Failure provisions are the
governing route.

Point (4) requires the lock to be reversible in flight, twice: unlock to attempt
a restart, and re-lock if the restart fails.

## Compliance

- Design decision record: whether a rotor-locking device is incorporated, and therefore whether [[CS-E 710]] or [[CS-E 525]] governs continued rotation [AMC E 710(1)].
- Maximum rotational torque assessment covering both damaged and undamaged engine rotors, and the environmental conditions that produce it [AMC E 710(1)].
- Failure mode assessment of the device under [[CS-E 510]], including failure to lock and uncommanded or inadvertent activation in flight [AMC E 710(2)].
- Deterioration assessment against serviceable limits over normal operation, with any maintenance interval it relies on published under [[CS-E 510|CS-E 510(e)(1)]] and [[CS-E 25]] [AMC E 710(3)].
- Design evidence that the flight crew can unlock for a restart attempt and re-lock afterwards [AMC E 710(4)].
- Consideration of induction air and external surface temperatures where relevant to the design [AMC E 710(5)].
- The device qualified as any other engine component, including the environmental conditions of [[AMC E 80]] [AMC E 710(1)].

## Application to this engine

The AMC applies only if a rotor locking device is incorporated. See the
`[VERIFY]` in [[CS-E 710]].

The decision is sharper here than on a fixed-wing installation.
[[AMC E 525|AMC E 525(1)]] identifies clutch drag in a multi-engine rotorcraft as
a source of continued rotation alongside windmilling, so the CS-E 525 case for
this engine covers a driven mechanism as well as an aerodynamic one. A locking
device removes the need for that case but replaces it with the device's own
Failure modes, which point (2) requires to be assessed in full.

The restart provision in point (4) connects to [[CS-E 910]], relighting in
flight. A locked rotor must be releasable for the relight attempt that CS-E 910
substantiates, and re-lockable if the attempt fails.

The maximum rotational torque in point (1) must consider damaged rotors, which
links to the blade loss work of [[CS-E 810]] and to the unbalance and continued
rotation data required by [[CS-E 520|CS-E 520(c)(2)]].

## References

Specification: [[CS-E 710]]
Related: [[CS-E 525]] · [[CS-E 510]] · [[CS-E 520]] · [[CS-E 810]] · [[CS-E 910]] · [[CS-E 25]] · [[CS-E 20]] · [[AMC E 525]] · [[AMC E 80]]
