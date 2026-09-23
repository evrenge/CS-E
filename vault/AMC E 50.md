---
id: "AMC E 50"
type: AMC
subpart: A
pages: 36-38
changed_in: []
imports: [AMC-20]
tags: [control-system, eecs, fadec, over-speed, oei, security, rotorcraft]
covers: ["AMC E 50", "AMC E 50(e)", "AMC E 50(j)", "AMC to CS-E 50(l)"]
---
# AMC E 50 — Engine Control System

> [!summary]
> Four AMC paragraphs serve CS-E 50. The general AMC fixes what counts as the
> Engine Control System and reads CS-E 50(a)(3) for a rotorcraft as power
> turbine speed control. AMC E 50(e) covers over-speed protection testing,
> AMC E 50(j) the automatic control of 30-Second OEI power, and AMC to
> CS-E 50(l) the security assessment. All four bind: the engine uses a
> full-authority EECS and declares a 30-Second OEI rating.

## Requirement

### AMC E 50 — scope and interpretation

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | CS-E 50 applies to every control system architecture, from hydromechanical to dual-channel full-authority EECS, analogue or digital. The Engine Control System includes any system or device that controls, limits or monitors engine operation and is necessary for continued airworthiness. | Statement |
| **(2)** | CS-E 50 sets objectives for general design and functioning. It does not replace or supersede other specifications, such as CS-E 560 for the fuel system, so individual components such as alternators, sensors and actuators should also be covered under CS-E 80 or CS-E 170 as appropriate. | Accepted method |
| **(3)** | For rotorcraft control systems with a power turbine speed governing mode, the CS-E 50(a)(3) specification for modulation of engine power should be read as the ability to manage power to maintain power turbine speed within specified limits. | Accepted method |
| **(4)** | The intent of CS-E 50(c) is control system integrity consistent with the operational specifications of the application. Electronic control systems should provide at least an equivalent level of safety and reliability to engines with hydromechanical control and protection systems and magneto systems. | Accepted method |
| **(5)** | Control systems in hydromechanical or other non-electrical technology should inherently comply with CS-E 50(h). Where functions are implemented electrically or electronically and depend on aircraft-supplied electrical power, the system should be evaluated against that rule. | Accepted method |
| **(6)** | CS-E 50(i) covers ingress of foreign matter — sand, dust, water, insects — that could block signal lines and adversely affect engine operation. Precautions should be taken, and corrosion effects addressed. | Accepted method |

### What is inside the Engine Control System [(1)]

The Engine Control System includes the electronic control unit(s), fuel metering
unit(s), variable-geometry actuators, cables, wires and sensors. It also covers
the protection systems against over-speed, over-torque and over-temperature
[AMC E 50(1)].

The main engine fuel pump is not usually included, even though it is often
engine-mounted and physically integrated with the fuel metering unit
[AMC E 50(1)].

Blade shedding or engine design related over-speed protection is not included,
because that protection is purely mechanical and works without influence from
the control system [AMC E 50(1)].

Engine monitoring systems are covered when physically or functionally integrated
with the control system, or when they perform functions affecting engine safety,
or are used for continued-operation or return-to-service decisions. Low cycle
fatigue (LCF) cycle-counters for Engine Critical Parts are included. Most trend
monitors and maintenance information devices are not — those fall under
[[CS-E 170]] [AMC E 50(1)].

### Air signal line precautions [(6)]

The worked example given is that lines measuring static pressure in the
compressor of turbine engines could be blocked by frozen water, leading to a
loss of power. The suggested precautions are protected openings, filters, drains
for water, and heating of the lines to prevent freezing of condensed water
[AMC E 50(6)].

### AMC E 50(e) — over-speed protection testing

| Ref | Obligation | Strength |
|---|---|---|
| — | Over-speed protection is usually provided as part of the electronic Engine Control System, even where the devices are nominally independent. Periodic testing by built-in test equipment (BITE) or a functional test is one acceptable method of showing the protection function is available. | Accepted method |
| — | For an over-speed protection system, the BITE test should provide a complete test of the electrical and electronic part of the protection system. | Accepted method |
| — | The need for inspections or tests of the mechanical or actuating part of the protection system should be based on the results of the safety analysis for that part. | Accepted method |

The split matters. The electrical and electronic part is covered by a complete
BITE test. The mechanical and actuating part is not. The need for its inspection
or test is based on the safety analysis for that part, not on this AMC
[AMC E 50(e)].

### AMC E 50(j) — automatic control of 30-Second OEI power

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | The 30-Second OEI rating should be applied and controlled by an automatic means requiring no pilot input or control other than a termination command. Once activated it automatically controls the 30-Second OEI power and prevents the engine exceeding the limits associated with the rating in the type certificate data sheet. | Accepted method |
| **(1)** | The automatic control within the operating limitations should be effective during normal and abnormal operations. | Accepted method |
| **(2)** | The means required by CS-E 50(j) should not prevent the engine from reaching and maintaining its rated 30-Second OEI Power. | Accepted method |

### Why automatic control is required [(1)]

The flight and operating conditions requiring use of this rating may create a
high pilot workload to maintain safe flight. That is the stated reason for
automatic application and control [AMC E 50(j)(1)].

The rating could already use almost all the available margins in the engine
design. Exceeding the limits associated with it would therefore likely result in
an engine Failure — unacceptable in a critical flight condition with one engine
already failed [AMC E 50(j)(1)].

The automatic control is intended to remove the need to monitor engine
parameters during the event: output shaft torque or power, output shaft speed,
gas generator speed and gas path temperatures [AMC E 50(j)(1)].

### The two-sided constraint

Point (1) asks the means to prevent the engine exceeding rating limits
[AMC E 50(j)(1)]. Point (2) asks the same means not to prevent the engine
reaching and maintaining rated 30-Second OEI Power [AMC E 50(j)(2)]. The control
therefore sits between those bounds, which is why [[AMC E 20|AMC E 20(f)(5)]]
asks for information showing that limiter settings do not block the rating.

### AMC to CS-E 50(l) — information system security protection

| Ref | Obligation | Strength |
|---|---|---|
| — | AMC 20-42 provides the acceptable means, guidance and methods for CS-E 50(l), with special consideration of any external engine interfaces and the aircraft-to-engine interfaces. | Accepted method |
| — | The security risk assessment should take into account specific cases of intentional unauthorised electronic interactions (IUEIs) that could have similar effects on all the Engine Control Systems of an aircraft, and not only interactions that could adversely affect a single engine. | Accepted method |

The second obligation is the substantive one. Under this accepted means, a
security assessment scoped to one engine is not sufficient. The assessment
should also take into account interactions that could have similar effects on
all the Engine Control Systems of an aircraft [AMC to CS-E 50(l)].

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
[[CS-E 50|CS-E 50(a)(3)]] means holding power turbine speed within limits
[AMC E 50(3)].

Point (5) applies in full. The engine uses a full-authority EECS, so it does not
inherit the inherent compliance of a hydromechanical system. Every function that
depends on aircraft-supplied electrical power is evaluated against
[[CS-E 50|CS-E 50(h)]] [AMC E 50(5)].

Point (1) settles where "OEI override" is assessed. If the feature controls,
limits or monitors engine operation and is necessary for continued
airworthiness, it is part of the Engine Control System [AMC E 50(1)]. It falls
under CS-E 50 — not under [[CS-E 40]] as a rating.

AMC 20-1 and AMC 20-3 are now held. The detailed interpretation this AMC defers
to is in [[AMC 20-3B]], which that note records in full: the rotorcraft loss of
power control definition, the rate of one event per 100 000 engine flight hours,
the HIRF and lightning pass criteria, and the over-speed protection targets.
AMC 20-1A is its aircraft-level companion; its guidance relates to aircraft
certification and so addresses the installer [ext AMC 20-1A 3].

### Over-speed protection

[VERIFY: which route of [[CS-E 50|CS-E 50(e)]] governs over-speed protection on
this engine. Sub-point (e)(1) applies where the protection is electronic and
(e)(2) where it is not, and AMC E 50(1) names a third case — blade-shedding or
engine-design over-speed protection — that is outside the Engine Control System
altogether. A full-authority EECS does not by itself settle which, and
`engine_profile.md` does not declare the protection technology. The BITE method
described here is the accepted means for the electronic route.]

AMC E 50(1) records that blade shedding or engine design related over-speed
protection is not part of the Engine Control System, because it is purely
mechanical. Where such a means is used in addition, it falls outside this AMC
[AMC E 50(1)].

[VERIFY: AMC E 50(e) refers to a CS-E 50(e) specification for reasonable
assurance that the protection function works. No such wording appears in
CS-E 50(e) at Amendment 8, which instead requires "a means for testing the
system to establish the availability of the protection function". Confirm the
AMC is being read against the current CS-E 50(e) text.]

### 30-Second OEI automatic control

AMC E 50(j) applies. The applicant declares a 30-Second OEI Power rating, so
[[CS-E 50|CS-E 50(j)]] applies and this is its accepted means.

The engine uses a full-authority EECS. That architecture can provide what the
AMC describes: automatic application, automatic limiting, and no need for the
pilot to monitor shaft torque, shaft speed, gas generator speed or gas path
temperature during the event [AMC E 50(j)(1)].

The link to [[AMC E 20|AMC E 20(f)(5)]] is a compliance dependency, not a
cross-reference. The same limiter settings — engine speed, measured gas
temperature and fuel flow — protect the engine under point (1), and should not
prevent the engine reaching the rating under point (2) [AMC E 50(j)(2)].
AMC E 20(f)(5) directs particular attention to take-off with a cold-soaked
engine [AMC E 20(f)(5)].

[[AMC E 40|AMC E 40(b)(3)(4)]] records that certification assumes up to three
uses of the rating in one flight, and that mandatory maintenance follows any
use.

### Security

The engine uses a full-authority EECS, which may depend on aircraft-supplied
data and electrical power. The aircraft-to-engine interfaces named here are
therefore in scope for the assessment [AMC to CS-E 50(l)].

The common-mode provision is the one that drives scope. In a multi-engine
rotorcraft with engines of this type, each engine carries the same control
system, so an interaction exploiting a shared vulnerability could reach all of
them. The assessment should cover that case [AMC to CS-E 50(l)].

AMC 20-42 is now held, and it names the process: a product information security
risk assessment, run in seven steps from determining the security environment to
iterating until every residual risk is acceptable [ext AMC 20-42 5(a)].
[[AMC 20-42]] sets out the steps, the acceptance criterion, the verification of
the mitigations and the instructions for continued airworthiness in full.

Two of its consequences reach this note. A reported occurrence that has
generated an unsafe condition through an intentional unauthorised electronic
interaction is reported to the Agency under point 21.A.3A [ext AMC 20-42 9],
which is the route recorded in [[AMC E 515]]. And the accepted industry
documents are not held [ext AMC 20-42 1(b)], so the method inside the process
remains a dead end.

## Not applicable

- **AMC E 50(2)** — the propeller clause. AMC 20-1 and AMC 20-3 are cited for interfaces with the aircraft "and the Propeller when applicable"; a turboshaft has no propeller interface. The same two AMCs are cited again at AMC E 50(5), there without any propeller wording, and that citation is kept.

## References

Specification: [[CS-E 50]]
Related: [[CS-E 25]] · [[CS-E 40]] · [[CS-E 80]] · [[CS-E 170]] · [[CS-E 510]] · [[CS-E 560]] · [[CS-E 830]] · [[AMC E 20]] · [[AMC E 25]] · [[AMC E 40]] · [[AMC E 60]] · [[AMC E 170]]
External: [[AMC 20-1A]] · [[AMC 20-3B]] · [[AMC 20-42]] · [[AMC 20-115D]]

## Amendment history

All four AMC paragraphs are unchanged at Amendments 7 and 8. AMC to CS-E 50(l)
was introduced at Amendment 6.

The heading of AMC E 50 point (3) is spelled "Rotocraft Engines" in Amendment 8.
This is a typographical error in the source; the body text reads "rotorcraft".
