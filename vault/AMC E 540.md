---
id: "AMC E 540"
type: AMC
subpart: D
pages: 109-110
changed_in: []
tags: [foreign-matter, bird-strike, ingestion, struts, 200-knots]
---
# AMC E 540 — Strike and ingestion of foreign matter

> [!summary]
> This AMC bounds the work CS-E 540 requires. Loose objects such as tools and
> fasteners need substantiation only where they are more severe than the single
> large bird case. The large bird test results should be assessed against CS-E
> 510, including damage to lines and wiring housed in structural struts. Bird
> strike above 200 knots should be considered when verifying the Extremely
> Remote criterion. For multi-engine threats, the related test paragraphs are
> intended to be sufficient.

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | Carry out substantiation of the strike and ingestion effects of foreign objects such as cleaning cloths, hand tools, rivets, bolts and screws only if these are likely to be more severe than those of the single large bird strike or ingestion. | Relief |
| **(1)** | Assess the effects of the large bird ingestion test of CS-E 800 on the spinner or any engine static part, as a result of a bird strike, against the criteria of CS-E 510. | Accepted method |
| **(1)** | Consider the potential for bird induced damage to ducts, lines or wires housed in main frame struts or strut fairings — fuel, oil, hydraulic, high-pressure bleed air lines, or wiring associated with the engine control system — with regard to the objective of CS-E 540. | Accepted method |
| **(1)** | In order to verify the Extremely Remote criteria for Hazardous Engine Effects in case of bird strikes as required in CS-E 540(a), give consideration to the possibility of aircraft operation at speeds higher than 200 knots, associated with the corresponding probability of occurrence of encountering a single bird under such conditions. | Accepted method |
| **(2)** | CS-E 540(b) is intended to address, for example, rain, hail, ice, gravel, sand, small and medium birds. | Statement |
| **(2)** | For some threats, interpret the specifications of CS-E 540(b) in relation to other CS-E specifications, such as CS-E 800 for birds or CS-E 790 for rain and hail, which may quantify the safety objectives of CS-E 540(b). | Accepted method |
| **(2)** | Those related paragraphs are therefore intended to be sufficient for demonstrating compliance with CS-E 540(b) for the considered subject. | Statement |
| **(2)** | Assess any unusual finding made during those demonstrations of compliance against the safety objective of CS-E 540(b), continued safe flight and landing. | Accepted method |

The relief in (1) is a real reduction in work. Loose-object substantiation is
conditional: it is needed only where the object is likely to be more severe than
the single large bird case already demonstrated under [[CS-E 800]].

The 200-knot consideration is the one place where the AMC adds work beyond the
test paragraphs [AMC E 540(1)]. [[CS-E 800]] fixes an aeroplane test speed of
200 knots. This
AMC asks the applicant to consider operation above that speed when verifying
the Extremely Remote criterion, together with the probability of encountering a
single bird there.

Paragraph (2) is what keeps CS-E 540 from becoming a duplicate test programme.
The related paragraphs are intended to be sufficient for their own subject. For
a subject they cover, CS-E 540(b) reasserts itself only where a demonstration
produces an unusual finding [AMC E 540(2)].

## Compliance

- Screening of loose-object threats against the single large bird case, with substantiation only for those likely to be more severe [AMC E 540(1)].
- Assessment of the [[CS-E 800]] large bird ingestion test results on the spinner and engine static parts against the criteria of [[CS-E 510]] [AMC E 540(1)].
- Assessment of bird-induced damage to fuel, oil, hydraulic and high-pressure bleed air lines, and to engine control system wiring, where these are housed in structural struts or strut fairings [AMC E 540(1)].
- Consideration of bird strike above 200 knots, with the associated probability of encountering a single bird, against the Extremely Remote criterion [AMC E 540(1)].
- Assessment of any unusual finding from the [[CS-E 800]], [[CS-E 790]] and related demonstrations against continued safe flight and landing [AMC E 540(2)].

## Application to this engine

The AMC applies. Nothing in it is restricted by rating or control system.

The strut damage assessment reaches the control system directly. Wiring
"associated with the engine control system" is named among the items that may be
housed in main frame struts [AMC E 540(1)]. This engine has a full-authority
EECS, so loss of that wiring is a control system Failure assessed under
[[CS-E 50|CS-E 50(d)]] and [[CS-E 510]].

The 200-knot consideration is the case that CS-E 540 adds beyond the test
paragraphs, and it matters differently here than for an aeroplane. [[CS-E 800]]
sets 200 knots as the aeroplane test condition; the rotorcraft case in that
paragraph is written to a different speed. The AMC's question — operation above
200 knots, with the corresponding single-bird encounter probability — is
therefore assessed against the speeds this installation actually reaches.

[VERIFY: the maximum operating speed of the intended rotorcraft installation is
not recorded in `engine_profile.md`. It determines whether the AMC E 540(1)
consideration of operation above 200 knots arises for this engine, and is an
installation assumption under CS-E 30.]

## Not applicable

- **(1)**, in part — the naming of bifurcation strut fairings among the structures that may house lines and wiring. A bifurcation strut fairing is a bypass-duct structure and does not arise on this engine architecture. The main frame strut case in the same sentence applies, and the obligation to consider bird-induced damage to the lines and wiring is unaffected.

## References

Specification: [[CS-E 540]]
Related: [[CS-E 510]] · [[CS-E 50]] · [[CS-E 30]] · [[CS-E 580]] · [[CS-E 790]] · [[CS-E 800]] · [[CS-E 780]] · [[AMC E 80]]
