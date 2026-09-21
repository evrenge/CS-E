---
id: "AMC 20-3B"
type: EXT
document: AMC-20_Amendment_23.pdf
tags: [eecs, control-system, lopc, safety-assessment, software, hirf, lightning, aircraft-supplied-data]
---
# AMC 20-3B — Certification of Engines Equipped with Electronic Engine Control Systems

> [!summary]
> AMC 20-3B is the acceptable means of compliance for an engine with an
> electronic engine control system. CS-E 50 names it in its banner, as AMC 20-3.
> It interprets CS-E paragraph by paragraph, and it is where the numbers live:
> the loss of power control rate, the definition of a loss of power control
> event for a rotorcraft, the pass and fail criteria for HIRF and lightning, and
> the over-speed protection targets. For a turboshaft it is the most important
> document outside CS-E itself.

## Requirement

The verbs are AMC 20-3B's own. It is an acceptable means of compliance, so
"should" marks an accepted method and an applicant may propose an alternative
and justify it.

### Scope and general

| Ref | Obligation | Strength |
|---|---|---|
| **(2)** | The AMC is relevant to engine certification specifications for an EECS, whether electrical or electronic, analogue or digital. It is in addition to other AMC such as AMC E 50 or AMC E 80. | Statement |
| **(2)** | It covers control, protection, limiting and monitoring functions, and integrated aircraft or propeller functions to the extent that they affect compliance with CS-E. The principles apply to the whole EECS, not only the power function. | Statement |
| **(3)** | For a turbine engine, the specifications most relevant to the control system itself are CS-E 20, CS-E 25, CS-E 30, CS-E 50, CS-E 60, CS-E 80, CS-E 110, CS-E 130, CS-E 140, CS-E 170, CS-E 500, CS-E 510, CS-E 560, CS-E 745 and CS-E 1030. | Statement |
| **(5)** | Compliance of the control system with the aircraft certification specifications is determined at aircraft certification, not engine certification. | Statement |
| **(5)** | Where the installation is unknown at engine certification, make reasonable installation and operational assumptions for the target installation, and note any installation limitation or operational issue in the instructions for installation or operation, or the TCDS. | Accepted method |

### System design and validation, section (6)

| Ref | Obligation | Strength |
|---|---|---|
| **(6)(a)** | Perform all testing and analysis necessary to ensure that every Control Mode, including those arising from Fault Accommodation, is implemented as required. | Accepted method |
| **(6)(a)** | Review the need for protective functions, such as over-speed protection, for all Control Modes including Alternate Modes. | Accepted method |
| **(6)(a)** | State any limitation on operation in an Alternate Mode in the engine instructions for installation and operation, and describe the functioning of the system in its Primary and Alternate Modes there. | Accepted method |
| **(6)(a)** | Substantiate by analysis or test that operating in an Alternate Mode has no unacceptable effect on engine durability or endurance. Component testing under CS-E 170 is the primary route. | Accepted method |
| **(6)(a)(ii)** | Establish the availability of any Back-up Mode by routine testing or monitoring, and document the frequency of that check in the instructions for continued airworthiness. | Accepted method |
| **(6)(b)** | The AMC is not specifically intended to apply to crew training modes, which are installation-specific and negotiated case by case. Assess them, including lock-out systems, in the system safety analysis of CS-E 50(d), and design against inadvertent entry. | Accepted method |
| **(6)(c)** | For a non-dispatchable configuration, compliance with CS-E 50(a) does not imply strict compliance with the operability specifications, if no likely pilot input in the intended installation results in surge, stall, flame-out or unmanageable delay in power recovery. | Relief |
| **(6)(c)** | Consider, when assessing a reduced-capability Back-up Mode: its installed operating characteristics and how they differ from the Primary Mode, the likely impact on pilot workload, and the frequency of transfer from Primary to Back-up. | Accepted method |
| **(6)(d)** | Accomplish transition to an Alternate Mode automatically, in general. A system needing pilot action to engage the Back-up Mode may also be acceptable, provided the reliance on manual transition does not pose an unacceptable operating characteristic or crew workload, or require exceptional skill. | Accepted method |
| **(6)(d)** | Review the transient power change on transfer for compliance with CS-E 50(b), considering transfer frequency, transient magnitude, and a demonstration that the system controls the engine safely through the transition. | Accepted method |
| **(6)(d)** | For a rotorcraft, a determination that the mode transition is safe may not be possible from analysis or simulation alone, so a flight test programme is normally expected. | Accepted method |
| **(6)(d)** | Provide an analysis identifying the Faults that cause a Control Mode transition, automatically or through pilot action. | Accepted method |
| **(6)(d)** | For a turboshaft, the transition must not cause excessive rotor over-speed or under-speed that could cause emergency shutdown, loss of electrical generator power or the setting-off of warning devices. Declare the power change in the instructions for installing the engine. | Accepted method |
| **(6)(d)(i)** | Identify any observable time delay associated with a mode, channel or system transition, or in re-establishing the pilot's ability to modulate power, in the instructions for installation and operation. | Accepted method |
| **(6)(d)(ii)** | Match the type of flight crew annunciation to the nature of the transition, and state its intent and purpose in the instructions for installation and operation. | Accepted method |
| **(6)(e)(i)** | Test the control system at levels agreed between the engine and aircraft applicants where the installation is known. Where it is not, use the external threat level defined at aircraft level with assumptions on installation attenuation, or agree default HIRF levels with EASA. | Accepted method |
| **(6)(e)(ii)** | Base certification testing on the installed control system including representative engine-aircraft interface cables. | Accepted method |
| **(6)(e)(ii)** | Conduct HIRF and lightning tests as system tests on closed-loop or open-loop laboratory set-ups, with the system controlling at the most sensitive operating point. | Accepted method |
| **(6)(e)(iii)** | Interpret the pass and fail criteria of CS-E 170 for HIRF and lightning as no adverse effect on the functionality of the system. | Accepted method |
| **(6)(e)(iv)** | Provide a maintenance plan for any protection system that is part of the control system type design and is needed to meet the qualified EMI, HIRF and lightning levels, with engineering validation of the maintenance actions. | Accepted method |

### Integrity of the engine control system, section (7)

| Ref | Obligation | Strength |
|---|---|---|
| **(7)(b)(ii)** | For a turbine engine intended for a rotorcraft, a loss of power control event is one where the control system loses the capability of modulating power between idle and 90% of maximum rated power at the flight condition, except OEI power ratings; or suffers a Fault causing a power oscillation above the level in (7)(c); or loses the capability to govern the engine in compliance with CS-E 500(a) and CS-E 745. | Statement |
| **(7)(b)(ii)** | For a rotorcraft, the inability to meet the operability specifications in an Alternate Mode need not be counted as an LOPC event. | Relief |
| **(7)(b)(ii)** | For a multi-engine rotorcraft, the LOPC definition may exclude the inability to meet the operability specifications in an Alternate Mode, because the affected engine can be left at a reasonably fixed power while the others manoeuvre the aircraft. Acceptability may have to be demonstrated at aircraft certification. | Relief |
| **(7)(b)(ii)** | A single-engine rotorcraft must meet the operability specifications in the Alternate Modes unless the lack of that capability is shown acceptable at aircraft level. Operability in the Alternate Modes is a necessity where the control transitions to it more often than the acceptable LOPC rate, or where normal crew activity requires rapid power changes. | Statement |
| **(7)(c)** | Keep any uncommanded power oscillation to a magnitude that does not impact aircraft controllability in the intended installation. | Accepted method |
| **(7)(c)** | An event where the flight crew has to shut an engine down because of unacceptable power oscillations caused by the control system is an in-service LOPC event, whatever the levels discussed. | Statement |
| **(7)(d)(i)** | For a turbine engine, the EECS should not cause more than one LOTC/LOPC event per 100 000 engine flight hours. | Accepted method |
| **(7)(d)** | An applicant may propose a different rate, substantiated against the criticality of the engine and control system in the intended installation, to show equivalence with existing systems in comparable installations. | Permitted |
| **(7)(e)** | Submit a system reliability analysis substantiating the agreed rate. A numerical analysis such as a Markov model, a fault tree or an equivalent approach is expected. | Accepted method |
| **(7)(e)** | Address every component that can contribute, including electrical, mechanical, hydromechanical and pneumatic elements, and conduct the analysis together with the system safety assessment of CS-E 50(d). | Accepted method |
| **(7)(e)** | Include sensors or elements outside the engine type design that can contribute, such as an installer-supplied power lever transducer, and include the effects of loss, corruption or Failure of Aircraft-Supplied Data. State the reliability and interface requirements for those elements in the instructions for installation, avoiding double counting in the aircraft analyses. | Accepted method |
| **(7)(e)** | Consider all Faults, detected and undetected, and state in the instructions for continued airworthiness any periodic maintenance needed to find and repair Covered and Uncovered Faults in order to meet the rate. | Accepted method |
| **(7)(f)** | Where the type design specifies commercial or industrial grade electronic parts, have available the reliability data substantiating each Failure rate used, the procurement and quality assurance plans, and separate databases for similar parts from different vendors. | Accepted method |
| **(7)(f)** | Where the declared temperature environment exceeds the rated range of such parts, substantiate the extended range, adjust the Failure rates used in the analyses, and state any cooling provision in the instructions for installation. | Accepted method |
| **(7)(g)** | Substantiate compliance with the single Fault specifications of CS-E 50(c)(2) and (3) by a combination of test and analysis. In its full-up configuration the control system should be essentially single Fault tolerant of electrical and electronic component Failures with respect to LOTC/LOPC events. | Accepted method |
| **(7)(h)** | Consider as local events under CS-E 50(c)(4): overheat conditions such as those from a hot air duct burst, fires, and fluid leaks or mechanical disruptions damaging harnesses, connectors or control units. | Accepted method |
| **(7)(h)** | Where freedom from a Hazardous Engine Effect relies on another function providing protection, show that the same local event does not render that function inoperative. | Accepted method |
| **(7)(h)** | There is no probability associated with CS-E 50(c)(4), so consider all foreseeable local events, identified by sound engineering judgement and well documented to aid installation certification. | Statement |
| **(7)(h)** | Test or analyse each wire or combination of wires that a local event could affect, for opens, shorts to ground and shorts to power, and show the Faults give identified responses and no Hazardous Engine Effect. Inform the installer of the potential effects of interface wiring Faults. | Accepted method |
| **(7)(h)** | Assess by analysis or test the effects of fluid leaks impinging on control system components; they must not cause a Hazardous Engine Effect or a potential latent Failure condition on circuitry. | Accepted method |

### System safety assessment, section (8)

| Ref | Obligation | Strength |
|---|---|---|
| **(8)(a)** | Address all operating modes in the assessment required by CS-E 50(d), and substantiate the data used. | Accepted method |
| **(8)(a)** | The LOTC/LOPC analysis is a subset of the assessment; the two may be separate or combined. | Statement |
| **(8)(a)** | Include Faults in aircraft signals that could affect more than one engine in a multi-engine installation, which CS-E 50(g) addresses. | Accepted method |
| **(8)(a)** | Identify the assumptions, installation requirements and limitations the analysis establishes, and state them in the instructions for installation and operation; where necessary place them in the airworthiness limitations section under CS-E 25(b)(1). | Accepted method |
| **(8)(a)** | Provide a summary listing the malfunctions and Failures caused by the control system and their effects, including those resulting in LOTC/LOPC, those leaving the engine unable to meet the operability specifications, transmission of erroneous parameters, Failures of integrated aircraft functions, and Failures resulting in Major or Hazardous Engine Effects. | Accepted method |
| **(8)(a)** | Consider all signals used by the control system, in particular cross-engine control signals and air signals as described in CS-E 50(i). | Accepted method |
| **(8)(b)** | Demonstrate compliance with CS-E 510, with the agreed LOTC/LOPC rate, and with the expected total frequency of occurrence of Failures that leave the engine non-compliant with the operability specifications without being LOPC events. | Accepted method |
| **(8)(b)(iv)** | Identify the consequence of the transmission of a faulty parameter and include it in the LOTC/LOPC analysis as appropriate, with any mitigating information placed in the engine operating instructions. | Accepted method |
| **(8)(c)** | Uncovered Faults giving a power change of less than 3% in the take-off envelope are generally acceptable, without detracting from the obligation to ensure the full-up system provides the declared minimum rated power. | Statement |
| **(8)(c)** | Record in the assessment documentation the frequency of occurrence of Uncovered Faults giving a power change greater than 3% but less than an LOTC/LOPC event. There is no firm specification for this class, but the rate should be of the order of 10⁻⁴ events per Engine flight hour or less. | Accepted method |
| **(8)(c)** | Detected Faults giving a power change of up to 10% in the take-off envelope may be acceptable where the total frequency of occurrence is low; a total frequency above 10⁻⁴ events per Engine flight hour would not normally be acceptable. | Statement |
| **(8)(c)** | Limit the authority of cross-engine signals at the receiving control system so that undetected Faults do not cause an unacceptable power change, generally no more than 3% absolute difference of the current operating condition, and accommodate detected Faults in those signals to the same limit. | Accepted method |

### Protective functions, section (9)

| Ref | Obligation | Strength |
|---|---|---|
| **(9)(a)** | Rotor over-speed protection is usually achieved by an independent protection system, so that two independent Faults are needed to produce an uncontrolled over-speed. | Statement |
| **(9)(a)** | Where the protection is provided solely by a control system function, show in the safety assessment that the probability per Engine flight hour of an uncontrolled over-speed from any cause combined with a Failure of the protection system is less than 10⁻⁸ events per Engine flight hour. | Accepted method |
| **(9)(a)** | The protection system itself would be expected to have a Failure rate of less than 10⁻⁴ Failures per Engine flight hour. | Statement |
| **(9)(a)** | A self-test before each flight is normally necessary; verifying functionality at engine shutdown or start-up is adequate. Where an engine is routinely not shut down between flight cycles, account for that in the analyses. | Accepted method |
| **(9)(a)** | Where multiple protection paths exist, testing a different path each engine cycle is acceptable so long as the system meets the 10⁻⁴ rate, the objective being a complete test in the minimum number of cycles. | Permitted |
| **(9)(a)** | Data showing that the mechanical parts of the protection system operate without Failure between stated periods is acceptable in lieu of testing them each cycle, with a periodic inspection established instead. | Permitted |
| **(9)(b)** | Make the integrity of any other protective function provided by the control system consistent with the safety analysis of that function. Where the function is not an engine function it may not be part of engine certification. | Accepted method |
| **(9)(b)** | Include all Failure modes of all functions incorporated in the system in the safety assessment, including functions added to support aircraft certification, so that they reach the airframe assessment. | Accepted method |

### Software and airborne electronic hardware, section (10)

| Ref | Obligation | Strength |
|---|---|---|
| **(10)(a)** | The objective of CS-E 50(f) is to prevent as far as possible software and AEH errors that would result in an unacceptable effect on power, or any unsafe condition. | Statement |
| **(10)(a)** | In a multiple engine installation, the possibility of errors common to more than one control system may determine the criticality level. | Statement |
| **(10)(b)** | Methods compliant with the latest edition of AMC 20-115 for software, or AMC 20-152 for AEH, are acceptable. An alternative method may be proposed and is subject to EASA approval. | Accepted method |
| **(10)(c)** | The criticality level is determined by the engine safety assessment process, and the software and AEH should be developed at the levels agreed between the engine and aircraft applicants. | Accepted method |
| **(10)(d)** | Where on-board or field loading is implemented, release the software by an approved design change and a service bulletin, verify the part number by electronic means or update the nameplate, and keep an approved configuration control system with a compatibility table under configuration control. | Accepted method |
| **(10)(f)** | To certify a control system with provision for software modification by someone other than the type certificate holder, provide the information needed to approve the change and demonstrate that precautions prevent the modification from affecting engine airworthiness. | Accepted method |

### Aircraft-supplied data and electrical power, sections (12) and (13)

| Ref | Obligation | Strength |
|---|---|---|
| **(12)(a)** | Under CS-E 50(g), on loss, interruption or corruption of Aircraft-Supplied Data the engine should continue to function safely and acceptably, without unacceptable power effects, Hazardous Engine Effects, or loss of the ability to comply with the operability specifications. | Accepted method |
| **(12)(b)** | The regulatory intent is Fault Accommodation against single Failures of Aircraft-Supplied Data, which may be accommodation by transition into a Control Mode independent of that data. | Statement |
| **(12)(b)** | Keep software in the data path at a level consistent with the EECS, state in the instructions for installation that the aircraft applicant is responsible for preserving data integrity through that path, supply the effects of faulty and corrupted data, and state the assumed reliability level used in the analyses. | Accepted method |
| **(12)(c)** | Prepare a Fault Accommodation chart defining the architecture for Aircraft-Supplied Data, and where the aircraft Failure modes are unknown assume loss of data and erroneous data. | Accepted method |
| **(12)(e)** | Demonstrate the functionality of the Fault Accommodation logic by test, analysis or both. Where the aircraft air data system is lost with all aircraft generated power, demonstrate acceptable engine operation by test. | Accepted method |
| **(13)(a)** | The objective is an electrical power source that is single Fault tolerant, including common cause and common mode, so that the EECS can comply with CS-E 50(c)(2). | Statement |
| **(13)(b)** | An engine dedicated power source supplies a single control system alone, usually from an alternator driven by the engine or by the rotorcraft transmission. Batteries count as aircraft-supplied power for a turbine engine. | Statement |
| **(13)(c)** | Analyse the design architecture to identify which sources are dedicated and which are aircraft-supplied, including the effects of losing each. | Accepted method |
| **(13)(c)** | Give the dedicated source enough capacity margin under CS-E 50(h)(2) to keep the control system functioning wherever automatic in-flight recovery is expected, including immediate automatic relight after an unintended shutdown, accounting for temperature, tolerances, idle speed variation and deterioration over life, substantiated by test or analysis. | Accepted method |
| **(13)(d)** | State any aircraft-supplied power reliability value used in the analyses in the instructions for installation, and include aircraft power Faults in the safety assessment and LOTC/LOPC analysis where they can contribute. | Accepted method |
| **(13)(e)** | State the control system's electrical power supply quality requirements in the instructions for installation under CS-E 50(h)(3), including steady state and transient under-voltage and over-voltage limits. The power input standards of ED-14 are an acceptable definition. | Accepted method |
| **(13)(e)** | Low voltage transients outside the declared capability must not cause permanent loss of function, inappropriate operation causing an operating limit to be exceeded, or transmission of unacceptable erroneous data, and the system should resume normal operation when power recovers, within a time stated in the instructions for installation. | Accepted method |
| **(13)(g)** | Demonstrate the effects of loss of aircraft-supplied power by engine test, system validation test, bench test or a combination. | Accepted method |

### Integration with the aircraft, section (15)

| Ref | Obligation | Strength |
|---|---|---|
| **(15)(b)** | Where aircraft systems implement engine control functions, the engine applicant is responsible for specifying the requirements for the EECS in the instructions for installation and for substantiating their adequacy. | Statement |
| **(15)(c)(ii)** | Identify system responsibilities and interface definitions between engine and aircraft in the appropriate documents, covering functional requirements and criticality, Fault Accommodation strategies, maintenance strategies, criticality levels, the reliability objectives for LOTC/LOPC events and faulty parameter transmission, the environmental requirements, interface data and characteristics, and aircraft power supply requirements. | Accepted method |
| **(15)(c)(iii)** | Identify and agree the distribution of compliance tasks between the engine and aircraft applicants with the respective authorities. Evidence provided for engine certification should be used for aircraft certification. | Accepted method |

This note records the sections that bear on a turboshaft engine. Four are not
expanded, and each for a stated reason. Section (1) states the purpose, which
the summary above carries. Section (4) defines the mode vocabulary — Primary
Mode, Alternate Mode, Back-up Mode — in a figure, and accuracy rule 6 keeps the
vault from restating a figure in words; the terms themselves are CS-E's and are
defined in [[CS-E 15]]. Section (11) is reserved. Section (14), Piston Engines,
states only that the sections above address them. The propeller, thrust reverser
and automatic take-off thrust control examples in sections (9), (12) and (15)
are named above where they set the pattern, and are not expanded, because none
of them arises on this engine.

One reading is recorded rather than assumed. Sub-point (7)(b)(ii) writes that
the inability to meet the operability specifications in the Alternate Modes
"may not be included as LOPC events". The vault reads that as a relief, not a
prohibition, because the sentence sits among the rotorcraft reliefs and the
bullet below it writes the same allowance as "may not need to include". The row
above is labelled Relief on that reading.

## Bearing on this engine

AMC 20-3B is not a CS-E paragraph and creates no CS-E obligation. What it does
is fix the numbers that [[CS-E 50]] and [[AMC E 50]] leave open, and several of
them are written for a rotorcraft.

**The LOPC definition is rotorcraft-specific, and the OEI ratings are carved out
of it.** An event is a loss of power control where the system loses "the
capability of modulating power between idle and 90% of maximum rated power at
the flight condition, except OEI power ratings" [ext AMC 20-3B(7)(b)(ii)]. The
engine declares 30-Second OEI, 2-Minute OEI and Continuous OEI, so those ratings
sit outside the LOPC definition and the analysis is built around the
all-engines-operating power band.

**The multi-engine installation earns a relief.** For a multi-engine rotorcraft
the LOPC definition need not include the inability to meet the operability
specifications in an Alternate Mode, because the affected engine "can be left at
reasonably fixed power conditions" while the others manoeuvre the aircraft
[ext AMC 20-3B(7)(b)(ii)]. `engine_profile.md` declares a multi-engine
installation, so this relief is available. It is not free: acceptability may be
demonstrated at aircraft certification, and a single-engine installation would
lose it entirely.

**The rate is one event per 100 000 engine flight hours** for a turbine engine
[ext AMC 20-3B(7)(d)(i)], substantiated by a Markov model, a fault tree or an
equivalent numerical analysis [ext AMC 20-3B(7)(e)]. The analysis has to reach
beyond the engine type design, to installer-supplied elements such as the power
lever transducer, and it has to be done with the CS-E 50(d) safety assessment
rather than beside it.

**Three numbers govern power disturbance.** Uncommanded oscillations below 10%
peak to peak of Take-off Power have been accepted in some installations where
one engine only is affected [ext AMC 20-3B(7)(c)]. Uncovered Faults giving less
than a 3% power change in the take-off envelope are generally acceptable, and
the frequency of those above 3% should be of the order of 10⁻⁴ events per engine
flight hour or less [ext AMC 20-3B(8)(c)]. Cross-engine signals are limited to
about 3% absolute difference of the current operating condition.

That last one carries a warning for this installation. The AMC records that
"signals sent from one Engine control to another in a rotorcraft installation,
such as load sharing and One Engine Inoperative (OEI), can have a much greater
impact on Engine power when those signals fail", and that the data for those
Failure modes belongs in the safety assessment [ext AMC 20-3B(8)(c)]. The
cross-engine signals of [[CS-E 50|CS-E 50(g)]] and [[CS-E 50|CS-E 50(i)]] are
therefore not bounded by the 3% figure on this engine.

**Over-speed protection has two targets.** An uncontrolled over-speed from any
cause combined with a Failure of the protection system is to be shown less
probable than 10⁻⁸ events per Engine flight hour, and the protection system
itself is expected to fail less often than 10⁻⁴ per Engine flight hour
[ext AMC 20-3B(9)(a)]. A self-test before each flight is normally necessary, and
shutdown or start-up testing is accepted. This is the substance behind
[[CS-E 50|CS-E 50(e)]], which this engine meets by the electronic route because
the control system is a full-authority EECS.

**The HIRF and lightning pass criterion is defined here, not in CS-E 170.** No
adverse effect means, among other things, no "greater than 3 % change of
Take-off Power or Thrust for a period of more than 2 seconds", no transfer to an
Alternate Channel, Back-up System or Alternate Mode, no component damage, no
false annunciation, and no erroneous operation of a protection system
[ext AMC 20-3B(6)(e)(iii)]. It also creates a maintenance duty: any protection
needed to hold the qualified levels gets a maintenance plan in the instructions
for continued airworthiness of [[CS-E 25]].

**Aircraft dependence is where a full-authority EECS is most exposed.** Sections
(12) and (13) both end in the same place: the assumed reliability, the quality
requirements and the effects of loss belong in the instructions for installation
of [[CS-E 20|CS-E 20(d)]], and the assumptions behind them in [[CS-E 30]]. The
dedicated power source is expected to keep the control system running through an
immediate automatic relight after an unintended shutdown, with margin for
deterioration over the life of the engine [ext AMC 20-3B(13)(c)].

[VERIFY: CS-E Amendment 8 cites "AMC 20-3" without a revision letter, and
AMC-20 Amendment 23 carries AMC 20-3B. Confirm with the Agency that AMC 20-3B is
the revision applicable to this application, and record it in the certification
programme. The same question applies to AMC 20-1, held as AMC 20-1A, and to
AMC 20-115, held as AMC 20-115D.]

[VERIFY: whether the applicant seeks the multi-engine rotorcraft relief of
AMC 20-3B(7)(b)(ii), which excludes Alternate Mode operability from the LOPC
definition. It changes what the LOPC analysis has to cover, and its
acceptability may be revisited at aircraft certification.]

Two sections name documents this vault does not hold. The environmental test
procedures of section (6)(e) run through ED-14 and DO-160, and the software
methods of section (10) run through AMC 20-115 and the ED-12 and DO-178 series.
Both are recorded as dead ends in `review/dead_ends.md`.

## References

Bears on: [[CS-E 50]] · [[AMC E 50]] · [[AMC E 80]] · [[AMC E 170]] · [[CS-E 510]] · [[CS-E 20]] · [[CS-E 30]] · [[CS-E 25]]
