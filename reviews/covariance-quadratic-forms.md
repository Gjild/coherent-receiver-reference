# K04 separate AI review and closeout

2026-10-29. Checked provisional teaching draft; human review pending.
Fresh codex-cli 0.165.0 reviewer requested gpt-6.1-sol / high, read-only shell.
Session: 01a18768-8e3d-7500-b10e-45aba10f368e. Exact runtime
model/effort not independently exposed. No author history or dispositions supplied.
Frozen initial inputs (SHA-256):

- book/covariance-quadratic-forms.qmd: `0bf7d425a916e6becd5123d8d122630f6b194586ec47599eaab16bff631ceefa`
- references/source-notes/covariance-quadratic-forms.md: `41892da6e023bacff4936fe79e42a2972df1ea22c900272eadf613af99482f3e`
- book/scalar-stochastic-phase.qmd: `1370c77f06f9a2a55153a351d662097ae50e27e84ad013706ddaa1991ea99937`
- project/technical-coverage.md: `13486c7ce6600ca82a203c25386a2f7910f66216ffe6754ee7d934f997836580`
- project/annotated-toc.md: `9441c0715abdab2c7da078ee8729dc18c6501bf6b6916356d69fbd4952d5cdcb`
- standards/technical-authoring.md: `fcaef573dfa9969d9e02a1402366ae31613dd60405dfdd982269123fadadbd34`
- standards/sources-and-evidence.md: `7bd1f76293f2d8a04d37151b31af410ddd3304617d483c19035bcbb67cce3918`
- standards/verification-and-acceptance.md: `f542ca24ac86a858a2f3afa547bd86687f6fddd111ac56c59d7a12cbcb205fa2`
- standards/notation-and-conventions.md: `4f5ee34533463abc134682a7535c3bd5bf1b80a2260d57a1f87b7db07d886200`

## Initial findings and dispositions

- Pedagogical: ambiguous singular-value square-root wording. Corrected explicit
s_i=sqrt(lambda_i(A^H A)), forward gain s_i and inverse gain 1/s_i.
- Applicability: independence alone did not justify RMS error formula. Added
centered equal-variance assumptions and the general differential-bias MSE term.
- Pedagogical: rank/nonsingularity and inverse conjugate transpose were undefined.
Added a local rank/nullity and coordinate bridge.

Reviewer reproduced source covariance, quadratic forms, eigenvalues/determinant,
asymmetric complex conjugation and coordinate invariance, nonphysical covariance,
source cancellation and near-singular inversion using independent finite ensembles.
Gallager PDF text at pp.230–231 was freshly examined; page-image retrieval failed.
NumPy was unavailable; reviewer reran with standard-library computations.
No critical covariance-core defect was found. Corrections restrict the RMS claim
and repair the local mathematical bridge; example covariance numbers are unchanged.

## Reassessment

All three findings are resolved in the corrected unit. **No consequential new defects found in the revised passages. AI review only; this does not establish human acceptance.**

1. **Singular-value scaling—resolved.** [Lines 167–173](../book/covariance-quadratic-forms.qmd) correctly distinguish \(s_i=\sqrt{\lambda_i(A^HA)}\), forward gain \(s_i\), and inverse gain \(1/s_i\) for a nonzero mode. Direct norm calculations confirm the diagonal example’s gains \(4,1\).

2. **Noise centering and bias—resolved.** [Lines 157–163](../book/covariance-quadratic-forms.qmd) explicitly require centered independent noises for the original RMS result. The added formula is correct under the retained independence assumption:
   \[
   \mathrm{MSE}(\widehat b)
   =\operatorname{var}(\widehat b-b)+[E(\widehat b-b)]^2
   =\frac{v_1+v_2+(\mu_2-\mu_1)^2}{\epsilon^2}.
   \]
   Equal common biases cancel; differential bias is amplified. Independent finite-ensemble checks passed for zero, equal and unequal means, with positive and negative \(\epsilon\).

3. **Rank and coordinate bridge—resolved for this selected unit.** [Lines 133–144](../book/covariance-quadratic-forms.qmd) now define rank, state the correct input-dimension/nullity relationship, and explain \(T^{-H}\). Independent calculations confirmed rank/nullity for the source mapping and covariance examples, and verified the inverse-transpose weight transformation using exact arithmetic.

Checks used newly written, standard-library Python calculations; all assertions passed. No repository check code was inspected. No edits, delegation or connectors were used. These checks address mathematical consistency, not physical validation or demonstrated teaching effectiveness.

Final manuscript SHA-256: `5caf8f2ae043e80ad63e2aea91cdaa3710cf8c1ccf9f415e0a51575f58a6d502`.

## Author checks and limitations

Thirteen foundation unittest checks passed across the batch, including source
ensemble vs matrix calculation, complex conjugation, coordinates, nonphysical
covariance, inverse amplification and differential bias. Nineteen existing pilot
unittest checks also passed. Eight-page HTML book render passed with temporary
XDG cache. No browser pixel inspection or actual reader testing. No physical
validation, specialist review or human technical acceptance. Full pytest remains
unavailable; no dependencies installed. K04/chapter completion and physical noise
network/application modeling are not claimed. Raw CLI logs are temporary under
/tmp/coherent-batch-audit; this record preserves findings and dispositions.
