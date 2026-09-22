---
id: "CS-E 20"
type: CS
subpart: A
pages: 18-18
changed_in: []
imports: [CS-27, CS-29]
tags: [type-design, interfaces, manuals, installation, oei]
---
# CS-E 20 — Engine Configuration and Interfaces

> [!summary]
> This paragraph fixes the boundary of the type certificate: what is inside the
> declared engine configuration, what sits on the engine but outside it, and
> what the installer must be told. It requires the installation and operating
> manuals, the engine performance data pack, and — for an engine with OEI
> ratings — the data the aircraft manufacturer needs to build power assurance
> procedures. All of it binds here, including sub-point (f).

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| **(a)** | Establish the list of all parts and equipment, with references to the relevant drawings, defining the proposed engine type design. | Required |
| **(b)** | Identify the aircraft certification specification code assumed applicable to the intended installation, under CS-E 30. | Required |
| **(c)** | Identify the aircraft parts and equipment that may be mounted on, or driven by, the engine but are outside the declared engine configuration and therefore outside the engine type certificate. | Required |
| **(d)** | Provide manuals containing instructions for installing and operating the engine. They must define the physical and functional interfaces with the aircraft and aircraft equipment, and describe the Primary Mode, all Alternate Modes and any Back-up System of the Engine Control System and its interface with the aircraft systems, with their limitations. Include interface security requirements when necessary. | Required |
| **(e)** | Provide engine performance data for aircraft certification performance, handling and stressing, compatible with the engine acceptance and operating limitations. The data must allow a 'minimum' and a 'maximum' engine to be derived, and must include means of determining the effect on performance of engine bleed, power off-take, forward speed, ambient pressure, temperature and humidity. | Required |
| **(f)** | For engines having one or more OEI ratings, provide data on engine performance characteristics and variability, so the aircraft manufacturer can establish power assurance procedures. | Required if claimed |

This paragraph fixes the boundary of the type certificate. Sub-point (a) says
what is inside it, and sub-point (c) says what sits on the engine but is not.

## Compliance

- Type design definition: parts and equipment list with drawing references [CS-E 20(a)].
- Statement of the assumed aircraft certification specification code [CS-E 20(b)], carried into the assumptions of [[CS-E 30]].
- List of aircraft parts and equipment mounted on or driven by the engine and excluded from the type certificate [CS-E 20(c)].
- Installation manual: physical and functional interfaces, Control Mode descriptions and their limitations, interface security requirements where necessary [CS-E 20(d)].
- Operating manual [CS-E 20(d)].
- Performance data pack supporting minimum and maximum engine derivation, with bleed, off-take, forward speed, ambient pressure, temperature and humidity effects [CS-E 20(e)].
- OEI performance characteristics and variability data for power assurance [CS-E 20(f)], scope per [[AMC E 20|AMC E 20(f)]].

Guidance on all of the above: [[AMC E 20]].

## Application to this engine

Sub-point (f) binds. The applicant declares 30-Second OEI, 2-Minute OEI and
Continuous OEI, so the power assurance data set is mandatory [CS-E 20(f)].
[[AMC E 20|AMC E 20(f)]] was amended at Amendment 8 and governs its content.

Sub-point (d) requires the Control Mode description. For a full-authority EECS
that means the Primary Mode, every Alternate Mode and any Back-up System, each
with its limitations [CS-E 20(d)]. The propeller clause in (d) does not arise.

The installer also needs engine data for the rotor drive system tests of the
rotorcraft code. Under CS-29 that includes the rotational speed expected after
an engine control device failure. The over-speed test runs at not less than the
higher of that speed or 105% of the maximum rotational speed expected in service
[ext CS 29.927(d)]. CS-27 asks for no such figure, because it prescribes no
over-speed test for the rotor drive system [ext CS 27.927]. The data item is
therefore a CS-29 item. An engine offered for installation under either code
carries it because CS-29 asks for it. See [[CS 29.927]] and [[CS 27.927]].

Aircraft-supplied resources on which the EECS depends are specified in the
engine instructions for installation, the manuals of sub-point (d)
[AMC E 20(6)]. [[AMC E 20]] names the recording of rotorcraft One Engine
Inoperative data as one such resource [AMC E 20(6)].

## Not applicable

- **(d)**, propeller clause — the Control System interface description covers "including the Propeller when applicable"; a turboshaft drives a rotor and has no propeller control interface.
- Throughout — where the source pairs thrust with power, in any of the forms it uses, only the power term is carried. This engine produces shaft power; the thrust half of each pair has no turboshaft case.

## References

Accepted means: [[AMC E 20]] · [[AMC E 20|AMC E 20(f)]]
Related: [[CS-E 25]] · [[CS-E 30]] · [[CS-E 50]] · [[CS-E 40]]
External: [[CS 29.927]] · [[CS 27.927]]

## Amendment history

Unchanged at Amendments 7 and 8. [[AMC E 20|AMC E 20(f)]] was amended at
Amendment 8.
