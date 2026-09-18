---
id: "CS-E 20"
type: CS
subpart: A
chapter: A
pages: 18-18
changed_in: []
tags: [type-design, interfaces, manuals, installation, oei]
---
# CS-E 20 — Engine Configuration and Interfaces

> [!summary]
> Fixes the boundary of the type certificate: what is inside the declared engine
> configuration, what sits on the engine but outside it, and what the installer
> must be told. It requires the installation and operating manuals, the engine
> performance data pack, and — for an engine with OEI ratings — the data the
> aircraft manufacturer needs to build power assurance procedures. All of it
> binds here, including sub-point (f).

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| **(a)** | Establish the list of all parts and equipment, with references to the relevant drawings, defining the proposed engine type design. | Required |
| **(b)** | Identify the aircraft certification specification code assumed applicable to the intended installation, under CS-E 30. | Required |
| **(c)** | Identify the aircraft parts and equipment that may be mounted on, or driven by, the engine but are outside the declared engine configuration and therefore outside the engine type certificate. | Required |
| **(d)** | Provide manuals containing instructions for installing and operating the engine. They must define the physical and functional interfaces with the aircraft and aircraft equipment, and describe the Primary Mode, all Alternate Modes and any Back-up System of the Engine Control System with their limitations. Include interface security requirements when necessary. | Required |
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
Continuous OEI, so the power assurance data set is mandatory. [[AMC E 20|AMC E 20(f)]] was
amended at Amendment 8 and governs its content.

Sub-point (d) requires the Control Mode description. For a full-authority EECS
that means the Primary Mode, every Alternate Mode and any Back-up System, each
with its limitations. The propeller clause in (d) does not arise.

Sub-point (c) is where aircraft-supplied resources are declared. [[AMC E 20]]
names recorded rotorcraft OEI data as one such resource.

## Not applicable

- **(d)**, propeller clause — the Control System interface description covers "including the Propeller when applicable"; a turboshaft drives a rotor and has no propeller control interface.

## References

Accepted means: [[AMC E 20]] · [[AMC E 20|AMC E 20(f)]]
Related: [[CS-E 25]] · [[CS-E 30]] · [[CS-E 50]] · [[CS-E 40]]

## Amendment history

Unchanged at Amendments 7 and 8. [[AMC E 20|AMC E 20(f)]] was amended at Amendment 8.
