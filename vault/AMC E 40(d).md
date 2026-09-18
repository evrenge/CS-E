---
id: "AMC E 40(d)"
type: AMC
subpart: A
pages: 31-33
changed_in: []
tags: [operating-limitations, tcds, oil, fuel, over-limits]
---
# AMC E 40(d) — Operating Limitations

> [!quote] AMC E 40(d)
> "The Operating limitations established under CS-E 40(d) should normally include those items listed below."

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | General items: the environmental conditions, meaning the flight envelope; and the equipment approved for use on the engine. | Accepted method |
| **(3)** | Turbine engine items: the twenty-one limitations listed below. | Accepted method |

### Turbine engine limitations [AMC E 40(d)(3)]

| Ref | Limitation |
|---|---|
| **(a)** | RPM, indicated turbine gas temperature and time, for Take-off conditions, Maximum Continuous conditions, and the Contingency conditions where applicable |
| **(b)** | Oil brand(s) and type(s) |
| **(c)** | Fuel specification(s) |
| **(d)** | Hydraulic fluid specification(s), if applicable |
| **(e)** | Inlet air distortion at the engine inlet |
| **(f)** | Maximum and minimum fuel pressure |
| **(g)** | Maximum and minimum fuel temperature |
| **(h)** | Maximum indicated oil temperature for Take-off, Maximum Continuous, Contingency and transient conditions, with the transient time limitation(s) |
| **(i)** | Minimum indicated oil temperature for starting |
| **(j)** | Minimum indicated oil temperature for acceleration from idle |
| **(k)** | Minimum oil pressure for completion of flight at Maximum Continuous conditions |
| **(l)** | Maximum normal oil pressure at Maximum Continuous conditions |
| **(m)** | Use of compressor bleed air |
| **(n)** | Maximum Power Turbine speed for Autorotation, if applicable |
| **(o)** | Maximum Power Turbine torque, and the maximum rpm at which use of maximum torque is approved |
| **(p)** | Maximum Over-torque transient and time limit |
| **(q)** | Maximum Over-speed transient(s) and time limit(s) for each applicable operating condition |
| **(r)** | Maximum Over-temperature transient and time limit |

## Compliance

- Operating limitations schedule covering every applicable item of AMC E 40(d)(1) and (3) [CS-E 40(d)].
- The rated powers and the limitations the crew must respect, entered in the TCDS under point 21.A.41 of Part 21 [CS-E 40(e)].
- Over-limit transients and their time limits [AMC E 40(d)(3)(p), (q), (r)], substantiated by [[CS-E 820]], [[CS-E 830]] and [[CS-E 870]].
- Power turbine autorotation speed and torque limits [AMC E 40(d)(3)(n), (o)].

## Application to this engine

Items (n) and (o) are the rotorcraft-defining rows. Maximum Power Turbine speed
for Autorotation and Maximum Power Turbine torque have no analogue on a turbofan;
on a turboshaft they are primary declared limitations.

Item (a) requires RPM, indicated turbine gas temperature and time for each rating.
The declared ratings are Take-off, Maximum Continuous, Rated 30-Minute Power,
30-Second OEI, 2-Minute OEI and Continuous OEI — see `engine_profile.md`.

[VERIFY: item (a) lists "Maximum Contingency", "Intermediate Contingency" and
"30-minute Contingency" conditions. None of these names appears in [[CS-E 40]],
which uses the OEI rating names and Rated 30-Minute Power. The Contingency
terminology appears to predate the current rating names. Confirm the mapping with
EASA before entering these rows in the TCDS.]

## Not applicable

- **(1)(b)** — maximum declared engine conditions for Reversible Pitch Propeller operations.
- **(1)(c)** — types of Propellers approved.
- **(2)** — the eighteen piston engine limitations.
- **(3)(s)** — maximum refrigerant flow rate; refrigerant injection is not used, see `engine_profile.md`.
- **(3)(t)** — maximum reverse thrust conditions and time limitations; no thrust reverser is fitted.
- **(3)(u)** — maximum rpm for application of the Propeller brake.

## References

Specification: [[CS-E 40]]
Related: [[CS-E 60]] · [[CS-E 560]] · [[CS-E 570]] · [[CS-E 820]] · [[CS-E 830]] · [[CS-E 870]] · [[AMC E 40]]

## Amendment history

Unchanged at Amendments 7 and 8.
