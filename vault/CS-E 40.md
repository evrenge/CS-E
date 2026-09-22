---
id: "CS-E 40"
type: CS
subpart: A
pages: 29-30
changed_in: [Amdt7]
imports: [CS-27, CS-29, Part 21]
tags: [ratings, oei, limitations, tcds]
---
# CS-E 40 — Ratings

> [!summary]
> Take-off Power and Maximum Continuous Power must be established for every
> engine. All other ratings are elective, but substantiation is mandatory once
> claimed. This engine declares three rotorcraft OEI ratings and Rated 30-Minute
> Power. The three OEI ratings select the endurance schedule of
> CS-E 740(c)(3)(i). Ratings are declared for the weakest engine of the type,
> not the test engine.

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| **(a)** | Establish Take-off Power and Maximum Continuous Power. | Required |
| **(b)(3)** | Other ratings may be established for turbine engines for multi-engined rotorcraft, among them (i) 30-Second OEI Power, (ii) 2-Minute OEI Power and (v) Continuous OEI Power. | Required if claimed |
| **(b)(4)** | Rated 30-Minute Power may be established for rotorcraft engines. | Required if claimed |
| **(c)** | The engine Power ratings will be based on standard atmospheric conditions, with no air bleed for aircraft services, and with only the accessories essential for engine functioning installed, including controls. Any other basis is declared in the engine type certificate data sheet (TCDS). | Statement |
| **(d)** | Establish operating limitations for the intended operating conditions. | Required |
| **(e)** | List rated powers, and limitations the crew must respect, in the TCDS under point 21.A.41 of Part 21. | Required |
| **(e)** | The engine type certificate data sheet must also identify, or make reference to, all other information found necessary for the safe operation of the engine. | Required |
| **(f)** | Define each rating for the lowest power that all engines of the type may be expected to produce under the conditions used to determine the rating. Define the minimum testing, with its conditions, that ensures all engines meet this. | Required |
| **(g)** | Account for the accuracy limits of the Engine Control System and instrumentation, as defined in CS-E 60(b). | Required |

A rating under (b) is elective. Once the applicant claims it, substantiation is
mandatory [CS-E 40(b)].

Sub-point (f) governs the declared value. The rating reflects the weakest engine
of the type, not the test engine [CS-E 40(f)].

## Compliance

- Rating declaration covering Take-off Power and Maximum Continuous Power [CS-E 40(a)].
- Rating declaration covering 30-Second OEI, 2-Minute OEI and Continuous OEI Power [CS-E 40(b)(3)(i), (ii), (v)], substantiated per [[AMC E 40|AMC E 40(b)(3)]].
- Rating declaration covering Rated 30-Minute Power [CS-E 40(b)(4)(i)].
- Statement of the declaration basis, or a TCDS entry where the basis departs from standard atmospheric conditions without bleed [CS-E 40(c)].
- Operating limitations schedule [CS-E 40(d)], scope per [[AMC E 40|AMC E 40(d)]].
- TCDS entry under point 21.A.41 of Part 21, listing rated powers and crew-respected limitations [CS-E 40(e)].
- Minimum-engine substantiation: the test programme and conditions demonstrating that every engine of the type meets the declared ratings [CS-E 40(f)].
- Accuracy budget for the Engine Control System and instrumentation [CS-E 40(g)], against the tolerances of [[CS-E 60|CS-E 60(b)]].

## Application to this engine

The applicant declares 30-Second OEI, 2-Minute OEI and Continuous OEI Power
under (b)(3) [CS-E 40(b)(3)]. It declares Rated 30-Minute Power under (b)(4)
[CS-E 40(b)(4)].

Two rotorcraft ratings remain available but are not claimed: 2½-Minute OEI
[CS-E 40(b)(3)(iii)] and 30-Minute OEI [CS-E 40(b)(3)(iv)]. Their absence
removes the 2½-minute insertions from the endurance schedule — see [[CS-E 740]].

The declared combination of 30-Second, 2-Minute and Continuous OEI selects the
endurance schedule of CS-E 740(c)(3)(i), complemented by the additional test of
CS-E 740(c)(3)(iii) [CS-E 740(c)(3)(i)].

The declared ratings also bear on the rotorcraft applicant's transmission test.
Where turbine engine torque output to the transmission can exceed the highest
engine or transmission torque limit, and the pilot does not directly control
that output, both codes prescribe an OEI torque test. With each engine in turn
inoperative, each remaining transmission input is tested at the maximum torque
attainable under probable operating conditions for at least 15 minutes
[ext CS 29.927(b)(2)], [ext CS 27.927(b)(2)]. That duration is longer than the
30-Second and the 2-Minute OEI Power Ratings. See [[CS 29.927]] and
[[CS 27.927]].

**What sub-point (e) points to.** Point 21.A.41 states what a type certificate
includes: the type design, the operating limitations, the instructions for
continued airworthiness, the type certificate data sheet for airworthiness and
emissions, the applicable type certification basis and environmental protection
requirements, and "any other conditions or limitations prescribed for the
product … in the applicable certification specifications and environmental
protection requirements" [ext 21.A.41]. The rated powers and the
crew limitations of CS-E 40(e) enter the certificate through that last item.
The same point adds that "the engine type-certificate data sheet shall include
the record of exhaust emissions compliance", which is the data sheet duty
discussed in [[CS 34.2]] and [[AMC E 1020]].

"OEI override" is a control-system feature, not a rating under this paragraph,
as `engine_profile.md` records. It is assessed under [[CS-E 50]] and the
[[CS-E 510]] safety analysis.

## Not applicable

- **(b)(1)**, **(h)** — piston engine rating definitions.
- **(b)(2)** — OEI ratings for multi-engined aeroplanes; (b)(3) governs rotorcraft.
- **(b)(3)(iii)**, **(b)(3)(iv)** — the 2½-Minute OEI and 30-Minute OEI Power rating definitions. `engine_profile.md` declares neither, and the consequences of not claiming them are in `## Application to this engine`.
- Throughout — where the source pairs thrust with power, in any of the forms it uses, only the power term is carried. This engine produces shaft power; the thrust half of each pair has no turboshaft case.

## References

Accepted means: [[AMC E 40]] · [[AMC E 40|AMC E 40(b)(3)]] · [[AMC E 40|AMC E 40(d)]]
Related: [[CS-E 25]] · [[CS-E 50]] · [[CS-E 60]] · [[CS-E 740]] · [[AMC E 20|AMC E 20(f)]]
External: [[CS 29.927]] · [[CS 27.927]] · [[CS 34.2]]

## Amendment history

Amended at Amendment 7. The amendment inserted "point" and "of Part 21" in
sub-point (e), aligning the citation format with Part 21. No change to the
ratings themselves.
