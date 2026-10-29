# K02: separate-context AI review and closeout

2026-10-29. Checked provisional teaching draft; human specialist review and
reader testing pending. No physical validation, compliance or publication acceptance.

## Inputs and provenance

Author: Codex. Reviewer invocation: codex-cli 0.165.0, gpt-6.1-sol,
model_reasoning_effort=high, fresh read-only session 01a18757-9b22-73e0-9cf4-326c2311850c. Runtime model
was not independently exposed to the reviewer. No author conversation supplied.
Initial frozen inputs (SHA-256):

- book/scalar-stochastic-phase.qmd: `4c4246a6944c99f893a3ad4bcedfa42e6d1b5f3d121134af3e93e441aa02ac7c`
- references/source-notes/scalar-stochastic-phase.md: `4273a9a510eae1bb973861a47d2f9915715eb5944619f5a92f7e1763079c7809`
- project/technical-coverage.md: `13486c7ce6600ca82a203c25386a2f7910f66216ffe6754ee7d934f997836580`
- project/annotated-toc.md: `9441c0715abdab2c7da078ee8729dc18c6501bf6b6916356d69fbd4952d5cdcb`
- standards/technical-authoring.md: `fcaef573dfa9969d9e02a1402366ae31613dd60405dfdd982269123fadadbd34`
- standards/sources-and-evidence.md: `7bd1f76293f2d8a04d37151b31af410ddd3304617d483c19035bcbb67cce3918`
- standards/verification-and-acceptance.md: `f542ca24ac86a858a2f3afa547bd86687f6fddd111ac56c59d7a12cbcb205fa2`
- standards/notation-and-conventions.md: `4f5ee34533463abc134682a7535c3bd5bf1b80a2260d57a1f87b7db07d886200`

## Findings and dispositions

1. Model/applicability: marginal circularity does not survive a dependent random
signal-frame rotation. Corrected fixed-signal and conditional assumptions; added
reviewer's exact counterexample. Consequence: v/(2A²) is restricted accordingly.
2. Pedagogical: joint Gaussianity was unexplained. Added definition, implication
chain and Gaussian-marginal counterexample.
3. Pedagogical: transfer model was underspecified. Added epsilon_k=(-1)^k B and
explicit unequal-quadrature variances; observable remains unchanged.
4. Optional: quadrature RMS alone did not justify small total noise. Added both
quadrature and tail qualifications to the numerical example.

Reviewer independently checked conditional variance, finite averaging, rotated
pseudo-covariance and complex-log expansion. Reviewer examined Gallager §7.8 PDF
text; screenshot inspection failed. Its first numerical check swapped variances;
it corrected that reviewer error. No author test code was supplied before reasoning.

## Reassessment (reviewer response)

The four original findings are resolved. I found **no consequential new defect** in the corrected unit.

1. **Signal/noise dependence — resolved.**  
   [Lines 132–154](/home/anon/coherent-receiver-reference/book/scalar-stochastic-phase.qmd:132) declare fixed signal phase, exclude \(z=0\), and distinguish conditional assumptions from marginal circularity. Independently, \(n=r e^{j\Theta}\), \(\phi=\Theta\) gives \(ne^{-j\phi}=r\), confirming the counterexample and the need for that qualification.

2. **Joint-Gaussian teaching bridge — resolved.**  
   [Lines 110–119](/home/anon/coherent-receiver-reference/book/scalar-stochastic-phase.qmd:110) define joint Gaussianity and explain the chain from \(P=0\) to equal variances, independence and rotational invariance. One minor precision correction remains: explicitly make \(X\) **zero-mean, nondegenerate Gaussian** in the new counterexample. For general \(E[X]=\mu\), its centered pseudo-covariance is \(-\mu^2\), rather than zero.

3. **Underspecified transfer exercise — resolved.**  
   [Lines 166–172](/home/anon/coherent-receiver-reference/book/scalar-stochastic-phase.qmd:166) supply explicit models and distinguish changing the model from changing the observable. Independently summing the alternating coefficients confirms zero average variance for even \(N\), and \(\sigma^2/N^2\) for odd \(N\). Minor sign correction: with indexing \(k=1,\ldots,N\), the odd-\(N\) coefficient sum is **−1**, not +1; the variance is unaffected. The 90° quadrature interchange and factor-four variance change are correct for fixed amplitude.

4. **Numerical approximation conditions — resolved.**  
   [Lines 156–160](/home/anon/coherent-receiver-reference/book/scalar-stochastic-phase.qmd:156) specify both quadratures, small excursions and fixed amplitude. The local \(0.01\) rad RMS prediction and stated breakdown at \(A=0.01\) V follow.

Source re-examination was unnecessary: the cited Gaussian result and its use remain consistent with the passage examined previously. This reassessment used manuscript reasoning; no code, rendering, physical tests or reader trials were performed. No files were edited, and no delegation or connectors were used.

Reviewed manuscript SHA-256: `2c96aea4f19b10afdcbba56d7baf2a6205928a8653e3cfed9ab3639e5b369dd8`.

This is AI reassessment only; it grants no human acceptance.

Author then made the two requested precision edits: zero-mean nondegenerate X,
and odd coefficient sum minus one. These do not change the variance conclusions.
Final manuscript SHA-256: `1370c77f06f9a2a55153a351d662097ae50e27e84ad013706ddaa1991ea99937`.

## Executed checks and limits

Five standard-library unittest checks passed: exact averaging ensemble, dependence
counterexample, proper/noncircular support, phase Taylor error scaling/fade contrast,
and alternating/dependent-rotation cases. An initial expected-value transcription
in the test failed and was corrected; manuscript rounding was unchanged.
Scaffold check passed. HTML render passed with XDG_CACHE_HOME in /tmp after two
cache-path failures. Generated page has math containers and no ?? markers; no
browser pixel inspection performed. pytest invocation failed (module absent).
No installation. No human engineer, laboratory or reader trial occurred.

Raw CLI event logs are temporary operational artifacts under
/tmp/coherent-batch-audit; this record preserves findings, dispositions and hashes.
