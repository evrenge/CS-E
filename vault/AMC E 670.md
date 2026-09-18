---
id: "AMC E 670"
type: AMC
subpart: E
pages: 131-133
changed_in: []
tags: [contaminated-fuel, contaminant-table, water, icing, filter-blockage, carbon-fibre]
---
# AMC E 670 — Contaminated Fuel Testing

> [!summary]
> This AMC supplies the contaminant specification that CS-E 670 leaves open, and
> the test procedure that uses it. Solid contaminants are tabulated by type,
> particle size and quantity, with an extra carbon fibre entry for engines fitted
> to aircraft with composite fuel tanks. The test runs on a running engine or a
> rig at a defined contamination rate, establishes the blockage indication point,
> then continues to an equivalent of 500 hours of normal operation. A separate
> water contaminant test follows.

## Requirement

### AMC E 670(1)(a) — the solid contaminant specification

The contaminant table is embedded as its source crops. It is laid out as a table,
and the chemical formulas carry subscripts that the text layer destroys —
Fe₃O₄ extracts as "Fe 3 0 4", with a digit zero in place of the oxygen — so a
transcription would be an unverifiable restatement under accuracy rule 6.

![[AMC_E_670_p131.png]]
![[AMC_E_670_p132.png]]
![[AMC_E_670_p132_2.png]]

| Ref | Obligation | Strength |
|---|---|---|
| **(1)(a)** | A contaminant with the characteristics detailed in the table is acceptable. | Accepted method |

The table is introduced as one acceptable contaminant, not the only one. An
alternative may be proposed and justified, as for any accepted means.

The final block of the table is conditional: the carbon fibre rod entry applies
"Additionally, for engines to be fitted to Aircraft with Carbon Fibre Composite
Material Fuel Tanks" [AMC E 670(1)(a)]. It is therefore installation-dependent
rather than universal.

### AMC E 670(1)(b) to (d) — the solid contaminant test

| Ref | Obligation | Strength |
|---|---|---|
| **(1)(b)** | Carry out a test on the complete fuel system, either on a running engine or on a rig, using fuel continuously contaminated at a rate of 4.5 g of contaminant per 4 500 litres. | Accepted method |
| **(1)(c)** | Establish the point at which impending filter blockage will be indicated to the flight crew. | Accepted method |
| **(1)(c)** | Show the fuel system capable of continuing to operate without causing engine malfunction for a further period equal to at least half the maximum flight duration of the aircraft in which it is likely to be installed. | Accepted method |
| **(1)(c)** | Once that has been established, it is permissible to clean or replace filters as frequently as necessary for the remainder of the test. | Permitted |
| **(1)(c)** | If blockage has not occurred by the time the total quantity of contaminant has reached the level specified in (1)(d), the objective of (1)(c) may be considered to have been met. | Accepted method |
| **(1)(d)** | Continue the test at typical running conditions with respect to rotational speeds, pressures and fuel flow, for a sufficient time to ensure that the total weight of contaminant passing into the system would be equivalent to 500 hours of normal operation with fuel contaminated to a level of 0.5 g per 4 500 litres. | Accepted method |
| **(1)(d)** | At the conclusion of the test, the fuel system should be functioning satisfactorily. | Accepted method |

The two contamination rates are different and both matter. The **test** runs at
4.5 g per 4 500 litres — nine times the 0.5 g per 4 500 litres rate that defines
"normal operation" — and the test duration is set so that the total contaminant
mass equals 500 service hours at the normal rate. The test is accelerated by
concentration, not by time.

### AMC E 670(2) to (3) — water and transient icing

| Ref | Obligation | Strength |
|---|---|---|
| **(2)** | Carry out a test on the fuel system using fuel contaminated with water, either on a running engine or on a rig. | Accepted method |
| **(2)** | Make the contaminated fuel from fuel initially saturated with water at a fuel and water temperature of 27 °C, into which a further 0.2 ml of free water per litre of fuel has been evenly dispersed. | Accepted method |
| **(2)** | Conduct the test with the contaminated mixture cooled to the most critical condition for icing likely to be encountered in operation. | Accepted method |
| **(3)** | In compliance with CS-E 670(a), consider the effect on engine operability of the transient fuel icing conditions likely to be encountered in service, in accordance with AMC E 560(4). | Accepted method |

The water test has two stages built into its preparation: saturation at 27 °C,
then a further 0.2 ml per litre of **free** water dispersed on top. Saturated fuel
alone does not meet the specification.

## Compliance

- Contaminant batch prepared to the table, with the carbon fibre entry included where the installation has composite fuel tanks [AMC E 670(1)(a)].
- Complete fuel system contamination test at 4.5 g per 4 500 litres, on a running engine or a rig [AMC E 670(1)(b)].
- Established filter blockage indication point, and the continued operation demonstration from that point [AMC E 670(1)(c)], against [[CS-E 670|CS-E 670(b)(2)]] and the indication required by [[CS-E 560|CS-E 560(b)(2)]].
- Test continuation to a contaminant mass equivalent to 500 hours at 0.5 g per 4 500 litres, with the fuel system functioning satisfactorily at the end [AMC E 670(1)(d)].
- Water contaminant test at 27 °C saturation plus 0.2 ml free water per litre, cooled to the most critical icing condition [AMC E 670(2)].
- Transient fuel icing operability assessment per [[AMC E 560|AMC E 560(4)]] [AMC E 670(3)].

## Application to this engine

The AMC applies in full. Nothing in it is restricted by engine type, rating or
control system.

**The flight duration in (1)(c) is an installation input.** The continued
operation period is half the maximum flight duration of the aircraft the engine
is likely to be installed in, which for this engine is the rotorcraft. The value
is not fixed by CS-E and is not recorded in `engine_profile.md`; it is an
assumption under [[CS-E 30|CS-E 30(a)]]. See the `[VERIFY]` in [[CS-E 670]] on
the aeroplane and aircraft wording difference between the specification and this
AMC.

[VERIFY: whether the intended rotorcraft has carbon fibre composite material fuel
tanks. The carbon fibre rod entry in the contaminant table applies only then, and
it is the largest single solid contaminant quantity in the table.]

**The by-pass interaction.** The test at (1)(c) runs past the blockage indication,
which is the region where [[CS-E 560|CS-E 560(c)]] governs: a by-pass must keep
fuel flowing, must not release collected contaminants downstream, and must not
allow operation on contaminated fuel to cause a Hazardous Engine Effect. The
permission in (1)(c) to clean or replace filters for the remainder of the test
applies only after the continued-operation demonstration is complete.

**Transient fuel icing appears here as well as in the fuel system paragraph.**
Point (3) routes it to [[AMC E 560|AMC E 560(4)]], where the ice originates in
the aircraft fuel system and the threat assessment belongs to the aircraft
manufacturer in the first instance. The same open item applies: assess the threat,
or declare that no capability has been demonstrated.

## References

Specification: [[CS-E 670]]
Related: [[CS-E 560]] · [[CS-E 660]] · [[CS-E 780]] · [[CS-E 30]] · [[CS-E 20]] · [[AMC E 560]] · [[AMC E 80]]
