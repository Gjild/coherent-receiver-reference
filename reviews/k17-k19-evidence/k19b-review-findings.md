The principal scientific and numerical results reproduce. I found one moderate reader-facing inconsistency and two minor presentation issues; no major mathematical defect emerged from the checks below.

All **346 SHA256SUMS entries match**, including `book/index.qmd` and `rendered/index.html`, which were hashed only as opaque bytes. Review remained read-only.

**Findings**

| Severity | Location | Finding |
|---|---|---|
| Moderate | [Manuscript, line 516](/tmp/k1719/k19b-input/book/multirate-finite-resources.qmd:516); `page-12.png` and `page-13.png` | The prose assigns general correction feasibility to “Chapter 20,” but the rendered navigation identifies Chapter 20 as **Mathematical Publishing Proof of Concept**. The canonical K20/K23 boundaries are appropriate, but the current reader cannot follow these numbered references reliably. Distinguish planned canonical chapters from the numbered development supplements. |
| Minor | Figure 19.3; `asset2.png`, `page-05.png` | At the displayed scale, the eight-point/16 MS/s phase curve is effectively indistinguishable from zero. Its independently calculated maximum is approximately **0.0009654°**. The conservative bound is stated correctly, but a small numerical annotation or inset would make the actual improvement visible. |
| Minor | Figure 19.4; `asset4.png`, `page-08.png` | The RMS-error ordinate is logarithmic, but the axis does not explicitly identify that scale. The unusual ticks—0.1, 0.447, 2, 8.94, 40—make comparisons less immediate. Labeling the scale and using conventional logarithmic ticks would improve instruction. |

**Independent scientific and numerical results**

- **Real mixing and aliases:** Expanding the real cosine produces both translated partners. Positive 20/30/40 MHz become 0/10/20 MHz; negative partners become −40/−50/−60 MHz. At 16 MS/s, −50 MHz folds to −2 MHz. The nearest wanted-band alias intervals are ±[14,18] MHz; therefore the stipulated stopband beginning at 6 MHz is deliberately stronger. The two-blocker phasor allocation gives **114.183053 dB**, consistent with the text.
- **Epoch and channelizer:** Symmetry gives \(H(f)=e^{-j2\pi fD/F_s}B(f)\), hence the stated effective epoch \((8m+r-128)/F_s\). The **1 μs group delay**, **2 μs fresh-history interval**, and delivery latency describe different events. Direct calculations with a nonzero origin reproduced the channelizer factor \(e^{-j2\pi\ell r/M}\) and positive-sign Fourier sum; omitting the origin factor produced substantial errors.
- **Continuous-frequency bound:** The centered-response curvature argument is valid for complex interpolation; it does not require treating real and imaginary errors separately. Independently generated Bessel-series coefficients gave \(K_2=1.27704005\times10^{-12}\,\mathrm{Hz}^{-2}\) and remainder **\(9.51468981\times10^{-9}\)**.

| Filter calculation | Independent result |
|---|---:|
| Unrounded sampled stop rejection | 118.166372 dB |
| Unrounded continuous-frequency rejection bound | 118.099713 dB |
| F17 rounded rejection bound | 81.704748 dB |
| F23 rounded rejection bound | 114.545493 dB |
| F29 rounded rejection bound | 118.092735 dB |

F17 and F23 fail even at sampled frequencies, so their rejection is not merely an inconclusive conservative-bound result. F29’s passband bounds also reproduce. These numerical evaluations use floating arithmetic, rather than interval-certified FFT calculations.

- **Lagrange interpolation:** The complex divided-difference remainder is sound. I obtained **0.000154645455** for the uniform isolated-tone bound. The maximum absolute-weight sum is exactly **1.48828125**: writing \(s=\mu(1-\mu)\), the sum becomes \(1+11s/6+17s^2/36+s^3/36\), maximized at \(\mu=1/2\). The midpoint independent-noise variance factor is **0.745332718**.
- **Rate change:** At 8 MS/s, the unchanged eight-point interpolator reaches **−0.195034 dB** amplitude error and **0.315120°** phase error. At 4 MS/s, the old filter’s approximately **0.4999993** response at translated 4 MHz folds onto zero, confirming the stronger failure.
- **Remote clocks:** The forward mapping \(q=F_B(\alpha t+\beta)\) has the correct orientation. Substituting estimated parameters yields epoch error \((t\,\delta\alpha+\delta\beta)/\alpha\). The stated envelope gives **0.504° at 2 MHz**; a separate 0.01° allocation requires **13.8889 ps**. Baseband alignment or DC insensitivity does not establish RF/LO coherence.

**Word arithmetic, composition and state**

Independent integer calculations, using rational nearest-even rounding and checking every FIR addition, reproduced:

| Case | RMS processing error | Wrap events |
|---|---:|---:|
| F17 / 72-bit FIR | 21.871555 μV | 0 |
| F23 / 72-bit FIR | 0.376538 μV | 0 |
| F29 / 72-bit FIR | 0.190134 μV | 0 |
| F29 / 56-bit FIR | 8.185090 mV | 208,040 |

The controlled component bounds are approximately **1.43514 V** after mixing, **2.19946 V** after FIR filtering, and **3.27341 V** after interpolation. The FIR bound is **\(3.24583\times10^{20}\)** integer units, requiring 70 signed bits at F67. The selected 72-bit/F67 and 56-bit/F50 accumulators have different ranges and cannot be compared by width alone.

The independently reconstructed joined modulated pipeline produced **984 outputs**, **0.006179149%** normalized error, fitted phase **−0.00000625289°**, and epochs **1.230–62.6675 μs**. Checking its resampler’s intermediate sums also found no overflow.

The asynchronous examples reproduced **0.009108466%**, **0.009126570%**, and **0.010415927%** for floating, quantized-coefficient, and integer processing respectively.

The NCO tuning-word decisions reproduce. State-fault simulations settled to **−90°** after the positive NCO phase step and **+56.25°** after loss plus renumbering. A known missing raw index contaminates the stated **33 FIR outputs**, with fresh support at index **2312**. For the specific subsequent interpolation \(q=k-0.32\), that contamination expands to **40 interpolated output positions**; the manuscript correctly requires this further support propagation.

**Resources, transport and timing**

The arithmetic count reproduces: **16.448 G** direct FIR MACs/s, **8.256 G** using symmetry, and **9.28 G** including mixing and interpolation. Forty-eight qualified lanes at 250 MHz imply **77.33%** simplified utilization. The table requires **1 MiB** and **512 MB/s** of coefficient reads before distribution.

The packet calculations reproduce **192.75 MB/s** packed and **256.75 MB/s** padded. An independent event calculation found:

- Packed peak: **239,216 bytes at 512 μs**, with no modeled loss.
- Padded case: **105,056 bytes lost** over the six-millisecond simulation.
- Fluid recovery: **2.03968254 ms**; outage-duty ceiling **19.6875%**.
- Initial headroom consumed by the stated 20 ppm mismatch: **34.0005 s**.

Five fresh executions of the supplied integer FIR/NCO function took **0.098830–0.102244 s**, median **0.0990711 s**, approximately **82,688 inputs/s**. This independently confirms rejection for a 128 MS/s stream. It does not authenticate the manuscript’s earlier five timings or establish a maximum host capability.

All **eight scoped multirate tests passed**.

**Actual-pixel review**

I inspected all **22 supplied PNGs**: six asset rasters, the complete page, fourteen overlapping crops, and the fresh smoke image. Pixel comparison confirmed that every crop exactly matches its corresponding full-page region; together they cover **all 18,370 rows without gaps**, including the final navigation.

The six assets have readable legends, units and annotations. Mixing arrows and delay/transport geometry are coherent; filter masks and rejection signs agree with the calculations. Fractional-delay curves have the expected symmetry, and the state-fault plot visibly settles at the stated signed phases. The queue’s packet steps, capacity clipping and eventual packed-stream drainage agree with the event calculation.

Across `page-00.png` through `page-13.png`, displayed equations, equation numbers, tables and captions remain within the content column; I found no visible mathematical-width collision. Crop-edge cuts are overlaps, not missing page content. The six rendered alt texts agree with their figures, although they are qualitative descriptions rather than numerical substitutes. The smoke image visibly contains the labeled blue circle; it provides display evidence only.

**Limits and missing checks**

The source notes record author examination of external documents. I accessed those notes, **not authenticated original PDFs or source-diagram pixels**.

Still absent are a streaming test of frequency/rate/coefficient changes at declared application samples, end-to-end validity propagation through packet loss and resampling, the original raw timing record, and positive device-specific scheduling, routed timing, CDC and sustained-interface evidence. These are limits on demonstrated implementation behavior; the chapter generally states those limits accurately.

The learning progression is effective: physical translation leads to finite-filter decisions, then timing, word arithmetic and transport. Useful alternatives remain conditional: for example, **F24 already gives a 116.570376 dB filter-only bound**, but reducing precision would require renewed arithmetic and joined-pipeline checks. K16 clock estimation, K20 inverse feasibility and K23 complete recovery integration should remain external.

The initial shell path discrepancy resolved to two names for the **same directory and inode**. Only packet filenames were listed before that was established; no outside material, prohibited status/history contents, or index contents were interpreted.

This AI review confers no human acceptance or hardware qualification.
