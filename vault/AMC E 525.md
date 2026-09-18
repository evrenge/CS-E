---
id: "AMC E 525"
type: AMC
subpart: D
pages: 109-109
changed_in: []
tags: [continued-rotation, windmilling, clutch-drag, rotorcraft, oil-loss, unbalance]
covers: ["AMC E 525"]
---
# AMC E 525 — Continued rotation

> [!summary]
> One short AMC serves CS-E 525, and it names the rotorcraft case directly.
> Continued rotation comes from windmilling or from mechanical effects such as
> clutch drag in a multi-engine rotorcraft. Compliance may be by test or
> analysis. Two conditions must be addressed if applicable: complete loss of
> engine oil, and rotor unbalance from blade loss with subsequent rotor damage.
> The resulting interface conditions go to the installer.

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | Continued rotation can be either due to windmilling or due to mechanical effects such as clutch drag in the case of a multi-engined rotorcraft. | Statement |
| **(1)** | Compliance with CS-E 525 may be established by test or analysis, and should take into account the conditions imposed on the engine by a typical aircraft installation. | Permitted |
| **(2)** | Include consideration of all expected aircraft applications for the engine when determining the conditions imposed on the engine after in-flight shutdown and their maximum duration. | Accepted method |
| **(3)** | Consider and address, if determined to be applicable, complete loss of engine oil. | Accepted method |
| **(3)** | Consider and address, if determined to be applicable, rotor unbalance resulting from blade loss and subsequent rotor damage. | Accepted method |
| **(3)** | Give consideration to extended periods of continued rotation under these conditions, in conjunction with the assumed flight envelope with one engine shut down. | Accepted method |
| **(4)** | Determine by analysis or test or both, as required by CS-E 520(c)(2), the conditions imposed at the engine-to-aircraft interface as a result of the rotor unbalance and rotational speed associated with continued rotation following an engine blade loss and subsequent rotor damage, covering the entire flight envelope. | Accepted method |
| **(4)** | Provide those conditions in the installation documents required by CS-E 20. | Accepted method |

The list in (3) is explicitly open: the conditions to consider "should include,
but are not limited to, those identified below" [AMC E 525(3)].

Paragraph (4) does not create a second analysis. It routes the continued rotation
interface conditions into the engine model work already required by
[[CS-E 520|CS-E 520(c)(2)]], and then into the installation documents of
[[CS-E 20]].

## Compliance

- Test or analysis demonstrating acceptable effects of continued rotation, taking account of the conditions imposed by a typical aircraft installation [AMC E 525(1)].
- Statement of the conditions imposed after in-flight shutdown and their maximum duration, covering the expected aircraft applications [AMC E 525(2)].
- Assessment of complete loss of engine oil during continued rotation [AMC E 525(3)].
- Assessment of rotor unbalance from blade loss and subsequent rotor damage, over extended periods [AMC E 525(3)].
- Engine-to-aircraft interface conditions from unbalance and rotational speed across the entire flight envelope, delivered in the installation documents of [[CS-E 20]] [AMC E 525(4)], determined under [[CS-E 520|CS-E 520(c)(2)]].

## Application to this engine

The AMC applies, and paragraph (1) is written for this installation. Clutch drag
"in the case of a multi-engined rotorcraft" is named as a mechanism alongside
windmilling [AMC E 525(1)], so continued rotation here is not only aerodynamic.
The free-wheel unit is the means that would prevent driven rotation, and its drag
is what keeps the case live.

Paragraph (2) asks for consideration of all expected aircraft applications. For
this engine the declared application is a rotorcraft, which bounds the exercise:
the flight envelope with one engine shut down is the OEI envelope, flown on the
remaining engine at the ratings declared in `engine_profile.md`.

Complete loss of engine oil under (3) is the condition that makes
[[AMC E 130|AMC E 130(2)(c)]] treat turbine oil system components differently
from fuel components. Oil may keep flowing after shutdown precisely because of
continued rotation, which is why those components are usually evaluated to a
Fireproof rather than a Fire Resistant standard. It also connects to
[[CS-E 570|CS-E 570(e)(1)]], where the oil shut-off means must prevent the
discharge of hazardous quantities of oil.

## Not applicable

- **(2)**, in part — the aircraft applications listed include turbopropeller, subsonic aircraft and supersonic aircraft, and **(3)** refers to supersonic and supersonic-to-subsonic transition flight conditions. The declared application is a rotorcraft, so those cases do not arise. The obligation to consider the expected applications for this engine is unaffected.

## References

Specification: [[CS-E 525]]
Related: [[CS-E 510]] · [[CS-E 520]] · [[CS-E 570]] · [[CS-E 810]] · [[CS-E 20]] · [[CS-E 30]] · [[AMC E 130]] · [[AMC E 520]]
