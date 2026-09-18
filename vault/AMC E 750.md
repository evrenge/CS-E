---
id: "AMC E 750"
type: AMC
subpart: E
pages: 176-176
changed_in: []
tags: [starting, false-start, drainage, fuel]
covers: ["AMC E 750(b)"]
---
# AMC E 750 — Starting tests

> [!summary]
> One sentence pair serves CS-E 750, and it defines the declared drainage period.
> It is the minimum period necessary to allow surplus fuel to drain from the
> engine before another start is attempted, measured from the moment the starter
> is switched off or the engine fuel cock is closed during a false start.

## Requirement

### AMC E 750(b) — the declared drainage period

| Ref | Obligation | Strength |
|---|---|---|
| **(b)** | The declared drainage period referred to in CS-E 750(b) is the minimum period necessary to allow surplus fuel to drain from the engine prior to making a further attempt to start the engine. | Statement |
| **(b)** | The period is measured from the time at which the starter is switched off and/or the engine fuel cock is closed, during a false start. | Statement |

AMC E 750(b) is a definition and the only AMC material under CS-E 750.

Two things follow from it. The period is a **minimum**, so declaring a longer one
does not satisfy the definition more safely — it is the shortest period that
achieves drainage. The clock starts at the shutdown action, at the point
where the start attempt was abandoned, so the declared value must be measured
from a defined event.

The period is declared by the applicant, and [[CS-E 750|CS-E 750(b)]] requires a
normal start immediately on its expiry. That makes it a tested value rather than
a stated one: ten False Starts each end with a start attempt at the declared
period.

## Compliance

- Declared drainage period, with its basis in the drainage behaviour of the engine [AMC E 750(b)].
- Definition of the event from which the period is measured — starter switched off, or fuel cock closed [AMC E 750(b)].
- Evidence from the ten False Starts of [[CS-E 750|CS-E 750(b)]] that a normal start follows immediately on expiry of that period.
- The declared period carried into the engine operating instructions of [[CS-E 20|CS-E 20(d)]].

## Application to this engine

The AMC applies. Nothing in it is restricted by engine type or rating.

The drainage period is the link between the starting tests and the fire
protection provisions. [[CS-E 130|CS-E 130(f)]] requires unintentional
accumulation of hazardous quantities of flammable fluid within the engine to be
prevented by draining and venting, and
[[AMC E 130|AMC E 130(6)]] names "a combustor drain system which typically drains
off residual fuel after an aborted Engine start" as an example of a part that may
be exempt from the Fire Resistant specification, because it does not convey
flammable fluid during normal operation.

The False Start sequence is therefore a functional test of that drain system, and
the declared drainage period is the operational limit that makes the exemption
argument hold.

## References

Specification: [[CS-E 750]]
Related: [[CS-E 130]] · [[CS-E 560]] · [[CS-E 740]] · [[CS-E 770]] · [[CS-E 500]] · [[CS-E 20]] · [[AMC E 130]]
