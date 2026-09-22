---
id: "AMC E 600"
type: AMC
subpart: E
pages: 115-115
changed_in: []
tags: [test, attitude, rotorcraft, installation]
covers: ["AMC E 600(e)"]
---
# AMC E 600 — Test - General

> [!summary]
> One sentence serves CS-E 600, and it addresses the rotorcraft attitude clause
> of CS-E 600(e). Where the engine attitude during the tests differs from the
> attitude in the intended rotorcraft installations, the applicant should
> justify the difference. The AMC does not forbid the difference. It expects the
> reason to be stated for each intended installation.

## Requirement

### AMC E 600(e) — test attitude

| Ref | Obligation | Strength |
|---|---|---|
| **(e)** | Justify any difference between the engine attitude during the tests and the engine attitude in the intended rotorcraft installations. | Accepted method |

AMC E 600(e) is a single sentence and the only AMC material under CS-E 600.

The text reads "any difference", without a threshold. Two things follow.
The intended installation attitude has to be known before the justification can
exist, and the word "installations" is plural, so more than one intended
installation means more than one comparison.

This is the accepted means for the word "normally" in [[CS-E 600|CS-E 600(e)]].
The specification requires tests to be made normally in the installed attitude;
the AMC says what to do when they are not [AMC E 600(e)].

## Compliance

- Statement of the engine attitude used in each test [AMC E 600(e)].
- Statement of the engine attitude in each intended rotorcraft installation [AMC E 600(e)].
- Justification of every difference between the two [AMC E 600(e)].

## Application to this engine

The AMC applies directly: it is rotorcraft-specific by its own wording, and the
declared application is a rotorcraft.

The justification depends on knowing the installation attitude, which is an
assumption under [[CS-E 30|CS-E 30(a)]] and therefore installation information
under [[CS-E 20|CS-E 20(d)]]. Since the rotorcraft installation is not fixed,
the comparison cannot be closed yet.

[VERIFY: the intended rotorcraft installation attitude, or attitudes, are not
recorded in `engine_profile.md`. AMC E 600(e) expects a justification for every
difference from the test attitude, and the plural "installations" means each
intended installation is compared.]

The systems most sensitive to attitude are the oil system of [[CS-E 570]], whose
functioning must be assured in all intended flight attitudes, and the effects
tested by [[CS-E 680]].

## References

Specification: [[CS-E 600]]
Related: [[CS-E 30]] · [[CS-E 20]] · [[CS-E 570]] · [[CS-E 680]] · [[CS-E 140]] · [[CS-E 150]]
