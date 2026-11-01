All **365 manifest hashes match**, including a repeat check after testing. No duplicate entries or unlisted payload files were found; only `SHA256SUMS` is outside its own manifest. No files were changed.

I found one substantive procedure gap and four smaller issues:

1. **Medium — operational offset handling is unstated.**
   [Chapter 23](/tmp/k2022/k21-input/book/calibration-procedures-coherence.qmd:80) reports held-out waveform and DC performance, but [the execution](/tmp/k2022/k21-input/engineering/examples/calibration_models.py:51) generates offset-free operational records after supplying nonzero offsets during calibration. Phase cycling removes offsets from the calibration projection; it does not remove them from subsequent science samples.

   Retaining the supplied \(b_B=3-j1\) mV produces **129.464%** held-out record error and DC gain **\(1.808023-j0.343275\)**. The text should either declare these offsets exclusive to the calibration observation instrument, or specify operational offset estimation/subtraction and its uncertainty. Subtracting the science-record mean would destroy wanted DC information.

2. **Low — the fixture-omitted residual needs an explicit estimator label.**
   [Chapter 23](/tmp/k2022/k21-input/book/calibration-procedures-coherence.qmd:49) carefully distinguishes the nominal unconstrained and selected real-echo residuals, but the following **6.5886%** comparison uses the unconstrained fit. With the fixture omitted, the selected real-echo residual is **46.13446%**, the discarded echo imaginary part is **−0.553909**, and \(\hat a=1.648579\). Label both residuals and flag the resulting correction-feasibility failure.

3. **Low — the common-fixture uncertainty shortcut needs its approximation stated.**
   [The implementation](/tmp/k2022/k21-input/engineering/examples/calibration_models.py:82) adds \(0.002^2+0.001^2\) directly to the maximum reading variance. For its target-normalized output \(R=QH/T\), physical propagation gives fixture variance
   \[
   |R(f)|^2(0.002^2+0.001^2).
   \]
   Constructing shared amplitude/phase errors across all training frequencies and propagating them through the selected fit gives approximately **0.223878%**, versus the reported **0.223809%**. The difference is small and does not change the example’s conclusion, but exceeds the displayed precision.

4. **Low — the swap exercise should explicitly include the discrete ambiguity.**
   [Chapter 13.1’s exercise](/tmp/k2022/k21-input/book/calibration-observability-metrology.qmd:104) should distinguish common reference freedoms from the remaining phase branch. With \(h=H_B/H_A\), \(p=P_B/P_A\),
   \[
   r_1=hp,\qquad r_2=h/p,\qquad h^2=r_1r_2.
   \]
   Both \((h,p)\) and \((-h,-p)\) fit. Unique relative phase requires additional branch information. An unknown phase change during reconnection preserves identifiable magnitude under the stated phase-only fault, but destroys phase identification.

5. **Low — Figure 13.1 exposes literal mathematical markup.**
   [The actual asset](/tmp/k2022/k21-input/images/view-0.png) displays `Y_ik`, `P_i^cal`, and similar underscore/caret notation. Geometry and signs are correct, but subscripts and superscripts should be typeset consistently with the adjoining equation.

Independent read-only calculations reproduced the principal published results:

| Quantity | Independent result |
|---|---:|
| Unconstrained / selected training residual | 0.003627595% / 0.007247472% |
| Integer held-out record error | 0.036752040% |
| Nominal signed-grid maximum error | 0.038137678% |
| Changed gain / changed echo maximum error | 3.619510% / 7.523187% |
| Offset-free DC gain | \(0.999784470+j0.000047684\) |
| Coefficient energy / output noise RMS | 1.929113374 / 27.778505 μV |

Additional challenges established:

- Common-source and independent fixture gauges preserve observations; phase cycling rejects constant offsets while retaining synchronous leakage. An external-path phase change remains invisible to downstream injection.
- A single unnormalized conjugate conversion defeats common-source phase cancellation. The four training frequencies also admit a **32-sample delay alternative with a gain-sign reversal**, confirming why the known-delay assumption matters.
- Independent integer arithmetic reproduced the held-out result and maximum accumulator magnitude **21,881,069,915**. The finite inverse is causal; the estimation advance does not enter runtime filtering.
- Ratio-noise covariance and the real-coordinate fit/correction Jacobian agree with independent differentiation. A physical common fixture model has two shared real latent errors and nonzero complex pseudocovariance; it does not average down with repetitions. A 60,000-realization check supported the uncertainty scale.
- Maintenance arithmetic gives \(10\le C\le14.85\) s for the short burst, age **10.15 s**, and envelope **0.00806 rad** at \(C=10\) s. The one-second burst is infeasible. Doubling drift and allowing 1% downtime gives incompatible bounds **\(C\ge20\) s** and **\(C\le7.35\) s**. Failed bursts must preserve evidence age; an unbounded outage phase jump invalidates extrapolation immediately.
- Wanted-transfer magnitudes at 0.01 Hz are **0.099503719**, **1**, and **0.901044498** for the three models. Shared science measurement noise follows \(|1-L|^2\), not an independent-noise sum.

All **12 supplied calibration/alignment tests passed** under `python -B`.

Visual coverage was **17/17 actual images**: four assets `view-0`–`view-3`; complete pages `view-4`–`view-5`; all three Chapter 13 crops and seven Chapter 23 crops; and smoke `view-6`. Every crop exactly matches its complete-page pixels, with overlap and coverage through both bottom navigations. All **3,856 curve vertices** agree with independent equations within SVG rounding precision. Axes, units, logarithmic scales, thresholds, arrows, captions, and displayed equations were checked. Navigation targets exist: Chapter 13 links to 12/14; Chapter 23 links to 22/24, with 24 visibly titled “Mathematical Publishing Proof of Concept.” The smoke disk has the expected 120-pixel diameter.

The interface/evidence requirements and fixed, periodic, and pilot-tracking alternatives are appropriate as supplied contracts. RF fixture terminology remains an evidence requirement rather than a demonstrated physical implementation. No future state/environment methods were audited.

Original source PDFs are absent, so source authentication and original-source figure inspection were unperformed; source claims were checked only against packet notes and bibliography. No fresh browser execution, instrument measurements, hardware timing, specialist validation, or reader validation was performed. This review grants no acceptance authority.

Inadvertent exposure: ancillary source notes for model adequacy, tracking, and phase comparison contained prior-examination/review-status metadata. That metadata was excluded from the evidence; no separate prior-review, history, status, or preface document was opened.
