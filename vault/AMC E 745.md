---
id: "AMC E 745"
type: AMC
subpart: E
pages: 175-175
changed_in: []
tags: [acceleration, minimum-test-bed-idle, over-temperature, surge, bleed]
---
# AMC E 745 — Engine Acceleration

> [!summary]
> Four points serve CS-E 745. Compliance may be shown during tests run for other
> parts of CS-E. The adverse bleed and offtake combination is different for
> over-temperature than for surge and stall, and over-temperature is defined
> against the values substantiated under CS-E 740. Minimum test bed idle is
> defined for rotorcraft engines. An acceleration slower than 5 seconds must be
> justified against operational aspects and the installation's certification
> specifications.

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | Compliance with CS-E 745 may be demonstrated during tests performed to meet other sections of CS-E. | Permitted |
| **(2)** | In complying with CS-E 745(a)(1) and (a)(2), for evaluation of a potential over-temperature the appropriate adverse combination is probably maximum bleed air and maximum power extraction. | Accepted method |
| **(2)** | For evaluation of surge and stall, the combination should probably be no bleed air and maximum power extraction. | Accepted method |
| **(2)** | An over-temperature event is considered as being any exceedence of the steady state and transient values which are substantiated under CS-E 740. | Statement |
| **(3)** | The minimum test bed idle referenced for rotorcraft engines in CS-E 745(a) or other CS-E paragraphs is the minimum practically possible power extraction from the engine in the test facility while the output shaft is at the governed speed. | Statement |
| **(4)** | If an acceleration time longer than 5 seconds is experienced when complying with CS-E 745(a)(3), address in the justification the operational aspects as well as the aircraft certification specifications for the intended installation. | Accepted method |

Point (2) is the operative guidance. The two failure modes have opposite worst
cases on bleed: maximum bleed loads the engine thermally, while no bleed narrows
the surge margin. A test run at one condition does not evidence the other.

Point (3) has reach beyond this paragraph. It defines minimum test bed idle as
the term is used "in CS-E 745(a) or other CS-E paragraphs" [AMC E 745(3)], so it
governs wherever the term appears — including the endurance schedule of
[[CS-E 740|CS-E 740(c)(3)(i)]] and the acceleration provisions of
[[CS-E 740|CS-E 740(d)(1)(ii)]].

Point (4) gives the reason a longer acceleration may be accepted: very large
engines may have difficulty meeting exactly the 5 seconds because of rotor
inertia.

## Compliance

- Identification of which other CS-E tests are relied on to demonstrate CS-E 745 compliance [AMC E 745(1)].
- Test conditions selected separately for the over-temperature case and the surge and stall case, with the bleed and power extraction combination stated for each [AMC E 745(2)].
- The steady state and transient values substantiated under [[CS-E 740]], used as the over-temperature threshold [AMC E 745(2)].
- Definition of the minimum test bed idle condition used, with the output shaft at governed speed [AMC E 745(3)].
- Justification addressing operational aspects and the installation's certification specifications, where the acceleration exceeds 5 seconds [AMC E 745(4)].

## Application to this engine

All four points apply, and two are written for a rotorcraft engine.

**Point (3) is the definition this whole test rests on.** For a free
power-turbine turboshaft, minimum test bed idle is not a lever position but a
condition: minimum practically possible power extraction with the output shaft at
the governed speed. That is the state the one-second step of
[[CS-E 745|CS-E 745(a)(2)]] starts from, and it reflects how the engine sits in a
rotorcraft with the rotor turning.

**Point (2) makes the test matrix at least two-dimensional.** The surge case
needs no bleed with maximum power extraction; the over-temperature case needs
maximum bleed with maximum power extraction. Both must be covered, and the bleed
configuration interacts with [[CS-E 690]].

**Point (4) is unlikely to be reached here.** The justification route exists for
very large engines whose rotor inertia prevents the 5-second response. A
turboshaft in a rotorcraft is at the other end of that scale, and rapid power
response is what the installation demands.

The dependency in point (2) on [[CS-E 740]] sets a sequence: the endurance test
fixes the steady state and transient temperature values, and only then can an
acceleration be judged to have produced an over-temperature.

## References

Specification: [[CS-E 745]]
Related: [[CS-E 740]] · [[CS-E 690]] · [[CS-E 500]] · [[CS-E 50]] · [[CS-E 750]] · [[CS-E 770]] · [[CS-E 30]] · [[AMC E 740]]
