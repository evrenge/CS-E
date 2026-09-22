---
id: "AMC E 620"
type: AMC
subpart: E
pages: 116-117
changed_in: []
tags: [performance-correction, formulae, notation, isa]
---
# AMC E 620 — Performance: Formulae

> [!summary]
> This AMC gives the correction formulae for CS-E 620, with their notation and
> suffix convention. The formulae are conditional in two ways: they apply within
> the range of conditions appropriate to the engine type, taking account of the
> control system characteristics and possible Reynolds Number effects, and they
> give way to more accurate or additional corrections where the Agency has agreed
> or required them.

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | Use the following corrections from the observed test conditions to the assumed atmospheric conditions of pressure and temperature, within the range of conditions appropriate to the particular type of engine — taking into account the characteristics of the Engine Control System, and the possible effect of Reynolds Number — unless more accurate or additional corrections for a particular type of engine have been agreed or required by the Agency. | Accepted method |
| **(1)** | Where certain proprietary types of air flowmeter are employed, note that Wo is the actual air consumption of the engine during test. | Statement |
| **(2)** | The notation used by the formulae is set out in the Notation table below. | Statement |
| **(3)** | Suffix 'o' denotes an observed result, corrected for instrument temperature and scale errors only. Suffix 'c' denotes a result corrected to the standard atmospheric pressure and temperature conditions of CS-E 620. | Statement |

The formulae are reproduced here as images. The text layer renders a fraction as
two separate lines, with nothing to mark the division. It also loses the extent
of a square root. The rotational speed correction extracts as text suggesting
√288 divided by θ. The source shows the square root taken over the whole ratio
288/θ. A transcription would therefore be an unverifiable restatement, so
accuracy rule 6 applies.

### Gas pressures, gas temperatures and rotational speed

![[AMC_E_620_p116.png]]

### Thrust and mass air flow

![[AMC_E_620_p116_2.png]]

### Fuel flow

![[AMC_E_620_p116_3.png]]

### Power

![[AMC_E_620_p117.png]]

### Notation

| Symbol | Meaning | Unit |
|---|---|---|
| **B** | Barometric pressure in test chamber | hPa |
| **θ** | Observed intake temperature, corrected for instrument temperature and scale errors only | K |
| **P** | Pressure | hPa |
| **T** | Temperature | K |
| **N** | Rotational speed | rpm |
| **W** | Mass air flow | kg/s |
| **w** | Fuel flow | kg/h |
| **P** | Power | kW |

The notation list uses **P** for both pressure and power, and distinguishes mass
air flow **W** from fuel flow **w** only by case. Both collisions are in the
source, and the meaning is fixed by which formula the symbol appears in.

## Compliance

- Corrected performance data, with the correction formulae used and the observed values they were applied to [AMC E 620(1)].
- Statement of the range of conditions over which the formulae are appropriate for this engine type, accounting for the Engine Control System characteristics and Reynolds Number effects [AMC E 620(1)].
- Where more accurate or additional corrections are used, the agreement with the Agency [AMC E 620(1)].
- Air flowmeter type and the basis for Wo, where a proprietary flowmeter is used [AMC E 620(1)].

## Application to this engine

The AMC applies. The formulae are not engine-type specific.

**The power correction is the one that governs here.** A turboshaft is rated in
power, so the power formula is the operative one and the thrust formula does not
apply [AMC E 620(1)]. Both are given in the source and both are shown above. The
two formulae differ, so one cannot be substituted for the other.

**The control system qualifier matters for a FADEC engine.** Paragraph (1)
requires the formulae to be applied "taking into account the characteristics of
the Engine Control System" [AMC E 620(1)]. For this full-authority EECS, the
range over which these corrections hold has to be established rather than
assumed. Where they do not hold, the AMC's own alternative applies: more
accurate or additional corrections, agreed with the Agency.

The corrections feed the calibration test of [[CS-E 730]] and the declared
ratings of [[CS-E 40]]. The test bed and measuring equipment that produce the
observed values must be appropriately calibrated under
[[CS-E 150|CS-E 150(f)]].

## Not applicable

- **(1)**, in part — the thrust correction formula, and **(2)**, in part — the symbol F for thrust. This engine is rated in shaft power. The thrust formula shares its image with the mass air flow formula, which applies, so the image is kept whole.

## References

Specification: [[CS-E 620]]
Related: [[CS-E 40]] · [[CS-E 60]] · [[CS-E 150]] · [[CS-E 730]] · [[CS-E 740]] · [[CS-E 50]]
