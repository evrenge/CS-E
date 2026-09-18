---
id: "AMC E 50"
type: AMC
subpart: A
pages: 36-38
changed_in: []
tags: [control-system, eecs, fadec, over-speed, oei, security, rotorcraft]
covers: ["AMC E 50", "AMC E 50(e)", "AMC E 50(j)", "AMC to CS-E 50(l)"]
---
# AMC E 50 — Engine Control System

> [!summary]
> Four AMC paragraphs serve CS-E 50. The general AMC fixes what counts as the
> Engine Control System and reads CS-E 50(a)(3) for a rotorcraft as power turbine
> speed control. AMC E 50(e) covers over-speed protection testing, AMC E 50(j)
> the automatic control of 30-Second OEI power, and AMC to CS-E 50(l) the
> security assessment. All four bind: the engine uses a full-authority EECS and
> declares a 30-Second OEI rating.

## Requirement

### AMC E 50 — scope and interpretation

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


### AMC E 50(e) — over-speed protection testing

| Ref | Obligation | Strength |
|---|---|---|
| — | Over-speed protection is usually provided as part of the electronic Engine Control System, even where the devices are nominally independent. Periodic testing by built-in test equipment (BITE) or a functional test is one acceptable method of showing the protection function is available. | Accepted method |
| — | For an over-speed protection system, the BITE test should provide a complete test of the electrical and electronic part of the protection system. | Accepted method |
| — | The need for inspections or tests of the mechanical or actuating part of the protection system should be based on the results of the safety analysis for that part. | Accepted method |

The split matters. The electrical and electronic part is covered by a complete
BITE test. The mechanical and actuating part is not, and its inspection interval
is decided by safety analysis rather than by this AMC.


### AMC E 50(j) — automatic control of 30-Second OEI power

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
which is why [[AMC E 20|AMC E 20(f)(5)]] asks for evidence that limiter settings do not
block the rating.


### AMC to CS-E 50(l) — information system security protection

| Ref | Obligation | Strength |
|---|---|---|
| — | AMC 20-42 provides the acceptable means, guidance and methods for CS-E 50(l), with special consideration of any external engine interfaces and the aircraft-to-engine interfaces. | Accepted method |
| — | The security risk assessment should take into account specific cases of intentional unauthorised electronic interactions (IUEIs) that could have similar effects on all the Engine Control Systems of an aircraft, and not only interactions that could adversely affect a single engine. | Accepted method |

The second obligation is the substantive one. A security assessment scoped to one
engine is not sufficient: the assessment must consider an interaction that
reaches every control system on the aircraft at once.


## Compliance

### Scope and interpretation

- Control system boundary definition, stating what is inside and outside the Engine Control System [AMC E 50(1)].
- Component-level coverage of control system items under [[CS-E 80]] and [[CS-E 170]] in addition to CS-E 50 [AMC E 50(2)].
- Power modulation demonstration expressed as power turbine speed control within specified limits [AMC E 50(3)], against [[CS-E 50|CS-E 50(a)(3)]].
- Integrity case showing at least equivalent safety and reliability to a hydromechanical and magneto system [AMC E 50(4)], supporting [[CS-E 50|CS-E 50(c)]].
- Evaluation against [[CS-E 50|CS-E 50(h)]] for every function depending on aircraft-supplied electrical power [AMC E 50(5)].
- Air signal line design precautions and corrosion assessment [AMC E 50(6)], within the safety assessment of [[CS-E 50|CS-E 50(d)]].

### Over-speed protection

- BITE or functional test design providing a complete test of the electrical and electronic part of the over-speed protection [AMC E 50(e)], satisfying [[CS-E 50|CS-E 50(e)(1)]].
- Safety analysis of the mechanical or actuating part of the protection system, establishing whether inspection or test is needed and at what interval [AMC E 50(e)], within [[CS-E 510]].
- Manual test specification in the instructions for operation where the test is not fully automatic [CS-E 50(e)(1)].

### 30-Second OEI automatic control

- Automatic activation and control design for 30-Second OEI power, requiring no pilot input other than a termination command [AMC E 50(j)(1)], satisfying [[CS-E 50|CS-E 50(j)]].
- Demonstration that automatic control is effective in normal and abnormal operation [AMC E 50(j)(1)].
- Demonstration that the means does not prevent the engine reaching and maintaining rated 30-Second OEI Power [AMC E 50(j)(2)], evidenced jointly with [[AMC E 20|AMC E 20(f)(5)]].
- Type certificate data sheet entry for the limits associated with the rating [AMC E 50(j)(1)], under [[CS-E 40|CS-E 40(e)]].

### Security

- Security risk and vulnerability assessment under AMC 20-42 [AMC to CS-E 50(l)], satisfying [[CS-E 50|CS-E 50(l)]].
- Explicit treatment of common-mode IUEIs affecting all engine control systems of an aircraft, alongside single-engine cases [AMC to CS-E 50(l)].
- Assessment of external engine interfaces and aircraft-to-engine interfaces [AMC to CS-E 50(l)].
- Procedures and Instructions for Continued Airworthiness maintaining the security protections [CS-E 50(l)], carried into [[CS-E 25|CS-E 25(c)(13)]].

## Application to this engine

### Scope and interpretation

Point (3) is the rotorcraft-specific provision and it changes what must be
demonstrated. On a turboshaft with power turbine speed governing, "modulation of
Engine power or thrust with adequate sensitivity and accuracy" under
[[CS-E 50|CS-E 50(a)(3)]] means holding power turbine speed within limits.

Point (5) binds fully. The engine uses a full-authority EECS, so it does not
inherit the inherent compliance that a hydromechanical system enjoys, and every
aircraft-supplied electrical power dependency must be evaluated against
[[CS-E 50|CS-E 50(h)]].

Point (1) settles where "OEI override" is assessed. If the feature controls,
limits or monitors engine operation and is necessary for continued airworthiness,
it is part of the Engine Control System and falls under CS-E 50 — not under
[[CS-E 40]] as a rating.

[VERIFY: AMC E 50(2) and (5) cite AMC 20-1 and AMC 20-3 for detailed
interpretation of CS-E 50 for EECS. Neither is held in `source/`.]

### Over-speed protection

The engine uses a full-authority EECS, so over-speed protection falls under the
electronic route of [[CS-E 50|CS-E 50(e)(1)]] rather than the hydromechanical route of
(e)(2). The BITE method described here is the applicable accepted means.

[[AMC E 50|AMC E 50(1)]] records that blade shedding or engine design related over-speed
protection is not part of the Engine Control System, because it is purely
mechanical. Where such a means is used in addition, it falls outside this AMC.

[VERIFY: AMC E 50(e) refers to a CS-E 50(e) specification for reasonable
assurance that the protection function works. No such wording appears in
CS-E 50(e) at Amendment 8, which instead requires "a means for testing the system
to establish the availability of the protection function". Confirm the AMC is
being read against the current CS-E 50(e) text.]

### 30-Second OEI automatic control

This note binds. The applicant declares a 30-Second OEI Power rating, so
[[CS-E 50|CS-E 50(j)]] applies and this is its accepted means.

The engine uses a full-authority EECS, which is the architecture this AMC assumes:
automatic application, automatic limiting, and no pilot monitoring of shaft
torque, shaft speed, gas generator speed or gas path temperature during the event.

The link to [[AMC E 20|AMC E 20(f)(5)]] is a compliance dependency, not a cross-reference.
The same limiter settings — engine speed, measured gas temperature and fuel flow —
must be shown both to protect the engine and not to block the rating, with
particular attention to take-off with a cold-soaked engine.

[[AMC E 40|AMC E 40(b)(3)(4)]] records that certification assumes up to three uses of the
rating in one flight, and that mandatory maintenance follows any use.

### Security

The engine uses a full-authority EECS with aircraft-supplied data and electrical
power, so the aircraft-to-engine interfaces named here are real attack surfaces
rather than a theoretical case.

The common-mode requirement is the one that drives scope. In a multi-engine
rotorcraft, every engine carries the same control system, so an interaction
exploiting a shared vulnerability reaches all of them. The assessment must cover
that case.

[VERIFY: AMC 20-42 is the named acceptable means for this paragraph and is not
held in `source/`. Obtain it before settling the security compliance method.]

## Not applicable

- **AMC E 50(2)** — the propeller clause. AMC 20-1 and AMC 20-3 are cited for interfaces with the aircraft "and the Propeller when applicable"; a turboshaft has no propeller interface. The same two AMCs are cited again at AMC E 50(5), there without any propeller wording, and that citation is kept.

## References

Specification: [[CS-E 50]]
Related: [[CS-E 25]] · [[CS-E 40]] · [[CS-E 80]] · [[CS-E 170]] · [[CS-E 510]] · [[CS-E 560]] · [[CS-E 830]] · [[AMC E 20]] · [[AMC E 25]] · [[AMC E 40]] · [[AMC E 60]] · [[AMC E 170]]

## Amendment history

All four AMC paragraphs are unchanged at Amendments 7 and 8. AMC to CS-E 50(l)
was introduced at Amendment 6.

The heading of AMC E 50 point (3) is spelled "Rotocraft Engines" in Amendment 8.
This is a typographical error in the source; the body text reads "rotorcraft".
