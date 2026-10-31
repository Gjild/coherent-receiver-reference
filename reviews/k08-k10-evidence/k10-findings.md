The bounded chapter substantially covers K10 and §§10.1–10.4. I found no consequential error in its worked likelihood, variance factors, weights, detection probabilities, or leakage calculation. Required corrections concern the executable input contract, attribution of simulation evidence, and figure wording/notation. Physical applicability and teaching effectiveness remain separate evidence questions.

1. **Implementation error: incomplete records receive an invalid normalization.** [bounded_extract](/tmp/k0810/k10-input/engineering/examples/physical_models.py:150) uses `zip(w,x)`, silently accepting missing or extra observations. An empty record returns `decision=False`; a NaN also becomes a negative decision. For a record containing only the first mode, the function uses variance \(101/26\), although that mode’s actual variance is \(76\). Under the declared Gaussian model, its false-alarm probability becomes approximately **0.24239**, rather than 0.001. Require exactly two finite complex observations and reject invalid records distinctly from nondetections. Validate finite parameters, nonnegative jammer variance, and the probability domain too. This defect does not invalidate results for valid two-mode inputs.

2. **Evidence-attribution error: the cited file does not perform the claimed source-draw evaluation.** [§10.4](/tmp/k0810/k10-input/book/extraction-integration-rejection.qmd:320) says `physical_models.py` realizes and evaluates the rule with independent Gaussian source draws. Its extraction functions realize the rule; `chapter10()` generates deterministic figures. The source-draw evaluation is in [ExtractionModels](/tmp/k0810/k10-input/tests/test_physical_models_stdlib.py:153). Cite that test explicitly and distinguish detector execution, Monte Carlo evaluation, and figure generation.

3. **Visual notation error and teaching defect in Figure 10.3.** The ordinate says \(\sigma^2q\), but \(q=a^HC^{-1}a\) was defined for the optimum. The first-mode and hard-null curves represent their respective output SNR factors. Label the common ordinate “output SNR divided by \(A^2/\sigma^2\),” reserving \(\sigma^2q\) for the optimum. Also annotate or magnify the separation: at \(30^\circ\), the optimum and null give 0.257426 and 0.25. Their near-overlap at page scale weakens the claim that the figure makes their difference visible.

4. **Teaching defect in Figure 10.4’s title.** “A leaked wanted signal can be learned and subtracted” suggests wanted-containing training. This example explicitly trains with \(s=0\), then freezes \(h\). It demonstrates operational leakage being subtracted by an already learned interferer weight. Change the title to match that mechanism; retain training contamination as the separately explained case.

5. **Applicability clarification for phase mismatch.** [The residual-phase equation](/tmp/k0810/k10-input/book/extraction-integration-rejection.qmd:186) is exact conditional on specified phase errors. If those errors are random across trials, \(N\rho L_N\) is a conditional quantity; marginal detection probability requires averaging the conditional detection law, including rotation. The existing warning that the real-part test depends on rotation is correct. Explicit conditioning would prevent readers from substituting an averaged retention factor into a Gaussian detection formula.

Independent expansion gives
\[
\log\Lambda=2A\Re(a^HC^{-1}x)-A^2a^HC^{-1}a.
\]
Thus \(\Re t\) is sufficient for the declared binary, known-phase decision. It is not sufficient for arbitrary subsequent sensing, delay search, or complex-amplitude estimation. Strictly, the **likelihood ratio** depends only on this statistic; individual densities retain a common data-dependent factor. The intended factorization argument is sound.

I obtain \(E[t]=Aq\), complex noise variance \(q\), and real-part variance \(q/2\). Consequently \(r=t/\sqrt q\) has unit complex noise variance, while \(Z=\sqrt2\Re r\) has unit real variance. The units—\(t\) in V\(^{-1}\), \(q\) in V\(^{-2}\), and dimensionless \(r,\rho,Z\)—are consistent. The threshold \(3.090232306\), Gaussian-tail detection expression, union bound, and independence qualification are correct. The finite reversed-conjugated matched-filter kernel produces the stated correlation at sample \(M-1\).

Completing the square independently also gives complex-amplitude estimate \(t/q\), error variance \(1/q\), and unconstrained real-amplitude variance \(1/(2q)\). Clipping a nonnegative estimate changes its distribution and bias. The chapter appropriately separates these estimation properties from detection probability and ambiguity.

For the source-constructed covariance, resolving along \(b\) and perpendicular to it gives eigenvalues \(101\sigma^2,\sigma^2\), hence
\[
q_0=\sin^2\theta+\cos^2\theta/101.
\]
Direct matrix calculation independently reproduces the \(30^\circ\) covariance, \(w=(1,-25\sqrt3/26)^T\), unit desired response, and the following results:

| Extraction | Output variance/\(\sigma^2\) | \(P_D\), \(A/\sigma=4\) |
|---|---:|---:|
| Colored optimum | 3.884615 | 0.412894 |
| Exact null | 4 | 0.396736 |
| First mode | 76 | 0.007316 |

The required \(\rho=9.556247\), \(A^2/\sigma^2=37.122345\), and \(A=6.092811\) mV for \(P_D=0.9\) also check. These are conditional synthetic receiver results. The calibrated mode basis and path vectors require an application-specific physical mapping; template separation is correctly distinguished from antenna bearing.

For arbitrary complex amplitude, maximizing the likelihood gives \(Q=|t|^2/q\). Under the null it is unit exponential, with threshold 6.907755; under a fixed signal, \(2Q\) has two real degrees of freedom and noncentrality \(2\rho\). Both reported moments check. As an additional comparison, this example’s unknown-phase single-record \(P_D\) is approximately **0.24456**.

Independent coherent combination gives \(N\rho\), reproducing four-record \(P_D=0.995976\). For a deterministic phase progression,
\[
L_4=\cos^2\delta\,\cos^2(\delta/2).
\]
This confirms cancellation at \(90^\circ\) and \(180^\circ\). Noncoherent accumulation instead has the stated gamma null, or equivalently a central chi-square law for \(2Q_N\); its fixed-signal alternative is noncentral chi-square. At the same false-alarm probability, four records require \(\eta=13.062241\) and give \(P_D\approx0.89947\). Including this comparison would strengthen teaching: retained energy alone does not establish equivalent detection performance.

For stochastic correlation, Gaussian fourth-moment pairing independently gives
\[
E|xy^*|^2=C_{xx}C_{yy}+|c|^2,\qquad
E[(xy^*-c)^2]=c^2.
\]
The chapter’s complex MSE, complementary variance, and real/imaginary variance split follow. Its RMS uncertainty 0.0101\(\sigma^2\) and real-part SD 0.00714213\(\sigma^2\) check. I also checked unequal receiver variances and a complex source-path coefficient; the conjugation and complementary-variance sign remained consistent. “Independent samples” should clearly mean independent observation pairs across records, since \(x\) and \(y\) share \(s\).

The rejection argument correctly distinguishes arbitrary nuisance amplitudes from finite Gaussian interference. Projection leaves \(M-\operatorname{rank}U\) complex coordinates; the retained SNR is \(A^2\|a_\perp\|^2\), with \(\|a_\perp\|^2\) carrying V\(^{-2}\) under the stated whitening. At coincidence, the arbitrary-nuisance hypotheses are indistinguishable, whereas finite random interference leaves \(q_0=1/101\) and \(P_D\approx0.005746\). Renormalization cannot restore discarded information.

The leakage expansion has the correct signs and conjugation convention. With frozen \(h=100/101\), residual disturbance variance is \(201/101\), wanted amplitude is \(s/101\), noise improves 17.05447 dB, wanted power falls 40.08643 dB, and SNR worsens 23.03196 dB. The statement that desired-containing covariance training does not automatically self-null an exactly constrained, perfectly known template is also correct. Conditioning, mismatch, finite training, and held-out transfer checks remain consequential.

The transfer exercise is useful but would benefit from answer checks and an explicit phase-uncertainty set. For four equal desired phases sharing one interferer draw,
\[
C_{\rm stack}/\sigma^2=I_8+100(\mathbf1_4\mathbf1_4^T)\otimes bb^H.
\]
I obtain \(q_{0,\rm stack}=404/401\) and \(P_D\approx0.995170\). Keeping the independent-record normalization instead gives false-alarm probability approximately 0.001510. The standardized threshold remains 3.090232 after correct normalization. For leakage uncertainty \(|\ell-\ell_0|\le\epsilon\), a useful bound is
\[
|1-h\ell|\ge\max(0,\ |1-h\ell_0|-|h|\epsilon).
\]

Actual-image observations support the mathematical checks:

- **Figure 10.1:** density peaks near 0.399, means 0 and 2.8701, and threshold just right of the signal mean are correct. Whitening both inputs is explicit. Tail shading would be optional teaching polish.
- **Figure 10.2:** the quarter-turn arrows close counterclockwise; aligned arrows add. \(L_4(45^\circ)=0.426777\) and \(L_4(135^\circ)=0.073223\) match the curve.
- **Figure 10.3:** the projected arrow points down-right, perpendicular to \(b\), with half the desired-vector length and one-quarter squared norm. Curve limits are correct.
- **Figure 10.4:** wanted leakage reaches the reference, and \(hr\) enters the negative branch. The crossing without a junction dot does not introduce an unintended connection. \(20\log_{10}|1-h\ell|\) correctly represents power-transfer dB; midpoint and endpoint are approximately −5.935 and −40.086 dB.

The complete page and crops show readable typeset equations, correctly associated captions, and coherent section progression. Main content is not clipped; cropped sidebars reflect crop boundaries. Figure text becomes smaller than body text after embedding but remains readable in the detail crops. Internal fragment targets and figure assets resolve in the supplied HTML. Navigation destinations outside this packet were not verified.

Exposure comprised the manuscript, requirements, four supplied standards, source note and source summaries, rendered HTML, four SVG assets and matching rendered copies; all four standalone PNGs; `page-full.png` at **1425×10951**; and all seven crops `k10b-crop00.png` through `06.png`, inspected before author-code review. Code review covered the extraction functions, `chapter10()`, imports, and `ExtractionModels`; other chapter implementations were not re-audited. All six extraction tests passed, and all manifest hashes matched. Independent SVG-coordinate checks agreed within rounding.

No files were changed or figures regenerated. Supplied source summaries were examined; the linked PDFs were **not freshly examined**. Hardware behavior, reader performance, browser interaction, and human acceptance were not established.