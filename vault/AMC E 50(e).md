---
id: "AMC E 50(e)"
type: AMC
subpart: A
pages: 37-37
changed_in: []
tags: [over-speed, protection, bite, testing]
---
# AMC E 50(e) — Rotor integrity

> [!quote] AMC E 50(e)
> "In case of the over-speed protection system, the BITE test should provide complete test of the electrical/electronic part of the protection system."

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| — | Over-speed protection is usually provided as part of the electronic Engine Control System, even where the devices are nominally independent. Periodic testing by built-in test equipment (BITE) or a functional test is one acceptable method of showing the protection function is available. | Accepted method |
| — | For an over-speed protection system, the BITE test should provide a complete test of the electrical and electronic part of the protection system. | Accepted method |
| — | The need for inspections or tests of the mechanical or actuating part of the protection system should be based on the results of the safety analysis for that part. | Accepted method |

The split matters. The electrical and electronic part is covered by a complete
BITE test. The mechanical and actuating part is not, and its inspection interval
is decided by safety analysis rather than by this AMC.

## Compliance

- BITE or functional test design providing a complete test of the electrical and electronic part of the over-speed protection [AMC E 50(e)], satisfying [[CS-E 50]](e)(1).
- Safety analysis of the mechanical or actuating part of the protection system, establishing whether inspection or test is needed and at what interval [AMC E 50(e)], within [[CS-E 510]].
- Manual test specification in the instructions for operation where the test is not fully automatic [CS-E 50(e)(1)].

## Application to this engine

The engine uses a full-authority EECS, so over-speed protection falls under the
electronic route of [[CS-E 50]](e)(1) rather than the hydromechanical route of
(e)(2). The BITE method described here is the applicable accepted means.

[[AMC E 50]](1) records that blade shedding or engine design related over-speed
protection is not part of the Engine Control System, because it is purely
mechanical. Where such a means is used in addition, it falls outside this AMC.

[VERIFY: this AMC refers to "the specification for 'reasonable assurance' of
providing functionality of the protection systems or circuits". That phrase does
not appear in CS-E 50(e) at Amendment 8, which requires "a means for testing the
system to establish the availability of the protection function". Confirm the AMC
is being read against the current CS-E 50(e) wording.]

## References

Specification: [[CS-E 50]]
Related: [[CS-E 510]] · [[CS-E 830]] · [[AMC E 50]]

## Amendment history

Unchanged at Amendments 7 and 8.
