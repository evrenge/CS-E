---
id: "CS-E 50"
type: CS
subpart: A
pages: 33-36
changed_in: []
tags: [control-system, eecs, fadec, lotc, software, security, oei]
---
# CS-E 50 — Engine Control System

> [!summary]
> The longest paragraph in Subpart A, with 28 obligations covering control system
> operation, Control Mode transitions, failure rates, the system safety
> assessment, over-speed protection, software, aircraft-supplied data and power,
> air signal lines, rapid shutdown and information security. For this engine it
> also requires automatic availability and automatic control of 30-Second OEI
> power. Two of its cross-references — CS-E 390 and CS-E 210 — are piston
> paragraphs and do not bind a turbine engine.

## Requirement

### Operation and control transitions

| Ref | Obligation | Strength |
|---|---|---|
| **(a)** | Substantiate by test, analysis or a combination that the Engine Control System performs its intended functions. | Required |
| **(a)(1)** | Maintain selected values of relevant control parameters and keep the engine within approved operating limits over changing atmospheric conditions in the declared flight envelope. | Required |
| **(a)(2)** | Comply with the operability specifications of CS-E 500(a) and CS-E 745 under all likely system inputs and allowable power demands, unless it is demonstrated that this is not required for non-dispatchable specific Control Modes. The engine approval is endorsed accordingly. | Required |
| **(a)(3)** | Allow modulation of power with adequate sensitivity and accuracy over the declared range of operating conditions. | Required |
| **(a)(4)** | Do not create unacceptable power oscillations. | Required |
| **(b)** | Demonstrate that a Fault or Failure changing Control Mode, changing channel, or moving from the Primary System to the Back-up System produces the outcomes at (b)(1) to (b)(3). | Required |
| **(b)(1)** | The engine does not exceed any of its operating limitations. | Required |
| **(b)(2)** | The engine does not surge, stall, flame-out, or show unacceptable power changes, oscillations or other unacceptable characteristics. | Required |
| **(b)(3)** | Where the flight crew must initiate, respond to, or be aware of a Control Mode change, provide a means to alert the crew. Describe the provision in the instructions for installation and the crew action in the instructions for operation. | Required |
| **(b)** closing | Identify the magnitude of any power change and the associated transition time, and describe both in the instructions for installation and operation. | Required |

### Failures and safety assessment

| Ref | Obligation | Strength |
|---|---|---|
| **(c)(1)** | Achieve a Loss of Power Control (LOPC) event rate consistent with the safety objective of the intended aircraft application. | Required |
| **(c)(2)** | In the Full-up Configuration, be essentially single-Fault tolerant for electrical and electronic Failures with respect to LOPC events. | Required |
| **(c)(3)** | Single Failures of control system components do not result in a Hazardous Engine Effect. | Required |
| **(c)(4)** | Foreseeable Failures or malfunctions causing local events in the intended installation — fire, overheat, or damage to control system components — do not result in a Hazardous Engine Effect. | Required |
| **(d)** | Complete a system safety assessment for the Engine Control System when complying with CS-E 510. It must identify Faults or Failures causing a power change, a transmission of erroneous data, or an effect on operability, together with their predicted frequency of occurrence. See also [[CS-E 110|CS-E 110(e)]]. | Required |

### Protection systems, software and signal lines

| Ref | Obligation | Strength |
|---|---|---|
| **(e)(1)** | Where electronic over-speed protection is provided, include a means of testing the system to establish that the protection function is available. A complete test must be achievable in the minimum number of cycles. If the test is not fully automatic, put the manual test specification in the instructions for operation. | Required |
| **(e)(2)** | Where over-speed protection is hydromechanical or mechanical, demonstrate by test or other acceptable means that the function remains available between inspection and maintenance periods. | Required |
| **(f)** | Design, implement and verify all associated software and encoded logic to minimise the existence of errors, using an approved method consistent with the criticality of the functions performed. | Required |
| **(i)** | Consider the effects of blockage or leakage of air pressure signal lines as part of the system safety assessment of CS-E 50(d), and adopt the appropriate design precautions. | Required |

### Aircraft-supplied data and electrical power

| Ref | Obligation | Strength |
|---|---|---|
| **(g)(1)** | Single Failures causing loss, interruption or corruption of Aircraft-Supplied Data, or of data shared between engines, do not result in a Hazardous Engine Effect for any engine. | Required |
| **(g)(2)** | Such Failures must be detected and accommodated. The accommodation strategy must not cause an unacceptable power change or an unacceptable change in operating and starting characteristics. Evaluate and document these effects throughout the flight envelope. | Required |
| **(g)(2)** exception | CS-E 50(g)(2) does not apply to thrust or power command signals from the aircraft. | Relief |
| **(h)(1)** | Design the control system so that loss or interruption of aircraft-supplied electrical power does not result in a Hazardous Engine Effect (i) or cause unacceptable transmission of erroneous data (ii). Take that effect into account when complying with CS-E 50(c)(1). | Required |
| **(h)(2)** | Where an engine-dedicated power source is required for compliance with CS-E 50(h)(1), its capacity should provide sufficient margin for engine operation below idle where the control system is designed to recover engine operation automatically. | Recommended |
| **(h)(3)** | Identify and declare in the instructions for installation the need for, and characteristics of, any aircraft-supplied electrical power for starting and operating the engine, including transient and steady-state voltage limits. | Required |
| **(h)(4)** | Low voltage transients outside the declared limits must meet CS-E 50(h)(1), and the control system must resume normal operation when power returns within the declared limits. | Required |

### Rating availability, shutdown and security

| Ref | Obligation | Strength |
|---|---|---|
| **(j)** | Engines having a 30-Second OEI Power Rating must incorporate means, or provision for means, for automatic availability and automatic control of 30-Second OEI Power within its operating limitations. | Required if claimed |
| **(k)** | Provide means for shutting down the engine rapidly. | Required |
| **(l)** | Design and install the control system, including networks, software and data, so that it is protected from intentional unauthorised electronic interactions (IUEIs) that may adversely affect aircraft safety. Identify, assess and mitigate the security risks and vulnerabilities. Make available procedures and Instructions for Continued Airworthiness that keep the security protections maintained. | Required |

Sub-point (h)(2) is one of the few CS-E paragraphs using "should". It is a
recommendation inside a binding specification, and is weaker than the "must" in
(h)(1) that it supports.

## Compliance

### Substantiation

- Control system functional substantiation by test, analysis or a combination [CS-E 50(a)].
- Demonstration of Control Mode, channel and Primary-to-Back-up transitions [CS-E 50(b)].
- Over-speed protection availability test, by the route matching the protection technology [CS-E 50(e)(1), (e)(2)], guidance at [[AMC E 50|AMC E 50(e)]].
- Demonstration that low voltage transients outside declared limits meet (h)(1), and that normal operation resumes [CS-E 50(h)(4)].

### Analysis

- System safety assessment of the Engine Control System, identifying Faults and Failures causing power change, erroneous data or operability effects, with predicted frequency [CS-E 50(d)], under [[CS-E 510]].
- LOPC rate analysis against the safety objective of the intended aircraft application [CS-E 50(c)(1)].
- Single-Fault tolerance analysis for the Full-up Configuration [CS-E 50(c)(2)].
- Local event analysis: fire, overheat and control component damage [CS-E 50(c)(4)].
- Air pressure signal line blockage and leakage, within the (d) assessment [CS-E 50(i)].
- Aircraft-supplied data failure evaluation, documented across the flight envelope [CS-E 50(g)(2)].
- Security risk and vulnerability assessment [CS-E 50(l)], guidance at [[AMC E 50|AMC to CS-E 50(l)]].

### Documents

- Software and encoded logic development evidence under an approved method matched to criticality [CS-E 50(f)].
- Instructions for installation: Control Mode alert provision [CS-E 50(b)(3)]; power change magnitude and transition time [CS-E 50(b)]; electrical power need, characteristics and voltage limits [CS-E 50(h)(3)].
- Instructions for operation: crew action on Control Mode change [CS-E 50(b)(3)]; manual over-speed test specification where the test is not fully automatic [CS-E 50(e)(1)].
- ICA covering maintenance of the security protections [CS-E 50(l)], carried into [[CS-E 25|CS-E 25(c)(13)]].

Guidance on the whole paragraph: [[AMC E 50]]. CS-E 50 also cites AMC 20-1,
AMC 20-3 and AMC 20-115, which are not held in `source/`.

## Application to this engine

Sub-point (j) binds. The applicant declares a 30-Second OEI Power rating, so
automatic availability and automatic control of that rating are mandatory.
[[AMC E 50|AMC E 50(j)]] governs the method.

"OEI override" is a control-system feature, not a rating under [[CS-E 40]]. It is
assessed here and in the [[CS-E 510]] safety assessment required by (d).

The engine uses a full-authority EECS, so the electronic route at (e)(1) applies
to over-speed protection rather than the hydromechanical route at (e)(2), and the
software obligations at (f) carry their full weight.

Sub-point (a)(2) cites CS-E 390 as well as CS-E 500(a) and CS-E 745. CS-E 390 is
in Subpart C and applies to piston engines, so only CS-E 500(a) and CS-E 745 bind
here. Sub-point (d) likewise cites CS-E 210, a Subpart B paragraph; [[CS-E 510]]
is the turbine engine route.

[VERIFY: AMC 20-1, AMC 20-3 and AMC 20-115 are cited by this paragraph and are
not held in `source/`. Obtain them before settling the control system compliance
method.]

## Not applicable

- **(a)(2)**, in part — the reference to CS-E 390, a Subpart C piston engine paragraph, alongside CS-E 500. Subpart C is outside this vault by scope.
- **(d)**, in part — the reference to CS-E 210, a Subpart B piston engine paragraph. Subpart B is outside this vault by scope. The CS-E 110(e) reference in the same sub-point is in scope and is carried.

## References

Accepted means: [[AMC E 50]] · [[AMC E 50|AMC E 50(e)]] · [[AMC E 50|AMC E 50(j)]] · [[AMC E 50|AMC to CS-E 50(l)]]
Related: [[CS-E 20]] · [[CS-E 25]] · [[CS-E 30]] · [[CS-E 40]] · [[CS-E 110]] · [[CS-E 510]] · [[AMC E 170]]

## Amendment history

Unchanged at Amendments 7 and 8.
