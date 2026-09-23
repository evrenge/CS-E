---
id: "AMC 20-1A"
type: EXT
document: AMC-20_Amendment_23.pdf
tags: [eecs, control-system, installation, aircraft-interface, software, aeh, local-events, compliance-distribution]
---
# AMC 20-1A — Certification of Aircraft Propulsion Systems Equipped with Electronic Control Systems

> [!summary]
> AMC 20-1A is the installation side of the electronic control system case. It
> is written for aircraft certification, so it addresses the installer, not the
> engine applicant. It sets precautions for aircraft-supplied electrical power
> and data, for local events, for software and AEH criticality levels, and for
> environmental protection levels. It also divides the compliance tasks between
> the engine and the aircraft applicant. Its engine-side counterpart is
> AMC 20-3B.

## Requirement

The verbs are AMC 20-1A's own. It is an acceptable means of compliance, so
"should" marks an accepted method and an applicant may propose an alternative
and justify it.

### Scope, and the relationship to AMC 20-3B

| Ref | Obligation | Strength |
|---|---|---|
| **1** | The existing certification specifications for Engine, Propeller and aircraft certification may require special interpretation for Engines and Propellers equipped with electronic control systems, because of the nature of the technology and the greater interdependence of Engine, Propeller and aircraft systems. | Statement |
| **1** | AMC 20-1 addresses the compliance tasks relating to the certification of the installation of propulsion systems equipped with electronic control systems. | Statement |
| **1** | AMC 20-3 is dedicated to certification of Engine control systems, but identifies some Engine-installation-related issues that should be read in conjunction with AMC 20-1. | Accepted method |
| **2** | For aircraft certification, the related specifications are listed for aeroplanes in CS-25 and, where applicable, CS-23; for rotorcraft they are the equivalent specifications in CS-27 and CS-29. | Statement |
| **3** | The AMC is relevant to the specifications for aircraft installation of Engines or Propellers with electronic control systems, whether the technology is electrical or electronic, analogue or digital. | Statement |
| **3** | It gives guidance on the precautions to be taken for the use of electrical and electronic technology for Engine and Propeller control, protection and monitoring, and, where applicable, for integration of functions specific to the aircraft. | Statement |
| **3** | Precautions have to be adapted to the criticality of the functions. | Required |
| **3** | The precautions may be affected by the degree of authority of the system, the phase of flight, and the availability of a backup system. | Statement |
| **3** | The AMC also discusses the division of compliance tasks between the applicants for Engine, Propeller and aircraft type certificates. Its guidance relates to issues to be considered during aircraft certification. | Statement |
| **3** | The AMC does not cover APU control systems. APUs are not used as propulsion systems and are addressed in the dedicated AMC 20-2. | Statement |

### Precautions, section 4

| Ref | Obligation | Strength |
|---|---|---|
| **4(a)** | The introduction of electrical and electronic technology can entail greater interdependence of the Engine or Propeller and the aircraft owing to the exchange of electrical power or data between them, increased integration of the control and related indication functions, and a risk of significant Failures common to more than one Engine or Propeller. | Statement |
| **4(a)** | Such common Failures might occur as a result of insufficient protection from electromagnetic disturbance, insufficient integrity of the aircraft electrical power supply, insufficient integrity of data supplied from the aircraft, hidden design faults or discrepancies within the propulsion system control software or airborne electronic hardware, or omissions or errors in the system, software or AEH specification. | Statement |
| **4(a)** | Take appropriate design and integration precautions to minimise these risks. | Accepted method |
| **4(b)** | The introduction of electronic control systems should provide for the aircraft at least the equivalent level of safety, and the related reliability level, as achieved in aircraft equipped with Engine and Propellers using hydromechanical control and protection systems. | Accepted method |
| **4(b)** | Coordinate early between the Engine, Propeller and aircraft applicants when possible, in association with EASA. | Accepted method |
| **4(c)** | Give due consideration to the reliability of the electrical power and data supplied to the electronic control systems and peripheral components. | Accepted method |
| **4(c)** | The potential adverse effects on Engine and Propeller operation of any loss of electrical power supply from the aircraft, or failure of data coming from the aircraft, are assessed during the Engine and Propeller certification. | Statement |
| **4(c)** | Check the assumptions made as part of the Engine and Propeller certification on the reliability of aircraft power and data for consistency with the actual aircraft design, during aircraft certification. | Accepted method |
| **4(c)** | Protect the aircraft from unacceptable effects of faults due to a single cause simultaneously affecting more than one Engine or Propeller. Consider in particular erroneous data received from the aircraft where the data source is common to more than one Engine or Propeller, and control system operating faults propagating via data links between Engines or Propellers. | Accepted method |
| **4(c)** | Any precautions needed may be taken either through the aircraft system architecture or by logic internal to the electronic control system. | Permitted |
| **4(d)** | Assess the effects of local events for Engine and Propeller certification. Whatever the local event, the behaviour of the electronic control system should not cause a hazard to the aircraft. | Accepted method |
| **4(d)** | This requires consideration of effects such as the control of thrust reverser deployment, the overspeed of the Engine, transient effects, and inadvertent Propeller pitch change under any flight condition. | Statement |
| **4(d)** | Where the demonstration that there is no hazard to the aircraft assumes that another function affords the necessary protection, show that this function is not rendered inoperative by the same local event, including destruction of wires, ducts and power supplies. | Accepted method |
| **4(d)** | Review the local event assessment during aircraft certification. | Accepted method |
| **4(e)** | The acceptability of the criticality levels and of the methods used for the development and verification of the software and AEH that are part of the Engine and Propeller type designs should have been agreed between the aircraft, Engine and Propeller designers prior to the certification activity. | Accepted method |
| **4(e)** | In this AMC, criticality level means either the software level of a software item or the AEH design assurance level of an AEH item. | Statement |
| **4(f)** | The validated protection levels for the Engine and Propeller electronic control systems, and their emissions of radio frequency energy, are established during the Engine and Propeller certification and are contained in the instructions for installation. | Statement |
| **4(f)** | Substantiate at aircraft certification that those levels are appropriate. | Accepted method |

### Interrelation between Engine, Propeller and aircraft certification, sections 5 and 6

| Ref | Obligation | Strength |
|---|---|---|
| **5(a)** | An analysis of the consequences of failures of the system on the aircraft has to be made, in order to satisfy the aircraft certification specifications such as CS 25.901, CS 25.903 and CS 25.1309. | Required |
| **5(a)** | Ensure that the software and AEH criticality levels, and the safety and reliability objectives for the electronic control system, are consistent with those requirements. | Accepted method |
| **5(b)** | The interface has to be identified for the AEH and software aspects between the Engine, Propeller and aircraft systems in the appropriate documents. | Required |
| **5(b)** | The Engine, Propeller and aircraft documents should cover in particular the software and AEH criticality level, per function if necessary; the reliability objectives for a loss of Engine or Propeller control or a significant change in thrust, including an IFSD due to a control system malfunction, and for the transmission of faulty parameters; the degree of protection against lightning or other electromagnetic effects, such as the level of induced voltages that can be supported at the interfaces; the Engine, Propeller and aircraft interface data and characteristics; and the aircraft power supply and its characteristics. | Accepted method |
| **5(c)** | The certification tasks of an aircraft propulsion system equipped with electronic control systems may be shared between the Engine, Propeller and aircraft certification. | Permitted |
| **5(c)** | Identify the distribution of tasks between the different certification activities and agree it with EASA and the appropriate Engine and aircraft authorities. | Accepted method |
| **5(c)** | Use appropriate evidence provided for Engine and Propeller certification for aircraft certification. The quality of any aircraft function software or AEH, and of the interface logic, already demonstrated for Engine or Propeller certification should need no additional substantiation for aircraft certification. | Accepted method |
| **5(c)** | Aircraft certification should deal with the specific precautions taken in respect of the physical and functional interfaces with the Engine and Propeller. | Accepted method |
| **6** | Section 6 gives an example of the distribution of the tasks between the Engine certification and the aircraft certification. Where necessary, take a similar approach for Propeller applications. | Accepted method |

[VERIFY: unlisted construction. The three rows above that carry Required use
"have to be adapted", "has to be made" and "has to be identified". None of them
is one of the seven source verbs, and none is in the declaratory table. The
vault reads a statement of necessity as Required, as it reads "is required to".
[[AMC 20-3B]] records the same open question for its own rows, and the owner
decides the construction once for every row in the vault that carries it.]

Section 6 is a table and the vault does not restate it in words: accuracy rule 6
puts a table in a crop, and the cropping tool reads the CS-E source only. Two
things about it are recorded because they are not in the crop's gift. Its
substantiation columns are headed CS-E and CS-25, so the worked example is an
aeroplane one, and the AMC offers no rotorcraft column. And its task rows reach
beyond the engine control function, to monitoring, aircraft data, thrust
reverser control, control system electrical supply, environmental conditions,
lightning and other electromagnetic effects, and fire protection.

### How this AMC and AMC 20-3B divide the work

Both documents state the division, and they state it the same way. AMC 20-1A
writes that "AMC 20-3( ) is dedicated to certification of Engine control systems
but identifies some Engine-installation-related issues that should be read in
conjunction with AMC 20-1( )" [ext AMC 20-1A 1]. AMC 20-3B writes the mirror
image: its own guidance "relates to issues to be considered during Engine
certification. AMC 20-1( ) addresses issues associated with the Engine
installation in the aircraft" [ext AMC 20-3B(2)]. AMC 20-3B sends the reader
here twice more, for the distribution of compliance tasks
[ext AMC 20-3B(15)(c)(iii)] and for the loss of the aircraft air data system
[ext AMC 20-3B(12)(c)].

**The split is by certification activity, not by rank.** AMC 20-1A states that
its guidance "relates to issues to be considered during aircraft certification"
[ext AMC 20-1A 3]; AMC 20-3B states that its own relates to engine
certification. Neither document supersedes the other, and neither text says so.
The overlap that follows is real and is visible in three places: both list the
same risks of electrical and electronic technology, both require the protecting
function to survive the same local event, and both ask for the interface
definition and the distribution of compliance tasks to be agreed. In each case
the duty is written from a different side. AMC 20-3B writes of "greater
dependence of the Engine on the aircraft" and cites the CS-E sub-point behind
each risk; AMC 20-1A writes of "greater interdependence" of the two and cites
none [ext AMC 20-1A 4(a)].

[VERIFY: neither document states which one governs where their texts overlap,
and neither states a precedence. The reading above is that the addressee decides
it — the engine applicant works to AMC 20-3B and the installer to AMC 20-1A —
but that reading is the vault's, not the documents'. It matters wherever the
two describe the same duty in different words, as at local events and at the
interface definition. Confirm the reading with the Agency and record it in the
certification programme.]

## Bearing on this engine

**AMC 20-1A creates no CS-E obligation.** It is an acceptable means for aircraft
certification, and its guidance "relates to issues to be considered during
aircraft certification" [ext AMC 20-1A 3]. The engine applicant is not its
addressee. What it does is fix what the installer will ask for, and every one of
those items is produced under CS-E.

**It names four engine-side deliverables.** The assumptions on the reliability
of aircraft power and data are made at engine certification and checked against
the actual aircraft design at aircraft certification [ext AMC 20-1A 4(c)]; those
assumptions are the subject of [[CS-E 30]] and are stated under
[[CS-E 20|CS-E 20(d)]]. The validated protection levels and the radio frequency
emissions are established at engine certification and carried in the
instructions for installation [ext AMC 20-1A 4(f)], which is the output of
[[CS-E 170]] and [[CS-E 80]]. The software and AEH criticality levels are agreed
between the designers before the certification activity begins
[ext AMC 20-1A 4(e)], which is the agreement [[CS-E 50|CS-E 50(f)]] depends on.
And the interface definition documents [ext AMC 20-1A 5(b)] carry the
reliability objectives that [[CS-E 50]] and [[CS-E 510]] establish.

**The multi-engine case is the one this document adds.** `engine_profile.md`
declares a multi-engine installation, and AMC 20-1A puts the duty to protect
against a single cause affecting more than one Engine on the aircraft, through
the aircraft system architecture or through logic internal to the control system
[ext AMC 20-1A 4(c)]. The engine side of the same problem is
[[CS-E 50|CS-E 50(g)]] and [[CS-E 50|CS-E 50(i)]], and the numbers for it are in
[[AMC 20-3B]].

**For a rotorcraft the aircraft specifications are not listed here.** Section 2
enumerates paragraph numbers for CS-25 and, where applicable, CS-23, and for
rotorcraft names only "equivalent specifications in CS-27 and CS-29"
[ext AMC 20-1A 2]. Section 5(a) then works its example against CS 25.901,
CS 25.903 and CS 25.1309 [ext AMC 20-1A 5(a)]. The AMC gives no rotorcraft
paragraph numbers anywhere, so the vault names none either. Identifying the
equivalents is the installer's task, and it is bound to the airframe code, which
is the open item in [[CS-E 30]].

**Two of its examples do not arise on this engine.** The local event list at
section 4(d) names the control of thrust reverser deployment and inadvertent
Propeller pitch change [ext AMC 20-1A 4(d)]. `engine_profile.md` declares no
thrust reverser and no propeller. The third example in the same list, the
overspeed of the Engine, does arise, and its engine-side treatment is
[[CS-E 50|CS-E 50(e)]] with the targets recorded in [[AMC 20-3B]].

The APU exclusion at section 3 does not reach this engine either: the engine is
a propulsion system, and the exclusion is for APUs that are not used as one
[ext AMC 20-1A 3].

## References

Bears on: [[CS-E 20]] · [[CS-E 30]] · [[CS-E 50]] · [[CS-E 80]] · [[CS-E 170]] · [[CS-E 510]] · [[AMC E 50]] · [[AMC E 170]]
Related: [[AMC 20-3B]] · [[AMC 20-115D]]
