---
id: "AMC E 60"
type: AMC
subpart: A
pages: 39-41
changed_in: [Amdt7]
imports: [CS-27, CS-29]
tags: [instruments, oei, monitoring, oil-pressure, assurance-level]
covers: ["AMC E 60", "AMC E 60(d)"]
---
# AMC E 60 — Provision for Instruments

> [!summary]
> Two AMC paragraphs serve CS-E 60. The general AMC covers what instrumentation
> to define, and where on the engine to sense a parameter so the reading
> protects the component it is meant to protect. AMC E 60(d) covers the OEI
> usage recording system: when a power level counts as used, what the record
> should contain, the development assurance level it needs, and when a genuine
> over-limit event does not count as OEI usage.

## Requirement

### AMC E 60 — instrumentation to define and where to sense it

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | Define the instrumentation necessary for engine operation within its limitations, and make provision for installing it. | Accepted method |
| **(1)** | Beyond instrumentation that may be required for aircraft certification, treat the engine safety analysis as a source of further instrumentation needs, where it shows the flight crew or maintenance personnel need information to prevent a Failure or to mitigate its consequences. | Accepted method |
| **(2)** | Exercise care in selecting the position on the engine at which a parameter is sensed, so the indication suits the protection of the relevant components. | Accepted method |
| **(2)(a)** | Choose the pick-up point for the oil pressure gauge and the low oil pressure warning device with due regard to all critical components, to ensure a satisfactory indication of the oil pressure to the main engine bearings. | Accepted method |
| **(2)(b)** | Unless otherwise agreed, place no relief valve or other component liable to Failure between the oil pressure gauge and warning device connection and the main engine bearings. | Accepted method |
| **(2)(b)** | Choose filters that protect oil jets or metering orifices so as to reduce the possibility of blockage to a minimum, and make them accessible for periodic inspection. | Accepted method |
| **(4)** | Allow the recording system to be reset by maintenance personnel only, and not by the flight crew, to prevent further engine operation before the prescribed mandatory post-flight inspection and maintenance action. | Accepted method |

Sub-point (1) names three examples of instrumentation that may be required for
aircraft certification: "indication of engine ice protection system activation,
rotor system unbalance, and fuel flow" [AMC E 60(1)]. The rotor system unbalance
example is specific to rotorcraft. The examples are the Amendment 7 insertion —
see **Amendment history**.

### AMC E 60(d) — OEI usage recording

| Ref | Obligation | Strength |
|---|---|---|
| **(d)(1)** | Treat the 30-Second OEI power level as used whenever one or more of the operating limitations applicable to the 2-Minute OEI power level are exceeded. | Statement |
| **(d)(1)** | Treat the 2-Minute OEI power level as used whenever one or more of the operating limitations applicable to the next lower OEI power rating, or other engine rating if applicable, are exceeded. | Statement |
| **(d)(2)** | The required means, provided by the applicant or by the rotorcraft manufacturer, are intended to automatically record entry into and subsequent usage of the defined power levels, and to alert the pilot automatically of entry, of impending time expiration, and of the time expiration point. | Statement |
| **(d)(2)** | Make the automatic recording compatible with the maintenance instructions prescribed for these ratings. | Accepted method |
| **(d)(2)** | Record the number of usages and the time of each usage or the accumulated time, including any exceedance of 30-Second OEI or 2-Minute OEI operating limitations or relevant time limitations. | Accepted method |
| **(d)(2)** | Provide a means to alert maintenance personnel that usage or exceedance of 30-Second or 2-Minute OEI power has taken place. | Accepted method |
| **(d)(3)** | Make the overall development assurance level of the recording and retrieval system consistent with the objective of having the information needed for mandatory maintenance actions available after use of the ratings. | Accepted method |
| **(d)(3)** | Base the development assurance levels of the recording and retrieval components on the criticality of the functions they perform, as determined through the system safety analysis required under CS-E 50(d). | Accepted method |
| **(d)(3)** | Where the recording or retrieval system is not part of the engine, state in the instructions for installation the objective of the system and that its overall development assurance level should be consistent with that objective. | Accepted method |
| **(d)(3)** | If the recording and/or retrieval system is not part of the engine, the aircraft should still comply with CS-27/29.1305 specifications. | Accepted method |
| **(d)(4)** | Allow the recording systems to be reset by maintenance personnel only, and not by the flight crew. | Accepted method |
| **(d)(5)** | An engine may be approved with 30-Second and 2-Minute OEI Power Ratings together with any combination of Maximum Engine Over-torque, Maximum Engine Over-speed and Maximum Exhaust Gas Over-Temperature in compliance with CS-E 820, CS-E 830 and CS-E 870. | Permitted |
| **(d)(5)** | In that case, engine operation above the Take-off Rating limits but within the limits established under CS-E 820, CS-E 830 and CS-E 870 need not be counted as usage of the 30-Second or 2-Minute OEI Power Ratings, where the event was a true over-torque, over-speed or over-temperature event and it can be demonstrated that the recording system can distinguish (i) an over-speed, over-torque or over-temperature with all engines operating from (ii) use of the ratings with one engine inoperative. | Relief |

AMC E 60(d)(1) defines usage by exceedance of the limitations of the level
below, not by a power reading. The 30-Second OEI level counts as used when a
2-Minute OEI limitation is exceeded, and the 2-Minute OEI level counts as used
when a limitation of the next lower rating is exceeded. Declared ratings
therefore determine what the recorder watches, and the definition chains
downward through every claimed OEI rating [AMC E 60(d)(1)].

AMC E 60(d)(2) also points to "paragraph (5) of AMC E 40(b) regarding exceedence
of the 2 minute time limitation at 2-Minute OEI power" [AMC E 60(d)(2)]. See
[[AMC E 40|AMC E 40(b)(3)]].

The relief in (d)(5) is conditional on two things at once: the event must be
genuine, and the recording system must be able to tell an all-engines-operating
over-limit event from OEI use. Without the second, the relief is not available
[AMC E 60(d)(5)].

## Compliance

- Instrumentation definition traced to the engine safety analysis, and provision for its installation [AMC E 60(1)], against [[CS-E 60|CS-E 60(a)]].
- Sensing-position justification for oil pressure, covering the pick-up point, the absence of a relief valve upstream of the bearings, and filter selection and access [AMC E 60(2)], against [[CS-E 60|CS-E 60(a)]] and [[CS-E 570]].
- Definition of the recorded events, tied to the operating limitations of each claimed OEI level [AMC E 60(d)(1)].
- Recording and alerting system description: what is recorded, how the pilot is alerted, how maintenance personnel are alerted, and how data is retrieved [AMC E 60(d)(2)], against [[CS-E 60|CS-E 60(d)]].
- Development assurance level assessment for the recording and retrieval system, derived from the system safety analysis of [[CS-E 50|CS-E 50(d)]] [AMC E 60(d)(3)].
- Instructions for installation stating the system objective and its assurance level, where the system is not part of the engine [AMC E 60(d)(3)].
- Reset-authority design evidence: maintenance personnel only [AMC E 60(4)], [AMC E 60(d)(4)].
- Where the relief of (d)(5) is used, evidence that the recording system discriminates all-engines-operating over-limit events from OEI usage [AMC E 60(d)(5)], against [[CS-E 820]], [[CS-E 830]] and [[CS-E 870]].

## Application to this engine

Both AMC paragraphs apply. `engine_profile.md` declares 30-Second OEI and
2-Minute OEI, which triggers [[CS-E 60|CS-E 60(d)]] and all of AMC E 60(d).

The (d)(1) definition chains through the declared ratings. The 2-Minute OEI
level counts as used when a limitation of "the next lower OEI power rating or
other Engine rating (if applicable)" is exceeded [AMC E 60(d)(1)]. For this
engine, the next lower OEI rating is Continuous OEI. So Continuous OEI
limitations set the trigger for 2-Minute OEI recording, even though Continuous
OEI itself is not recorded under CS-E 60(d).

AMC E 60(d)(3) states that where the recording or retrieval system is not part
of the engine, "the aircraft should still comply with CS-27/29.1305
specifications" [AMC E 60(d)(3)]. CS-E names the two rotorcraft codes
interchangeably here, at the same sub-paragraph number, so the obligation does
not depend on which code the installation targets. The duty falls on the
aircraft; the engine applicant's duty is the instructions for installation.

**What point 1305 requires is now readable, and it runs parallel to
CS-E 60(d).** For each turbine engine using 30-Second and 2-Minute OEI Power,
both codes require a device or system for use by ground personnel which
automatically records each usage and duration of power at those levels, permits
retrieval of the recorded data, can be reset only by ground maintenance
personnel, and has a means to verify proper operation [ext CS 29.1305(a)(26)],
[ext CS 27.1305(u)]. The pilot alerting duty is written in both places as well,
in nearly the same words [ext CS 29.1305(a)(25)], [ext CS 27.1305(t)] and
[[CS-E 60|CS-E 60(d)(1)]].

Two differences are worth carrying into the installation instructions. The
rotorcraft codes say the device can be "reset only by ground maintenance
personnel", where [[CS-E 60|CS-E 60(d)(2)]] says the means cannot be reset in
flight. And CS-E 60(d)(2)(ii) adds a duty the codes do not carry: the means must
alert maintenance personnel in a positive manner that the engine has been
operated at either or both levels.

A third item is live for this engine because of a rating CS-E 60(d) does not
cover. Where a 30-minute power rating is claimed, both codes require a means to
alert the pilot when the engines are at that rating level, when the event
begins, when the time interval expires and, where a cumulative limit in one
flight exists, when that cumulative time is reached [ext CS 29.1305(a)(27)],
[ext CS 27.1305(w)]. `engine_profile.md` declares Rated 30-Minute Power under
[[CS-E 40|CS-E 40(b)(4)]], so the installer needs the engine data to support
that alerting.

The (d)(5) relief is available only if the applicant declares Maximum Engine
Over-torque, Maximum Engine Over-speed or Maximum Exhaust Gas Over-Temperature
under [[CS-E 820]], [[CS-E 830]] or [[CS-E 870]].

[VERIFY: whether the applicant declares Maximum Engine Over-torque, Maximum
Engine Over-speed or Maximum Exhaust Gas Over-Temperature. `engine_profile.md`
does not record these, and they decide whether the AMC E 60(d)(5) relief is
available and whether the recorder needs discrimination logic.]

## Not applicable

- **AMC E 60(3)** — the worked example for CS-E 60(c) is inadvertent in-flight deployment of a thrust reverser. Thrust reversers are excluded from this vault by scope. The CS-E 60(c) segregation specification itself still applies and is covered in [[CS-E 60]].

## References

Specification: [[CS-E 60]]
Related: [[CS-E 40]] · [[CS-E 50]] · [[CS-E 510]] · [[CS-E 570]] · [[CS-E 820]] · [[CS-E 830]] · [[CS-E 870]] · [[AMC E 40]]
External: [[CS 29.1305]] · [[CS 27.1305]]

## Amendment history

AMC E 60(1) was amended at Amendment 7. The sentence about instrumentation
required for aircraft certification was rewritten:

- **Before:** "In addition to powerplant instrumentation required for aircraft certification, the Engine safety analysis might show the need for specific instrumentation…"
- **After:** "In addition to instrumentation which may be required for aircraft certification (for example, indication of engine ice protection system activation, rotor system unbalance, and fuel flow), the Engine safety analysis might show the need for specific instrumentation…"

The change drops "powerplant", softens "required" to "which may be required",
and adds the three examples. It widens the scope of instrumentation to consider
beyond powerplant instrumentation and names rotorcraft-relevant cases, but it
does not change the obligation: the operative duty remains on the safety
analysis to show what further instrumentation is needed. The paragraph carries
`[Amdt. No.: E/1]` and `[Amdt. No.: E/7]`.

AMC E 60(d) is unchanged at Amendments 7 and 8, and carries `[Amdt. No.: E/1]`.
