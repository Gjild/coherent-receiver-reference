# ADR-0005 — Provisional Relative-Phase Pilot Acceptance

**Status:** provisionally accepted by the project owner for analytical teaching
and technical-authoring workflow development. **Recorded:** 2026-10-29.
**Authority:** the owner's explicit acceptance/closeout instruction, following
focused AI-assisted technical review, targeted corrections and reported numerical
checks. Codex records this decision; no independent human specialist approval is
asserted.

## Decision and exact artifacts

Close development of the corrected dual-channel relative-phase-stability pilot
for the limited purpose above. Use it as a bounded analytical teaching example
and as evidence for assessing authoring methods. This is permission for that use,
not demonstrated educational effectiveness or general engineering authority.

The accepted working-tree bytes are identified by SHA-256 below. At capture,
HEAD was be286af44321092975e2f6efc1d471edf9716e2b; it does not contain the staged
pilot additions. All six artifacts matched their staged bytes. The hashes, not
that contextual revision, identify the accepted artifacts. This closeout changes
none of them and creates no commit, tag or index update.

| Artifact | SHA-256 |
|---|---|
| [book/relative-phase-stability.qmd](../../book/relative-phase-stability.qmd) | 47464ca685f0c5a320ee0da0a96620f2ac93ea19e07257c919dddf7580c49b1f |
| [engineering/src/coherent_receiver/relative_phase.py](../../engineering/src/coherent_receiver/relative_phase.py) | 0cbb1ec38f0e6db3ee56ed42054fa2645a043c58284680a44e91067fb1447e53 |
| [engineering/examples/relative_phase_pilot.py](../../engineering/examples/relative_phase_pilot.py) | 01a5efc26e41446240c03d3eeb4ed5aeff770188ba23a909cd5eb5ab8a9d33d6 |
| [tests/test_relative_phase.py](../../tests/test_relative_phase.py) | 67339bdec224fb6cb50a69883cca1a22e2f9930a2e9db6422abfebd1ac2a087c |
| [book/figures/relative-phase-reference-planes.svg](../../book/figures/relative-phase-reference-planes.svg) | cb78b44d7b15669d739e944faa711f29a5dcc2371f377adffaf297e7852178a8 |
| [book/figures/relative-phase-state-sequence.svg](../../book/figures/relative-phase-state-sequence.svg) | 4f57255a213cc7dd7be97948c4b44c27e11193d080da20cca3ce9209239e2f28 |

The [pilot brief](../pilots/relative-phase-stability.md) records scope and
canonical destinations. The [review record](../../reviews/relative-phase-pilot.md)
owns the nine correction dispositions and detailed evidence. Existing standards,
[source notes](../../references/source-notes/relative-phase-stability.md) and
bibliography provide context; they are not globally approved by this decision.
Pilot-local conventions remain local; book-wide adoption needs separate review.

## Evidence and checks

Available evidence: readable derivations with stated assumptions; reproducible
illustrative calculations; focused AI-assisted critique/corrections; authorial
checks; narrow claim-level source examinations recorded previously. AI review
and software agreement are not independent physical evidence.

Closeout reran 19 standard-library tests successfully: cross-spectral ordering,
unequal correlated endpoint paths, pure-delay/lowpass limits, time/spectral
observation equivalence, Gaussian accumulation, DC-rejecting versus absolute
calibration uncertainty, held updates, asymmetric regression/reference conversion,
wrapped/state/fixture ambiguity, complex-filter perturbation, covariance-sum
conditions, input validation, snapshot precision/timing and fixed-LO/fixed-IF
slopes. The example reproduced its tables and corrected maintenance allocation.
These support mathematical/computational consistency under encoded assumptions;
a scalar correction identity is not a demonstrated calibration algorithm.

Python 3.12.3 and Quarto 1.10.18 were available. Scaffold integrity and four-page
HTML rendering passed; final link/hash/preservation/whitespace outcomes are
recorded in [current work](../current-work.md). Full pytest execution could not
start because pytest is absent; NumPy is also absent, so original NumPy-based
tests remain unexecuted. No packages were installed.

## Qualifications, reconsideration and next boundary

This acceptance does **not** establish physical-model validation for particular
receiver hardware, experimental confirmation, educational effectiveness, general
receiver-design applicability or product compliance. No laboratory campaign,
actual reader trial or independent human specialist review occurred. Browser
pixel inspection remains pending; HTML generation/source inspection is narrower.
PDF rendering and offline MathJax availability are not demonstrated.

Endpoint spectra/correlations, thermal and supply sensitivities, fixture response,
acquisition alias/linearity effects, 0.03-degree remaining snapshot uncertainty
and settling/update interfaces remain assumptions requiring evidence before
hardware use. Specialist examination of mathematics, calibration identifiability,
finite-record/update operators and measurement uncertainty remains outstanding.

Reconsider the affected accepted use if a consequential derivation or test is
found wrong, reproducibility fails, sources fail to support an imported claim,
changed assumptions/reference planes invalidate a calculation, or reader/
specialist evidence exposes misleading teaching. Changed accepted artifact bytes
require explicit assessment of the acceptance scope; extending to hardware,
other operating regimes or broader claims requires new evidence and owner
decision. Preserve ADR-0002–0004 and all earlier qualifications.

**Next activity:** post-pilot development-method assessment and sustained authoring
preparation — **not yet started**. This administrative closeout performs neither
that assessment nor subsequent chapter/reference-design work. Stop here.
