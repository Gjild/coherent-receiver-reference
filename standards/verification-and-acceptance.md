# Verification and Acceptance Standard

**Status:** provisional.

## What evidence establishes
- Algebraic/symbolic checks support mathematical consistency under encoded assumptions.
- Unit tests support implementation correctness for tested cases.
- Limiting cases, independent derivations, reference comparisons and convergence checks broaden confidence but do not automatically validate physics.
- Physical validation requires representative empirical evidence with stated domain and uncertainty.
- Requirements compliance is specific to the implemented system and its specified conditions.

## Risk-proportionate review
Use stronger independent methods for consequential system budgets, synchronization promises, phase-noise models, calibration identifiability and acceptance criteria. Do not treat repeated AI reasoning as independent physical evidence.

## Technical states
- **Draft:** unaccepted material.
- **Checked:** specific mechanical/mathematical/computational checks recorded.
- **Reviewed:** an engineer examined relevant reasoning and limitations.
- **Accepted for stated use:** human decision backed by adequate evidence; may later be restricted or superseded.
These labels are not identical to evidence type or publication readiness.

## Minimum acceptance information
Claim and intended use, assumptions, evidence/checks executed, important uncertainties, blocking issues, reviewing engineer and date/revision if formally accepted. Never fabricate a review record or claim human acceptance.

## Pilot checks and educational assessment

For consequential calculations compare distinct formulations, appropriate limits,
units, convergence and sampling error. A seeded simulation is reproducible, not
independent physical evidence. Code and analytical formulas sharing an assumption
cannot validate that assumption. Record unavailable dependencies and failed
commands as well as successful checks.

A reader assessment requires an actual RF-engineer participant to define a
measurand, calculate a decision, reject a misleading result, change the model for
a new topology/observation, and find applicability conditions. Record assistance,
reasoning errors and revisions; a small trial cannot establish general learning
effectiveness. A critical reference/sign/correlation/observability error requires
revision and reassessment. Authorial self-check is not specialist review.

Final human acceptance states separately: planning suitability; mathematical
correctness under assumptions; physical applicability; educational/practical
adequacy; experimental confirmation; and compliance for a named implementation.
Missing review or empirical evidence remains pending rather than inferred.

## Review of connections and task closure

Challenge the connections between observable, physical model, calculation,
implementation/procedure and evidence, not just the individual formulas. Use
asymmetric inputs or changed references/operators where symmetry can hide a defect.
Record correction propagation to dependent results and repeat affected checks.
A bounded task may close as a completed, checked provisional draft with human
review pending; this is distinct from human technical acceptance and publication
integration. Assess physical applicability separately; theoretical identities do
not universally require laboratory tests, while hardware-performance claims need
representative evidence. Publication integration additionally needs reading-path,
notation, cross-reference and rendered-presentation review for the intended edition.

## Separate-context AI review

AI review is additional evidence, not the human **Reviewed** state. Use a fresh
conversation with no author history or correctness assertions. Freeze input bytes
and record SHA-256 when HEAD does not identify them. Give the reviewer accepted
requirements, manuscript, applicable standards and actual source access; inspect
reasoning before author check code. Seek alternative derivations, limiting cases,
asymmetric counterexamples and failures of assumptions, reference planes and
engineering interpretation.

Classify findings as demonstrated errors, model/applicability concerns, missing
evidence, pedagogical defects or optional improvements. Record location, consequence,
evidence, author disposition, correction propagation and reassessment. Identify AI
model/effort/session, sources actually examined, checks run and unperformed checks.
A separate context using the same model retains correlated failure risks. Review
failure blocks progression; unavailable evidence restricts dependent claims.

## Visual-adequacy gate for bounded teaching units

Assess scientific correctness and pedagogical communication separately. Check
quantitative curves through independent formulations, limits and spot values;
check schematic paths, signs, planes and correlation against the model. Follow
[the actual-image procedure](../docs/VISUAL-INSPECTION.md): inspect standalone pixels
and the complete rendered page with readable detail crops, equations and captions.
Fresh read-only AI review receives actual raster attachments and frozen models;
record image access, readability limits, findings and correction reassessment.
Source parsing, successful capture and render success alone never clear this gate.

A missing indispensable explanation, consequential model/graphical error, unreadable
figure, failed image inspection or unresolved consequential review finding blocks
a positive visual-adequacy recommendation. Optional polish can remain documented.
AI visual review does not grant human acceptance, reader-trial evidence or physical
validation, and does not authorize subsequent canonical authoring.


At the start of **every authoring batch**, a newly executed environment smoke
test and actual author inspection of its PNG are required before manuscript/figure
development. Record executable versions, command/exit, hashes and visible content;
include the current smoke PNG in the first separate-context technical/visual
review packet. A prior successful batch is not a smoke-test waiver. If the route
is unavailable, preserve the visual gate and exact continuation boundary; diagnose
the missing dependency/permission specifically. Do not repeatedly invoke a reviewer
against a known usage limit or count failed invocations as completed review.

Review physical interpretation and model applicability as well as signs, scaling,
units, normalization, limiting cases, plotted geometry and schematic paths.
Review figure readability, captions, alt text and contribution to the surrounding
derivation/learning progression. Independent graphical verification must test the
model-to-figure mapping, not just rerun the same generator. Freeze corrected input
bytes and actual PNGs for fresh read-only targeted reassessment of consequential
changes. Retain original findings and author dispositions separately and archive
enough supplied inputs/images to reproduce the review after temporary files expire.

[ADR-0007](../project/decisions/ADR-0007-provisional-html-visual-pedagogy-acceptance.md)
is the owner's scoped visual acceptance for HTML analytical teaching/development.
It does not confer the human specialist **Reviewed** state, empirical validation,
educational effectiveness, PDF/offline compatibility, assistive-technology compliance
or publication readiness. Later owner decisions must state their own use and evidence.
