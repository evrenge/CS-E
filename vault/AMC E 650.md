---
id: "AMC E 650"
type: AMC
subpart: E
pages: 120-130
changed_in: [Amdt7, Amdt8]
tags: [vibration, survey, flutter, baseline-test, validated-analysis, dwell, corrected-speed, hcf]
---
# AMC E 650 — Vibration Surveys

> [!summary]
> The longest AMC in Subpart E. It defines the vocabulary the specification uses,
> then works through component selection, test conditions, environmental effects,
> Fault conditions, inlet distortion, flutter, material and frequency variation,
> dwell testing, transient response, installation compatibility and the
> baseline-test plus validated-analysis route. Two provisions permit the required
> test speeds to be reduced with Agency agreement, and one makes the test-analysis
> equivalence explicit: a baseline test plus validated analysis is equivalent to a
> new test.

## Requirement

### AMC E 650(1) — definitions

The definitions are embedded as images. They are laid out as a table, and the
corrected speed formula carries an empirical exponent that the text layer loses,
so a transcription would be an unverifiable restatement under accuracy rule 6.

![[AMC_E_650_p120.png]]
![[AMC_E_650_p121.png]]

The definitions matter beyond vocabulary. **Module** is defined so that a subset
of stages isolated from a multi-stage compressor or turbine does not qualify,
which fixes what "each rotor module" in [[CS-E 650|CS-E 650(b)]] means.
**Significant Response** is defined against a level previously agreed with the
Agency as giving acceptable margin under [[CS-E 70]] and [[CS-E 100]], so it is
an agreed threshold rather than an absolute one. **Declared Flight Envelope**
expressly includes start-up, shutdown and windmilling rotation in flight.

### AMC E 650(2) to (4) — intent, component selection, test conditions

| Ref | Obligation | Strength |
|---|---|---|
| **(2)** | The intent of the rule is to ensure the acceptable dynamic behaviour of all components and assemblies in a gas turbine engine, and more specifically the avoidance of damaging high cycle fatigue failures. | Statement |
| **(3)** | Base component selection for the survey on an appropriate combination of experience, analysis and component test. | Accepted method |
| **(3)** | The selected components would normally include the most critical blades and vanes from a vibration point of view in each compressor and turbine module; all blade rows adjacent to variable incidence vanes; all compressor and turbine discs and spacers; all main rotor shaft systems, and gears when included in such systems; and any other component specifically identified as requiring engine test to substantiate analysis or supplement component tests. | Accepted method |
| **(4)** | A test or series of tests is an essential element of the survey, whether the tests are new or baseline. | Statement |
| **(4)(a)** | Normally, a full engine test is the preferred means to complete the survey. | Accepted method |
| **(4)(a)** | An applicant may elect to use rig tests to overcome limitations of a full engine test, such as the amount of instrumentation that can be fitted or the range of inlet conditions that can be tested. | Permitted |
| **(4)(a)** | Where rig tests are employed, demonstrate that all pertinent interface conditions and physical hardware closely replicate actual engine conditions. | Accepted method |
| **(4)(b)** | Make it the goal of the test programme to cover at least the ranges of conditions required under CS-E 650(b) and (c). | Accepted method |
| **(4)(b)** | Where it proves physically impracticable to achieve the extended test conditions of CS-E 650(b)(1), the Agency may accept an alternative that complies with the intent. | Permitted |
| **(4)(b)** | Where it can be demonstrated that the characteristics of the Engine Control System are such that the maximum rated speed cannot be exceeded in fault-free operation, the required maximum tested speed may, with the agreement of the Agency, be adjusted downward, but may not be less than 100 %. | Permitted |
| **(4)(b)** | Where tested components are deliberately selected to cover an adverse range of manufacturing variability, or any other effect normally captured by the further 2 % of CS-E 650(c), the required maximum tested speed may, with Agency agreement, be adjusted downward, but not below the maximum speed established for CS-E 650(b). | Permitted |
| **(4)(b)** | Justify any reduction in the speed range requirements and have it agreed by the Agency; normally any test shortfall would be expected to be covered by validated analysis. | Accepted method |
| **(4)(c)** | Use suitable instrumentation, data acquisition and analyser systems, which may include dynamic strain gauges, accelerometers, dynamic pressure gauges and time-of-arrival sensors. | Accepted method |
| **(4)(c)** | Maintain strain gauge accuracy throughout the test conditions, particularly under repeated exposure to high temperatures for extended periods, and take measurements at locations sensitive to the peak responses of interest but tolerant of a degree of mislocation or alignment variability. | Accepted method |
| **(4)(c)** | Where such locations are not suitable or accessible, stresses may be measured nearby, provided the relationships between those stresses and the stresses at critical locations are known and predictable. | Permitted |
| **(4)(c)** | Where time-of-arrival sensors are used, calibrate them properly, understand their capabilities, and show the displacement-to-stress conversion to be sufficiently accurate or at least conservative. | Accepted method |
| **(4)(c)** | Do not use time-of-arrival data for vibratory modes where measured displacements have low sensitivity in relation to stresses in critical areas, in order to avoid excessive uncertainty in endurance limit calculations. | Accepted method |
| **(4)(d)** | Where instrumentation can survive only for short periods, complete the substantiation by validated analysis, keep instrumentation loss minimal, and base the associated analysis primarily on the surviving instrumentation data. | Accepted method |
| **(4)(e)** | Where the engine is modified or adjusted during testing to achieve the desired speeds or other test conditions, evaluate the alterations to show their effects are not detrimental and do not compromise the intent of the test and the test results. | Accepted method |

The two speed reliefs in (4)(b) rest on different arguments and have different
floors. The first is a control system argument against the 3 % transient
overshoot margin, and it floors at 100 %. The second is a hardware selection
argument against the further 2 % for engine-to-engine variability, and it floors
at the [[CS-E 650|CS-E 650(b)]] speed. Neither is available without Agency
agreement.

### AMC E 650(5) to (7) — environment, Fault conditions, inlet distortion

| Ref | Obligation | Strength |
|---|---|---|
| **(5)** | Include in the evaluated conditions icing and rain and hail conditions under which sustained engine operation is expected to occur and which may lead to high rotor imbalance, severe rotor-case interaction, higher vibratory amplitudes, or flutter. | Accepted method |
| **(5)** | The applicant may take into account the tests performed to show compliance with CS-E 780 and CS-E 790 to characterise the engine vibration behaviour. | Permitted |
| **(5)** | Provide appropriate justification that the worst operating conditions in the declared flight envelope have been fully explored. | Accepted method |
| **(5)** | Engine tests may be conducted by flight test, in altitude facilities, or in other facilities such that the effects of altitude and temperature are properly represented and can be evaluated. | Permitted |
| **(5)** | The dependency of certain vibratory phenomena on temperature and altitude can be characterised as a dependency on corrected speed, which enables investigation by sea-level testing, provided the entire required corrected speed range can be achieved. | Statement |
| **(6)** | Evaluate any change in vibration response caused by a Fault condition and show it does not result in a Hazardous Engine Effect. | Accepted method |
| **(6)** | CS-E 650(g) applies to those Fault conditions that would cause abnormal vibrations difficult to identify in a timely manner so that appropriate mitigating action can be taken. | Statement |
| **(6)** | The applicant may use prior experience with Faults that occurred on other similar engines, where after exposure the engine was able either to continue in safe operation or to be shut down without creating a Hazardous Engine Effect. | Permitted |
| **(6)** | Applicants may also use field experience or other means to show that certain Fault conditions are Extremely Remote because of specific engine configurations, design features or operating conditions. | Permitted |
| **(6)** | CS-E 650(g) applies to the same components considered under CS-E 650(a). Where the effects of these Fault conditions extend to the rest of the engine, they must be addressed under CS-E 100 or CS-E 520. | Statement |
| **(7)** | Take into account conditions consistent with the most adverse inlet airflow distortion pattern declared by the applicant, which may be associated with the air intake, crosswinds, or other operating and aircraft installation conditions. | Accepted method |
| **(7)** | Where an engine test is performed, the inlet distortion may be achieved by various means, such as external crosswind devices, inlet distortion plates or suppression screens. | Permitted |

Paragraph (6) explains why (g) exists as a separate sub-point. The concern is
Faults whose vibration signature is **not recognised in time**, so that the
engine keeps running and the Fault escalates. The worked example is the loss of
an airfoil tip: the resulting out-of-balance may be indicated by the means of
[[CS-E 60]] and [[CS-E 510]] and still not be recognised as abnormal. Other named
Faults are incorrectly scheduled compressor variables, stator vane blockages or
enlargement, and blockages of fuel nozzles.

### AMC E 650(8) — flutter

| Ref | Obligation | Strength |
|---|---|---|
| **(8)** | Testing to demonstrate satisfactory vibratory clearance from flutter boundaries may be accomplished by rig or engine, sea-level or altitude test. | Permitted |
| **(8)(a)** | The presence of flutter may be acceptable in some circumstances, for example in a speed range encountered only briefly or infrequently, or where the flutter amplitude is limited to a safe level. | Permitted |
| **(8)(a)** | The resulting vibration stresses must always satisfy the requirements of CS-E 650(f). | Required |
| **(8)(a)** | Complete a thorough investigation of the flutter response and its effects to show that the flutter does not result in a Hazardous Engine Effect; the investigation may include dwell testing under paragraph (10). | Accepted method |
| **(8)(b)** | Recognise in the test procedure that some systems' susceptibilities to flutter will not be revealed if the relevant operating conditions are not sustained long enough for the flutter to develop. | Accepted method |
| **(8)(c)** | Give due consideration to possible variations between nominal and extreme values of, for example, tip clearances, mechanical damping, operating lines and bleed flows, since flutter is sensitive to small variations. | Accepted method |
| **(8)(c)** | Experience has shown there are differences in susceptibility to flutter from one blade set to another, and that 'tuned' blade sets might be more sensitive. | Statement |
| **(8)(d)** | Where tests will be conducted at sea level only, propose a procedure acceptable to the Agency to account for altitude effects. | Accepted method |
| **(8)(d)** | For certain engine modules, especially compressors, this is expected to be achieved by testing throughout the range of corrected speed the module will encounter in service, in which case the CS-E 650(b) and (c) speed requirements should be considered to apply also to corrected speed. | Accepted method |
| **(8)(e)** | For some turbines the propensity to flutter is not increased at maximum corrected speed, and other methods of demonstrating the absence of damaging flutter throughout the declared flight envelope may be more appropriate. | Permitted |
| **(8)(e)** | Ensure that the maximum stage inlet pressure at each physical speed is achieved, or that compensation is provided. | Accepted method |
| **(8)(f)** | Include in the methods used to verify the absence of damaging flutter consideration of applicable combinations of: the ranges of physical and corrected rotational speeds for each rotor module; the simultaneous occurrence of maximum compressor inlet air total temperature and maximum corrected rotational speed; the range of compressor operating lines within the flight envelope; the most adverse of other compressor inlet air conditions within the flight envelope; and the hardware standard, the intake conditions and margins to account for engine deterioration. | Accepted method |

Paragraph (8)(e) explains a result that is counter-intuitive and directly useful:
where a turbine operates aerodynamically choked and the mass flow is set by the
fixed blading geometry, corrected speed is essentially constant, and a lower
corrected speed **increases** blading Mach number. Running up to 100 % of maximum
mechanical speed then covers the worst forcing case.

### AMC E 650(9) to (12) — material variation, dwell, transients, instrumentation

| Ref | Obligation | Strength |
|---|---|---|
| **(9)(a)** | Take into account the influence on the endurance limit of manufacturing processes, local geometrical features and temperatures. The material property important to CS-E 650(f) is the endurance limit associated with specific combinations of mean stress and alternating stress, usually represented on a Goodman diagram. | Accepted method |
| **(9)(b)** | The stress margin is the difference between the material allowable at a particular location and the measured vibratory stress at that location. Account in the suitability criteria for variability in design, in operation including the effects due to icing, rain and hail conditions consistent with the corresponding certification test evidence, and for other mitigating factors identified during the certification test. | Accepted method |
| **(9)(c)** | The total vibratory stress at a given location is the sum of the resonant stresses of all active and concurrent normal modes, plus any other vibratory stresses at that rotational speed. Consider the stress amplitudes that occur within permitted blade-to-blade variations of natural frequency. | Accepted method |
| **(9)(c)** | Where more than one mode may be excited at the same time or speed, calculate the combined stress by breaking down the vibratory stress of each mode into its stress components and combining the modal contributions in proportion to the individual measured responses. | Accepted method |
| **(10)** | Determine all significant responses within the operating conditions prescribed in CS-E 650 and allow sufficient time for any associated resonant modes to respond, usually during slow acceleration and deceleration speed sweeps covering the range of required speeds. | Accepted method |
| **(10)** | Where a significant response is found, subject the relevant components to sufficient cycles of vibration close to or on the response peak to demonstrate compliance with CS-E 650(f). | Accepted method |
| **(10)** | This dwell testing would normally be incorporated into the incremental periods of the CS-E 740 Endurance Test as required by CS-E 740(g)(1), and components subjected to it should subsequently also meet the strip inspection requirements of CS-E 740(i). | Accepted method |
| **(11)** | Give consideration also to the speed range from zero to minimum rotational speed, especially in the case of supercritical shafts. Some predicted potentially damaging transient responses may require an aggressive control input to provoke a representative response. | Accepted method |
| **(12)** | Where the dimensions of the components to be tested are incompatible with the necessary instrumentation, instrumented engine tests and the variation of the Endurance Test incremental running prescribed in CS-E 740(g)(1) may be waived wholly or in part, if the Agency is satisfied that the total hours of operation accumulated on test beds or in flight under representative conditions prior to certification are sufficient to demonstrate that the vibration stress levels are acceptable. | Relief |

The blade-to-blade variation in (9)(c) is given a worked figure: "if for a
particular blade design the natural frequency (fn) range is fn ± 2.5 %, then the
combined amplitudes within this range should be considered"
[AMC E 650(9)(c)]. The figure is an example, not a specification.

### AMC E 650(13) to (15) — installation, modelling, inspection

| Ref | Obligation | Strength |
|---|---|---|
| **(13)** | The intent of CS-E 650(h) is to ensure vibratory compatibility between the engine and each intended installation configuration when the engine is installed and operated in accordance with the manufacturer's approved instructions. | Statement |
| **(13)** | Provide sufficient information in the engine instructions for installation to enable the aircraft manufacturers to establish that the installation does not unacceptably affect the engine's vibration characteristics. | Accepted method |
| **(13)** | Give consideration to the need to declare operating limitations and procedures, and consider at least: installation influences on inlet and exhaust conditions; stiffness and damping of the mount system; and rotor drive systems. | Accepted method |
| **(14)** | Acceptable analytical methods are based on the complementary concepts of a baseline test and validated analysis. The general principle is that a baseline test in conjunction with validated analysis is equivalent to a new test. | Statement |
| **(14)(a)** | A baseline test is usually an engine or rig test run on the first model of an engine type during type certification; an engine or rig test run on a previously certified engine type; or an engine or rig test specifically run to support the creation of the validated analysis. | Statement |
| **(14)(a)** | Show the design characteristics and operating conditions run in the baseline tests to be sufficiently similar to, and inclusive of, the domain of applicability for the engine being certified. | Accepted method |
| **(14)(a)** | A test from which the results are used to calibrate an analysis is not in general eligible to be considered a baseline test in relation to the validation of that analysis. The same test results cannot be used both to calibrate and validate an analysis. | Statement |
| **(14)(b)(i)** | Validate the analytical model against one or more baseline tests, showing for each that the analysis consistently predicts the observed behaviour and vibratory responses to an acceptable precision and accuracy, or alternatively that predictions reliably overpredict the vibratory response. | Accepted method |
| **(14)(b)(i)** | Clearly define the domain of applicability of the analysis, comprising the ranges of design characteristics and operating conditions for which it will be deemed validated, and have the analysis and its domain accepted by the Agency. | Accepted method |
| **(14)(b)(ii)** | Justify the similarity of the engine, module or components to be certified with previously tested and certified designs, and show that the design characteristics and operating conditions fall within the established domain of applicability. | Accepted method |
| **(14)(b)(ii)** | The demonstration of compliance will be considered to be the combination of the baseline tests used to create the validated analysis and the analysis performed on the engine for which approval is sought. | Statement |
| **(14)(b)(iii)** | Where the validated analysis is updated, for instance following new testing or service experience, have the updated analysis or its domain of applicability reviewed and accepted by the Agency. | Accepted method |
| **(15)** | Pre-certification development activities generating engineering data essential to supporting the certification test should be exempt from formal Agency approval of test plans and reports. | Accepted method |
| **(15)** | Limit inspection of type design hardware in accordance with point 21.A.33 of Part 21 to only those pertinent engine components and associated instrumentation that constitute the certification engine test or the baseline tests supporting the validated analysis. | Accepted method |

The domain of applicability in (14)(b)(i) is defined by a long list of design
characteristics: engine architecture, module type, component geometry, structural
dynamic characteristics, aeroelastic characteristics, sources of vibratory
excitation and forcing strength, and operating conditions. Among the structural
dynamic characteristics the AMC names the Modal Assurance Criterion, noting that
"a MAC value greater than 0.9 indicates there is close agreement between measured
and calculated mode shapes" [AMC E 650(14)(b)(i)]. Among the aeroelastic
characteristics it gives the Strouhal number or reduced frequency,
$k = \omega c / U$, where $\omega$ is frequency, $c$ is component length in the
flow direction and $U$ is flow velocity.

The bar in (14)(a) against using one test to both calibrate and validate an
analysis is the load-bearing sentence of the whole paragraph. Without it, the
equivalence between a baseline test plus analysis and a new test does not hold.

## Compliance

- Component selection list, with the basis in experience, analysis and component test [AMC E 650(3)].
- Vibration survey test plan: rig or full engine, with interface replication evidence where rig testing is used [AMC E 650(4)(a)].
- Speed coverage statement against [[CS-E 650|CS-E 650(b)]] and (c), with any agreed reduction justified and the shortfall covered by validated analysis [AMC E 650(4)(b)].
- Instrumentation plan covering gauge type, location, accuracy retention and, where used, time-of-arrival calibration and the displacement-to-stress conversion [AMC E 650(4)(c)].
- Evaluation of engine modifications made to reach test conditions [AMC E 650(4)(e)].
- Environmental coverage including icing and rain and hail, drawing on the [[CS-E 780]] and [[CS-E 790]] test evidence [AMC E 650(5)].
- Fault condition vibration evaluation, with prior or field experience where used, and Extremely Remote arguments where claimed [AMC E 650(6)].
- Inlet distortion representation and the declared adverse pattern [AMC E 650(7)].
- Flutter clearance evidence, including the sustained-condition consideration, the variation sensitivities, and the sea-level-to-altitude procedure agreed with the Agency [AMC E 650(8)].
- Goodman-type endurance limit data with manufacturing, geometry and temperature influences, and the stress margin criteria [AMC E 650(9)].
- Modal combination method and the blade-to-blade natural frequency range considered [AMC E 650(9)(c)].
- Dwell testing on each significant response, within the [[CS-E 740|CS-E 740(g)(1)]] incremental periods, with the [[CS-E 740|CS-E 740(i)]] strip inspection [AMC E 650(10)].
- Transient response consideration from zero to minimum rotational speed [AMC E 650(11)].
- Where the instrumentation waiver of (12) is claimed, the accumulated representative test bed or flight hours supporting it [AMC E 650(12)].
- Installation compatibility information in the instructions for installation of [[CS-E 20|CS-E 20(d)]], covering inlet and exhaust influences, mount stiffness and damping, and rotor drive systems [AMC E 650(13)].
- Baseline test records and the validated analysis with its defined domain of applicability, accepted by the Agency [AMC E 650(14)].
- Evidence that calibration and validation used different test results [AMC E 650(14)(a)].

## Application to this engine

The AMC applies in full, less the fan, propeller and thrust reverser items
recorded below.

**Turboshaft is named in the AMC itself.** The engine architecture list that
defines a validated analysis domain of applicability includes "2- or 3-shaft
design, turboshaft, turbofan, open rotor, geared fan"
[AMC E 650(14)(b)(i)]. Architecture is therefore an explicit boundary of the
domain: an analysis validated on a turbofan baseline does not automatically cover
a turboshaft.

**Rotor drive systems are an installation item.**
[[AMC E 650|AMC E 650(13)]] lists rotor drive systems among the installation
features to consider for vibratory compatibility. For a rotorcraft that is the
drive into the transmission, and it is the item most likely to need operating
limitations or procedures under [[CS-E 650|CS-E 650(h)]].

**The EECS speed relief.** (4)(b) allows the required maximum tested speed to be
reduced towards 100 % where the control system cannot exceed maximum rated speed
in fault-free operation. This engine has a full-authority EECS, so the relief is
available in principle; it rests on control system evidence under [[CS-E 50]] and
needs Agency agreement.

**Dwell testing binds this engine to the endurance test.** Any significant
response found in the survey is dwelt on within the incremental periods of
[[CS-E 740|CS-E 740(g)(1)]], and the components then go through the
[[CS-E 740|CS-E 740(i)]] strip inspection. The vibration survey and the endurance
test are therefore not independent programmes.

**Icing and rain and hail feed back into the stress margins.** (9)(b) requires
the stress margin suitability criteria to account for icing, rain and hail
effects "consistent with the corresponding certification test evidence", so
[[CS-E 780]] and [[CS-E 790]] results are inputs to the CS-E 650(f) margin
justification, not only to their own paragraphs.

## Not applicable

- **(3)**, in part — the fan is named among the modules whose most critical blades and vanes are selected, and among the discs and spacers to be covered. A turboshaft has no fan; the compressor and turbine cases in the same sentences apply.
- **(7)**, **(8)(d)**, **(8)(f)**, in part — the fan is named alongside the compressor in the inlet distortion, corrected speed and flutter verification passages. The compressor cases apply throughout.
- **(13)**, in part — "each Propeller approved for use on the Engine" and "each thrust reverser approved for use on the Engine" among the installation features to consider. A turboshaft driving a rotorcraft transmission has no propeller, and propeller and thrust reverser material is excluded from this vault by scope. The remaining three features apply.

## References

Specification: [[CS-E 650]]
Related: [[CS-E 70]] · [[CS-E 100]] · [[CS-E 520]] · [[CS-E 740]] · [[CS-E 780]] · [[CS-E 790]] · [[CS-E 830]] · [[CS-E 50]] · [[CS-E 60]] · [[CS-E 510]] · [[CS-E 20]] · [[AMC E 520]] · [[AMC E 740]]

## Amendment history

Amended at Amendment 7 and again at Amendment 8.

**Amendment 7** rewrote paragraph (5) and made three smaller corrections. The
heading changed from "Altitude and Temperature Effects" to "Altitude,
Temperature and Environmental Effects", and the paragraph gained the whole icing
and rain and hail passage:

- **Before:** "Changes in operating conditions associated with ambient temperature and altitude variations affect Engine performance and airflow characteristics. This can have a significant effect on aerodynamic forcing and damping, which, in turn, affects the vibratory response and behaviour of certain components."
- **After:** the same sentence widened to "ambient temperature, altitude and environmental variations", to "Engine performance, airflow characteristics and rotor imbalance", and to "aerodynamic and mechanical forcing and damping" — preceded by a new requirement that the evaluated conditions include icing and rain and hail conditions, and followed by the permission to use the CS-E 780 and CS-E 790 test evidence.

This adds work. Rotor imbalance and mechanical forcing were not named before, and
the icing and rain and hail conditions were not required to be included.
Amendment 7 also added the corresponding clause to (9)(b), so the stress margin
criteria must now account for icing, rain and hail effects, and added "stiffness
and damping of the mount system" to the installation features of (13), where the
previous text named only the mount. In (15) the Part 21 citation was corrected to
"point 21.A.33 of Part 21".

**Amendment 8** made a single cross-reference correction in paragraph (10), Dwell
Testing:

- **Before:** "Components subjected to such dwell testing should subsequently also meet the strip inspection requirements of CS-E 740(h)."
- **After:** "Components subjected to such dwell testing should subsequently also meet the strip inspection requirements of CS-E 740(i)."

The letter changed from (h) to (i). The obligation is unchanged; the reference now
points at the strip inspection sub-point as [[CS-E 740]] numbers it.

The paragraph carries `[Amdt No: E/1]`, `[Amdt No: E/4]`, `[Amdt No: E/7]` and
`[Amdt No: E/8]`.
