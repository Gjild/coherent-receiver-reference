All **398 SHA-256 manifest entries match**. The targeted calculations and plotted geometry checked here show no consequential mathematical error. One low-severity reading-path ambiguity remains.

**Findings**

- **Low — ambiguous future chapter number.** [Chapter 13, line 408](/tmp/k2022/connected-input/book/calibration-observability-metrology.qmd:408) and [Chapter 23, line 165](/tmp/k2022/connected-input/book/calibration-procedures-coherence.qmd:165) assign formal evidence decisions to “Chapter 24,” while the displayed sidebar numbers the publishing demonstration 24. The preface explains the temporary supplement numbering, so canonical ownership is recoverable, but a reader entering these chapters directly can follow the wrong destination. Naming the planned canonical treatment alongside its number would remove that ambiguity. This affects navigation, not the calculations.

No additional essential bridge was found missing **within the supplied bounded examples**. Complete state sequencing, physical implementation and instrument qualification remain external contracts; their methods were not presumed available merely because Chapters 21/22 have reserved slots.

**Independent mathematical and graphical checks**

For uniform area on the touching disk, independently changing to polar coordinates gives

\[
(r\cos\phi-1)^2+(r\sin\phi)^2\le1
\quad\Longrightarrow\quad
0<r<2\cos\phi,\quad |\phi|<\pi/2.
\]

Consequently,

\[
p_\phi(\phi)=\int_0^{2\cos\phi}\frac r\pi\,dr
=\frac{2\cos^2\phi}{\pi},
\]

with zero density outside that interval. Its integral is one, symmetry gives mean zero, and

\[
\operatorname{var}\phi=\frac{\pi^2}{12}-\frac12
=0.3224670334,\qquad
u_\phi=0.5678618084\ {\rm rad}.
\]

Independent midpoint integration reproduced normalization and variance; an independently sampled uniform-area disk gave variance approximately 0.322482.

The manuscript’s distinctions are sound:

- Uniform area assigns zero probability to the boundary point \(z=0\). Adding an atom there requires an invalid-phase outcome or explicit conditioning.
- A disk containing zero admits every direction geometrically; that fact alone supplies no angular probability law and does not prohibit scalar principal-phase reporting.
- The specified principal branch supports this calculation. Complex-voltage uncertainty alone cannot identify an unwrapped cycle count.
- Linearization gives \(u_\phi=0.5\) rad and understates the exact result. Even here, \(\pm u_\phi\) covers approximately **65.02%**, illustrating why standard uncertainty is not automatically a specified coverage interval.

The new raster geometry agrees quantitatively. In `disk-full.png`, the blue circle spans approximately \(x=199\ldots675\), \(y=174\ldots650\), preserving equal scales. The orange diameter is about 1.10 times larger. The density curve is near \(y=962\) at zero phase and \(y=1073\) at \(\pi/4\), matching \(2/\pi\) and \(1/\pi\) on the displayed axes. The ray, tangency, larger containing outline and density labels communicate the intended distinction.

For loading, independently differentiating the **test/target ratio** gives

\[
\delta c_L\big|_{Z_s}
=\operatorname{Im}\!\left[
\left(\frac1{Z_s+50}-\frac1{Z_s+Z_L}\right)\delta Z_s
\right].
\]

Finite differences agreed at both the worked point and an asymmetric complex-source example. At \(Z_L=45+j5,\ Z_s=50\), the source-coordinate sensitivities are approximately

\[
(0.000552486,\;-0.000497238)\ {\rm rad/\Omega}
\]

for real and imaginary source impedance. They vanish when test and target loads coincide. The worked loading factor, phase correction and load-only uncertainty reproduce:

\[
0.47513812+j0.02762431,\quad
0.0580741596\ {\rm rad},\quad
0.0023216609\ {\rm rad}.
\]

Thus the existing budgets remain consistent for the stipulated known source impedance. Uncertain source impedance requires additional sensitivities and covariance; differentiating test voltage alone would be incorrect.

Other important results reproduced:

| Check | Recomputed result |
|---|---:|
| \(N=100,\rho=0.9\): effective mean count | 5.813937 |
| Variance-estimate moment degrees of freedom | 11.401075 |
| Correlated reading-mean uncertainty | 0.003519096 rad |
| Combined uncertainty, original configuration | 0.004772226 rad |
| Reversal result / combined uncertainty | 0.101239811 / 0.003851250 rad |
| Independent-reference combined uncertainty | 0.012663906 rad |
| Changed \(\rho=0.99\): \(N_{\rm eff},\nu\) | 1.361018, 3.162204 |
| Changed \(\rho=0.99\): combined uncertainty | 0.007955607 rad |
| Inside/outside-zero finite residuals | 0.0282111%, 0.0792282% |
| Corresponding target delays | 0.3125 μs, 2.3125 μs |
| Coefficient energies | 1.92901219, 2.19478600 |
| Changed echo, retained correction | 7.5261%, 11.9113% |
| Deep-attenuation DC-phasor SNR | 19.084850 dB |
| Different white-sample-noise observation | 39.041202 dB |
| Short-burst feasible cycle interval | 10–14.85 s |
| One-second burst constraints | \(C\ge50\) s, \(C\le15.83197\) s: incompatible |
| Doubled drift, 1% downtime | \(C\ge20\) s, \(C\le7.35\) s: incompatible |

The two supplied CSV means and correlation-corrected variance estimates reproduce. The moment degrees of freedom do not create an exact chi-square or Student interval. Positive covariance between the two subtracted correction estimates enters with a **positive** cross term; it cannot be deleted because both are “corrections.” A reversal-induced load change likewise survives the nominal fixture cancellation.

The finite-inverse polynomial identities agree to approximately \(2.3\times10^{-16}\). Independently calculated coefficient-rounding bounds reproduce the stated extra response errors. Chapter 19’s packet calculation gives the stated **239216-byte** peak with a release at outage onset; shifting the first release by 64 μs changes the peak, confirming its dependence on the declared packet timing. The 9.28 Goperations/s arithmetic count, 1 MiB coefficient table and approximately 34 s fixed-consumer FIFO exhaustion also reproduce.

**Confirmations on the connected argument**

- **Observability and access:** Chapter 13 correctly distinguishes common-source cancellation from fixture identification, absolute reference freedom, swap sign ambiguity and bypassed sensor/field response. Repeated measurements do not repair a rank deficiency.
- **References and physical planes:** Chapters 15–19 preserve the distinction between delivered reference phase, clock coordinate, aperture epoch, effective filtered epoch and transport arrival. Chapter 20’s common-input model is explicitly restricted; it does not silently become an array manifold.
- **Acquisition and wanted DC:** Chapter 23 separates phasor-readout offsets from raw operational offsets. Its known-zero acquisition explicitly requires preserved loading/state, settling and offset constancy. Subtracting that independently identified offset preserves wanted DC; subtracting the science mean would not.
- **State and age:** Fixed loading, reference state, identified sample support, coefficient version/application sample and evidence age are explicit conditions. Failed bursts do not renew evidence, and an unknown phase jump invalidates extrapolated holdover.
- **Correction feasibility:** The causal and future-data inverse constructions, finite-delay approximation, word ranges, accumulator checks and noise injection planes connect coherently. A true steady-state DC null and irreversible channel combination are correctly distinguished from finite attenuation.
- **Wanted information:** The pilot/science transfer equation preserves the wanted/nuisance distinction. At 0.01 Hz the science-derived tracker retains only **0.0995037** of wanted amplitude; the contaminated pilot retains **0.9010445**. Shared science noise must retain its covariance.
- **Uncertainty versus bias:** Correction knowledge, correlated record noise, coherent leakage bounds and deterministic maintenance envelopes remain separate. The passing standard-uncertainty allocation does not excuse the failing low-level coherent-bias allowance.
- **Held-out sensitivity:** Signed-frequency, waveform, actual DC and changed-state checks address different failure mechanisms. Neither a small training residual nor a successful old waveform authorizes changed loading, gain, echo or reference conditions.

The **final K20 clarifications are correct**. The zero-mean assumption makes the displayed regularized RMS decomposition valid for fixed nonzero \(S\); a nonzero noise mean introduces the stated bias/cross-term requirement. The visible label \(\lvert H_B(0)\rvert=0.9(1-a)\) correctly identifies the magnitude over the plotted \(a<1\) range. These clarifications agree with the actual deep-attenuation curves and adjoining prose.

Canonical ownership is otherwise consistent: propagation remains in Chapters 4/6, inference in 5, wanted-transfer reasoning in 7, fields in 8, inverse feasibility in 20, measurement freedoms/metrology in 13, and procedure/maintenance in 23. The checked references in 16–19 and the final Chapter 19 bridge use those destinations. The preface describes the alternative frequency plan and reading connections accurately. Its provisional-status language was treated only as manuscript wording, not technical evidence. Repeated local equations generally serve different observation models rather than duplicate competing general theories.

**Actual PNG coverage**

All **31 attached PNGs** were inspected. Crop-to-full-image comparisons also established exact pixel identity and coverage.

| Images | Readable coverage and limits |
|---|---|
| `13-full`, `13-detail-00`–`09` | All ten detail crops overlap and cover rows 0–13227 completely, including final exercise and bottom navigation. All five figures, equations and surrounding text were readable through the crops. |
| `19-full`, details `12`–`13` | Full-page structure and bottom coverage inspected; readable detail covers rows 16800–18667, including queue/resource figure and final reading bridge. Earlier full-page body text is too reduced for reliable pixel proofreading. |
| `20-full`, details `05`–`06` | Readable detail covers rows 7000–10000, including the RMS clarification, deep-null discussion and Figure 20.4. Earlier text and the final 435 rows lack readable detail coverage. |
| `23-full`, details `00`, `03`, `05`, `06` | Readable intervals: 0–1600, 4200–5800 and 7000–9492. Gaps 1600–4200 and 5800–7000 include much of the application/held-out treatment and cadence example/figure. Those were reviewed from source, without claiming readable pixel verification. Bottom exercise/navigation is readable. |
| Preface full and both details | Entire page readable across overlapping crops, including concluding reading guidance and bottom navigation. |
| Five standalone technical figures | Disk, alignment access/noise, calibration access and metrology access inspected at readable scale. Signal/injection arrows, shared-reference branches, legends and annotations were intact; no consequential clipping or overlap found. |
| `smoke-full` | Visible blue circle, “Radius 60 px” and text inspected. This was the supplied smoke capture, not a newly executed smoke test. |

In Chapter 13, the correlation and variance-information panels remain distinguishable, the leakage plot visibly crosses the separate bias limit, and the final crop includes the complete decision and transfer exercise. Full-page reductions establish layout continuity and bottom presence; they do not substitute for readable text inspection.

**Checks performed and limits**

Read the packet requirements, accepted excerpts and applicable local standards, manuscript material and current source notes before code inspection. Ran independent calculations with `python -B` and **21 affected metrology/alignment/calibration tests; all passed**. No generator/save entrypoints were invoked.

Original external sources were not authenticated or reopened; source-note descriptions were assessed as supplied evidence. No hardware, physical calibration, reader trial, live browser rerender, PDF/mobile/accessibility evaluation or comprehensive regression of Chapters 1–19 was performed.

No prohibited exposure was identified. No excluded reviews/dispositions, history, author conversation, current-work/status records, connectors or files outside the frozen packet were opened. Capture-origin paths were not followed. No files were edited.

This AI scrutiny supplies no human specialist, hardware or reader acceptance.
