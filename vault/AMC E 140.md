---
id: "AMC E 140"
type: AMC
subpart: A
pages: 60-61
changed_in: []
tags: [tests, accessory-drives, power-turbine, endurance]
covers: ["AMC E 140"]
---
# AMC E 140 — Test - Engine configuration

> [!summary]
> One short AMC serves CS-E 140, and it addresses turbine engines specifically.
> Where the power turbine accessory drives are not loaded during a test, the
> equivalent power is added at the output drive. The AMC states the purpose of
> that addition: the power turbine rotor assembly must be worked at or above the
> level it would see with the drives loaded.

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| — | For turbine engines, where the power turbine accessory drives are not loaded, add the equivalent power as required by CS-E 140(d)(1) to the required power at the output drive, so that the power turbine rotor assembly is operated at or above the same level as it would be if the power turbine accessory drives were loaded. | Accepted method |

AMC E 140 is a single unnumbered sentence, so the `Ref` cell carries no sub-point
identifier.

The AMC supplies the acceptance criterion that the specification leaves implicit.
[[CS-E 140|CS-E 140(d)(2)]] requires the equivalent power extraction to be added
to the engine shaft output but does not say what the addition has to achieve.
AMC E 140 states it: the power turbine rotor assembly is operated "at or above
the same level as it would be if the power turbine accessory drives were loaded"
[AMC E 140]. The test is therefore at least as severe on the power turbine as
the loaded case, never less.

The AMC cites CS-E 140(d)(1) while the unloading relief for the additional
endurance sequence sits in CS-E 140(d)(2). Both sub-points concern drive loading,
and (d)(2) is written as an exception to (d)(1), so the AMC covers the
arithmetic that (d)(2) requires.

## Compliance

- Calculation of the equivalent power for the unloaded power turbine accessory drives, and evidence that it was added at the output drive [AMC E 140].
- Demonstration that the power turbine rotor assembly operated at or above the loaded-drive level throughout the test [AMC E 140].

## Application to this engine

The AMC applies directly. It is written "For turbine engines" [AMC E 140], and
the power turbine it addresses is the free turbine that drives the rotorcraft
transmission.

The AMC matters most for the additional endurance sequence of
[[CS-E 740|CS-E 740(c)(3)(iii)]], which is where
[[CS-E 140|CS-E 140(d)(2)]] permits the drives to be left unloaded. This engine
declares 30-Second OEI, 2-Minute OEI and Continuous OEI, so that sequence is part
of the programme and the power addition is live.

## References

Specification: [[CS-E 140]]
Related: [[CS-E 740]] · [[CS-E 730]] · [[CS-E 150]] · [[CS-E 590]]

## Amendment history

Unchanged at Amendments 7 and 8. The paragraph carries `[Amdt. No.: E/1]` and
`[Amdt. No.: E/2]`.
