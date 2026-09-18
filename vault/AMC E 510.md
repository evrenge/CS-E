---
id: "AMC E 510"
type: AMC
subpart: D
pages: 83-91
changed_in: [Amdt7]
tags: [safety-analysis, fmea, fault-tree, hazardous-engine-effect, debris, toxic-products, maintenance-error]
---
# AMC E 510 — Safety analysis

> [!summary]
> One long AMC serves CS-E 510. It sets the objective of the analysis, explains
> why aircraft-level Failure classifications cannot be reused at engine level,
> and works through each Hazardous Engine Effect in turn — most extensively
> non-containment of high-energy debris, which Amendment 7 rewrote. It then
> covers Major and Minor Engine Effects, how to determine a Failure's effect,
> and what reliance on maintenance actions requires. Analytical techniques,
> reference documents and four definitions close it.

## Requirement

### AMC E 510(1) to (2) — introduction and objective

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | Compliance with CS-E 510 requires a safety analysis, substantiated when necessary by appropriate testing or comparable service experience. | Statement |
| **(1)** | The depth and scope of an acceptable safety assessment depend on the complexity and criticality of the functions performed, the severity of related Failure conditions, the uniqueness of the design, the extent of relevant service experience, the number and complexity of the identified Failures, and the detectability of contributing Failures. | Statement |
| **(1)** | Examples of methodologies are Fault Tree Analysis (FTA), Failure Mode and Effects Analysis (FMEA) and Markov Analysis. | Statement |
| **(2)** | The ultimate objective is to ensure that the risk to the aircraft from all engine Failure conditions is acceptably low, by managing the individual major and hazardous engine risks to acceptable levels and reducing the likelihood of an event proportionally with the severity of its effects. | Statement |
| **(2)** | The analysis should support the engine design goals such that there would not be Major or Hazardous Engine Effects exceeding the required probability of occurrence as a result of engine Failure modes. | Accepted method |
| **(2)** | The analysis should consider the full range of expected operations. | Accepted method |

### AMC E 510(3)(a) to (c) — classification, component level, typical installation

| Ref | Obligation | Strength |
|---|---|---|
| **(3)(a)** | Aircraft-level Failure classifications are not directly applicable to engine assessments, since the aircraft may have features that reduce or increase the consequences, and the same type-certificated engine may be used in a variety of installations. CS-E 510 defines the engine-level Failure conditions and presumed severity levels. | Statement |
| **(3)(a)** | Since aircraft-level specifications for individual Failure conditions may be more severe than the engine-level specifications, co-ordinate early between the applicant and the aircraft manufacturer to ensure engine and aircraft compatibility. | Accepted method |
| **(3)(b)** | A component level safety analysis may be an auditable part of the design process, or may be conducted specifically to demonstrate compliance. | Permitted |
| **(3)(b)** | Integrate the specific specifications of CS-E 50 for the Engine Control System into the overall engine safety analysis. | Accepted method |
| **(3)(c)** | "Typical installation" in CS-E 510(a)(1)(i) does not imply the aircraft-level effects are known, but that assumptions of typical aircraft devices and procedures — fire-extinguishing equipment, annunciation devices and similar — are clearly stated in the analysis. | Statement |
| **(3)(c)** | Where the applicant cannot determine the detailed Failure sequence, rate of occurrence or dormancy period of Failures of aircraft components, the applicant will assume a Failure rate for those components for engine certification. | Statement |
| **(3)(c)** | CS-E 510(a)(1)(i) requires the applicant to take account of aircraft-level devices in the engine safety analysis; the effects on the engine of a Failure of aircraft air ducts is the example the AMC gives. | Statement |
| **(3)(c)** | Compliance with CS-E 510(e) requires the applicant to provide, in the engine instructions for installation, the list of Failures of aircraft components that may result in or contribute to Hazardous or Major Engine Effects. | Required |
| **(3)(c)** | The mode of propagation to this effect should be described and the assumed Failure rates should be stated. | Accepted method |
| **(3)(c)** | Address such assumptions in compliance with CS-E 30. | Accepted method |

The instructions-for-installation duty in (3)(c) is the mechanism that makes the
engine analysis auditable at aircraft level. The installer receives the list of
aircraft-component Failures the engine analysis depends on, the propagation
mode, and the rates assumed, and can then substitute the actual rates.

### AMC E 510(3)(d) — Hazardous Engine Effects

| Ref | Obligation | Strength |
|---|---|---|
| **(3)(d)(i)** | The acceptable occurrence rate of Hazardous Engine Effects applies to each individual effect. Absolute proof is not possible at this order of magnitude, and reliance should be placed on engineering judgement and previous experience combined with sound design and test philosophies. | Statement |
| **(3)(d)(i)** | The probability target of not greater than 10⁻⁷ per Engine flight hour for each Hazardous Engine Effect applies to the summation of the probabilities of that effect arising from individual Failure modes or combinations, other than the Failure of Engine Critical Parts such as discs, hubs and spacers. | Accepted method |
| **(3)(d)(i)** | Include the possible dormant period of Failures in the calculations of Failure rates. | Accepted method |
| **(3)(d)(i)** | If each individual Failure is less than 10⁻⁸ per Engine flight hour, summation is not required. | Relief |
| **(3)(d)(ii)** | Where the numerical Failure rate of primary Failures of certain single elements such as Engine Critical Parts cannot be sensibly estimated, and their Failure is likely to result in Hazardous Engine Effects, place reliance on their meeting the prescribed integrity specifications, such as CS-E 515 among others. | Accepted method |
| **(3)(d)(ii)** | These specifications are considered to support a design goal that, among other goals, primary LCF (Low Cycle Fatigue) Failure of the component should be Extremely Remote throughout its operational life. | Statement |
| **(3)(d)(ii)** | There is no specification to include the estimated primary Failure rates of such single elements in the summation of Failures for each Hazardous Engine Effect, due to the difficulty of producing and substantiating such an estimate. | Relief |
| **(3)(d)(iii)** | Uncontained debris covers a large spectrum of energy levels, due to the various sizes and velocities of parts released in an engine Failure. | Statement |
| **(3)(d)(iii)** | As a general principle, if a Failure can result in debris being released with an energy and trajectory that cause an unsafe condition, consider such debris as uncontained high-energy debris causing a Hazardous Engine Effect. | Accepted method |
| **(3)(d)(iii)** | Engine containment structures are not required to contain major rotating parts should they fail. Unless containment has been demonstrated, assume the Failure of discs, hubs, impellers, large rotating seals and other similar large rotating components results in uncontained high-energy debris, causing a Hazardous Engine Effect. | Accepted method |
| **(3)(d)(iii)** | For such parts, the Extremely Remote probability objective necessary for compliance with CS-E 510(a)(3) can only be ensured through compliance with CS-E 515, supplemented by CS-E 840 and CS-E 850. | Statement |
| **(3)(d)(iii)** | The engine must be designed to ensure that debris resulting from the shedding of compressor or turbine blades, either singly or in likely combinations, will be radially contained. | Required |
| **(3)(d)(iii)** | Where blade debris is released forward, rearward or otherwise outside the containment structure with an energy and trajectory that could cause an unsafe condition, consider it uncontained high-energy debris causing a Hazardous Engine Effect, and assess the overall probability of occurrence of the unsafe condition. | Accepted method |
| **(3)(d)(iii)** | The integrity specifications of CS-E 515 provide some reliability benefits when applied to a blade, particularly when it forms a part of a blisk, also named integrally bladed rotor. | Statement |
| **(3)(d)(iii)** | However, those specifications do not provide a valid basis to demonstrate an Extremely Remote blade Failure probability. Blade reliability is affected by many factors; CS-E 515 addresses some, such as low- and high-cycle fatigue, manufacturing quality and service management, and not others, such as foreign object damage. | Statement |
| **(3)(d)(iii)** | Use engineering judgement based on available test and service experience of comparable designs as the basis for a conservative estimate of blade reliability. | Accepted method |
| **(3)(d)(iii)** | Determine the likelihood of a blade failure resulting in an unsafe condition primarily from debris energy and trajectories observed in testing and in service, with an assessment of the trajectories that could impact the aircraft. | Accepted method |
| **(3)(d)(iii)** | Where possible, assess the threat to aircraft safety in coordination with the aircraft manufacturer. In any case, include assumptions regarding the ability of the aircraft to withstand debris impact in the Manuals required by CS-E 20(d). | Accepted method |
| **(3)(d)(iii)** | Consider that other components may be released following Failure; service experience has shown that rupture of the high-pressure casings can generate high-energy debris. Assess the probability that an unsafe condition results from such a Failure. | Accepted method |
| **(3)(d)(iii)** | An Extremely Remote probability must be demonstrated for compliance with CS-E 510(a)(3). | Required |
| **(3)(d)(iv)** | CS-E 510(g)(2)(ii) concerns generation and delivery of toxic products caused by abnormal engine operation sufficient to incapacitate crew or passengers during the flight. | Statement |
| **(3)(d)(iv)** | Make no assumptions of cabin air dilution or mixing in the engine-level analysis; these can only be properly evaluated during aircraft certification. | Accepted method |
| **(3)(d)(iv)** | The intent of CS-E 510(g)(2)(ii) is to address the relative concentration of toxic products in the engine bleed air delivery. The Hazardous Engine Effect of toxic products relates to significant concentrations, with "significant" defined as concentrations sufficient to incapacitate persons exposed to those concentrations. | Statement |
| **(3)(d)(iv)** | Provide information on delivery rates and concentrations of toxic products in the engine bleed air for the cabin to the installer as part of the engine instructions for installation. | Accepted method |
| **(3)(d)(vi)** | Interpret an uncontrolled fire as an extensive or persistent nacelle fire not effectively confined to a designated fire zone, or which cannot be extinguished using the aircraft means identified in the assumptions. | Accepted method |
| **(3)(d)(vi)** | Provision for flammable fluid drainage, fire containment, fire detection and fire extinguishing may be taken into account when assessing the severity of the effects of a fire. | Permitted |
| **(3)(d)(vii)** | Complete inability to shut down the engine is a Hazardous Engine Effect because continued running, even at low thrust or power, represents a hazard — inhibiting safe evacuation, causing directional control problems during landing, or preventing safe shutdown following a Failure. | Statement |
| **(3)(d)(vii)** | It is acceptable to take account of aircraft-supplied equipment, such as fuel cut-off means, to protect against the complete inability to shut down the engine. | Permitted |
| **(3)(d)(vii)** | The inclusion of this item within the Hazardous Engine Effects should not preclude hardware or software intended to protect against inadvertent engine shutdown, including aircraft logic to mitigate against the inadvertent shutdown of all engines. | Statement |

Three scenarios are given for toxic products: "Rapid flow of toxic products
impossible to stop prior to incapacitation", "No effective means to prevent flow
of toxic products to crew or passenger compartments", and "Toxic products
impossible to detect prior to incapacitation" [AMC E 510(3)(d)(iv)]. The named
sources are degradation of abradable materials in the compressor when rubbed by
rotating blades, and degradation of oil leaking into the compressor air flow —
both linked to the abradable lining assessment of [[AMC E 130|AMC E 130(3)(d)]].

The debris treatment separates three populations with different rules. **Major
rotating parts** are assumed uncontained unless containment is demonstrated, and
their Extremely Remote objective is met only through [[CS-E 515]], supplemented
by [[CS-E 840]] and [[CS-E 850]]. **Blades** must be radially contained under
[[CS-E 520|CS-E 520(c)(1)]], but forward or rearward release still needs a
probability assessment, and CS-E 515 explicitly does not support an Extremely
Remote blade failure claim because it does not address foreign object damage.
**Other components**, such as high-pressure casings, need their own assessment.

### AMC E 510(3)(e) to (f) — Major and Minor Engine Effects

| Ref | Obligation | Strength |
|---|---|---|
| **(3)(e)** | Compliance with CS-E 510(a)(4) can be shown if the individual Failures or combinations of Failures resulting in Major Engine Effects have probabilities not greater than 10⁻⁵ per Engine flight hour. | Accepted method |
| **(3)(e)** | No summation of probabilities of Failure modes resulting in the same Major Engine Effect is required. | Relief |
| **(3)(e)** | Major Engine Effects are likely to significantly increase crew workload, or reduce the safety margins. Not all the listed effects may be applicable to all engines or installations, and the list is not intended to be exhaustive. | Statement |
| **(3)(e)** | Typically the following may be considered Major Engine Effects: controlled fires; case burn-through where no propagation to Hazardous Engine Effects is shown; release of low-energy parts where no such propagation is shown; vibration levels causing crew discomfort; concentration of toxic products in the engine bleed air for the cabin sufficient to degrade crew performance; thrust in the opposite direction to that commanded by the pilot below the hazardous level; loss of integrity of the load path of the engine supporting system without actual engine separation; generation of thrust greater than maximum rated thrust; significant uncontrollable thrust oscillation. | Statement |
| **(3)(e)** | The concentration of toxic products in the engine bleed air may be interpreted as generation and delivery of toxic products, as a result of abnormal engine operation, that would incapacitate the crew or passengers, except that the products are slow-enough acting and/or readily detectable so as to be stopped by crew action prior to incapacitation. | Permitted |
| **(3)(e)** | Consider possible reductions in crew capabilities due to their exposure while acting in identifying and stopping the products, if appropriate. | Accepted method |
| **(3)(e)** | Provide information on delivery rates and concentrations of toxic products in the engine bleed air for the cabin to the installer as part of the engine instructions for installation. | Accepted method |
| **(3)(f)** | It is generally recognised that engine Failures involving complete loss of power from the affected engine can be expected to occur in service, and that the aircraft should be capable of controlled flight following such an event. | Statement |
| **(3)(f)** | Engine Failure with no external effect other than loss of power and services may be regarded as a Failure with a minor effect, for the purpose of the engine safety analysis and engine certification. | Permitted |
| **(3)(f)** | That assumption may be revisited during aircraft certification, where installation effects such as engine redundancy may be fully taken into consideration. | Permitted |
| **(3)(f)** | The Failure to achieve any given power rating for which the engine is certificated should be covered in the safety analysis, and may be regarded as a minor engine effect. | Accepted method |
| **(3)(f)** | Similarly, that assumption may be revisited during aircraft certification, particularly multi-engine rotorcraft certification. | Permitted |
| **(3)(f)** | The re-examination applies only to aircraft certification and is not intended to impact engine certification. | Statement |

### AMC E 510(3)(g) to (h) — determining effects, and reliance on maintenance

| Ref | Obligation | Strength |
|---|---|---|
| **(3)(g)** | Where prediction of the likely progression of an engine Failure relies extensively on engineering judgement and cannot be proved absolutely, and there is question over its validity to the extent that the conclusions could be invalid, additional substantiation may be required. | Statement |
| **(3)(g)** | Additional substantiation may consist of engine test, rig test, component test, material test, engineering analysis, previous relevant service experience, or a combination. | Permitted |
| **(3)(g)** | If significant doubt exists over the validity of that substantiation, additional testing or other validation may be required under CS-E 510(b). | Statement |
| **(3)(h)** | For CS-E 510(e)(1), general statements in the analysis summary referring to regular maintenance in a shop and on the line are acceptable. Where specific Failure rates rely on special or unique maintenance checks, state those explicitly in the analysis. | Accepted method |
| **(3)(h)** | The engine maintenance manual, overhaul manual or other relevant manuals may serve as the appropriate substantiation for the maintenance error element of CS-E 510(e)(1). | Permitted |
| **(3)(h)** | A listing of all possible incorrect maintenance actions is not required. | Relief |
| **(3)(h)** | Take precautions in the engine design to minimise the likelihood of maintenance errors, and give consideration to mitigating their effects in the engine design, since completely eliminating sources of maintenance error during design is not possible. | Accepted method |
| **(3)(h)** | If appropriate, give consideration to communicating strategies against performing contemporaneous maintenance of multiple engines. | Accepted method |
| **(3)(h)** | Design components undergoing frequent maintenance to facilitate the maintenance and correct re-assembly. | Accepted method |
| **(3)(h)** | For CS-E 510(e)(2), wherever specific Failure rates rely on special or unique maintenance checks for protective devices, state those explicitly in the analysis. | Accepted method |

The maintenance error list is drawn from service events: failure to restore oil
system or borescope access integrity after routine maintenance, with similar
consideration for other systems; mis-installation of or failure to refit O-rings;
servicing with incorrect fluids; and failure to install, omitting to torque,
under-torquing or over-torquing nuts [AMC E 510(3)(h)]. Improper maintenance on
discs, hubs and spacers is called out separately, with overlooking existing
cracks or damage during inspection, and failure to apply or incorrect application
of protective coatings, as service examples.

The multi-engine concern in (3)(h) is that similar incorrect actions performed on
several engines during the same maintenance availability by one crew defeat
redundancy. The AMC calls this primarily an aircraft-level concern and says precautions
should be taken in the engine design to minimise the likelihood of such
maintenance errors.

### AMC E 510(4) to (6) — techniques, documents, definitions

| Ref | Obligation | Strength |
|---|---|---|
| **(4)** | Other comparable techniques exist and may be proposed by an applicant; variations or combinations of these techniques are also acceptable. | Permitted |
| **(4)** | For derivative engines, it is acceptable to limit the scope of the analysis to modified components or operating conditions and their effects on the rest of the engine. | Permitted |
| **(4)** | Reach early agreement between the applicant and the Agency on the scope and methods of assessment to be used. | Accepted method |
| **(4)** | Failure Modes and Effects Analysis is a structured, inductive, bottom-up analysis evaluating the effects on the engine of each possible element or component Failure; properly formatted, it aids in identifying latent Failures and the possible causes of each Failure mode. | Statement |
| **(4)** | Fault Tree and Dependence Diagram analyses are structured, deductive, top-down analyses identifying the conditions, Failures and events that would cause each defined Failure condition. A Fault Tree Analysis is Failure oriented; a Dependence Diagram Analysis is success-oriented. | Statement |
| **(6)** | Dormant Failure: a Failure the effect of which is not detected for a given period of time. | Statement |
| **(6)** | Failure condition: a condition with direct, consequential engine-level effect, caused or contributed to by one or more Failures. Examples include limitation of thrust to idle or oil exhaustion. | Statement |
| **(6)** | Failure mode: the cause of the Failure or the manner in which an item or function can fail. Examples include Failures due to corrosion or fatigue, or Failure in jammed open position. | Statement |
| **(6)** | Toxic products: products that act as or have the effect of a poison when humans are exposed to them. | Statement |

The definitions in (6) carry a restriction that is easy to overlook: they "should
not be assumed to apply to the same or similar terms used in other
specifications or AMCs" [AMC E 510(6)]. They are local to CS-E 510.

## Compliance

- Safety analysis using an accepted methodology — FMEA, Fault Tree, Dependence Diagram, Markov, or a justified alternative — with the scope and method agreed with the Agency early [AMC E 510(1)], [AMC E 510(4)].
- Statement of assumed aircraft devices and procedures for the typical installation, with assumed Failure rates for aircraft components where the applicant cannot determine them [AMC E 510(3)(c)].
- List in the instructions for installation of aircraft-component Failures contributing to Hazardous or Major Engine Effects, their propagation mode and assumed rates [AMC E 510(3)(c)], against [[CS-E 30]] and [[CS-E 20|CS-E 20(d)]].
- Engine Control System safety analysis integrated into the overall engine analysis [AMC E 510(3)(b)], against [[CS-E 50|CS-E 50(d)]].
- Summation of Failure modes per Hazardous Engine Effect against 10⁻⁷ per engine flight hour, with dormant periods included, excluding Engine Critical Parts, and omitting summation where each individual Failure is below 10⁻⁸ [AMC E 510(3)(d)(i)].
- Containment demonstration for major rotating parts, or the assumption of non-containment with the [[CS-E 515]], [[CS-E 840]] and [[CS-E 850]] route [AMC E 510(3)(d)(iii)].
- Radial containment demonstration for compressor and turbine blade shedding, singly and in likely combinations [AMC E 510(3)(d)(iii)], against [[CS-E 520|CS-E 520(c)(1)]] and [[CS-E 810]].
- Blade reliability estimate from test and service experience of comparable designs, with debris energy and trajectory assessment and, where possible, coordination with the aircraft manufacturer [AMC E 510(3)(d)(iii)].
- Debris impact assumptions recorded in the Manuals required by [[CS-E 20|CS-E 20(d)]] [AMC E 510(3)(d)(iii)].
- Assessment of other high-energy debris sources, including high-pressure casing rupture [AMC E 510(3)(d)(iii)].
- Toxic product delivery rates and concentrations in the engine bleed air, provided to the installer, with no cabin dilution or mixing assumed [AMC E 510(3)(d)(iv)], [AMC E 510(3)(e)].
- Uncontrolled fire assessment against the nacelle fire zone and the assumed aircraft extinguishing means [AMC E 510(3)(d)(vi)], against [[CS-E 130]].
- Engine shutdown assessment, which may take account of aircraft-supplied fuel cut-off means [AMC E 510(3)(d)(vii)].
- Major Engine Effect probabilities against 10⁻⁵ per engine flight hour, without summation [AMC E 510(3)(e)].
- Maintenance reliance statements, with special or unique checks stated explicitly, and the maintenance manuals as substantiation for the maintenance error element [AMC E 510(3)(h)], feeding the airworthiness limitations of [[CS-E 25]].
- Design precautions minimising and mitigating maintenance error, and design for correct re-assembly of frequently maintained components [AMC E 510(3)(h)].

## Application to this engine

The AMC applies throughout, less the passages recorded below.

**Rotorcraft is named explicitly, and so is engine redundancy.**
AMC E 510(3)(f) carries two minor-effect assumptions and gives each
its own qualifier, which are not interchangeable. The assumption that an engine
Failure with no external effect beyond loss of power is a Minor Engine Effect
"may be revisited during aircraft certification, where installation effects such
as Engine redundancy may be fully taken into consideration". The separate
assumption, that failing to achieve a certificated rating is a minor engine
effect, may be revisited "particularly multi-Engine rotorcraft certification".

Both bear on this engine, and the first bears harder: a multi-engine rotorcraft
is precisely an installation whose redundancy the aircraft applicant will take
into account. Engine certification is unaffected either way — the AMC says the
re-examination "applies only to aircraft certification" — but both assumptions
are provisional at aircraft level. This is the same boundary the OEI ratings
exist to manage, and it links to [[AMC E 20|AMC E 20(f)]], where the safety
analysis must consider dormant Failures leading to non-availability of the OEI
ratings.

**Power, not thrust.** Several passages are written in thrust terms — "Generation
of thrust greater than maximum rated thrust" and "Significant uncontrollable
thrust oscillation" in the Major Engine Effects list [AMC E 510(3)(e)], and
"limitation of thrust to idle" as a Failure condition example
[AMC E 510(6)]. For a turboshaft these read as power, and the equivalent effects
are excess power above the maximum rated value and uncontrollable power
oscillation. The list is explicitly non-exhaustive and not all items apply to all
engines, so this is interpretation rather than omission.

**The control system.** AMC E 510(3)(b) says the CS-E 50 specifications for the
Engine Control System should be integrated into the overall engine safety
analysis rather than analysed separately. For a full-authority
EECS this is the central structural requirement of the analysis, and it is the
analysis that [[AMC E 60|AMC E 60(d)(3)]] draws on for the development assurance
level of the OEI recording and retrieval system.

**Bleed air and toxic products.** The named sources — abradable material
degradation from blade rubs, and oil leaking into the compressor air flow — apply
to any turbine engine supplying bleed air. This connects to [[CS-E 690]] and to
the abradable lining evaluation of [[AMC E 130|AMC E 130(3)(d)]].

[VERIFY: AMC1 21.A.3B(b) defines the unsafe condition that the debris criterion
turns on, and is not held in `source/`. The distinction between debris that does
and does not cause an unsafe condition cannot be resolved here.]

[VERIFY: the reference documents in AMC E 510(5) are not held in `source/`:
AMC 25.1309 of CS-25; "Systematic Safety" by E Lloyd and W Tye, Taylor Young
Limited; SAE/EUROCAE ARP4754A / ED-79A; SAE ARP 926A; SAE ARP 4761; and Carter,
A.D.S., Mechanical Reliability, 2nd edition, Macmillan, 1986. They are named as
sources of detailed descriptions of analytical techniques, not as obligations.]

## Not applicable

- **(3)(d)(v)** — the elaboration of significant thrust in the opposite direction to that commanded by the pilot, and all three of the examples it gives. Each names thrust reverser or propeller equipment this engine does not have, and the source qualifies the list with "if applicable to CS-E certification". The parent definition at [[CS-E 510|CS-E 510(g)(2)(iii)]] therefore has no accepted-means elaboration that reaches a turboshaft.
- Throughout — where the source pairs thrust with power, in any of the forms it uses, only the power term is carried. This engine produces shaft power; the thrust half of each pair has no turboshaft case.

## References

Specification: [[CS-E 510]]
Related: [[CS-E 515]] · [[CS-E 50]] · [[CS-E 30]] · [[CS-E 20]] · [[CS-E 25]] · [[CS-E 130]] · [[CS-E 520]] · [[CS-E 690]] · [[CS-E 810]] · [[CS-E 840]] · [[CS-E 850]] · [[AMC E 20]] · [[AMC E 60]] · [[AMC E 130]]

## Amendment history

Amended at Amendment 7. The change rewrote the non-containment of high-energy
debris passage at (3)(d)(iii), and it is a substantive change, not an editorial
one.

- **Before:** "The Engine has a containment structure which is designed to withstand the consequences of the release of a single blade (see CS-E 810(a)), and which is often adequate to contain additional released blades and static parts. The Engine containment structure is not expected to contain major rotating parts should they fracture. Discs, hubs, impellers, large rotating seals, and other similar large rotating components should therefore always be considered to represent potential high-energy debris."
- **After:** "Due to the extremely high energies involved, the Engine containment structures are not required to contain major rotating parts should they fail. Unless containment has been demonstrated, the Failure of discs, hubs, impellers, large rotating seals, and other similar large rotating components should therefore be assumed to result in uncontained high-energy debris, causing a Hazardous Engine Effect."

Three things changed in obligation, not only in wording. The old text said the
containment structure "is not expected to contain" major rotating parts; the new
text says containment "are not required to contain" them, and adds the escape
"Unless containment has been demonstrated". So demonstrated containment is now an
available route where previously the assumption was absolute. Second, the old
text classified such parts as "potential high-energy debris"; the new text names
the consequence directly as "uncontained high-energy debris, causing a Hazardous
Engine Effect". Third, the amendment added the compliance route that was
previously absent: the Extremely Remote objective for such parts "can only be
ensured through compliance with CS-E 515, supplemented by CS-E 840 and
CS-E 850".

Amendment 7 also added the whole **Blades** passage — radial containment, the
forward and rearward release case, the statement that [[CS-E 515]] does not
support an Extremely Remote blade failure claim, and the debris energy and
trajectory method — and the general principle sentence referring to
AMC1 21.A.3B(b). The casing material was rewritten into the **Other Sources of
Uncontained High-Energy Debris** heading, with the requirement that an Extremely
Remote probability be demonstrated.

The net effect is more work, not less: blade debris outside the containment
structure now requires an explicit probability assessment that the previous text
did not call for.

The paragraph carries `[Amdt. No.: E/1]`, `[Amdt. No.: E/4]` and
`[Amdt. No.: E/7]`.
