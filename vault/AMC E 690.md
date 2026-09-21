---
id: "AMC E 690"
type: AMC
subpart: E
pages: 134-134
changed_in: [Amdt8]
tags: [bleed, oei, endurance, secondary-air, strip-examination]
---
# AMC E 690 — Engine bleed

> [!summary]
> One paragraph serves CS-E 690, and it addresses the OEI endurance sequence.
> Maximum air bleed need not be used during the 2-hour test of CS-E 740(c)(3)(iii)
> if the applicant can show, by test or by analysis based on test, that leaving
> the bleed off does not make it easier for the engine to pass the strip
> examination. The analysis must cover the secondary air system cooling effect and
> the thermodynamic cycle effect of bleed.

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| — | For reducing test complexity, and for improved flexibility needed to attain the key parameters — speed, temperature and torque — during the 2-hour test of CS-E 740(c)(3)(iii), maximum air bleed for engine and aircraft services need not be used, if the applicant can show by test or analysis based on test that the engine's ability to meet the strip examination specifications of CS-E 740(i)(2) is not enhanced. | Relief |
| — | Include in the analysis the effect of the bleed air extraction on the engine's secondary air system, which provides cooling air to various engine components. | Accepted method |
| — | Include in the analysis the thermodynamic cycle effects of bleed, for example gas generator speed to output shaft speed changes. | Accepted method |

AMC E 690 is a single unnumbered paragraph with a two-item list, so the `Ref`
cells carry no sub-point identifier.

The test the relief must pass is unusual and worth stating precisely. The
applicant does not have to show that omitting bleed is harmless; the applicant
has to show that the engine's ability to pass the strip examination "is not
enhanced" [AMC E 690]. Running without bleed must not make the strip examination
easier to pass. That is a one-sided criterion, and it is why both named effects matter.
Removing bleed extraction returns cooling air to the secondary air system. It
also changes the relationship between gas generator speed and output shaft
speed.

The relief is the accepted means for [[CS-E 690|CS-E 690(a)(3)(ii)]]. That
paragraph states that an air bleed extraction need not be used during the four
test sequences of [[CS-E 740|CS-E 740(c)(3)(iii)]], where it is shown that the
validity of the test is not compromised.

## Compliance

- Statement of the maximum air bleed for engine and aircraft services that would otherwise be used during the [[CS-E 740|CS-E 740(c)(3)(iii)]] 2-hour test [AMC E 690].
- Test, or analysis based on test, showing that the engine's ability to meet the [[CS-E 740|CS-E 740(i)(2)]] strip examination specifications is not enhanced by omitting the bleed [AMC E 690].
- Secondary air system cooling analysis for the bleed extraction removed [AMC E 690].
- Thermodynamic cycle analysis of the bleed effect, including the gas generator speed to output shaft speed relationship [AMC E 690].

## Application to this engine

The AMC applies and is directly relevant. The 2-hour test of
[[CS-E 740|CS-E 740(c)(3)(iii)]] is the OEI endurance sequence, and
`engine_profile.md` declares 30-Second OEI, 2-Minute OEI and Continuous OEI.

The key parameters the relief exists to help attain — "speed, temperature and
torque" [AMC E 690] — are the turboshaft parameters. Torque is the output
measure for a shaft engine, which is why this relief is framed around it rather
than around thrust.

The thermodynamic effect the analysis must cover is stated in turboshaft terms as
well: "gas generator speed to output shaft speed changes" [AMC E 690]. Removing
bleed shifts that relationship. The same shaft speed no longer corresponds to
the same gas generator condition. The severity the endurance sequence was
meant to impose can then change.

The strip examination that the criterion is measured against is
[[CS-E 740|CS-E 740(i)(2)]], and the bleed provisions that this AMC supports are
in [[CS-E 690|CS-E 690(a)(3)(ii)]]. The secondary air system it names is the same
one that [[CS-E 580]] protects from foreign matter ingress and that
[[CS-E 60|CS-E 60(e)]] requires turbine cooling instrumentation for.

## References

Specification: [[CS-E 690]]
Related: [[CS-E 740]] · [[CS-E 730]] · [[CS-E 580]] · [[CS-E 60]] · [[CS-E 650]] · [[CS-E 510]] · [[AMC E 650]] · [[AMC E 740]]

## Amendment history

Amended at Amendment 8. The substantive change is a cross-reference correction;
the rest is punctuation and capitalisation.

- **Before:** "the Engine's ability to meet the strip examination specifications of CS-E 740(h)(2) is not enhanced"
- **After:** "the Engine's ability to meet the strip examination specifications of CS-E 740(i)(2) is not enhanced"

The letter changed from (h) to (i), so the reference now points at the strip
examination sub-point as [[CS-E 740]] numbers it after the same amendment. This
is the same correction Amendment 8 made in [[AMC E 650|AMC E 650(10)]].

Amendment 8 also replaced the straight apostrophe with a typographic one, changed
the list introduction from "The analysis should include" to "The analysis should
include:", lower-cased the two list items, replaced the comma separating them
with a semicolon, added "'s" to "the Engine secondary air system", and removed a
comma from "(e.g., gas generator speed)". None of these alters the obligation.

The paragraph carries `[Amdt. No.: E/1]` and `[Amdt No: E/8]`.
