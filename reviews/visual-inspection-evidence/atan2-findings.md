I found **no mathematical defect in the exact equality or local linearization**, within the stated small-perturbation scope. No downstream correction follows. This conclusion does not extend to arbitrary unwrapped phase errors, fades, or noise characterized only by small RMS.

At [relative-phase-stability.qmd:80](/tmp/coherent-atan2-reassessment/book/relative-phase-stability.qmd:80), write
\[
z=e^{j\alpha}(A+n'),\qquad A>0.
\]
The exact **principal signal-frame error** is
\[
\eta_p=\operatorname{Arg}(ze^{-j\alpha})
=\operatorname{Arg}(A+n')
=\operatorname{atan2}(\operatorname{Im}n',A+\operatorname{Re}n'),
\]
provided \(A+n'\ne0\), with consistent principal-angle conventions.

The independent checks establish these boundaries:

- **Quadrants:** `atan2` is correct throughout the nonzero complex plane. With \(A=1,\ n'=-2+0.1j\), it gives \(3.041924\) rad. Replacing it with the one-argument arctangent of the quotient gives \(-0.099669\) rad—a demonstrated \(\pi\) error. The supplied paragraph uses the correct function.
- **Branches:** \(\eta_p=\operatorname{wrap}(\operatorname{Arg}z-\alpha)\), rather than unrestricted subtraction of principal angles. For \(\alpha=179^\circ\) and \(n'=j\tan2^\circ\), the signal-frame error is \(2^\circ\), while \(\operatorname{Arg}z=-179^\circ\); raw subtraction gives \(-358^\circ\). The negative real axis has a defined angle, with the endpoint represented as \(+\pi\) or \(-\pi\) according to convention. A globally unwrapped error additionally requires continuity and acquisition information.
- **Zero amplitude:** Exact cancellation, \(n'=-A\), makes the observed phase undefined. A library’s numerical return for `atan2(0,0)` cannot supply that phase. If \(A=0\) but noise remains nonzero, the noisy sample has an angle, but there is no nonzero signal phasor against which to define this phase error.
- **Local approximation:** Put \(u=n'/A\). For \(|u|<1\), the signal-frame phasor lies in the right half-plane and
  \[
  \eta_p=\operatorname{Im}\log(1+u)
  =\operatorname{Im}u-\tfrac12\operatorname{Im}(u^2)+O(|u|^3).
  \]
  Hence \(\eta_p\simeq\operatorname{Im}n'/A\) is correct. For \(|u|\le r<1\), a concrete remainder bound is
  \[
  |\eta_p-\operatorname{Im}u|\le\frac{r^2}{2(1-r)}.
  \]

The [scalar comparison at line 132](/tmp/coherent-atan2-reassessment/book/scalar-stochastic-phase.qmd:132) makes \(A>0\), the principal-error interpretation, and \(|n|\ll A\) explicit. Its conditional-noise caveat and circular-noise variance \(v/(2A^2)\) are consistent with this derivation. Making those same conventions explicit in the pilot paragraph would improve self-containment; their current implicit treatment is not a demonstrated mathematical error.

Small RMS alone is insufficient for phase-variance prediction. Independently constructed zero-mean, real noise with \(A=1\),
\[
n'=\begin{cases}
-2,&\text{probability }p,\\
2p/(1-p),&\text{probability }1-p,
\end{cases}
\]
has RMS \(0.020001\) at \(p=10^{-4}\). Its quadrature is identically zero, so linearized phase variance is zero. Nevertheless, rare sign reversals give exact principal phase variance \(\pi^2p(1-p)\approx0.000986862\ \mathrm{rad}^2\). This violates small-excursion validity, rather than contradicting the local expansion. The scalar chapter expressly requires negligible large excursions.

Downstream, expansion of \(z_2z_1^*\) gives the stated first-order contribution \(\eta_2-\eta_1\), including
\[
\operatorname{var}(\eta_2-\eta_1)
=V_2+V_1-2\operatorname{cov}(\eta_2,\eta_1).
\]
Common additive voltage noise need not cancel after different signal-frame rotations or amplitude normalization. An asymmetric check with \(z_1=1+0.01\), \(z_2=2j+0.01\) gave differential error \(-0.0049999583\) rad versus the linear prediction \(-0.005\).

The architecture tables use declared **phase** spectra, rather than an unrestricted conversion from additive voltage noise. Independent quadrature reproduced the [architecture results](/tmp/coherent-atan2-reassessment/book/relative-phase-stability.qmd:336): approximately \(0.362364^\circ\) versus \(1.145858^\circ\) for compact distribution, and \(3.623641^\circ\) versus \(1.145858^\circ\) for exposed distribution. It also reproduced the [snapshot uncertainties](/tmp/coherent-atan2-reassessment/book/relative-phase-stability.qmd:449). Their conditional preferences and snapshot-duration decisions therefore remain unchanged. Gaussian coherent-performance formulas retain their separate distribution and amplitude assumptions.

Checks performed were independent algebra, explicit quadrant/branch/zero and rare-excursion counterexamples, an 816-case rotation-identity grid with maximum circular discrepancy \(1.54\times10^{-15}\) rad, shrinking-noise remainder checks, and numerical integration at two resolutions. These are mathematical/computational checks, not empirical validation.

All **seven** entries in [inputs.sha256](/tmp/coherent-atan2-reassessment/inputs.sha256) matched. The manuscript hashes were:

```text
book/relative-phase-stability.qmd
9d1018b4cd95cc844d93d8a6c60b60f6a6be5b909de8746cade323f9ad022e05

book/scalar-stochastic-phase.qmd
1370c77f06f9a2a55153a351d662097ae50e27e84ad013706ddaa1991ea99937
```

This establishes consistency with the supplied manifest, not independent provenance.

Files actually read, in full:

- [AGENTS.md](/tmp/coherent-atan2-reassessment/AGENTS.md), [inputs.sha256](/tmp/coherent-atan2-reassessment/inputs.sha256), and [project/charter.md](/tmp/coherent-atan2-reassessment/project/charter.md).
- Both manuscript files linked above.
- [notation-and-conventions.md](/tmp/coherent-atan2-reassessment/standards/notation-and-conventions.md), [technical-authoring.md](/tmp/coherent-atan2-reassessment/standards/technical-authoring.md), [verification-and-acceptance.md](/tmp/coherent-atan2-reassessment/standards/verification-and-acceptance.md), and [sources-and-evidence.md](/tmp/coherent-atan2-reassessment/standards/sources-and-evidence.md).

Unverified matters include actual receiver noise tails, amplitude/SNR gates, sampling and unwrapping reliability, hardware spectra, empirical performance, cited external sources, referenced supporting code, and rendered presentation. Requirements were treated as requirements, not correctness evidence.

No inadvertent exposure was identified. No prohibited records or outside-packet files were inspected; no connectors, edits, or delegation were used. This Codex AI review, dated 2026-10-30, grants no human acceptance; exact runtime model revision and effort metadata were not verified.