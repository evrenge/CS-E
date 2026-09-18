---
id: "AMC E 730"
type: AMC
subpart: E
pages: 137-137
changed_in: []
tags: [calibration, parameters, speed-range, oei, endurance]
covers: ["AMC E 730"]
---
# AMC E 730 — Calibration Tests

> [!summary]
> Three points serve CS-E 730. The calibration parameters are those appropriate
> to the engine design, with torque, rotational speed and exhaust gas temperature
> among the typical ones. The test should cover the maximum possible rotational
> speed range, and at least from minimum idle to the normal maximum for the test
> day. The curves are established up to the highest rating approved for more than
> two minutes, before the additional endurance test, and the 30-Second and
> 2-Minute OEI ratings are excluded because running at them changes the hardware.

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | The parameters used for the calibration curves are those appropriate to, and compatible with, the engine's design. Thrust, Power, Torque, Rotational Speed, EPR (Engine Pressure Ratio) and EGT (Exhaust Gas Temperature) are typical parameters of known engine designs. | Statement |
| **(2)** | Run the Calibration Test to cover the maximum possible rotational speed range, but at least to cover the range from minimum idle to the normal maximum compatible with the ambient external atmospheric condition of the test day. | Accepted method |
| **(3)** | Establish the pre and post test calibration curves required by CS-E 730 up to the highest rating to be approved for a duration of more than 2 minutes, prior to the additional endurance test of CS-E 740(c)(3)(iii). | Accepted method |
| **(3)** | Because engine operation at the 30-Second and 2-Minute OEI Power ratings could significantly affect engine hardware conditions, these engine ratings are not required to comply with the calibration specifications of CS-E 730. | Relief |

Point (2) sets two bounds and they are not the same. The goal is the maximum
possible rotational speed range; the floor is minimum idle to the normal maximum
achievable on the test day. Ambient conditions on the day therefore limit what
the test can reach, and the AMC accepts that limit while asking for more where
possible.

Point (3) converts the CS-E 730 exclusion into a rating criterion. The ceiling is
"the highest rating to be approved for a duration of more than 2 minutes"
[AMC E 730(3)], which is the same two-minute boundary that
[[CS-E 650|CS-E 650(b)]] uses to split the vibration survey speeds — but applied
in the opposite direction. CS-E 650(b)(1) includes ratings of two minutes **or
longer**; AMC E 730(3) includes ratings of **more than** two minutes.

## Compliance

- Calibration parameter set, justified as appropriate to and compatible with this engine's design [AMC E 730(1)].
- Calibration test covering at least minimum idle to the normal maximum for the test day ambient condition, and the maximum possible speed range where achievable [AMC E 730(2)].
- Pre and post test calibration curves up to the highest rating approved for more than two minutes, established before the [[CS-E 740|CS-E 740(c)(3)(iii)]] additional endurance test [AMC E 730(3)].
- Record of the ratings excluded from calibration and the basis for the exclusion [AMC E 730(3)].

## Application to this engine

The AMC applies, and point (3) is written for a rating set like this one.

**The two-minute boundary excludes both short OEI ratings.** `engine_profile.md`
declares 30-Second OEI and 2-Minute OEI. Neither is approved "for a duration of
more than 2 minutes" — 2-Minute OEI is exactly two minutes, not more — so neither
enters the calibration. Continuous OEI, Rated 30-Minute Power, Take-off Power and
Maximum Continuous Power all exceed two minutes and are included.

This is worth noting against [[CS-E 650]], which draws its boundary at "two
minutes or longer" and therefore puts 2-Minute OEI on the **inside** of the
103 % vibration survey requirement. The same rating falls on opposite sides of
two boundaries that differ by one word.

**Torque is a named parameter.** Point (1) lists Torque and Rotational Speed among
the typical calibration parameters, which is what a turboshaft calibration is
built on. Thrust and EPR are listed in the same sentence and do not apply here.

**The timing matters.** The curves are established before the OEI endurance
sequence of [[CS-E 740|CS-E 740(c)(3)(iii)]], so the calibration baseline is taken
from an engine that has not yet been run at the short OEI ratings. That is the
point of the relief: the ratings that would change the hardware are kept out of
the measurement that the endurance comparison depends on.

## References

Specification: [[CS-E 730]]
Related: [[CS-E 740]] · [[CS-E 620]] · [[CS-E 650]] · [[CS-E 690]] · [[CS-E 40]] · [[CS-E 60]] · [[CS-E 150]] · [[AMC E 620]] · [[AMC E 690]]
