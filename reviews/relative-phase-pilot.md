# Current acceptance — analytical teaching and workflow development

**2026-10-29:** The project owner provisionally accepts the corrected pilot for
**analytical teaching and technical-authoring workflow development** under
[ADR-0005](../project/decisions/ADR-0005-provisional-relative-phase-pilot-acceptance.md).
That decision identifies the exact manuscript, figures, module, example and
tests by SHA-256. The development stage is closed for this use.

The owner authorizes limited acceptance following focused AI-assisted review
and corrections. This is not independent human specialist approval, physical
validation for receiver hardware, experimental confirmation, demonstrated reader
learning, general receiver-design applicability or product compliance. Technical
and educational specialist work, browser visual inspection and physical evidence
remain outstanding as detailed below. Local conventions are not adopted book-wide.

Closeout reran 19 pilot tests and the reproducible example successfully, rendered
four HTML pages and checked repository consistency. Full pytest could not start
(pytest and NumPy absent); no dependencies were installed. See
[current work](../project/current-work.md) for final checks and repository-state
observations. No new source examination, measurement, specialist review or actual
reader trial is asserted.

Reconsideration conditions are in ADR-0005. Next is **post-pilot development-method
assessment and sustained authoring preparation, not yet started**. This record
does not initiate that activity.

---

# Focused correction pass — evidence record before acceptance

The focused review requested nine corrections; the dispositions below describe
implemented changes and authorial checks, not specialist acceptance. The prior
implementation record is retained below as history. Its eight-test count and
calibration procedure are superseded by this correction record.

## Finding-by-finding disposition

| Finding | Correction and evidence | Remaining limit |
|---|---|---|
| 1. Static calibration vs band statistic | Removed static variance addition to DC-rejecting B. Defined absolute Var(X-C) with covariance and sampled zero-sum cancellation. Added held-update two-time covariance and randomized-grid hold spectrum | Real update/use correlations and filter edges need data; frozen-coefficient validation does not establish operational update performance |
| 2. Regression reference | Distinguish b_mean from b0; named PhaseDelayFit retains three-field tuple compatibility and phase_at(f0) converts explicitly; asymmetric and symmetric cases tested | Locally unwrapped common-state line fit only; no global ambiguity resolution or fixture removal |
| 3. Observation filtering | B acts after phase extraction. Derived complex-filter small-perturbation phase/AM/additive-noise transfer and tested against direct complex filtering | No full acquisition alias/image/blocker/noise budget |
| 4. Executable frequency access | Fixed 990 MHz LO, simultaneous comb 999/1000/1001.5 MHz plus held-out 1000.5 MHz; complex 32 Msample/s acquisition and per-tone DDC before 100 ksample/s decimation | Hardware satisfying passband, rejection, linearity and coherent phase-state interfaces not selected |
| 5. Spectral admissibility | Separate full Hermitian PSD condition from pairwise bounds and hardware realizability; three-channel counterexample and unequal correlated endpoint test | quadratic_spectrum is not a full matrix PSD validator; physical matrix validity remains explicit caller precondition |
| 6. Thermal and calibration age | RF P-to-mixer delay sign fixed, epoch is snapshot center, precision allocated/calculated, settling/latency/data gating and center-period bounds derived | Drift and remaining error/settling allocations assumed; no experimental demonstration |
| 7. Measurement identifiability | Added source/fixture/receiver/LO/acquisition/instrument equation; Q analog IF planes distinguished from post-channelizer O; interventions traced | Swaps identify stable reversible combinations, not every physical contributor or absolute truth |
| 8. Variance reduction | Independence replaced by zero aggregate off-diagonal covariance condition for equal-variance samples | Applicable covariance must be justified, not inferred from record length |
| 9. Software validation | Finite scalar/sequence/callback/matrix checks; paired lengths checked; invalid densities/corners/times rejected; wrapped/mixed/missing stated states rejected | Undeclared wrapping/state errors and full covariance validity cannot be inferred from samples |

## Recalculated results and engineering decision

The existing architecture band table is unchanged: compact shared/local SD
0.362364/1.145858 degrees; exposed shared/local 3.623641/1.145858 degrees.
Constant calibration uncertainty does not change those DC-rejecting statistics.
A separate absolute residual with independent 0.05-degree uncertainty and
0.362364-degree phase SD has SD 0.365797 degree; relevant covariance changes this
number according to Var(X-C). These are different observables.

A 10 ms extracted-phase snapshot predicts SD 0.025353 degree for compact shared
LO and 0.080173 degree for local synthesis. The latter **fails** the 0.04-degree
stochastic snapshot allocation. At 50 ms local synthesis predicts 0.034379
degree. With independent 0.03-degree remaining uncertainty, snapshot SDs are
0.039278 and 0.045628 degree for the selected 10/50 ms procedures.

Using a 20 ms pre-snapshot settle and 100 ms application time after snapshot end,
and allowing bounded-rate snapshot-to-center bias, maximum center periods are
2.207315 s (compact) and 2.177315 s (local). P=2 s yields deterministic drift
bounds 0.45522/0.46170 degree and invalid fractions 6.5%/8.5%. The 2.314815 s
number is the drift-only age scale, not a complete practical update period.
The allocation supports conditional procedure feasibility under the declared
model; uncertainty floors, actual settling or additional slow noise can invalidate
it. A 100 s frozen validation record is distinct from online calibration.

## Correction-pass checks actually executed

- 19 standard-library unittest tests pass, comprising eight retained/refined
  checks and eleven added methods. All previous correct cross-spectrum and Gaussian
  tests pass.
- New regression coverage: DC rejection with correlated constant calibration;
  absolute phase covariance; hold-update spectral triangle transform;
  asymmetric fit/reference conversion; fixed-LO versus fixed-IF delay slopes; wrapped delay alternatives, state offsets
  and fixture slope ambiguity; unequal complex endpoint responses with correlated
  reference/branch sources; complex-filter phase/AM perturbation; covariance-sum
  condition; malformed/nonfinite inputs; snapshot precision/timing; rectangular
  spectral average versus independent time-domain covariance integration.
- The fixed scalar-correction check is explicitly an arithmetic identity, not
  evidence of an implemented calibration procedure. Synthetic OLS recovery is
  a local regression consistency check, not calibration validation.
- Reproducible example executes; Simpson 65536/131072 snapshot refinements differ
  by at most 7.27e-17 rad². The independent rectangular-average time-domain
  covariance check agrees within 1e-15 rad².
- Full pytest command attempted again: pytest absent. Existing NumPy-based tests
  remain unexecuted because NumPy is also absent; no package installation.
- Quarto HTML render succeeds (four pages) with the temporary cache override.
  Final HTML inspection resolves 32 internal fragment links on four pages,
  with no duplicate IDs or unresolved references. Eleven protected planning
  files and the pre-existing changes.patch/changes.zip are unchanged from the
  correction-start snapshot; ten existing files changed, with no new tracked
  files or index modification. Whitespace checks pass. See docs/VALIDATION.md. Browser visual inspection remains pending under the prior
  environment limitation; no new successful pixel inspection is asserted.
- Source comparison confirms byte preservation of the previously correct
  convolution/cross-spectrum, unequal-path transfer and Gaussian-coherence
  derivations. No new source passage, laboratory result or actual reader trial
  is claimed.

## Acceptance recommendation and remaining limitations

At correction delivery this was a candidate for provisional acceptance. The
owner has now authorized analytical teaching and workflow use under ADR-0005.
This is not demonstrated hardware calibration, physical validity, educational
validation or experimental confirmation; Codex grants no stronger acceptance.

Human review should specifically challenge finite-record/edge/update weighting,
fixture and state identifiability, achievable remaining 0.03-degree snapshot
uncertainty, passband/alias/linearity conditions, settling and thermal envelopes.
Unresolved physical inputs prevent any hardware adequacy/compliance recommendation.
Actual RF-engineer reader work and ordinary-browser visual inspection remain
pending. The correction record preceded the administrative closeout now
recorded above; no later chapter work is authorized by that closeout.

## Exact files modified by this correction pass

- book/relative-phase-stability.qmd
- engineering/src/coherent_receiver/relative_phase.py
- engineering/examples/relative_phase_pilot.py
- tests/test_relative_phase.py
- reviews/relative-phase-pilot.md
- docs/VALIDATION.md
- project/current-work.md
- project/pilots/relative-phase-stability.md
- references/source-notes/relative-phase-stability.md
- reviews/open-issues.md

---

# Original implementation record (historical; corrected above)

# Relative-phase pilot: check and review record

Date: 2026-10-29. Status: checked in the specific respects below; **human
technical acceptance pending**. Author/checker: Codex. No independent specialist,
actual reader participant, laboratory operator or approval is asserted. Artifacts
are the working-tree files delivered with this record; no commit was made.

## Intended use and concrete results

A bounded illustrative teaching/reference unit for experienced RF engineers.
Local conventions and physical envelopes are draft selections. Its predictions
are conditional, not device guarantees. Scope and canonical destinations are in
`project/pilots/relative-phase-stability.md`.

The two-sided 1–10000 Hz selected phase-noise variance is integrated explicitly.
Compact distribution: shared LO 0.00003999863189 rad² (0.362364 degrees standard
deviation), local reference-locked synthesis 0.0003999600008 rad² (1.145858
degrees). Exposed distribution: shared LO 0.003999863189 rad² (3.623641 degrees),
local synthesis 0.0003999600777 rad² (1.145858 degrees). The preference reversal
comes primarily from the declared additive distribution branch envelope. No
universal topology ranking or demonstrated hardware feasibility follows.

The illustrative 1.5-degree band limit admits both compact alternatives and
rejects the exposed shared-LO case. A per-branch noise allocation near
1.71e-8 rad²/Hz would restore its stochastic feasibility under the other stated
assumptions. Thermal examples at 1 GHz give 1.44 degrees for 2 ps/K over 2 K,
and 21.6 degrees for 30 ps/K. At the latter sensitivity and 0.02 K/s, a separate
0.5-degree drift allowance permits 2.315 s maximum calibration age, including
latency. Mitigation or sufficiently fast known-stimulus recalibration is needed;
blind correction can remove the wanted phase.

The corrected asymmetric synthetic fit recovers 0.3 rad at 1 GHz, 0.2979056 rad
at the 1000.1666667 MHz measurement mean, and 2 ns effective delay;
a held-out frequency is checked. The illustrative correlated uncertainty budget
gives 0.04858 degree standard uncertainty. Neither is a measured accuracy result.

## Executed checks

- `PYTHONPATH=engineering/src python3 -m unittest discover -s tests -p test_relative_phase.py -v`:
  **8 passed**. This dependency-free route was chosen after finding NumPy and
  pytest absent; no dependency installation or manifest change occurred.
- Complex covariance propagation versus explicitly constructed common and
  independent source coefficients, including complex cross-spectral ordering.
- Restricted equal-endpoint calculation versus pure-delay trigonometric identity
  and lowpass/equal-path limits; illustrative envelope preference reversal.
  This does not test all general endpoint/correlation cases.
- Spectral quadrature versus a time-domain exponential covariance with a
  three-time unequal-weight observation. 32768/65536-interval refinement and an
  analytical finite-tail bound control comparison error (2e-6 rad² quadrature
  allowance plus explicit tail bound).
- Shared-path allocation versus a closed-form cosine integral at 100 ns
  mismatch (absolute tolerance 2e-17 rad²); stable small-offset calculation at
  1 ps mismatch (relative agreement to 12 decimal places).
- Calibrated residual variance from four-time covariance versus expanded scalar
  expression; fixed correction preserves a wanted phase step whereas blind
  per-sample correction removes it.
- Gaussian process simulation: 12000 independent 20-sample records, 0.1 s sample
  interval, variance 0.25 rad², correlation time 0.2 s, seed 20261029. Expected
  accumulated power checked within five estimated Monte Carlo standard errors;
  mean complex amplitude and increment variance checked with declared absolute
  tolerances. Frozen-phase contrast has identical marginal variance but unity
  within-record accumulated power. These are synthetic ensemble checks.
- `PYTHONPATH=engineering/src python3 engineering/examples/relative_phase_pilot.py`:
  completed; table values above reproduced. Simpson refinements 4096/8192/16384
  intervals changed the final variance by at most 5.42e-20 rad² for the delivered
  cases. This numerical agreement does not bound model error.
- `python3 scripts/check_repo.py`: passed, 13 scaffold paths present.
- `git diff --check`: passed.
- Read-only protection audit: charter, competence inventory, accepted technical
  and book architecture packages, annotated contents and ADR-0002/0003/0004
  (11 files) byte-for-byte unchanged against initial HEAD.
- Quarto 1.10.18 HTML render: passed for all four pages with
  `XDG_CACHE_HOME=/tmp/relative-phase-quarto-cache quarto render book --to html`.
  First attempt without cache override failed on read-only cache creation.
- HTML inspection: four pages, 29 internal fragment references resolved; equation
  links/numbers, citation anchors, bibliography and navigation markup present;
  no unresolved `??` references. Both SVG assets parse as XML.

## Failures, corrections and inspection limits

Initial covariance checking used an imaginary-part tolerance relative to the
nearly cancelled output. That falsely rejected an endpoint computation. The
check now scales its tolerance to the sum of input-term magnitudes, and the
common-source calculation combines source coefficients before squaring. The
cross-spectral source-construction test remains an independent formulation.

`python3 -m pytest` could not execute: pytest is absent. NumPy is also absent,
so the existing NumPy-based pure-delay test file could not be run. Its source and
tests are unchanged. Eight new unittest checks passed; this is not a claim that
the full existing suite passed. Python is 3.12.3 on this environment.

Rendered HTML source and structure were inspected; browser pixel inspection was
attempted but did not complete. Firefox failed on unavailable display/snap runtime
access. Brave failed in the sandbox on crashpad socket permission; an escalated
local-file retry encountered resource/inotify errors and produced no screenshot.
MathJax uses the existing CDN default, so actual browser mathematical typesetting,
network availability and visual layout remain a publishing acceptance item. No
successful browser inspection or offline self-contained output is claimed.

## Authorial critical review (not specialist acceptance)

The derivations were reread against observable/operator, sign, dimensional,
stationarity, covariance and limiting-case requirements. Specifically checked:
phase at O2 relative to O1; subtraction of LO phase; complex cross-spectrum
ordering; two-sided integration factors; calibration-time covariance; distinction
between E[C], |E[C]|² and E|C|²; and wanted-signal retention. This is authorial
self-check, not an independent review event.

Physical concerns remain: first-order endpoint reference transfer may omit real
PLL peaking/spurs; output branch densities and independence require evidence;
thermal gradients/strain and electrical paths need characterization; real
finite-record filters do not implement an ideal band selector exactly; actual
calibration fixtures and test references can conceal nuisance changes. The
manuscript restricts conclusions accordingly. Parameter sensitivity and a
preference reversal demonstrate model dependence, not hardware validity.

## Architecture and authoring findings

- The pilot needed probability, observation, inference and uncertainty bridges
  adjacent to its first engineering calculation. Their existence here tests a
  possible reading route, but does not establish that Chapters 1–7 teach enough.
- Calibration reasoning crosses Chapters 13/20/23 and physical constraints cross
  15/22. The pilot's lookup route joins these responsibilities. A future learner
  trial must determine whether navigation fragments the engineering argument.
- Selected-band noise, calibration-age drift and combination performance need
  separate definitions and allocations. The refined standards explicitly require
  this; a single phase-RMS budget would hide necessary reasoning.
- No baseline responsibility is declared missing. Proposed improvement: preserve
  a continuous reference-design route with the source/operator/allocation and
  evidence consequences visible together. Do not rewrite accepted chapter
  boundaries until actual review/learner evidence supports a specific change.

## Pending human decisions and acceptance criteria

1. Mathematical/time-frequency reviewer: examine derivations, cross-spectrum
   conventions, finite-record weighting and nonstationary limits. Decide whether
   pilot-local conventions may become broader defaults. Drafting is not passage
   of the convention acceptance gate.
2. Receiver/reference engineer: assess whether endpoint envelopes and illustrative
   cases are useful and physically realizable; replace assumptions with evidence
   before any hardware recommendation. Review thermal, supply and state scope.
3. Calibration/metrology reviewer: challenge fixture freedoms, correction limits,
   test-reference correlation, uncertainty propagation and instrument selection.
4. RF-engineer learner trial: have an actual participant define the observable,
   reproduce a calculation from the text, reject a misleading conclusion, adapt
   topology/observation assumptions, and retrieve applicability conditions. Record
   assistance and critical errors. Revise and reassess if sign, correlation,
   identifiability or evidence reasoning fails. No actual trial has occurred.
5. Publishing review: inspect browser-rendered equations/figures on an ordinary
   working browser; HTML rendering alone does not complete this check.

For each review record real reviewer/date/artifact and bounded decision only
when provided. Mathematical correctness under assumptions, physical applicability,
educational usefulness, experimental confirmation and compliance are separate
acceptance questions. No physical measurements, experimental confirmation or
system compliance are delivered. Stop after this bounded pilot; subsequent
chapters/reference designs require a separate instruction.

## Delivered file inventory

Updated: `standards/technical-authoring.md`,
`standards/notation-and-conventions.md`, `standards/sources-and-evidence.md`,
`standards/verification-and-acceptance.md`, `templates/technical-unit.md`,
`project/pilots/relative-phase-stability.md`, `project/current-work.md`,
`book/publishing-pilot.qmd`, `book/index.qmd`, `book/_quarto.yml`,
`references/references.bib`, `docs/VALIDATION.md`, `reviews/open-issues.md`.

Created: `book/relative-phase-stability.qmd`,
`book/figures/relative-phase-reference-planes.svg`,
`book/figures/relative-phase-state-sequence.svg`,
`engineering/src/coherent_receiver/relative_phase.py`,
`engineering/examples/relative_phase_pilot.py`, `tests/test_relative_phase.py`,
`references/source-notes/relative-phase-stability.md`, and this review record.
HTML/build/cache outputs are ignored artifacts. Quarto-generated `book/.gitignore`
was removed because root ignore rules already cover the build paths. No accepted
planning document, dependency specification or original phase-transfer source
was changed. No commit, publication or external communication occurred.
