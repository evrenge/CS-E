---
id: "AMC E 135"
type: AMC
subpart: A
pages: 59-60
changed_in: []
tags: [electrical-bonding, earth, continuity, inspection]
covers: ["AMC E 135"]
---
# AMC E 135 — Electrical Bonding

> [!summary]
> This AMC states what CS-E 135 is actually asking for and how to show it. The
> intent is twofold: the engine has a main earth, and a current path exists from
> externally mounted components to that earth. Compliance may be shown by
> examining the type design drawings, by electrical continuity checks, or by
> inspecting a representative engine.

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| — | Electrical bonding is a means to protect against the effects of electro-static discharges and currents from electrical Faults. | Statement |
| **(i)** | The intent of CS-E 135 is that a main engine earth is provided. This is generally achieved by showing that all the elements of the engine carcass are electrically bonded together. | Statement |
| **(ii)** | The intent of CS-E 135 is that a current path for electrical bonding exists between certain components mounted externally to the engine and the main engine earth. | Statement |
| — | Show that the modules, assemblies, components and accessories installed in or on the engine are electrically bonded to the main engine earth, with respect to the accumulation of electro-static or electrical charge. | Accepted method |
| — | This may be accomplished by examination of the type design drawings, by electrical continuity checks, or by actual inspection of a representative engine. | Permitted |

AMC E 135 is a single unnumbered passage containing a two-item intent list, so
the `Ref` cells carry no sub-point identifier except for that list.

The AMC restates the population differently from the specification. CS-E 135
scopes by behaviour — components "susceptible to or … potential sources of"
static discharge or Fault current. The AMC asks the applicant to show that "the
modules, assemblies, components and accessories installed in or on the Engine"
are bonded [AMC E 135]. Showing the whole installed population is bonded
satisfies the narrower specification without having to argue the behaviour of
each item.

The three demonstration routes are alternatives, not a sequence. Drawing
examination is a design-data route; continuity checks and inspection of a
representative engine are hardware routes.

## Compliance

- Evidence that a main engine earth is provided, generally by showing that all elements of the engine carcass are electrically bonded together [AMC E 135(i)].
- Evidence of a current path between externally mounted components and the main engine earth [AMC E 135(ii)].
- Bonding evidence for the modules, assemblies, components and accessories installed in or on the engine, by one of the three accepted routes [AMC E 135].

## Application to this engine

The whole AMC applies. Nothing in it is restricted by engine type, rating or
control system.

Intent (ii) is the one that reaches a full-authority EECS. The engine electronic
control unit and its associated sensors and harnesses are components mounted
externally to the engine carcass, so the current path from each of them to the
main engine earth is exactly what (ii) asks for, and it is part of the evidence
supporting the interference consequence in [[CS-E 135]].

Where the drawing-examination route is used, the bonding provisions must be
visible on the type design drawings. That connects to
[[CS-E 110|CS-E 110(a)]], which requires the drawings to give full particulars
of the design.

## References

Specification: [[CS-E 135]]
Related: [[CS-E 130]] · [[CS-E 110]] · [[CS-E 50]] · [[CS-E 80]] · [[AMC E 80]]

## Amendment history

Unchanged at Amendments 7 and 8. The paragraph carries `[Amdt. No.: E/1]`.
