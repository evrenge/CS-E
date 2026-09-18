---
id: "AMC E 20(f)"
type: AMC
subpart: A
pages: 20-21
changed_in: [Amdt8]
tags: [oei, power-assurance, installation, trending, fmea]
---
# AMC E 20(f) — Power Assurance Data for Engines with One or More OEI Power Ratings

> [!quote] AMC E 20(f)(1)
> "For Engines having one or more OEI ratings, the applicant should provide in the instructions for installation the necessary Engine data to support the installer in meeting the power availability specifications of CS-27.45(f) or CS-29.45(f)."

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | Provide in the instructions for installation the engine data the installer needs to meet the power availability specifications of CS-27.45(f) or CS-29.45(f). The data should include the effects of installation losses definable at engine level — customer bleed, customer power extraction, and others as appropriate — up to and including the highest power rating. | Accepted method |
| **(2)** | The CS-E 510 safety analysis should consider dormant Failures that could make an OEI rating unavailable, and those results should form part of the CS-E 20(f) data. | Accepted method |
| **(3)** | The data should support maintenance procedures, intervals and standards, including sensors and indicating systems, that detect latent or dormant conditions not found by normal aircraft power assurance procedures. Validate the adequacy of those procedures, intervals and standards on the basis of the engine and engine systems FMEA required under CS-E 510. | Accepted method |
| **(4)** | The data should let the installer establish power assurance procedures in which results can be extrapolated from a lower power check level up to the highest OEI rating power. | Accepted method |
| **(5)** | Provide information on methods assuring that engine limiter settings would not prevent the engine from reaching the 30-Second or 2-Minute OEI power made automatically available under CS-E 50(j). | Accepted method |

Point (3) gives the objective: the installer must be able to confirm the engine
can obtain and sustain its OEI ratings within the rating operating limitations,
and the operator must be able to trend individual engine performance.

Two examples are given of conditions normal power assurance will not catch: fuel
control maximum flow capability, and turbine section distress. The reason given
is that the power assurance procedure will not include a topping check to the
highest OEI rating power level.

Point (4) sets out how to establish the minimum acceptable engine performance
characteristic. For a mature programme, production acceptance test data,
engine-to-engine variation and pre-overhaul testing can be used. For a new design
or a remote derivative, development and certification test experience should be
used, and an estimated worst engine-to-engine variation should be assumed
initially.

Point (5) names the limiter settings to examine: engine speed, measured gas
temperature and fuel flow. It directs particular attention to take-off conditions
with a cold-soaked engine.

## Compliance

- Installation data pack covering power availability, with installation losses to the highest power rating [AMC E 20(f)(1)].
- Dormant Failure analysis for OEI rating availability, within the [[CS-E 510]] safety analysis, delivered as part of the CS-E 20(f) data [AMC E 20(f)(2)].
- Engine and engine systems FMEA under [[CS-E 510]], used to validate the maintenance procedures, intervals and standards [AMC E 20(f)(3)].
- Engine database supporting the above: thermodynamic model, development and certification test experience, and field experience of this type or of similar design [AMC E 20(f)(3)].
- Extrapolation basis from a lower power check level to the highest OEI rating power, against a minimum acceptable engine performance characteristic in a deteriorated state [AMC E 20(f)(4)].
- Limiter setting assessment for 30-Second and 2-Minute OEI power availability, including the cold-soaked take-off case [AMC E 20(f)(5)].

## Application to this engine

All five points bind. The applicant declares 30-Second OEI, 2-Minute OEI and
Continuous OEI, and point (1) applies to an engine having one or more OEI ratings.

Point (5) links directly to [[CS-E 50]](j) and [[AMC E 50(j)]]: the 30-Second OEI
power must be automatically available, and limiter settings must not defeat that.

[VERIFY: point (1) cites CS-27.45(f) or CS-29.45(f). The applicable aircraft
certification specification code is identified under [[CS-E 20]](b) and is not yet
fixed in `engine_profile.md`.]

## References

Specification: [[CS-E 20]]
Related: [[CS-E 50]] · [[CS-E 510]] · [[CS-E 25]] · [[AMC E 50(j)]] · [[AMC E 40(b)(3)]]

## Amendment history

Amended at Amendment 8, under the change information document's "Editorial
corrections" heading. Two kinds of edit:

- the title was recapitalised: "Power **A**ssurance **D**ata for **E**ngines with **O**ne or more OEI **P**ower **R**atings";
- in point (5), the cross-reference "CS-E 50(**f**)" was corrected to "CS-E 50(**j**)". CS-E 50(j) is the paragraph requiring automatic availability of 30-Second OEI Power, so the earlier reference pointed at the wrong sub-point.

No change to the substance of the data required.
