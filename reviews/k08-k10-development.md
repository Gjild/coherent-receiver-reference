# K08–K10 bounded development — 2026-10-30

Managing-author record; AI findings remain in separately preserved outputs.
Owner authorized the three sequential units, connected assessment and safe local
checkpoints. No human technical review, physical confirmation or reader trial is
claimed. Accepted architecture, local conventions and ADR-0007 limits remain.

## Batch-start visual gate

Executed before authoring: ordinary sandbox preflight denied SO_PASSCRED (exit 2,
no capture); first scoped host invocation failed (exit 1) because the repository
output path exceeded Chromium's Unix socket length. The unchanged pipe helper
with short `/tmp/k0810-smoke` succeeded (exit 0). Node `/usr/bin/node` v26.12.1,
Brave `/usr/bin/brave` 156.1.98.62; browser sandbox retained. No installation,
resource/security change or capture redesign. Actual 1000×700 PNG opened: heading,
text, blue circle and “Radius 60 px” label readable without clipping.
Image SHA-256 `f28084e8baa85aa543e7179f6009083610ffed7a4c8e2a722769dbb96e9ac565`.
[Durable smoke pixels](k08-k10-evidence/smoke-image.png) and adjacent metadata.

## K08 / Chapter 8 — field-to-port and sensing bridge

Engineering question: what does matched electronic injection establish about
actual received relative phase? Outcomes: signed geometry/Doppler calculation,
polarization/basis-aware receiving and loaded-network model, derived scalar
condition, diagnosis of injection-blind external paths and physical ambiguity.
Manuscript: [fields, geometry and transduction](../book/fields-geometry-transduction.qmd).
Three indispensable figures: geometry/transduction/electronic planes; quantitative
polarization phase versus amplitude; physical range/index/reference paths.
Reproducible with `python3 engineering/examples/physical_models.py 8` using the
existing SVG language. A separate Doppler plot would repeat the signed path
derivative without resolving another misconception; the geometry figure supports it.

Consequential local results: sourceward geometry gives −0.250 ns/+90° in the
synthetic pair; quadrature cross-polar leakage gives 5.7106° added phase but
0.043214 dB amplitude-ratio error, limiting the illustrative 2° envelope to
±19.2496°. Curvature is 0.02356 rad at the stated 10 m range, not a complete
electromagnetic far-field test. Range and refractive-index changes can have
identical phase, with 15 mm round-trip vacuum ambiguity at 10 GHz. Real-leakage,
multipath and one-way/independent-reference exercises change the model.

[Claim-level source note](../references/source-notes/fields-geometry-transduction.md)
records actual Hum passage access and the unimported conjugation ambiguity.
No measured manifold, sensor/material coefficient or hardware performance supplied.

### Separate AI review and author dispositions

Every invocation was a new `codex exec --ephemeral`, requested `gpt-6.1-sol` /
`high`, explicit `-s read-only`, isolated frozen packet and actual PNG attachments;
no author-conversation fork. Hash manifests identify input bytes. Model routing
was not independently verified. Initial and final reviewers reported no excluded-state exposure; the intermediate
reviewer exposure is disclosed below.

- Initial session `01a18e0b-deae-76a2-993d-0a20b404f75c`, exit 0.
  [Raw findings](k08-k10-evidence/k8-findings.md): independent geometry, complex
  basis, asymmetric loaded-network, powers/phase and graphical-vertex checks agree.
  Actual smoke, three assets, complete page and five crops examined. Found medium
  versus vacuum speed ambiguity, missing conversion-orientation condition, wrong
  “all in ohms” prose, undefined sensing amplitude, asserted scalar condition and
  next-page mismatch. Author corrected speed to local v/c0, qualified normalized
  complex-linear G, corrected units/defined A, derived proportionality and described
  the physical-noise continuation as later planned material until integration.
- Intermediate session `01a18e11-a573-7d33-8da8-8cdedd16f76f`, exit 0: input was frozen before an author-detected raw-TeX
  delimiter error in the added proof was corrected; it remains historical evidence,
  not the final visual gate. [Intermediate findings](k08-k10-evidence/k8b-findings.md)
  identify that rendering and an early next-chapter phrase, both corrected in final
  inputs. Reviewer reported inadvertent acceptance/disposition-metadata exposure
  in the supplied accepted TOC/preface; no linked dispositions/current-work/author
  history were opened. It is not relied on as unexposed final review. Actual
  corrected pixels exposed the error. Original
  and intermediate inputs/findings remain separate from author dispositions.
- Final targeted session `01a18e12-aab0-7eb1-bdc5-62967112af85`, exit 0.
  [Raw reassessment](k08-k10-evidence/k8c-findings.md) examines actual full page and
  all five readable crops, independently checks nonvacuum n=1.5 and concludes no
  consequential defect in its target scope. Scalar identity is visibly typeset;
  G orientation/units and future wording are consistent. Degenerate zero-reference
  qualification is implicit in the stated nonzero-reference condition. No new
  calculation or field claim depends on optional expansion of that discussion.

### Checks and bounded closeout

Four new independent checks: exact spherical versus plane geometry and phase
derivative; loaded complex voltage/power and rotated basis; SVG curve coordinates
against complex voltages; sensing linearization/ambiguity. All pass. Available
regressions: 42 standard-library tests plus 19 pilot tests pass. Full pytest cannot
start: module absent; no installation. All three SVGs reproduce byte for byte.
Repository integrity and whitespace pass; final 12-page Quarto HTML build passes;
333 local links/fragments and 41 image uses check with no errors/missing alt text.
Final actual page is 1425×8064, viewport 1440×2200; full image and overlapping
readable crops cover every paragraph through bottom navigation, with visible
typeset math. Both changed asset PNGs were re-inspected. [Author observations and
checks](k08-k10-evidence/k8-author-observations.json) distinguish intermediate and
final captures. Existing Chapters 1–7 and pilot manuscript/figure bytes preserved.

K08 closes as a checked provisional bounded treatment, not a complete Chapter 8
or specialist-validated result. Remaining limits: no physical antenna/sensor
characterization, reader evaluation, broader responsive/assistive assessment,
PDF/offline math or human technical acceptance. Final batch integration must
verify actual Chapter 8→9→10 navigation, prerequisite/notation continuity and
canonical ownership. No scope or book-wide-convention intervention identified.

K08 checkpoint: `a29d739`. A later local wording clarification explicitly repeats
the already used rounded vacuum speed in both examples; final batch integration
will reassess those paragraphs. Numerical values and curves are unchanged.

## K09 / Chapter 9 — physical disturbance sources and paths

[Manuscript](../book/physical-disturbance-paths.qmd) asks which source and path
explain changed receiver noise, and derives delivered thermal power, active
voltage/current/shot models with conditions, physical coupled covariance,
reciprocal mixing and complete-waveform timing. Three figures show actual
resistive connectivity, spectral overlap/filter placement, and analog-slope versus
clock-dependent in-band error. Reproduce with `physical_models.py 9`.
A separate general covariance diagram would duplicate Chapter 4; the new circuit
makes its physical inputs concrete. No arbitrary covariance or device values are
used as physical evidence. [Source note](../references/source-notes/physical-disturbance-paths.md)
records fresh MT-047/MT-007/ADI mixer prose examination and translation limits.

Key synthetic results: matched 290 K/100 kHz noise is −123.9752 dBm; loaded
source covariance yields a 34.375% differential-noise overestimate if correlations
are ignored. Cooling the common source changes the cross term's sign without
changing impedance. A finite blocker produces 2.5 times the centre-tone
reciprocal noise (3.9794 dB error), requiring 8.9794 dB extra attenuation against
the supplied limit. An independent internal LO branch can prevent source-only
improvement. The complete two-tone waveform gives 0.4443 mV total raw timing
error instead of 0.4443 µV wanted-only error. The specified timing spectrum places
0.3142 mV RMS at the wanted band and gives a 0.225079 ps bound for the illustrative
40 dB allocation. These results depend on waveform/spectrum/filter assumptions.

Initial fresh read-only session `01a18e1e-f65e-7d20-9d9d-9a91fd47a4c0`, exit 0:
[findings](k08-k10-evidence/k9-findings.md). Independent source/KCL/modal,
normalization/cross-sign, convolution, sideband and curve checks agree; ten PNGs
actually inspected. Findings: implicit field-PSD representation, timing centering
and finite-slope conditions, insufficiently local LO independence, missing circuit
polarities/load-state distinction, selector bridge, lower diagram amplitude and
continuation wording. Author corrected each; revised timing ticks and low-amplitude
sampling as optional polish. Initial expected-value typo in one test was corrected
from 27.0461027 to 27.0467026 dB; manuscript's 27.05 dB did not change.
Initial reviewer inadvertently displayed Chapter 8 portions of shared generator/tests;
it did not assess them or open author state/history/prior reviews. This exposure
is retained, not concealed. Source assessment was of supplied passage summaries,
not fresh reviewer PDF access.

Fresh targeted read-only session `01a18e2c-7061-7c60-8993-c913ca3e4fb6`, exit 0:
[reassessment](k08-k10-evidence/k9e-findings.md). Eleven actual PNGs inspected,
including complete page and all seven overlapping crops. No consequential remaining
mathematical/physical defect in target scope. Confirms factor-four representation
bridge, first-order centered timing assumptions, conditional LO floor, source/port
signs, disconnected loads, selector power normalization and amplitude labels.
No prohibited exposure reported. Optional: explicitly write G[4SL]G^H and add a
near-zero blocker inset; current wording/scale preserve intended conclusions.
No curve is relied on to resolve the approximately one-pixel 1 mV transition.

Final actual page: 1425×10420 at viewport1440×2200, inspected through bottom
navigation with seven readable crops. Three final standalone assets inspected;
author corrected a ground/annotation clearance during pixel work before final
review. All 341 timing vertices match an independent time-slope average within
2.361e−5 relative error. All six batch SVGs regenerate byte-identically.
46 standard-library tests and 19 pilot tests pass; final HTML render (13 pages),
372 local links/fragments, 44 image uses, repository integrity and whitespace pass.
Full pytest remains unavailable. [Author pixel/check record](k08-k10-evidence/k9-author-observations.json)
and both frozen packet archives preserve exact inputs, actual images and events.

K09 closes as a checked provisional bounded Chapter 9 treatment. No hardware
covariance, oscillator/clock spectrum, physical noise floor, compliance or reader
performance was demonstrated. Full device noise-network physics, array validation,
converter realization and application budgets remain outside this bounded unit.
AI contexts retain correlated failure risks and confer no human Reviewed/Accepted
state. Next is K10; final integration must replace the temporary supplement
navigation with the connected Chapter 8→9→10 progression.

## K10 / Chapter 10 — detection, integration and retained information

Engineering question: does a quieter output improve detection, or remove the
wanted signal? Outcomes: derive a normalized likelihood/correlation statistic,
separate detection from estimation, calculate conditional detection probabilities,
compare coherent/energy accumulation, and evaluate exact rejection and reference
leakage. Four reproducible figures explain the decision distribution, phasor
accumulation, projection loss and frozen-weight leakage path. The statistical
foundations stay in Chapters 2–5; physical source construction stays in Chapter 9.
[Source examination](../references/source-notes/extraction-integration-rejection.md)
records the actual MIT matched-filter and whitened-pulse passages examined.
Complex-vector normalization and all numerical examples are local derivations.

At 30-degree template separation, independent background variance sigma² and a
100 sigma² Gaussian interferer give sigma²q=26/101. Unit desired response needs
weights (1,−25 sqrt(3)/26), output variance (101/26)sigma². A/sigma=4 gives
single-test P_FA=0.001 and known-phase P_D=0.412894, versus 0.007316 using only
the first mode. P_D≥0.9 requires A≥6.09281 mV when sigma=1 mV. Four correctly
phased independent records give 0.995976, while four energy records give
0.899473 under their different gamma-law threshold. A Poisson/gamma-mixture
derivation makes the latter calculation reproducible without a special-function
library. A template-only 90-degree phase mismatch leaves complex SNR unchanged
but reduces the declared real detector to P_D=P_FA.

A 30-degree hard null retains one-quarter of desired template energy; its unit
response variance is 4 sigma², slightly worse than finite-covariance weighting.
At zero separation a hard null erases the desired observation, while the finite
random-interference model still has nonzero q. Frozen cancellation trained with
the wanted source off can reduce operational noise by 17.05 dB while desired
power falls 40.09 dB: wanted-to-noise ratio worsens 23.03 dB. A complex leakage
disk yields a conditional retained-amplitude bound; its uncertainty set requires
external evidence. Shared interference across four records requires stacked
covariance, yielding sigma²q=404/401 rather than four independent-record q values.

Initial fresh read-only GPT-6.1 Sol/high session
`01a18e3c-2a47-7083-9ac4-13317339c8c0`, exit 0:
[findings](k08-k10-evidence/k10-findings.md). Independent likelihood, weights,
threshold, integration, fourth-moment and leakage calculations agreed; all 12
supplied PNGs were examined. Required corrections: validate exact finite frame
length rather than silently truncating zip inputs; distinguish invalid records
from nondetections; correct source-draw code attribution; replace a q-specific
ordinate on nonoptimal curves by general normalized output SNR; make the leakage
figure's source-off training/frozen operational mechanism explicit; condition
phase-error claims and average conditional detection probabilities for random
errors. Author corrected each. Added useful quantitative noncoherent detection,
whitening/mismatch bridges and transfer-answer checks. No excluded author-state
exposure was reported. Source summaries were reviewed, not freshly accessed PDFs.

Fresh targeted technical/visual session
`01a19050-7893-76e2-8743-8b92e0da7bfb`, exit 0:
[reassessment](k08-k10-evidence/k10c-findings.md). All thirteen actual PNGs
examined, 51 manifest entries verified twice, and 2,047 stored curve points
checked independently to coordinate-rounding accuracy. A separate normal-plus-
gamma quadrature reproduced the Poisson-mixture probabilities. All ten then-current
extraction tests passed. No consequential mathematical or visual defect remained
in the reviewed targets. Source notes still cannot substitute for fresh reviewer
access to original PDFs; no such access is claimed. No prohibited exposure reported.

The targeted reviewer found a further implementation defect: tuple conversion
consumed an entire iterable before checking its two-coordinate support. A
10,000-value example was fully read, and an acquisition RuntimeError escaped the
documented invalid-record contract. Author replaced eager conversion by at most
three iterator advances, normalized reader/conversion failures to ValueError,
and tested an endless reader, a failed acquisition and a valid iterator. This
bounds the algorithm's consumption, not the latency of an externally blocking
reader. A fresh implementation-only reassessment is recorded below; mathematical
and image bytes were unchanged by this correction.

Final fresh implementation-only session `01a19054-62f5-7ee2-918c-b958c551999c`, exit 0:
[reassessment](k08-k10-evidence/k10d-findings.md). Eleven extraction tests,
65 additional adversarial/domain assertions and 700 independent covariance-inverse
comparisons passed. Six manifest entries verified before/after; no consequential
remaining implementation defect or prohibited exposure reported. Reader blocking
latency remains an acquisition responsibility. No new visual assessment was
needed for the code-only change; prior frozen manuscript/figure bytes remain.

Final author pixel/check record is
[here](k08-k10-evidence/k10-author-observations.json). Actual final unit page
1425×12884 plus eight readable overlapping crops and all four standalone figures
were inspected. All 47 book SVGs regenerate byte-identically; 57 standard-library
tests plus 19 pilot tests pass. HTML render: 14 pages, 414 resolving local links,
48 image uses with alt text, no duplicate IDs/unresolved markers. Integrity and
whitespace pass. pytest and SciPy are absent; no installation or claim of those
checks succeeding. Frozen initial, mathematical/visual and implementation packets,
raw events and hashes preserve the review provenance. Requested model/effort is
GPT-6.1 Sol/high; backend identity is not independently attested.

K10 closes as a checked provisional bounded Chapter 10 treatment. No measured
sensitivity, valid hardware covariance/Gaussian law, real adaptive training,
receiver compliance or educational effectiveness was demonstrated. Independent
human specialist review, broader layouts/accessibility, PDF/offline mathematics
and hardware/reader evidence remain open. Next: connected K08–K10 integration
assessment only, then stop.
