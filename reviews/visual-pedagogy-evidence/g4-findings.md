The supplied pilot meets the visual-needs requirements under its declared synthetic assumptions. **I found no consequential mathematical or figure-content error.** I recommend a positive, bounded AI visual-adequacy assessment, with minor presentation improvements below. This is not human acceptance, physical validation or evidence of educational effectiveness.

All **161 entries in `inputs.sha256` verified successfully**. The eight standalone capture records match the supplied SVG and PNG bytes; the publishing and pilot capture records match the supplied HTML. All eight SVG copies embedded in `pages/figures` match their counterparts in `figures`.

The review remained read-only. I read the requirements and manuscript/model before generator code and independently calculated the principal results.

**Presentation findings are minor.**

- Long equations extend beyond the main text column in the narrower pilot capture: notably the endpoint spectrum in [crop-02]( /tmp/vp-g4-review/pages/pilot-narrow/crop-02.png), complex-filter bridge in [crop-03](/tmp/vp-g4-review/pages/pilot-narrow/crop-03.png), residual covariance in [crop-11](/tmp/vp-g4-review/pages/pilot-narrow/crop-11.png), and uncertainty calculation in [crop-15](/tmp/vp-g4-review/pages/pilot-narrow/crop-15.png). All terms remain visible within the supplied 945-pixel-wide page. Breaking these equations would improve responsive layout.
- Dense figure legends and explanatory text shrink to approximately 10.5–12 pixels in that view. They remain decipherable in the readable crops, but larger labels or separately expandable panels would improve accessibility.
- The publishing page visibly renders “Equation Equation 8.1,” “Table Table 8.1,” and “Figure Figure 8.1.” These are editorial defects; their targets resolve correctly.
- More purposeful ticks would strengthen the teaching: mark 1000 MHz and zero residual in the calibration plot, and the architectural crossover and branch-allocation threshold in the endpoint plot.
- HTML image alternatives are meaningful. Standalone SVG descriptions are generic and refer readers to adjoining captions; richer descriptions would improve their standalone accessibility.

I found no clipped figure content, missing scientific symbol, misleading discontinuity connection, or consequential label collision in the inspected images. The publishing page’s intentional reuse of the reference-plane diagram is appropriate for its stated inclusion test.

The independent endpoint calculation used

\[
V_{\rm shared}=8S_r\int_1^{10000}\sin^2(\pi f\Delta\tau)\,df+39996b,
\]

with the common-source integrand divided by \(1+(f/100)^2\) for local synthesis. Here \(b\) is the two-sided density **per endpoint**; the independent branch difference contributes \(2b\), integrated over both frequency bands.

| Envelope / architecture | Common contribution, rad² | Total variance, rad² | SD, degrees |
|---|---:|---:|---:|
| Compact shared, 10 ns | \(2.631894455\times10^{-9}\) | \(3.999863189\times10^{-5}\) | 0.362364130 |
| Compact local, 10 ns | \(7.772447843\times10^{-13}\) | \(3.999600008\times10^{-4}\) | 1.145858294 |
| Exposed shared, 100 ns | \(2.631889312\times10^{-7}\) | \(3.999863189\times10^{-3}\) | 3.623641301 |
| Exposed local, 100 ns | \(7.772439274\times10^{-11}\) | \(3.999600777\times10^{-4}\) | 1.145858404 |

These reproduce the manuscript’s rounded table and the plotted preference reversal. The local curve appropriately remains fixed while shared-distribution branch density varies.

The 1.5° variance limit is \(6.853891945\times10^{-4}\) rad². Its per-endpoint shared-branch allocation is:

- **10 ns:** \(1.713637770\times10^{-8}\) rad²/Hz.
- **100 ns:** \(1.712986313\times10^{-8}\) rad²/Hz.

Thus the stated \(1.71\times10^{-8}\) allocation is correct. Architectural equality occurs near \(b=10^{-8}\), separately from the 1.5° feasibility boundary. Preference reversal follows primarily from the assumed independent endpoint disturbances.

I checked the sine integral against an integrated small-delay series and the local response against its small-delay analytic integral. Appropriate limits hold: equal endpoint delays cancel the common source, zero branch density leaves common-path leakage, and an infinite local-response corner recovers the shared response. A separately constructed correlated complex source model reproduced the expanded endpoint cross terms. The manuscript correctly retains complex covariance and does not filter the already output-referred branch disturbance twice.

The fixed-LO calibration arrangement and asymmetric fit also check out.

With a 990 MHz lower-side LO, training RF frequencies 999, 1000 and 1001.5 MHz map to IF frequencies **9, 10 and 11.5 MHz**; the excluded 1000.5 MHz tone maps to **10.5 MHz**. Acquisition precedes per-tone DDC and decimation. The 100 ksample/s outputs represent separated narrowband envelopes, with acquisition/channelizer phase retained unless characterized independently.

Evaluating the complete nondispersive carrier-phase law gives:

\[
\left.\frac{dm}{df_{\rm RF}}\right|_{\rm LO}
=-2\pi(\Delta\tau_{\rm RF}+\Delta\tau_{\rm fixture}+\Delta\tau_{\rm IF}),
\]

while retuning LO with RF to hold IF fixed gives

\[
\frac{dm}{df_{\rm RF}}
=-2\pi(\Delta\tau_{\rm RF}+\Delta\tau_{\rm fixture})
+2\pi\Delta\tau_{\rm LO}.
\]

The manuscript’s signs agree. Its warnings about tuning-state offsets and inseparable fixture slope are consequential and correctly placed.

For the 2 ns synthetic line:

- Training phases are 0.312566371, 0.300000000 and 0.281150444 rad.
- Mean training frequency is 1000.166666667 MHz.
- Mean-frequency intercept is **0.297905604898 rad**.
- Carrier intercept is **0.300000000000 rad**.
- Held-out prediction is **0.293716814693 rad**.
- Subtracting the mean intercept leaves **+0.002094395102 rad** carrier bias.
- Correct carrier subtraction leaves +0.012566370614 rad at 999 MHz and −0.018849555922 rad at 1001.5 MHz.

The training dots and excluded square have distinct roles. The captions correctly limit the square to checking prediction from the same synthetic model. The 0.5 MHz grid’s 2 μs ambiguity interval is also correct.

The maintenance timeline distinguishes the required epochs.

| Quantity | 10 ms snapshot | 50 ms snapshot |
|---|---:|---:|
| Wanted-data gate relative to center | [−0.025, +0.105] s | [−0.045, +0.125] s |
| Invalid fraction at \(P=2\) s | 6.5% | 8.5% |
| Correction age when applied | 0.105 s | 0.125 s |
| Oldest age before replacement | 2.105 s | 2.125 s |
| Snapshot-center bias bound | 0.00054° | 0.00270° |
| Drift bound including center bias | **0.45522°** | **0.46170°** |
| Maximum permitted center separation | 2.207314815 s | 2.177314815 s |

The sawteeth retain the old coefficient through the gated interval and step down when its replacement applies. Their maxima conservatively include that invalid interval.

Independent sinc-squared integration reproduced phase-average SDs of **0.025352838°**, **0.080172706°**, and **0.034378823°** for compact/10 ms, local/10 ms, and local/50 ms respectively. Adding the independently assumed 0.03° remaining standard uncertainty in quadrature gives **0.039278065°**, **0.085601768°**, and **0.045627881°**. These support the stated snapshot choices. Standard uncertainty remains separate from the deterministic drift bound.

The constant-versus-updated correction treatment is correct. Zero-sum observation weights cancel a frozen coefficient pointwise, including when it is correlated with the measured process. Update steps require their actual observation mask and covariance propagation.

For independent equal-variance centered held errors, uniformly randomizing the grid origin gives the same-cell probability \((1-|\tau|/P)_+\). Its Fourier transform is

\[
R_c(\tau)=v_c(1-|\tau|/P)_+,\qquad
S_c(f)=v_cP\,\operatorname{sinc}^2(fP).
\]

I checked the triangle transform numerically, its zeros and sidelobe values, and spectral-area convergence to \(v_c\). The displayed interval \(|fP|\le3\) contains approximately **0.966410435** of the total normalized area; the remaining tails are consistent with the finite plotting range. Fixed-origin examples at identical lag gave different covariances, confirming why the stationarity qualification matters. The illustration appropriately separates its deterministic staircase from the stochastic model.

The measurement-chain and swap signs are consistent with fixed output labels:

- A characterized input-fixture exchange reverses the reversible fixture/source-path contribution while fixed receiver, LO and readout terms retain their assignments.
- A Q-input exchange reverses the pre-Q comparison; fixed readout asymmetry can remain.
- A whole-receiver exchange requires tracing the new assignments.
- Separate acquisitions share \(\delta_Q\), so \(m-m'=\epsilon-\epsilon'\).

The latter cancellation is algebraic and does not establish absolute accuracy. I independently constructed a common-error covariance example: the differenced variance was **0.0013**, whereas incorrectly treating the two readings as independent gave **0.1013** in the same squared units. The figure and prose preserve this distinction.

The guarded-decision boundaries are correct. For \(L=1\), \(U=0.2\), the five intervals are [0.3, 0.7], [0.6, 1], [0.8, 1.2], [1, 1.4], and [1.3, 1.7]. An upper endpoint equal to \(L\) supports acceptance under the bound; a lower endpoint equal to \(L\) remains inconclusive. Rejection requires the lower endpoint strictly above \(L\). The bound is explicitly distinguished from SD and automatic coverage.

The complex-filter bridge is appropriately bounded and connected to Chapter 3. It normalizes by nonzero carrier gain, takes real and imaginary parts of the **impulse response**, retains AM-to-PM coupling, and requires a small filtered carrier-relative perturbation. Chapter 3 additionally controls the filtered input-linearization remainder. Carrier notches, large normalized gains, fades, aliasing and other omitted implementation effects are identified. The pilot’s ideal band selector is explicitly post-extraction phase filtering.

Source/reference assumptions are similarly bounded: the common reference density is output-equivalent, multiplier phase gain requires corresponding squared PSD gain, and equal frequency does not fix endpoint phase or restart state. Synthetic spectra, timing assumptions and hardware-performance evidence remain distinguishable.

For Chapters 1–7, the supplied manuscripts and HTML support a coherent progression: physical planes and conversion signs → ensembles/circular phase/noise → observation operators and complex filtering → source-built covariance → local precision and ambiguity → approximation/model adequacy → wanted-signal retention and recovery. The pilot applies these results to architecture, calibration and measurement decisions. Its cross-chapter links resolve to supplied HTML anchors, and the scoped introductory treatments do not claim to supersede the pilot’s general calibrated-residual analysis. The rendered state sequence supplies explicit invalid-data gating and return through qualification steps.

I did not repeat the Chapters 1–7 mathematics/illustration batch reviews or inspect their separate chapter pixels.

Exact image coverage was:

| Coverage | Images inspected |
|---|---|
| Eight standalone PNGs | `relative-phase-reference-planes`, `endpoint-architecture-budget`, `calibration-fixed-lo`, `calibration-delay-fit`, `calibration-maintenance`, `correction-updates`, `measurement-swaps`, `guarded-decisions` |
| Complete page PNGs | `pages/pilot/image.png` (1425×25846), `pages/publishing/image.png` (1440×2200), `pages/pilot-narrow/image.png` (945×27670) |
| Every readable crop | Pilot `crop-00`–`crop-16`; publishing `crop-00`–`crop-01`; narrower pilot `crop-00`–`crop-17` |

That is **48 PNGs**, including all 37 crops. The crops are pixel-identical full-width slices and collectively cover each complete page. The integrated state-sequence figure was inspected in both pilot widths. Actual-image inspection was supplemented by numerical checks of SVG curve vertices; tested curves agreed with independently derived coordinates within 0.0005 SVG unit.

Unavailable evidence includes hardware characterization, measured spectra and covariance, actual acquisition/filter performance, restart experiments, reader trials, specialist acceptance, and the external source passages/source notes referenced by the manuscript. External citations were not freshly validated because this review was restricted to supplied files. Keyboard/screen-reader behavior and widths below the supplied narrower capture were not tested. SciPy was unavailable; NumPy quadrature, analytic alternatives and refinement completed the calculations.

Incidental exposure: supplied capture metadata identifies original-project and rendering-staging paths outside the packet. Requirement/manuscript prose also contains administrative status and historical-work wording. Those locations were not accessed, and those assertions were excluded from correctness evidence. No connectors, delegation, edits or original-repository access were used.