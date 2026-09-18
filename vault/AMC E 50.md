---
id: "AMC E 50"
type: AMC
subpart: A
pages: 36-37
changed_in: []
tags: [control-system, eecs, scope, integrity, rotorcraft, air-signal]
---
# AMC E 50 — Engine Control System

> [!quote] AMC E 50(1)
> "CS-E 50 is applicable to all types of Engine Control Systems."

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | CS-E 50 applies to every control system architecture, from hydromechanical to dual-channel full-authority EECS, analogue or digital. The Engine Control System includes any system or device that controls, limits or monitors engine operation and is necessary for continued airworthiness. | Statement |
| **(2)** | CS-E 50 sets objectives for general design and functioning. It does not replace other specifications, so individual components such as alternators, sensors and actuators should also be covered under CS-E 80 or CS-E 170 as appropriate. | Accepted method |
| **(3)** | For rotorcraft control systems with a power turbine speed governing mode, the CS-E 50(a)(3) specification for modulation of engine power should be read as the ability to manage power to maintain power turbine speed within specified limits. | Accepted method |
| **(4)** | The intent of CS-E 50(c) is control system integrity consistent with the operational specifications of the application. Electronic control systems should provide at least an equivalent level of safety and reliability to engines with hydromechanical control and protection systems and magneto systems. | Accepted method |
| **(5)** | Control systems in hydromechanical or other non-electrical technology should inherently comply with CS-E 50(h). Where functions are implemented electrically or electronically and depend on aircraft-supplied electrical power, the system should be evaluated against that rule. | Accepted method |
| **(6)** | CS-E 50(i) covers ingress of foreign matter — sand, dust, water, insects — that could block signal lines and adversely affect engine operation. Precautions should be taken, and corrosion effects addressed. | Accepted method |

### What is inside the Engine Control System [(1)]

Included: electronic control unit(s), fuel metering unit(s), variable-geometry
actuators, cables, wires and sensors. Also the protection systems against
over-speed, over-torque and over-temperature.

Not usually included: the main engine fuel pump, even though it is often
engine-mounted and physically integrated with the fuel metering unit.

Not included: blade shedding or engine design related over-speed protection,
because that protection is purely mechanical and works without influence from the
control system.

Engine monitoring systems are covered when physically or functionally integrated
with the control system, or when they perform functions affecting engine safety,
or are used for continued-operation or return-to-service decisions. Low cycle
fatigue (LCF) cycle-counters for Engine Critical Parts are included. Most trend
monitors and maintenance information devices are not — those fall under
[[CS-E 170]].

### Air signal line precautions [(6)]

The worked example given is that lines measuring static pressure in the
compressor of turbine engines could be blocked by frozen water, leading to a loss
of power. Suggested precautions: protected openings, filters, drains for water,
and heating of the lines to prevent freezing of condensed water.

## Compliance

- Control system boundary definition, stating what is inside and outside the Engine Control System [AMC E 50(1)].
- Component-level coverage of control system items under [[CS-E 80]] and [[CS-E 170]] in addition to CS-E 50 [AMC E 50(2)].
- Power modulation demonstration expressed as power turbine speed control within specified limits [AMC E 50(3)], against [[CS-E 50]](a)(3).
- Integrity case showing at least equivalent safety and reliability to a hydromechanical and magneto system [AMC E 50(4)], supporting [[CS-E 50]](c).
- Evaluation against [[CS-E 50]](h) for every function depending on aircraft-supplied electrical power [AMC E 50(5)].
- Air signal line design precautions and corrosion assessment [AMC E 50(6)], within the safety assessment of [[CS-E 50]](d).

## Application to this engine

Point (3) is the rotorcraft-specific provision and it changes what must be
demonstrated. On a turboshaft with power turbine speed governing, "modulation of
Engine power with adequate sensitivity and accuracy" under [[CS-E 50]](a)(3)
means holding power turbine speed within limits, not managing thrust.

Point (5) binds fully. The engine uses a full-authority EECS, so it does not
inherit the inherent compliance that a hydromechanical system enjoys, and every
aircraft-supplied electrical power dependency must be evaluated against
[[CS-E 50]](h).

Point (1) settles where "OEI override" is assessed. If the feature controls,
limits or monitors engine operation and is necessary for continued airworthiness,
it is part of the Engine Control System and falls under CS-E 50 — not under
[[CS-E 40]] as a rating.

[VERIFY: AMC E 50(2) and (5) cite AMC 20-1 and AMC 20-3 for detailed
interpretation of CS-E 50 for EECS. Neither is held in `source/`.]

## Not applicable

- **(2)**, **(5)** propeller clauses — AMC 20-1 and AMC 20-3 are cited for interfaces with the aircraft "and the Propeller when applicable"; a turboshaft has no propeller interface.

## References

Specification: [[CS-E 50]]
Related: [[CS-E 80]] · [[CS-E 170]] · [[CS-E 510]] · [[CS-E 560]] · [[AMC E 50(e)]] · [[AMC E 50(j)]] · [[AMC to CS-E 50(l)]] · [[AMC E 170]]

## Amendment history

Unchanged at Amendments 7 and 8.

The heading of point (3) is spelled "Rotocraft Engines" in Amendment 8. This is a
typographical error in the source; the body text reads "rotorcraft".
