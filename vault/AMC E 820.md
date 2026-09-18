---
id: "AMC E 820"
type: AMC
subpart: E
pages: 230-230
changed_in: []
tags: [over-torque, oei, strip, acceptance-criterion]
covers: ["AMC E 820(a)(2)"]
---
# AMC E 820 — Over-torque Test

> [!summary]
> One sentence serves CS-E 820, and it sets the acceptance criterion for the
> post-test strip. Compliance with CS-E 820(a)(2) requires showing that an
> over-torque event does not compromise the ability of the engine to reach its
> Rated 30-Second and 2-Minute OEI Power.

## Requirement

### AMC E 820(a)(2) — what the strip must establish

| Ref | Obligation | Strength |
|---|---|---|
| **(a)(2)** | In order to comply with CS-E 820(a)(2), show that an over-torque event does not compromise the ability of the engine to reach its Rated 30-Second and 2-Minute OEI Power. | Accepted method |

AMC E 820(a)(2) is a single sentence and the only AMC material under CS-E 820.

It converts a general condition into a specific one.
[[CS-E 820|CS-E 820(a)(2)]] requires the stripped condition to be "satisfactory
for continued running"; this AMC says what continued running has to include. The
engine must still be able to deliver the short OEI ratings after the over-torque,
not merely be fit to run.

That is a stricter test than serviceability. An engine could pass a strip
inspection with deterioration that nonetheless reduces the margin available at
30-Second OEI Power.

## Compliance

- Demonstration, after the over-torque test, that Rated 30-Second OEI Power and Rated 2-Minute OEI Power remain achievable [AMC E 820(a)(2)].
- Strip examination findings assessed against that capability, not only against serviceable limits [AMC E 820(a)(2)].

## Application to this engine

The AMC applies wherever [[CS-E 820]] is elected, and it is written for exactly
this rating set: `engine_profile.md` declares Rated 30-Second OEI Power and Rated
2-Minute OEI Power.

The criterion links the over-torque test to the endurance programme. The short
OEI ratings are substantiated by the additional test of
[[CS-E 740|CS-E 740(c)(3)(iii)]], and [[CS-E 740|CS-E 740(i)(2)(iii)]] accepts
that after that test the engine may show deterioration beyond what
CS-E 740(i)(1) permits. CS-E 820 runs the opposite way: after an over-torque, the
OEI capability must survive.

An identical criterion applies to the over-speed test. [[AMC E 830]] uses the
same wording for [[CS-E 830|CS-E 830(c)]], so the two tests share one acceptance
standard.

## References

Specification: [[CS-E 820]]
Related: [[CS-E 830]] · [[CS-E 870]] · [[CS-E 740]] · [[CS-E 40]] · [[CS-E 60]] · [[AMC E 830]] · [[AMC E 60]] · [[AMC E 740]]
