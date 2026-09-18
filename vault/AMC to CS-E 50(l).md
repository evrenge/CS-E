---
id: "AMC to CS-E 50(l)"
type: AMC
subpart: A
pages: 38-38
changed_in: []
tags: [security, iuei, eecs, risk-assessment]
---
# AMC to CS-E 50(l) — Information system security protection

> [!quote] AMC to CS-E 50(l)
> "For Engine Control Systems, AMC 20-42 provides acceptable means, guidance and methods to address CS-E 50(l), with special consideration given to any external interfaces of the Engine and the interfaces between the aircraft and the Engine, if applicable."

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| — | AMC 20-42 provides the acceptable means, guidance and methods for CS-E 50(l), with special consideration of any external engine interfaces and the aircraft-to-engine interfaces. | Accepted method |
| — | The security risk assessment should take into account specific cases of intentional unauthorised electronic interactions (IUEIs) that could have similar effects on all the Engine Control Systems of an aircraft, and not only interactions that could adversely affect a single engine. | Accepted method |

The second obligation is the substantive one. A security assessment scoped to one
engine is not sufficient: the assessment must consider an interaction that
reaches every control system on the aircraft at once.

## Compliance

- Security risk and vulnerability assessment under AMC 20-42 [AMC to CS-E 50(l)], satisfying [[CS-E 50]](l).
- Explicit treatment of common-mode IUEIs affecting all engine control systems of an aircraft, alongside single-engine cases [AMC to CS-E 50(l)].
- Assessment of external engine interfaces and aircraft-to-engine interfaces [AMC to CS-E 50(l)].
- Procedures and Instructions for Continued Airworthiness maintaining the security protections [CS-E 50(l)], carried into [[CS-E 25]](c)(13).

## Application to this engine

The engine uses a full-authority EECS with aircraft-supplied data and electrical
power, so the aircraft-to-engine interfaces named here are real attack surfaces
rather than a theoretical case.

The common-mode requirement is the one that drives scope. In a multi-engine
rotorcraft, every engine carries the same control system, so an interaction
exploiting a shared vulnerability reaches all of them. The assessment must cover
that case.

[VERIFY: AMC 20-42 is the named acceptable means for this paragraph and is not
held in `source/`. Obtain it before settling the security compliance method.]

## References

Specification: [[CS-E 50]]
Related: [[CS-E 25]] · [[CS-E 510]] · [[AMC E 50]]

## Amendment history

Unchanged at Amendments 7 and 8. Introduced at Amendment 6.
