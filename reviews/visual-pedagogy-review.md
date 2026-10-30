# Visual-pedagogy execution record — 2026-10-30

## Boundary and baseline

Owner approved the complete initiative; K08–K10 and new canonical authoring remain suspended. Initial working tree clean; baseline HEAD `eb4be1141cded238090adcba957b167a4009ae64`. No commit authorization was given, so no new Git checkpoint was created. Manuscript and original assets remain unchanged.

## Audit and checks executed

Author read 44 technical sections, eight technical introductions and supporting reader-facing pages. Audit specifies 24 indispensable and four strongly beneficial interventions; these are proposed visual needs, not delivered figures. Source models are existing manuscript equations and synthetic examples; no new external source examination or empirical evidence is claimed.

Standard-library spot calculations confirmed lower/upper conversion 40/−26 degrees; mixed-average RMS .0160449368961 rad at N=100; unequal-delay gain .38196601125 at fΔτ=.1; source difference variance .0014 rad²; local delay SD 1.00658424209 ns; shared-draw correlation threshold .987741056097; nonlinear cosine SD .0277260534695 at σ=.2 rad; holdover .127323954474 s; maintenance drift bounds .45522/.46170 degree. These checks concern proposed models, not generated curves or physical validity.

`python3 scripts/check_repo.py` passed (13 paths); `git diff --check` passed. A fresh copy under `/tmp/coherent-visual-render` rendered successfully with `XDG_CACHE_HOME=/tmp/coherent-visual-quarto-cache quarto render /tmp/coherent-visual-render/book --to html`: eleven HTML pages. This does not establish rendered visual adequacy. No implementation changed; regression tests were not rerun.

## Actual-image inspection blocker

Brave inside the parent sandbox failed on crashpad socket permissions. Permitted executions outside the parent sandbox emitted inotify/resource errors (`Too many open files`). Bounded page, blank-page, single-process and virtual-time trials timed out without PNG output. Firefox failed on display/Qt initialization and read-only `/run/user/1000/snap.firefox`. No image was obtained or visually inspected; no standalone figure or HTML placement is visually verified. No browser/dependency installation or system-limit modification was performed.

This blocks illustration development under the owner's requirement to establish inspection before substantial production. No new figure assets or manuscript illustrations have been generated. The appropriate next step is restoring a functioning browser/image-inspection environment, then completing the approved batches; source parsing or invented screenshots cannot substitute.

## Separate-context AI review

Initial `codex exec` failed to initialize its in-process app-server with a read-only filesystem error; that invocation is not completed review. A permitted retry outside the parent sandbox requested `gpt-6.1-sol`, high effort, with `-s read-only`, fresh ephemeral context and an isolated supplied packet under `/tmp/coherent-visual-audit-review`. Exact runtime routing is not independently introspected. Requirements, manuscripts, original SVGs and audit specification were supplied without author conversation, current-work or prior review dispositions. Reviewer may encounter status material embedded in supplied accepted requirement documents; actual exposure is to be recorded in its findings.

Frozen packet SHA-256 values:

```text
47464ca685f0c5a320ee0da0a96620f2ac93ea19e07257c919dddf7580c49b1f  book/relative-phase-stability.qmd
abef312ffad1aa6f59044d74e0c0f357db1d65968ffc555346316a8d734983fd  book/index.qmd
e540970f92f539508a5d040798e532a5c10af5d7994bc3a63b38d7461e8d913a  book/tracking-signal-retention.qmd
716ef649ca7fb29cac3cba133f157c33c0049cff6ac9c2eaf922886e45c7c077  book/references.qmd
cc9689d7c8bd6bb5db3e2506608072a2aba0997821ec3b0a1ba52eec1fbd6012  book/phase-delay-inference.qmd
0c23d1984084eb9c97fa06bfbdad36e15aafb920ea2a3159ebb9773754274c53  book/model-adequacy-uncertainty.qmd
1370c77f06f9a2a55153a351d662097ae50e27e84ad013706ddaa1991ea99937  book/scalar-stochastic-phase.qmd
fbb0846f017ffa00ba460c9b218eace59407f6bed024d4ce6f85811a92710b1f  book/publishing-pilot.qmd
1ec0b1f401846a47e784dc928de37c694686cb7e5dddeb8cbe83d861089683d0  book/phase-comparison.qmd
10798a3756a0e1f71bfff99d9513944019ab19eb7b2f28211cdf12a0f186f168  book/observation-weighted-coherence.qmd
5caf8f2ae043e80ad63e2aea91cdaa3710cf8c1ccf9f415e0a51575f58a6d502  book/covariance-quadratic-forms.qmd
4f57255a213cc7dd7be97948c4b44c27e11193d080da20cca3ce9209239e2f28  book/figures/relative-phase-state-sequence.svg
cb78b44d7b15669d739e944faa711f29a5dcc2371f377adffaf297e7852178a8  book/figures/relative-phase-reference-planes.svg
f542ca24ac86a858a2f3afa547bd86687f6fddd111ac56c59d7a12cbcb205fa2  standards/verification-and-acceptance.md
fcaef573dfa9969d9e02a1402366ae31613dd60405dfdd982269123fadadbd34  standards/technical-authoring.md
7bd1f76293f2d8a04d37151b31af410ddd3304617d483c19035bcbb67cce3918  standards/sources-and-evidence.md
4f5ee34533463abc134682a7535c3bd5bf1b80a2260d57a1f87b7db07d886200  standards/notation-and-conventions.md
e985bf9b74aef6aa26fc3b95403c11cae82dd083c4b8124c93def55ee7351aa6  project/charter.md
415038cf9053caaceb4d04ec3436c2eb9eff10b80647c3e86557b23131c92027  project/competence-inventory.md
9441c0715abdab2c7da078ee8729dc18c6501bf6b6916356d69fbd4952d5cdcb  project/annotated-toc.md
f4b92d033d473dd3146a86dbf7cd68e6a6f14b2b02c6ccf3c71cd9caece67027  project/book-architecture.md
13486c7ce6600ca82a203c25386a2f7910f66216ffe6754ee7d934f997836580  project/technical-coverage.md
c31215973ec7a7745d32260fb47748cbb07907528620757b37d7212427e2cadf  reviews/visual-pedagogy-audit.md
```

The reviewed audit snapshot precedes the appended proposed-guidance paragraph; its specification/ledger bytes are preserved in the frozen packet. Reviewer findings and author dispositions follow separately when available. This is audit review, not completed visual-remediation review or human acceptance.

## Independent reviewer findings (verbatim response)

The proposal needs revision before it is a complete visual specification. Its numerical examples are largely sound, and its section ledger is useful, but assigning a figure ID to every section does not establish that the section’s teaching needs are covered.

I independently read every substantive section of the eight technical manuscript pages, plus the preface, publishing demonstration and references page. The findings below concern the existing manuscript and proposed specifications; they do not establish rendered or educational adequacy.

1. **High priority — Missing visual treatment of complex filtering and AM-to-PM conversion.**  
   The audit maps “Which statistic did the requirement mean?” to V09/V10 ([audit:53](/tmp/coherent-visual-audit-review/reviews/visual-pedagogy-audit.md:53)), but those specifications cover extracted-phase weighting and coherence. They omit the consequential bridge in [the pilot:174](/tmp/coherent-visual-audit-review/book/relative-phase-stability.qmd:174): filtering complex samples before extracting phase can mix amplitude perturbations into phase.

   **Required correction:** Extend the specification with the chain “complex signal → filter → angle,” contrasted with “angle → phase filter.” Show the normalized filter’s real and imaginary impulse responses feeding phase and amplitude perturbations respectively, including \(H_0\ne0\) and the small-perturbation conditions. Include an AM-only counterexample producing output phase. This directly supports the authoring requirement to preserve observation operators and prevents an engineer from applying \(|H|^2S_\phi\) to an unjustified signal-domain filter.

2. **High priority — V10 does not explicitly specify all the quantities it promises to distinguish.**  
   [V10:151](/tmp/coherent-visual-audit-review/reviews/visual-pedagogy-audit.md:151) promises to separate phase-average uncertainty, \(E|C|^2\), and \(|E C|^2\). Its numerical check instead pairs coherent power with \(\exp[-\operatorname{var}(\bar\phi)]\), without explicitly requiring the actual \(|E C|^2\) curve.

   For the declared stationary Gaussian model, \(\sigma=1\) rad and \(T/t_c=10\), I obtain:

   | Quantity | Value |
   |---|---:|
   | \(\operatorname{var}(\bar\phi)\) | \(0.180000908\ \mathrm{rad^2}\) |
   | \(E|C|^2\) | \(0.456410128\) |
   | \(|E C|^2=e^{-1}\) | \(0.367879441\) |
   | \(\exp[-\operatorname{var}(\bar\phi)]\) | \(0.835269453\) |

   **Required correction:** Name and specify each curve explicitly. Label the last quantity as the rejected substitution for coherent-integration power. Separate phase RMS and dimensionless power into clearly distinguished panels or axes. Preserve the frozen-phase counterexample and the signed Gaussian/two-point coherence comparison.

3. **High priority — V24 covers the apparatus but misses the pilot’s calibration interpretation.**  
   [V24:277](/tmp/coherent-visual-audit-review/reviews/visual-pedagogy-audit.md:277) specifies the comb arrangement and acquisition chain. It does not specify a visual for the asymmetric fit’s two intercept references or for the delay left after scalar correction, both developed in [the pilot:386](/tmp/coherent-visual-audit-review/book/relative-phase-stability.qmd:386).

   **Required correction:** Add a pilot-specific fit panel showing training tones, the excluded held-out tone, \(f_0=1000\) MHz, and \(\bar f=1000.166667\) MHz. Mark \(b_0=0.3\) rad separately from \(b_{\rm mean}=0.297905605\) rad. Show that subtracting the carrier-phase coefficient leaves the 2 ns slope: residual phases are approximately \(+0.0125664\) rad at 999 MHz and \(-0.0188496\) rad at 1001.5 MHz. Cross-reference V15/V16 for general fitting and ambiguity rather than duplicating them.

4. **Medium priority — The probability-to-process bridge remains too dependent on formulas and summary curves.**  
   V05/V06/V12 ([audit:104](/tmp/coherent-visual-audit-review/reviews/visual-pedagogy-audit.md:104)) propose densities and estimator-performance curves, but no explicit representation connects repetitions, individual records and temporal covariance. That connection is central to [the scalar chapter:58](/tmp/coherent-visual-audit-review/book/scalar-stochastic-phase.qmd:58), particularly the stationary but nonergodic random-constant example.

   **Required correction:** Add paired illustrative records across several repetitions for independent and record-constant errors, with equal ensemble marginal variance. Identify record means and ensemble means separately, then connect them to the covariance sums and V06 curves. Label the traces synthetic illustrations, not evidence of stationarity or ergodicity. Specify the AR(1) parameters used in V12; include positive and negative correlation so the different behavior of mean and variance estimators is visible.

5. **Medium priority — Stationary-model boundaries lack a visual disposition.**  
   V09–V12 predominantly visualize stationary models. The ledger does not identify how readers will distinguish the exponential-covariance model from random-walk phase, although [the pilot:223](/tmp/coherent-visual-audit-review/book/relative-phase-stability.qmd:223) and [the observation chapter:182](/tmp/coherent-visual-audit-review/book/observation-weighted-coherence.qmd:182) make that boundary consequential.

   **Required correction:** Specify a bounded comparison of exponential-covariance and random-walk increment variance versus lag. Show saturation for the former and growth for the latter, while stating that random-walk absolute variance depends on epoch. Connect the stationary example’s covariance to its Lorentzian PSD. Do not suggest that an arbitrary low-frequency cutoff makes the stationary absolute-variance formulas applicable.

6. **Medium priority — Failed validity checks need an explicit visual route.**  
   The existing state SVG source contains a forward sequence and a textual invalidation instruction. [The audit:323](/tmp/coherent-visual-audit-review/reviews/visual-pedagogy-audit.md:323) leaves a return/gate path as something to “consider.” V22’s phase-line, holdover and latency panels do not replace a recovery/validity diagram.

   **Required correction:** Require explicit invalid-data states or gates for failed settling/checks, amplitude loss, reference loss, changed state and expired calibration. Show the conditions required before returning to use. Distinguish held-out fit checking from the differently referenced measurement needed to challenge acquisition/instrument error. This is a source-level specification finding; arrow placement and legibility remain uninspected.

7. **Medium priority — V13 needs to distinguish covariance projections from ellipse intersections.**  
   [V13:178](/tmp/coherent-visual-audit-review/reviews/visual-pedagogy-audit.md:178) combines a covariance ellipse with difference and quiet-weight directions. Without a projection construction, readers could interpret a radial ellipse intersection as the variance of \(w^Tx\).

   **Required correction:** Show that the projected half-width of the unit covariance ellipse is \(\sqrt{w^TCw}\). Label coefficient-vector normalization: \((-1,1)\) and \((-2,1)\) have different norms and define different observables. Draw the rank-one case as a degenerate line using its source construction; \(C^{-1}\) is undefined there. Retain the explicit warning that the ellipse is not automatically a probability region.

8. **Medium priority — V21’s “feasible region” needs a narrower label.**  
   [V21:250](/tmp/coherent-visual-audit-review/reviews/visual-pedagogy-audit.md:250) supplies an RMS-error target but no quantitative wanted-signal retention requirement. Its shading therefore cannot establish joint sensing feasibility.

   **Required correction:** Label the region “meets the illustrative true-residual RMS criterion.” Under the supplied model, its corner-frequency boundaries are approximately 28.27–134.33 Hz. State separately that wanted-signal adequacy remains unresolved without a retention requirement. The 100 Hz example passes the RMS criterion while retaining only about 0.01 of a 1 Hz wanted phase amplitude at the residual output.

9. **Demonstrated, localized manuscript error — The pilot’s phase equation loses quadrant information.**  
   [Pilot:80](/tmp/coherent-visual-audit-review/book/relative-phase-stability.qmd:80) writes
   \(\arg(A+n')=\arctan[\operatorname{Im}n'/(A+\operatorname{Re}n')]\)
   without a quadrant restriction. For \(n'=-2A\), the nonzero result has phase \(\pi\), while the displayed arctangent gives zero.

   **Required correction:** Use `atan2(Im n′, A + Re n′)`, consistent with V08 and [the scalar chapter:132](/tmp/coherent-visual-audit-review/book/scalar-stochastic-phase.qmd:132), and mark the zero-amplitude case undefined. Alternatively, explicitly restrict the arctangent equality to the positive-real-half-plane neighborhood used for linearization. This defect does not overturn the checked small-noise budgets.

The priorities also need refinement. V05’s conditioning/ensemble bridge and V12’s estimator uncertainty deserve earlier development than their “strongly beneficial” labels suggest. Conversely, V19’s numerical-cancellation plot is useful but can follow the prerequisite visual sequence. Optional improvements include an improper-noise ellipse in V07 connected to V08’s orientation-dependent phase variance, and explicit source/branch injection nodes in V23 showing that the local synthesizer’s output disturbance is added after its reference transfer.

Independent standard-library calculations reproduced the main proposed values: covariance quadratic forms and eigenvalues; delay precision and ambiguity; the correlation threshold \(0.987741\); nonlinear uncertainty; tracking noise/bias tradeoffs; holdover and latency boundaries; architecture reversal; snapshot uncertainties; cadence and downtime. Coherent-power, noise and snapshot integrals were checked with refined quadrature. The exponential-model phase-average variance also agreed between time and spectral calculations with a bounded spectral tail. These checks support the encoded mathematics, not hardware applicability.

All 23 supplied manifest hashes matched. The initial `python` invocation failed because that executable was unavailable; calculations succeeded with `python3` using only standard libraries.

Both original SVG files were submitted directly to the image-inspection tool; both failed as unsupported image data. Their XML source was examined, but their rendered appearance and HTML integration remain **uninspected**. No proposed figures were generated. External citations, omitted supporting code and publishing configuration were not examined.

Incidental exposure was limited to status, prior-review and disposition statements embedded in the supplied documents. I did not follow their links or use those statements as evidence of adequacy. No excluded repository/history material was opened, and no files were edited, agents delegated or connectors used. This AI review grants no human acceptance.

## Author dispositions and remaining work

All nine required findings are accepted. The audit amendment section specifies the added panels, corrected distinctions, explicit model parameters and revised priorities. The pilot atan2 correction was made narrowly; all other manuscript mathematics and figures remain unchanged. At A=1, n′=−2, atan2(0,−1)=π while arctan(0/−1)=0; at zero output phase is undefined. No independent correction reassessment has yet occurred. Reviewer findings do not clear the visual or audit gate.

The fresh review completed successfully (exit 0), requested model/effort and read-only settings as above. Existing SVG image-tool access failed; numerical calculations and XML reading are not visual verification. No final human Reviewed/Accepted status is granted. Browser inspection remains the execution blocker. No figures produced, no commits, no final visual-adequacy recommendation in favor of continuation.


## Independent atan2 correction reassessment — 2026-10-30

Fresh ephemeral context `01a18bdf-e8ad-7600-968d-ab4ce18c5ac6` requested
GPT-6.1 Sol / high with an explicit `-s read-only` shell; launch was scoped
outside the parent sandbox for CLI initialization. No conversation, previous
findings/dispositions or current-work were supplied. Seven frozen inputs matched.
[Raw reviewer findings](visual-inspection-evidence/atan2-findings.md),
[input hashes](visual-inspection-evidence/atan2-inputs.sha256) and
[prompt](visual-inspection-evidence/atan2-prompt.txt) are preserved separately.

Reviewer concluded no mathematical defect in the corrected exact equality or
local linearization within its small-perturbation scope, and no resulting
downstream correction. Quadrant, branch, zero amplitude, rare-excursion, asymmetric
channel and numerical-budget checks were reported. Principal-angle subtraction
needs wrapping; small RMS alone does not ensure negligible excursions. Pilot
self-containment could improve by explicitly repeating A>0/principal-error wording;
reviewer classified that as an optional clarification, not a demonstrated error.
No prohibited exposure was identified. Exact backend routing was not independently
verified. No pixel inspection, external-source examination or physical validation
was performed by this mathematics reviewer.

Author disposition: accept the bounded reassessment; retain the corrected
manuscript bytes unchanged (`9d1018b4cd95cc844d93d8a6c60b60f6a6be5b909de8746cade323f9ad022e05`).
No consequence requires broadening conventions or authoring now. This closes the
pending mathematical correction reassessment only. The amended audit specifications
and visual-remediation acceptance remain separate and incomplete; no human
Reviewed/Accepted status is granted.


## Resumed implementation — Chapters 1–3

Owner accepted the amended audit as the implementation baseline. Existing
environment-repair files and atan2 correction/reassessment were reconciled and
preserved. Baseline working tree had three modified tracked files plus the
inspection/audit/evidence files; no staged entries or new commits. HEAD remains
`eb4be1141cded238090adcba957b167a4009ae64`. Initial hashes are captured in
`/tmp/coherent-resume-baseline.json`; final preservation checks will distinguish
this initiative's edits from the externally supplied changes.

Current-session smoke: sandbox preflight exit 2 (SO_PASSCRED denied, no browser
launch); scoped host private-pipe capture exit 0, 1.369 s, 1000×700 pixels. Author
actually viewed the heading, blue circle and Radius 60 px label without clipping.
Fresh read-only reviewer examined the attached PNG successfully; its manifest
discovery was unavailable, so reviewer hash verification is not claimed for this
capability test. [Raw smoke findings](visual-pedagogy-evidence/resume-smoke-findings.md).

Seventeen generated SVGs implement V01–V12 and the amended operator/process
requirements; multiple panels/interpretive cross-references consolidate needs.
All models and synthetic parameters are in
`engineering/examples/visual_foundations.py`. Five independent mathematical
checks plus the prior 43 standard-library checks pass (48 total). SVG regeneration
is byte-identical. Actual author standalone pixels and complete chapter captures
with overlapping readable crops were inspected; typeset equations, captions,
labels and bottom navigation are visible. Initial page dimensions were
1425×10254, 1425×7617, 1425×9430 at viewport 1440×2200.

### Initial independent findings

[Unedited findings](visual-pedagogy-evidence/g1-initial-findings.md),
[frozen hashes](visual-pedagogy-evidence/g1-initial-inputs.sha256),
[prompt](visual-pedagogy-evidence/g1-initial-prompt.txt). Fresh ephemeral CLI
requested GPT-6.1 Sol/high and `-s read-only`, with 17 standalone and three
complete-page PNG attachments. Exit 0. Reviewer verified all 145 hashes and
reports inspection of all 17 figures, three page overviews and 29 crops. It
independently reproduced conversion signs, delay shifts, covariance sums,
coherent-power/time-spectrum relationships and AR(1) estimator uncertainty.
`python`/NumPy failed; standard-library Python3/Pillow checks succeeded. Source
notes exposed historical examination claims, which were not used as independent
evidence; no excluded repository/history access was reported. No external source
re-examination, hardware evidence or human acceptance is claimed.

### Author dispositions

Both consequential findings accepted: legend/axis clearance increased across
plots; local fractional-AM model and filtered-output smallness condition supplied
in prose and figure. The high-gain counterexample demonstrates why small inputs
alone are insufficient. Optional common covariance normalization, noise-resultant
label and coincident AR(1) annotation were added. Optional general mathematical
copyediting/log-tick refinements remain outside the indispensable corrections.
Existing derivations were preserved. Independent reassessment is running on a
new frozen packet and actual corrected images; no group closeout is yet claimed.

Two corrected captures initially failed because their private Unix-socket paths
were too long; the same documented route succeeded with shorter `/tmp/vg1-*`
paths. No browser flags, system settings or inspection helper were changed.

### Correction reassessments and group boundary

[First reassessment](visual-pedagogy-evidence/g1-reassessment-findings.md)
verified 134 frozen entries and all 17 figures/three pages/18 crops. It identified
filtered input-remainder control and stacked-panel spacing as remaining issues.
Both were corrected: the exact AM/PM model, elementary remainder bound and
convolution-norm conditions now make finite use explicit; two three-panel figures
have increased separation. No empirical or hardware claim was introduced.

[Focused final findings](visual-pedagogy-evidence/g1-final-findings.md),
[input hashes](visual-pedagogy-evidence/g1-final-inputs.sha256),
[prompt](visual-pedagogy-evidence/g1-final-prompt.txt) record a new fresh read-only
GPT-6.1 Sol/high request, exit 0, 30 matched entries, three corrected figures,
two complete-page images and twelve readable crops. Reviewer analytically verified
the remainder inequality and independently tested a different high-gain filter;
no consequential scientific defect remained, and spacing was separated/readable.
It proposed an optional explicit total phase-error bound. Author accepts the
reassessment; optional notation, integer/log ticks and footer polish remain
documented. Full rendered HTML/assets corresponding to this focused packet were
frozen separately at `/tmp/v1-final-rendered-snapshot`; the focused reviewer
examined manuscript/PNG mathematics, not those HTML source files. Initial and
first correction review packets did include rendered HTML/assets.

An initial focused launch failed on model capacity and was retried with the same
requested model/effort/read-only settings; the failed launch is not review.
Author inspected final standalone pixels and changed page regions; representative
960-pixel viewport captures were also inspected. Normal full-page coverage is
recorded above; no complete mobile/responsive or offline-math claim is made.

Chapters 1–3 close as checked provisional visual drafts within their declared
models, with optional polish and human acceptance pending. Proceed to the
authorized Chapters 4–6 group; K08–K10 remain suspended.


## Chapters 4–6 implementation; independent review incomplete

Eight SVGs implement V13–V19: shared/local source paths, covariance support
projections and rank-one geometry, inverse conditioning, frequency-span precision,
wrapped delay branches, correlation/coupling sensitivity, nonlinear uncertainty
and numerical cancellation. Prose introductions, interpretation, captions and
meaningful alt text are integrated without changing pre-existing display
derivations. Generator and synthetic inputs remain in the existing engineering
examples directory. Four additional mathematical checks pass (nine new checks,
33 foundation/visual standard-library checks plus 19 pilot checks: 52 total).
Independent formulations include finite-source covariance, ellipse-support extrema,
phasor alias equality and Gaussian density quadrature. Numerical curves use
65-digit Decimal comparisons with declared binary64 evaluation and omitted
out-of-range errors, not invented numerical floors.

Author inspected all eight standalone PNGs, all three complete-page overviews
and fourteen overlapping readable main-column crops. A full-width supplemental
view confirmed the matrix equation/units extending beyond the main-column crop.
Normal page dimensions at viewport 1440×2200: Chapter 4 1425×6603, Chapter 5
1425×5920, Chapter 6 1425×7529. Author also inspected representative narrower
960×1800 captures: output dimensions 945×7017, 945×6290 and 945×8109. This is
not exhaustive mobile/responsive or assistive-technology testing. Rendered equations,
figures, captions and final navigation were visible. Native SVG captures preserve
equal-scale covariance geometry. Author corrected initial title/annotation overlaps
before freezing the review packet.

[Incomplete reviewer event log](visual-pedagogy-evidence/g2-incomplete-review-events.jsonl),
[input manifest](visual-pedagogy-evidence/g2-inputs.sha256),
[prompt](visual-pedagogy-evidence/g2-prompt.txt),
[viewed captures](visual-pedagogy-evidence/g2-captures/captures.sha256).
The frozen packet `/tmp/v2-review` includes manuscript, model/provenance notes,
source SVGs, actual PNGs, rendered HTML/assets, accepted requirements and code.
The fresh launch requested GPT-6.1 Sol/high with `-s read-only`, eight figure and
three complete-page image attachments, and no author history/prior dispositions.
It exited 1 after the provider reported: “You’ve hit your usage limit.” No final
review report was returned. Partial calculations in the event log are additional
mathematical evidence, **not a completed technical/pedagogical or image review**.
No reviewer coverage/acceptance verdict is inferred. No model substitution,
native-subagent replacement or relaxation of the read-only/image gate was used.

### Boundary and next operation

Restart a **fresh** reviewer on the frozen current group once reviewer-account
capacity is restored; do not resume/fork the incomplete context. Reconcile any
source changes against the supplied hashes, correct consequential findings and
reassess before Chapter 7/state-diagram development. The following pilot group,
connected review and final visual-adequacy recommendation remain outstanding.
V20–V28 and the mandatory existing-state-diagram remediation have not started.
The three original-figure HTML alt-text omissions and old reference-plane label
defects remain for those scheduled groups. No K08–K10, owner acceptance, physical
validation or completed initiative is claimed.

### Repository/check closeout at the quota boundary

Python 3.12.3 and Quarto 1.10.18 observed. All 52 available selected standard-library
checks, scaffold integrity and whitespace checks pass; pytest remains absent, so
the full pytest suite was not run. Regenerating both implemented groups preserves
all 27 SVG bytes (25 new, two unchanged originals). Successful capture source
hashes match current SVG/HTML bytes. All pre-existing display-math blocks remain
identical to HEAD. The pilot, including its previously reassessed atan2 correction,
and all 106 externally supplied inspection files are byte-preserved from resume.
No staging, commit, push, installation, publishing or host-policy/resource change
was performed. Baseline HEAD remains `eb4be1141cded238090adcba957b167a4009ae64`.
Provisional visual-authoring and verification guidance/template additions are
implemented, but whole-initiative lessons/acceptance remain pending completion.


## Chapters 4–6 review completed on the replacement computer (2026-10-30)

Resume baseline was clean HEAD `2d2e4df`; the owner's prior checkpoint already
contains the visual production and historical records. Chapters 1–3 remain closed
as checked provisional visual drafts. The original `/tmp/v2-review` packet was
absent. Reconstruction matched 88/110 original entries, including all three
manuscripts, eight SVGs, eight figure PNGs, three full-page PNGs, code, source
notes and requirement files. Original crops were recreated from preserved PNGs;
fresh HTML/CSS was explicitly distinguished from old screenshot bytes. Seventeen
entries differ and five original files remain absent (three old command.txt and
two CSS paths). The original manifest and historical incomplete invocation were
not altered. [Reconciliation](visual-pedagogy-evidence/g2-resume-reconciliation.json),
[reconstructed input hashes](visual-pedagogy-evidence/g2-resume-inputs.sha256),
[archived packet](visual-pedagogy-evidence/g2-resume-packet.tar.gz).

Fresh GPT-6.1 Sol/high/read-only review returned final findings with exit 0:
[findings](visual-pedagogy-evidence/g2-resume-findings.md),
[prompt](visual-pedagogy-evidence/g2-resume-prompt.txt),
[invocation](visual-pedagogy-evidence/g2-resume-invocation.json),
[event provenance](visual-pedagogy-evidence/g2-resume-events.jsonl).
All 108 current inputs matched. Reviewer inspected all eight figures, three full
pages and fourteen readable crops and independently reproduced their consequential
values and limits. No consequential scientific/graphical defect was found. It
required inline-math typesetting and a derivation connecting covariance geometry
to projected observable width. Source-note history was incidentally visible and
was not adopted as correctness evidence. One truncated image transfer was
recovered by actual direct PNG viewing. No coverage is inferred from that failure.

Author accepted both findings. All seventeen original display-math blocks are
byte-preserved. Inline expressions in Chapters 4–6 now use mathematical markup.
Chapter 4 derives mapped-unit-ball support using Cauchy–Schwarz, the maximizing
point, coefficient-norm scaling, the distinct radial distance, and singular/null
limits. No SVG required modification or regeneration for these corrections.
[Focused checks](visual-pedagogy-evidence/g2-correction-checks.json).

The replacement computer initially lacked Node and uses a different Brave path.
After the owner made Node available, executable `/usr/bin/node` v26.12.1 and
`/usr/bin/brave` 156.1.98.62 were observed. Ordinary sandbox SO_PASSCRED fails;
scoped host capture succeeds using the unchanged private-pipe helper and retained
browser sandbox. Inotify allocation succeeds at the already configured limit
1024; no host settings were changed. Smoke author pixels show the heading,
text, blue circle and radius label at 1000×700. [Environment/check records](visual-pedagogy-evidence/resume-environment/).
No package was installed by the author. Initial failure evidence is retained.

Corrected full-page captures are Chapter 4 1425×7458, Chapter 5 1425×6045 and
Chapter 6 1425×7721 at viewport 1440×2200. Author inspected actual complete-page
PNGs and all fourteen overlapping full-width strips through bottom navigation;
all mathematical content is typeset and figures/captions are visible. Fresh
separate correction review also inspected these pixels, unchanged figure PNGs
and smoke PNG, verified all 111 hashes and independently rederived/checked the
geometry and dependent examples. [Reassessment](visual-pedagogy-evidence/g2-correction-findings.md),
[prompt](visual-pedagogy-evidence/g2-correction-prompt.txt),
[hashes](visual-pedagogy-evidence/g2-correction-inputs.sha256),
[invocation](visual-pedagogy-evidence/g2-correction-invocation.json),
[events](visual-pedagogy-evidence/g2-correction-events.jsonl),
[archived current packet](visual-pedagogy-evidence/g2-correction-packet.tar.gz).
No consequential error or unreadable content remained. Optional inline line-break
polish, broad matrix display, log-axis annotation and radial-direction overlay
remain documented. Author accepts the bounded reassessment; no human acceptance,
hardware applicability, reader effectiveness, PDF or exhaustive responsive check
is claimed. Requested model/effort are recorded; backend routing is not separately
introspected. Reviewer IDs: {"g2-resume": "01a18d63-95f3-7df1-a7c5-7b78e9c0c734", "g2-correction": "01a18d6b-8f64-72f1-8d86-5bc21ddfe6a5"}.

All 52 available selected tests pass; scaffold integrity passes; pytest is absent.
An initial pilot unittest import needed the documented engineering/src path and
passed after correction. Both generator groups reproduce all 25 generated SVG
bytes in scratch storage; the two other existing SVGs remain unchanged. Eleven
HTML pages render with Quarto 1.10.19/Python 3.14.7. Fresh render success alone
was not used to clear the image gate. Chapters 4–6 close as checked provisional
visual drafts. Proceed only to the approved Chapter 7/state group, then pilot
and connections; K08–K10 remain suspended.
