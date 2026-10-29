# K07 and connected foundations: separate AI review

2026-10-29. Checked provisional teaching draft; human specialist review pending.
Fresh codex-cli 0.165.0, requested gpt-6.1-sol / high, read-only shell; session
01a187a6-90bb-76b3-bb95-5bfb2f12f3f3. Exact runtime route
not independently exposed. No author conversation, dispositions or code supplied.
Initial frozen inputs (SHA-256):

- book/model-adequacy-uncertainty.qmd: `742fdd10b7067e74760601d0ea15c6673149a4117ef4bbb21839b2f67bc5fde3`
- references/source-notes/model-adequacy-uncertainty.md: `6b4cb64c2d20052d950dfc840aaf7786126944ab9e1b514286f726e293d1a072`
- project/technical-coverage.md: `13486c7ce6600ca82a203c25386a2f7910f66216ffe6754ee7d934f997836580`
- project/annotated-toc.md: `9441c0715abdab2c7da078ee8729dc18c6501bf6b6916356d69fbd4952d5cdcb`
- standards/technical-authoring.md: `fcaef573dfa9969d9e02a1402366ae31613dd60405dfdd982269123fadadbd34`
- standards/sources-and-evidence.md: `7bd1f76293f2d8a04d37151b31af410ddd3304617d483c19035bcbb67cce3918`
- standards/verification-and-acceptance.md: `f542ca24ac86a858a2f3afa547bd86687f6fddd111ac56c59d7a12cbcb205fa2`
- standards/notation-and-conventions.md: `4f5ee34533463abc134682a7535c3bd5bf1b80a2260d57a1f87b7db07d886200`
- book/phase-comparison.qmd: `1ec0b1f401846a47e784dc928de37c694686cb7e5dddeb8cbe83d861089683d0`
- book/scalar-stochastic-phase.qmd: `1370c77f06f9a2a55153a351d662097ae50e27e84ad013706ddaa1991ea99937`
- book/observation-weighted-coherence.qmd: `10798a3756a0e1f71bfff99d9513944019ab19eb7b2f28211cdf12a0f186f168`
- book/covariance-quadratic-forms.qmd: `5caf8f2ae043e80ad63e2aea91cdaa3710cf8c1ccf9f415e0a51575f58a6d502`
- book/phase-delay-inference.qmd: `cc9689d7c8bd6bb5db3e2506608072a2aba0997821ec3b0a1ba52eec1fbd6012`
- book/tracking-signal-retention.qmd: `e540970f92f539508a5d040798e532a5c10af5d7994bc3a63b38d7461e8d913a`

## Initial findings and corrections

- Demonstrated mathematical error: differentiability alone did not justify a
  quadratic Taylor remainder. Added bounded second derivatives and separate
  integrable remainder/moment conditions for the Hessian mean correction.
- Applicability: small frequency-gap standard deviation did not exclude reciprocal
  tails near zero. Added explicit bounded uniform input and explained tail/support
  requirements. Synthetic nominal numerical results remain unchanged.
- Observation/reference applicability: same shared-source draw lacked an acquisition
  interface. Specified simultaneous multitone observations with identical weighting
  and frequency-independent phase offset; added temporal-correlation sensitivity
  and the approximately 0.987741 shared-source correlation threshold.
- Navigation: explicitly linked Chapter 3's Gaussian and exponential-covariance
  prerequisites for this selected Chapter 6 unit.

## Connected learning progression

Reviewer examined all seven foundational manuscripts. The progression connects
phase/reference orientation to stochastic observations, covariance, inference,
model adequacy and tracking. It found no sign conflict, circular prerequisite or
competing canonical derivation. Chapter 4 separates covariance nulls from response
identifiability; Chapter 5 preserves nuisance/alias limits; Chapter 6 distinguishes
precision/bias/numerics/discrepancy; Chapter 7 preserves wanted transfer and the
true-versus-detector residual distinction. Corrections strengthen the temporal
observation-to-covariance connection. This is an AI editorial/technical assessment,
not demonstrated reader effectiveness or full chapter/treatment completion.

Reviewer freshly examined NIST TN1297 A.1–A.3 and the cited primary sources used
across Chapters 1–7. It used independent algebra, finite-difference sensitivity,
source-sum covariance, Gaussian quadrature/refinement, high-precision arithmetic,
coherent-power integration and tracking-noise integration. No forbidden files were
opened; filename discovery and one architecture search exposed status metadata
outside requested cards, which it excluded from technical judgment. No author
conversation or prior review dispositions were accessed.

## Correction and connected-progression reassessment

**AI review only: all four earlier findings are resolved for this bounded unit. No unresolved consequential defect was found.**

- **Taylor regularity — resolved.** [Lines 46–73](../book/model-adequacy-uncertainty.qmd) now require twice continuous differentiability and bounded second derivatives for the quadratic remainder, and separately require integrable remainder control for the Hessian mean correction. These conditions address the demonstrated differentiability counterexample.

- **Reciprocal tails — resolved under the declared uniform model.** [Lines 118–129](../book/model-adequacy-uncertainty.qmd) specify a half-width of \(\sqrt3\,1000=1732.050808\) Hz, giving exactly 1000 Hz standard deviation. The minimum gap is **9,998,267.949 Hz**, safely separated from zero.

  Independently integrating the reciprocal’s first two moments gives frequency-only delay standard deviation **0.000500000011 ns**, versus **0.000500000000 ns** from first-order propagation. Including the independent phase uncertainty gives **0.142353388918 ns** exactly under the model, versus **0.142353386783 ns** from combined first-order propagation. Numerical quadrature with 128 and 256 subdivisions reproduced these results. The approximation is adequate relative to the illustrative decision margin.

- **Observation timing and correlation — resolved.** [Lines 89–116](../book/model-adequacy-uncertainty.qmd) now identify simultaneous multitone observations, identical normalized time weighting, and a frequency-independent phase-offset component. They distinguish this assumption from an oscillator timing-error model.

  Independently solving
  \[
  0.00008+0.00072(1-\rho)
  \le [2\pi(10^7)(0.15\times10^{-9})]^2
  \]
  gives **\(\rho\ge0.9877410561\)**, confirming the stated approximate threshold. Including the subsequent uniform frequency uncertainty changes it slightly to **0.9877424306**; this does not materially change the example. The threshold concerns shared-source draws, as the correction explicitly states.

- **Prerequisites — resolved.** [Lines 9–13](../book/model-adequacy-uncertainty.qmd) now explicitly identify Chapter 3’s Gaussian and exponential-covariance results alongside Chapters 2, 4 and 5.

The **connected foundations assessment still holds**. Hash checks establish that Chapters 1–5 and 7 are unchanged from the earlier review. Chapter 6’s corrections strengthen the observation-to-covariance-to-inference connection without introducing a sign inconsistency, circular prerequisite or competing canonical treatment.

These checks establish mathematical and numerical consistency under synthetic assumptions. They do not establish physical covariance, calibration accuracy, acquisition reliability, complete chapter coverage or human acceptance. External sources were not freshly re-examined this turn.

No edits, delegation, connectors, tests, status/review material or additional author history were accessed. No new forbidden-path exposure occurred.

Final Chapter 6 manuscript SHA-256: `0c23d1984084eb9c97fa06bfbdad36e15aafb920ea2a3159ebb9773754274c53`.

## Author checks and limitations

Eleven new-batch unittest checks passed. Added checks cover covariance timing,
rare reciprocal tails and a bounded uniform reciprocal calculation; other new
checks cover inference, tracking and numerical/nonlinear adequacy. Together with
13 earlier foundation and 19 pilot checks, 43 standard-library tests are available.
Eleven-page HTML render passed. No browser pixel, PDF/offline math, actual reader,
hardware or qualified specialist validation. Full pytest unavailable. No K08 or
hardware campaign follows. Pilot migration audit was not performed by the reviewer;
author baseline byte-preservation checks are recorded separately.

Raw CLI logs are temporary in /tmp/coherent-next-batch; findings, input hashes,
source access and dispositions are preserved in these existing review records.
