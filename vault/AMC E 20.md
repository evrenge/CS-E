---
id: "AMC E 20"
type: AMC
subpart: A
pages: 19-19
changed_in: []
tags: [type-design, interfaces, eecs, installation]
---
# AMC E 20 — Engine Configuration and Interfaces

> [!quote] AMC E 20(1)
> "The components and equipment listed in the Engine type design (see CS-E 20(a)) should include those items necessary for the satisfactory functioning and control of the Engine."

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | The type design list should include the items necessary for satisfactory functioning and control of the engine. | Accepted method |
| **(2)** | Items providing non-mechanical inputs need not be listed if the characteristics of those inputs — voltage, current, timing, fuel, air — can be clearly specified. | Relief |
| **(3)** | Components identified under CS-E 20(c) are interfaces for CS-E 20(d). Consider their effect on the engine in normal and Failure cases during certification. The instructions for installation should state the need for such components to comply with CS-E 80(c). | Accepted method |
| **(4)** | Give the aircraft manufacturer the assumptions made during engine certification that must be taken into account when designing the installation. Where appropriate, coordinate with the aircraft manufacturer so that engine design considerations imposed by the assumed installation certification specifications are taken into account. | Accepted method |
| **(5)** | The instructions for installation should include, or reference, installation interface descriptions, limitations and specifications for the Engine Control System. | Accepted method |
| **(6)** | System integration may produce an EECS with other control functions integrated, or one that depends on aircraft resources. The applicant is responsible for specifying the EECS requirements for those aircraft-supplied resources in the instructions for installation, and for substantiating their adequacy. | Accepted method |
| **(7)** | The instructions for installation should describe all operational modes of the Engine Control System and its functional interface with the aircraft systems, including Back-up or Alternate Modes, whether dispatchable or not. | Accepted method |

Point (5) gives two worked examples: EECS power specifications and quality,
including interrupt limitations; and the impedance and buffering limitations for
signals the EECS provides for display and instrumentation, or consumes, such as
air data.

## Compliance

- Type design list scoped to items necessary for functioning and control [AMC E 20(1)].
- Interface effect assessment for CS-E 20(c) components, in normal and Failure cases [AMC E 20(3)], against [[CS-E 80]](c).
- Installation assumptions package handed to the aircraft manufacturer [AMC E 20(4)], the same material [[CS-E 30]] requires.
- Installation manual sections: control system interface descriptions, limitations and specifications [AMC E 20(5)]; EECS requirements on aircraft-supplied resources with adequacy substantiation [AMC E 20(6)]; all operational modes and their aircraft interface [AMC E 20(7)].

## Application to this engine

Point (6) is the one that binds hardest. It names "recording of rotorcraft One
Engine Inoperative data" as an example of an aircraft-supplied resource on which
an EECS may depend. The engine declares 30-Second and 2-Minute OEI ratings, whose
usage recording is required by [[CS-E 60]](d), so that dependency is real and its
adequacy must be substantiated here.

The engine uses a full-authority EECS, so points (5), (6) and (7) all apply at
full weight rather than as the hydromechanical minimum.

## Not applicable

- **(6)**, propeller example — the integrated Engine and Propeller Control System case does not arise for a turboshaft.

## References

Specification: [[CS-E 20]]
Related: [[CS-E 30]] · [[CS-E 50]] · [[CS-E 60]] · [[CS-E 80]] · [[AMC E 20(f)]]

## Amendment history

Unchanged at Amendments 7 and 8.
