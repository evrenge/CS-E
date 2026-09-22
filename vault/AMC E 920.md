---
id: "AMC E 920"
type: AMC
subpart: E
pages: 245-245
changed_in: [Amdt8]
tags: [over-temperature, oei, datum-temperature, transient-speed, turbine-integrity, amdt8]
---
# AMC E 920 — Over-temperature test

> [!summary]
> The AMC has two numbered parts. Part (1) is new at Amendment 8. It settles
> which engine condition fixes the datum turbine entry gas temperature: a
> deteriorated engine may be assumed. Part (2) defines "Maximum power-on rotor
> speed" for the CS-E 920(b) test. It also states what maintaining turbine
> integrity means after the test.

## Requirement

### AMC E 920(1) — the datum turbine entry gas temperature

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | To establish a datum turbine entry gas temperature, where this may vary at a fixed gas temperature operating limit depending on the deterioration condition of the engine, it is considered reasonable to assume an engine condition in which the gas temperature operating limit is likely to be achieved when at the maximum power setting. | Accepted method |
| **(1)** | This would normally suggest that a deteriorated engine condition may be assumed. | Statement |

The problem part (1) solves is that a margin above an operating limit gives a
definite test temperature only once the datum itself is fixed. On an engine
whose turbine entry gas temperature at a fixed operating limit varies with
deterioration, a new engine and a deteriorated engine give different absolute
datums. The AMC resolves it towards the condition in which the operating limit
is actually reached at maximum power — the deteriorated engine.

### AMC E 920(2) — maximum power-on rotor speed, and turbine integrity

| Ref | Obligation | Strength |
|---|---|---|
| **(2)** | For the purpose of the test of CS-E 920(b), "Maximum power-on rotor speed" is normally the steady state rotor speed associated with the 30-Second OEI Power rating. | Statement |
| **(2)** | This speed should be substituted by the transient rotor speed if the engine characteristic transient speed stabilisation exceeds 3 seconds during the transition to the 30-Second OEI power. | Accepted method |
| **(2)** | To demonstrate that the engine maintains the integrity of the turbine assembly after the over-temperature test, show that no burst, no blade Failure or no other significant Failure of any engine component would occur or become evident during the test, during shutdown, or during the subsequent strip examination. | Accepted method |
| **(2)** | Where any Failure becomes evident, analyse it and establish by analysis or test that the cause is not such that in service the OEI rating structure would not be satisfactorily achieved. | Accepted method |

The integrity criterion spans three windows, and all three count: during the
test, during shutdown, and during the subsequent strip examination. A Failure
that only becomes evident on strip is inside the criterion.

The last sentence is a double negative in the source and is easy to misread. Its
effect is this: a Failure does not automatically fail the test. The applicant
should establish that its cause would not prevent the OEI rating structure from
being satisfactorily achieved in service [AMC E 920(2)].

## Compliance

- A statement of the engine condition assumed for the datum turbine entry gas temperature, with its justification [AMC E 920(1)].
- Determination of the steady state rotor speed at the 30-Second OEI Power rating [AMC E 920(2)].
- Measurement of transient speed stabilisation time during the transition to 30-Second OEI power, and substitution of the transient rotor speed where it exceeds 3 seconds [AMC E 920(2)].
- Turbine integrity evidence covering the test, the shutdown and the strip examination: no burst, no blade Failure, no other significant Failure of any engine component [AMC E 920(2)].
- Where a Failure becomes evident, a cause analysis establishing that the OEI rating structure would still be satisfactorily achieved in service [AMC E 920(2)].

## Application to this engine

The AMC applies in full. Part (2) is written for exactly this rating structure,
naming the 30-Second OEI Power rating that the engine declares.

**The 3-second criterion is a measurement, not an assumption.**
[AMC E 920(2)] makes the test speed depend on the engine's own transient speed
stabilisation during the transition to 30-Second OEI power. That transition is
governed by the EECS-FADEC schedule, so the answer comes from the control system
behaviour established under [[CS-E 50]] and the power response work of
[[CS-E 745]]. It is measured before the CS-E 920(b) test condition can be
fixed.

**The deteriorated-engine datum makes the test hotter.**
Assuming a deteriorated condition under [AMC E 920(1)] raises the absolute
turbine entry gas temperature at which the operating limit is reached. The
margins of [[CS-E 920]] are then added to it: at least 19 °C in (b), and at
least 42 °C in (a) if point (1) governs that test too (see the open item under
Amendment history). The choice is conservative, and it is the one the AMC points
to.

**The integrity criterion is the same family as the over-limit tests.**
[[AMC E 820]], [[AMC E 830]] and [[AMC E 870]] each ask the applicant to show
that the short OEI ratings remain achievable after an over-limit event.
[AMC E 920(2)] sets the equivalent criterion in different words: the cause of
any Failure is shown not to prevent the OEI rating structure from being achieved
in service. The
over-temperature test of CS-E 920 differs in how its condition is fixed. The
specification sets the margins: at least 42 °C in [CS-E 920(a)] and at least
19 °C in [CS-E 920(b)]. [[CS-E 820]], [[CS-E 830]] and [[CS-E 870]] are run
instead at the over-limit values the applicant declares.

## References

Specification: [[CS-E 920]]
Related: [[CS-E 870]] · [[CS-E 860]] · [[CS-E 745]] · [[CS-E 50]] · [[CS-E 40]] · [[AMC E 820]] · [[AMC E 830]] · [[AMC E 870]]

## Amendment history

Amendment 8 amended AMC E 920, alongside the amendment to [[CS-E 920]].

| Change | Effect on obligation |
|---|---|
| The whole of **(1)** is inserted — the datum turbine entry gas temperature and the deteriorated engine condition | **New guidance.** The datum was previously unaddressed. |
| The remaining text is numbered **(2)** | Editorial. |
| The cross-reference becomes CS-E 920(b) | Follows the new sub-point structure of CS-E 920. It scopes the speed definition to the OEI test only, where before CS-E 920 had one test. |
| "Maximum power-on rpm" becomes "Maximum power-on rotor speed" | Editorial, and it aligns the AMC with the term CS-E 920(b) now uses. |
| "over temperature" becomes "over-temperature" | Editorial. |

Before the amendment the opening read: "For the purpose of the test of CS-E 920,
… is normally the steady state rotor speed associated with the 30-Second OEI
Power rating." [work/redline/AMC_E_920_Amdt8.md] The elided term is the one the
amendment replaced: Maximum power-on rpm.

The obligation on the OEI test is unchanged. What is new is the datum guidance
in (1). [VERIFY: whether that datum guidance also governs the new test of
CS-E 920(a). Point (1) is written without a scope, while point (2) is expressly
scoped to CS-E 920(b), so the reading is reasonable but the source does not make
it.]
