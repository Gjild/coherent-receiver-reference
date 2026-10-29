# K03 separate AI review and closeout

2026-10-29. Checked provisional teaching draft; human review pending.
Fresh codex-cli 0.165.0 reviewer, requested gpt-6.1-sol / high, read-only shell.
Session: 01a1875f-a315-74b3-9dce-9616a76f22f8. Runtime
model/effort not independently exposed. No author conversation or dispositions
provided. Inputs frozen and checked unchanged during initial review:

- book/observation-weighted-coherence.qmd: `3055bdfd7ccbed545dc70e5b5ba87f4b19055fe8dcdf635fe0a298707f84e426`
- references/source-notes/observation-weighted-coherence.md: `28c8119ddf83fb4282e8203407bad5953c8254ac83e30ea93cc11296fef50a9a`
- book/scalar-stochastic-phase.qmd: `1370c77f06f9a2a55153a351d662097ae50e27e84ad013706ddaa1991ea99937`
- project/technical-coverage.md: `13486c7ce6600ca82a203c25386a2f7910f66216ffe6754ee7d934f997836580`
- project/annotated-toc.md: `9441c0715abdab2c7da078ee8729dc18c6501bf6b6916356d69fbd4952d5cdcb`
- standards/technical-authoring.md: `fcaef573dfa9969d9e02a1402366ae31613dd60405dfdd982269123fadadbd34`
- standards/sources-and-evidence.md: `7bd1f76293f2d8a04d37151b31af410ddd3304617d483c19035bcbb67cce3918`
- standards/verification-and-acceptance.md: `f542ca24ac86a858a2f3afa547bd86687f6fddd111ac56c59d7a12cbcb205fa2`
- standards/notation-and-conventions.md: `4f5ee34533463abc134682a7535c3bd5bf1b80a2260d57a1f87b7db07d886200`

## Initial findings and corrections

- Applicability: WSS did not justify lag-only coherence. Retained epoch dependence
and specified sufficient increment stationarity / jointly Gaussian WSS assumptions.
- Applicability: arbitrary acquisition filtering does not filter phase linearly.
Restricted phase-domain/linearized response and added phasor-versus-angle contrast.
- Pedagogy: Gaussian characteristic function and fourth moments were asserted.
Added integration-by-parts and polynomial coefficient derivations.
- Pedagogy: coherence lacked a worked calculation. Added normalized coherent-power
integration and comparison with the inappropriate phase-average conversion.

The first and third findings blocked teaching closeout until corrected.
Reviewer independently examined Oppenheim–Verghese pp.183–184 PDF text; claim
support was confirmed narrowly. Initial SciPy calculation failed (module absent);
standard-library quadrature, resolution doubling, tail bounds and Gaussian moment
checks completed. No author code was consulted before reasoning. No physical,
reader, browser or specialist evidence was produced.

## Reassessment

All four original findings are resolved. I found no remaining consequential defect in the revised passages.

1. **Stationarity qualification — resolved.** [Lines 86 onward](../book/observation-weighted-coherence.qmd) retain epoch dependence in \(\Gamma(t,\tau)\) and correctly distinguish WSS from assumptions sufficient for stationary increment distributions.

2. **Filter applicability — resolved.** [Line 47](../book/observation-weighted-coherence.qmd) now restricts \(|H|^2S\) weighting to phase-domain LTI filtering or a justified linearized phase response. I independently confirmed the phasor-versus-angle example: \(0.321751\) versus \(0.392699\) rad.

3. **Gaussian derivations — resolved.** The integration-by-parts argument at [line 91](../book/observation-weighted-coherence.qmd) correctly gives \(F'(a)=-DaF(a)\), including restoration of the mean and the deterministic limit. Independent density quadrature confirmed examples with nonzero means and unequal variances.

   The fourth-moment derivation at [line 172](../book/observation-weighted-coherence.qmd) is also correct: comparing coefficients gives
   \[
   6E[X^2Y^2]=6\sigma_X^2\sigma_Y^2+12R^2.
   \]
   The warning that Gaussian marginals alone are insufficient is appropriate.

4. **Worked coherent-power calculation — resolved.** The pair-separation weighting and Gaussian specialization at [line 112](../book/observation-weighted-coherence.qmd) are correct. Independent quadrature, with resolution doubling, and a separate exponential-series evaluation both give
   \[
   E|C|^2=0.456410127844383.
   \]
   I also confirmed \(\operatorname{var}\bar\phi=0.180000907999\) rad² and its exponential \(0.835269452987\). The example clearly distinguishes normalized coherent power from phase-average variance.

One **nonblocking precision improvement** remains at line 88: “Only stationary increment distributions permit writing Gamma(tau)” overstates necessity. Stationary increment distributions are sufficient; epoch independence of this particular characteristic-function value can hold under weaker conditions. Replace “Only…” with “Stationary increment distributions permit…”.

The earlier blockers are cleared within this bounded reassessment. No edits, delegation, connectors, repository tests, rendering, hardware validation or reader trials were performed. The manuscript hash remained unchanged during review. AI review only; this does not grant human acceptance.

Author applied the requested final sufficiency wording correction. Final manuscript
SHA-256: `10798a3756a0e1f71bfff99d9513944019ab19eb7b2f28211cdf12a0f186f168`.

## Author checks and limits

Nine foundation unittest checks passed, including independent time/spectral
quadratures, exact finite-ensemble bias, unequal-delay and non-Gaussian coherence,
and normalized coherent-power/filter-domain counterexamples. Corrected HTML render
passed with temporary XDG cache; no browser pixel review. pytest remains absent.
No experimental validation, specialist review, learner trial or technical acceptance.
General pilot results remain in their existing home; this unit is an introductory
scalar treatment and does not complete Chapter 3 or the estimator catalogue.
Raw runtime logs are temporary in /tmp/coherent-batch-audit; evidence is summarized here.
