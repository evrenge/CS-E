---
id: "AMC E 20"
type: AMC
subpart: A
pages: 19-21
changed_in: [Amdt8]
tags: [type-design, interfaces, eecs, installation, oei, power-assurance]
covers: ["AMC E 20", "AMC E 20(f)"]
---
# AMC E 20 — Engine Configuration and Interfaces

> [!summary]
> Two AMC paragraphs serve CS-E 20. The general AMC sets what belongs in the type
> design list, how interfaces with the aircraft are described, and what the
> installation manual must carry for the Engine Control System. AMC E 20(f) is
> separate and much heavier: it governs the power assurance data an OEI engine
> must hand to the installer. Both bind here — the engine declares three OEI
> ratings and uses a full-authority EECS that depends on aircraft-supplied
> resources.

## Requirement

### AMC E 20 — configuration and interfaces

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | The type design list should include the items necessary for satisfactory functioning and control of the engine. | Accepted method |
| **(2)** | Items providing non-mechanical inputs need not be listed if the characteristics of those inputs — voltage, current, timing, fuel, air — can be clearly specified. | Relief |
| **(3)** | Components identified under CS-E 20(c) are interfaces for CS-E 20(d). Consider their effect on the engine in normal and Failure cases during certification. The instructions for installation should state the need for such components to comply with CS-E 80(c). | Accepted method |
| **(4)** | Give the aircraft manufacturer the assumptions made during engine certification that must be taken into account when designing the installation. Where appropriate, coordinate with the aircraft manufacturer so that engine design considerations imposed by the assumed installation certification specifications are taken into account. | Accepted method |
| **(4)** | For example, make all necessary provision in the engine for the fitment and operation of at least the mandatory items of equipment prescribed by the use of the word 'should' in the assumed applicable aircraft specifications. | Accepted method |
| **(5)** | The instructions for installation should include, or reference, installation interface descriptions, limitations and specifications for the Engine Control System. | Accepted method |
| **(6)** | The trend toward system integration may lead to an EECS that has other control functions integrated within it, or that depends on aircraft resources. Examples of such aircraft-supplied resources include recording of rotorcraft one-engine-inoperative data, and aircraft central computers performing some or all of the engine control functions. | Statement |
| **(6)** | The applicant is responsible for specifying the specifications for the EECS for those aircraft-supplied resources in the instructions for installation, and for substantiating the adequacy of those specifications. | Statement |
| **(7)** | The instructions for installation should describe all operational modes of the Engine Control System and its functional interface with the aircraft systems, including Back-up or Alternate Modes, whether dispatchable or not. | Accepted method |

Point (5) gives two worked examples: EECS power specifications and quality,
including interrupt limitations; and the impedance and buffering limitations for
signals the EECS provides for display and instrumentation, or consumes, such as
air data.

Point (6) allocates responsibility rather than creating a duty. The source writes
that the applicant "is responsible for" specifying and substantiating, which is
declaratory, so the row reads Statement. The binding duty is elsewhere: the
instructions for installation are required by [[CS-E 20|CS-E 20(d)]], and this
point fixes who must populate them for aircraft-supplied resources. Reading the
row as Statement does not make the work optional.

### AMC E 20(f) — power assurance data for OEI engines

| Ref | Obligation | Strength |
|---|---|---|
| **(f)(1)** | Provide in the instructions for installation the engine data the installer needs to meet the power availability specifications of CS-27.45(f) or CS-29.45(f). The data should include the effects of installation losses definable at engine level — customer bleed, customer power extraction, and others as appropriate — up to and including the highest power rating. | Accepted method |
| **(f)(2)** | The CS-E 510 safety analysis should consider dormant Failures that could make an OEI rating unavailable, and those results should form part of the CS-E 20(f) data. | Accepted method |
| **(f)(3)** | The data should support maintenance procedures, intervals and standards, including sensors and indicating systems, that detect latent or dormant conditions not found by normal aircraft power assurance procedures. Validate their adequacy on the basis of the engine and engine systems FMEA required under CS-E 510. | Accepted method |
| **(f)(4)** | The data should let the installer establish power assurance procedures in which results can be extrapolated from a lower power check level up to the highest OEI rating power. | Accepted method |
| **(f)(5)** | Provide information on methods assuring that engine limiter settings would not prevent the engine from reaching the 30-Second or 2-Minute OEI power made automatically available under CS-E 50(j). | Accepted method |

Point (f)(3) states the objective. The installer must be able to confirm the
engine can obtain and sustain its OEI ratings within the rating operating
limitations. The operator must also be able to trend individual engine
performance. Two examples are given of conditions that normal power assurance
will not catch: fuel control maximum flow capability, and turbine section
distress. Normal power assurance misses them because the procedure will not
include a topping check to the highest OEI rating power level.

Point (f)(4) sets out how to establish the minimum acceptable engine performance
characteristic. For a mature programme, production acceptance test data,
engine-to-engine variation and pre-overhaul testing can be used. For a new design
or a remote derivative, development and certification test experience should be
used, and an estimated worst engine-to-engine variation assumed initially.

Point (f)(5) names the limiter settings to examine: engine speed, measured gas
temperature and fuel flow. It directs particular attention to take-off conditions
with a cold-soaked engine.

## Compliance

### Configuration and interfaces

- Type design list scoped to items necessary for functioning and control [AMC E 20(1)].
- Interface effect assessment for CS-E 20(c) components, in normal and Failure cases [AMC E 20(3)], against [[CS-E 80|CS-E 80(c)]].
- Installation assumptions package handed to the aircraft manufacturer [AMC E 20(4)], the same material [[CS-E 30]] requires.
- Installation manual sections: control system interface descriptions, limitations and specifications [AMC E 20(5)]; the specifications for the EECS on aircraft-supplied resources, with substantiation of their adequacy [AMC E 20(6)]; all operational modes and their aircraft interface [AMC E 20(7)].

### Power assurance data

- Installation data pack covering power availability, with installation losses to the highest power rating [AMC E 20(f)(1)].
- Dormant Failure analysis for OEI rating availability, within the [[CS-E 510]] safety analysis, delivered as part of the CS-E 20(f) data [AMC E 20(f)(2)].
- Engine and engine systems FMEA under [[CS-E 510]], used to validate the maintenance procedures, intervals and standards [AMC E 20(f)(3)].
- Engine database supporting the above: thermodynamic model, development and certification test experience, and field experience of this type or of similar design [AMC E 20(f)(3)].
- Extrapolation basis from a lower power check level to the highest OEI rating power, against a minimum acceptable engine performance characteristic in a deteriorated state [AMC E 20(f)(4)].
- Limiter setting assessment for 30-Second and 2-Minute OEI power availability, including the cold-soaked take-off case [AMC E 20(f)(5)].

## Application to this engine

Point (6) is the one that binds hardest in the general AMC. It names "recording
of rotorcraft One Engine Inoperative data" as an example of an aircraft-supplied
resource on which an EECS may depend.

[VERIFY: whether this engine's EECS in fact depends on an aircraft-supplied
resource for OEI usage recording. [[CS-E 60|CS-E 60(d)(2)]] requires "means or
provision for means" to record each usage, and provision-for-means does not by
itself create a dependency on the aircraft. If the dependency exists, AMC E 20(6)
makes its specification and substantiation the applicant's responsibility.]

All of AMC E 20(f) binds: the applicant declares 30-Second OEI, 2-Minute OEI and
Continuous OEI, and (f)(1) applies to an engine having one or more OEI ratings.

Point (f)(5) links directly to [[CS-E 50|CS-E 50(j)]] and [[AMC E 50]]: the
30-Second OEI power must be automatically available, and limiter settings must
not defeat that.

The engine uses a full-authority EECS, so points (5), (6) and (7) apply at full
weight rather than as the hydromechanical minimum.

[VERIFY: AMC E 20(f)(1) cites CS-27.45(f) or CS-29.45(f). The applicable aircraft
certification specification code is identified under [[CS-E 20|CS-E 20(b)]] and is
not yet fixed in `engine_profile.md`.]

## Not applicable

- **AMC E 20(6)**, propeller example — the integrated Engine and Propeller Control System case does not arise for a turboshaft.
- **AMC E 20(7)**, in part — the propeller clause in the description of operational modes and functional interfaces. A turboshaft has no propeller interface.

## References

Specification: [[CS-E 20]]
Related: [[CS-E 30]] · [[CS-E 50]] · [[CS-E 60]] · [[CS-E 80]] · [[CS-E 510]] · [[CS-E 25]] · [[AMC E 50]] · [[AMC E 40]]

## Amendment history

AMC E 20 is unchanged at Amendments 7 and 8.

AMC E 20(f) was amended at Amendment 8, under the change information document's
"Editorial corrections" heading. Two kinds of edit:

- in the title, "OEI power ratings" was recapitalised to "OEI Power Ratings". The rest of the banner, "Power Assurance Data for Engines with One or More OEI", is unchanged;
- in point (5), the cross-reference "CS-E 50(**f**)" was corrected to "CS-E 50(**j**)". CS-E 50(j) is the paragraph requiring automatic availability of 30-Second OEI Power, so the earlier reference pointed at the wrong sub-point.

No change to the substance of the data required.
