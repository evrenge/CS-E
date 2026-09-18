---
id: "AMC E 50(j)"
type: AMC
subpart: A
pages: 37-38
changed_in: []
tags: [oei, 30-second, automatic-control, pilot-workload, limits]
---
# AMC E 50(j) — Controls - Engines having a 30-Second OEI Power Rating

> [!quote] AMC E 50(j)(1)
> "The 30-Second OEI rating is intended to provide a rotorcraft with a power reserve in the event of one Engine becoming inoperative."

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | The 30-Second OEI rating should be applied and controlled by an automatic means requiring no pilot input or control other than a termination command. Once activated it automatically controls the 30-Second OEI power and prevents the engine exceeding the limits associated with the rating in the type certificate data sheet. | Accepted method |
| **(1)** | The automatic control within the operating limitations should be effective during normal and abnormal operations. | Accepted method |
| **(2)** | The means required by CS-E 50(j) should not prevent the engine from reaching and maintaining its rated 30-Second OEI Power. | Accepted method |

### Why automatic control is required [(1)]

The flight and operating conditions requiring use of this rating may create a
high pilot workload to maintain safe flight. That is the stated reason for
demanding automatic application and control.

The rating could already use almost all the available margins in the engine
design. Exceeding the limits associated with it would therefore likely result in
an engine Failure — unacceptable in a critical flight condition with one engine
already failed.

The automatic control is intended to remove the need to monitor engine parameters
during the event: output shaft torque or power, output shaft speed, gas generator
speed and gas path temperatures.

### The two-sided constraint

Point (1) requires the means to prevent the engine exceeding rating limits.
Point (2) requires the same means not to prevent the engine reaching and
sustaining rated 30-Second OEI Power. The control must sit between those bounds,
which is why [[AMC E 20(f)|AMC E 20(f)(5)]] asks for evidence that limiter settings do not
block the rating.

## Compliance

- Automatic activation and control design for 30-Second OEI power, requiring no pilot input other than a termination command [AMC E 50(j)(1)], satisfying [[CS-E 50|CS-E 50(j)]].
- Demonstration that automatic control is effective in normal and abnormal operation [AMC E 50(j)(1)].
- Demonstration that the means does not prevent the engine reaching and maintaining rated 30-Second OEI Power [AMC E 50(j)(2)], evidenced jointly with [[AMC E 20(f)|AMC E 20(f)(5)]].
- Type certificate data sheet entry for the limits associated with the rating [AMC E 50(j)(1)], under [[CS-E 40|CS-E 40(e)]].

## Application to this engine

This note binds. The applicant declares a 30-Second OEI Power rating, so
[[CS-E 50|CS-E 50(j)]] applies and this is its accepted means.

The engine uses a full-authority EECS, which is the architecture this AMC assumes:
automatic application, automatic limiting, and no pilot monitoring of shaft
torque, shaft speed, gas generator speed or gas path temperature during the event.

The link to [[AMC E 20(f)|AMC E 20(f)(5)]] is a compliance dependency, not a cross-reference.
The same limiter settings — engine speed, measured gas temperature and fuel flow —
must be shown both to protect the engine and not to block the rating, with
particular attention to take-off with a cold-soaked engine.

[[AMC E 40(b)(3)|AMC E 40(b)(3)(4)]] records that certification assumes up to three uses of the
rating in one flight, and that mandatory maintenance follows any use.

## References

Specification: [[CS-E 50]]
Related: [[CS-E 25]] · [[CS-E 40]] · [[CS-E 60]] · [[AMC E 20(f)]] · [[AMC E 25]] · [[AMC E 40(b)(3)]] · [[AMC E 60(d)]]

## Amendment history

Unchanged at Amendments 7 and 8.
