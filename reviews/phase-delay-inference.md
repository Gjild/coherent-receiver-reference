# K05 separate AI review and closeout

2026-10-29. Checked provisional teaching draft; human specialist review pending.
Fresh codex-cli 0.165.0, requested gpt-6.1-sol / high, read-only shell; session
01a18794-d170-7743-b2c1-aefcd75c5782. Actual runtime route
not independently introspected. No author history or dispositions supplied.
Initial frozen inputs (SHA-256):

- book/phase-delay-inference.qmd: `6d4468b279225a407441a6df69d8286d76275708480e6250292438b63054bfbd`
- references/source-notes/phase-delay-inference.md: `9fd3569261c9dd1ecdf1dcbcc8074f08dc480ed3329bfb297f7d978a5531ec79`
- project/technical-coverage.md: `13486c7ce6600ca82a203c25386a2f7910f66216ffe6754ee7d934f997836580`
- project/annotated-toc.md: `9441c0715abdab2c7da078ee8729dc18c6501bf6b6916356d69fbd4952d5cdcb`
- standards/technical-authoring.md: `fcaef573dfa9969d9e02a1402366ae31613dd60405dfdd982269123fadadbd34`
- standards/sources-and-evidence.md: `7bd1f76293f2d8a04d37151b31af410ddd3304617d483c19035bcbb67cce3918`
- standards/verification-and-acceptance.md: `f542ca24ac86a858a2f3afa547bd86687f6fddd111ac56c59d7a12cbcb205fa2`
- standards/notation-and-conventions.md: `4f5ee34533463abc134682a7535c3bd5bf1b80a2260d57a1f87b7db07d886200`

## Findings and dispositions

- Demonstrated error: asymmetric grid alone did not imply quadratic slope bias.
  Replaced with exact third-moment condition, zero-bias counterexample and a
  specified nonzero-bias grid. Main estimator/precision numbers unchanged.
- Applicability: raw upper-side positive-IF phase reverses the delay sign.
  Defined swept physical RF frequency and explicit orientation translation using
  Chapter 1 relations before fitting. Unknown receiver delay remains a nuisance.
- Optional pedagogy: whitening undefined. Added WCW^T=I and deferred construction.

Reviewer independently used projection, pair differences and full Fisher matrix
inversion. MIT §§1.3–3 and NIST §4.1.4.3 were freshly examined; neither certifies
receiver independence or unwrapping. No source-access blocker remained.

## Correction reassessment

AI review only. **All three prior findings are resolved; no remaining consequential defect was identified in these corrections.**

- **Conversion orientation — resolved.** [Lines 20–30](../book/phase-delay-inference.qmd) now identify swept physical RF frequency and the input-oriented comparison. Independently substituting Chapter 1’s relations confirms:
  \[
  \theta_L=\Delta\phi-\Delta\lambda+\Delta\beta,\qquad
  \theta_U=-\Delta\phi+\Delta\lambda+\Delta\beta.
  \]
  Both stated translations recover \(y=\Delta\phi\) on a justified unwrapped branch. A numerical check with frequency-dependent LO and IF phase terms recovered +5 ns through both orientations. Unknown path delay remains appropriately identified as confounded with DUT delay.

- **Curvature projection — resolved.** [Lines 173–178](../book/phase-delay-inference.qmd) correctly give
  \[
  \Delta b=q\frac{\sum x_i^3}{S_{xx}}.
  \]
  Direct substitution verifies zero projection for \((-8,-7,1,5,9)\) MHz. Centering \((0,1,3)\) MHz gives \(\sum x_i^3=20/9\ \mathrm{MHz}^3\), \(S_{xx}=14/3\ \mathrm{MHz}^2\), hence \(\Delta b/q=10/21\ \mathrm{MHz}\): nonzero when \(q\ne0\).

- **Whitening definition — resolved.** [Lines 79–83](../book/phase-delay-inference.qmd) correctly define whitening for the real phase-error vector with known positive-definite covariance. A non-diagonal numerical example confirmed \(WCW^T=I\) and \(\|Wr\|^2=r^TC^{-1}r\). Deferring construction and coupled fitting is appropriate for this bounded treatment.

Checks comprised independent algebra and fresh numerical calculations; no author verification code was inspected. No edits, delegation or connectors were used. These checks establish consistency under the stated models, not physical validation or human acceptance.

Reviewed manuscript SHA-256: `cc9689d7c8bd6bb5db3e2506608072a2aba0997821ec3b0a1ba52eec1fbd6012`.

## Author checks and limits

Three new standard-library tests passed: exact finite-noise ensemble vs delay
variance, grid alias/hidden path, and curvature/orientation counterexamples.
Non-Gaussian enumeration checks linear variance, not Gaussian likelihood optimality.
Nine-page HTML render passed after correction. No browser pixel, reader, physical
or specialist validation. pytest remains unavailable. Scope is bounded phase/delay
inference, not complete K05 or Chapter 5. Raw logs are temporary in
/tmp/coherent-next-batch; findings and hashes are preserved here.
