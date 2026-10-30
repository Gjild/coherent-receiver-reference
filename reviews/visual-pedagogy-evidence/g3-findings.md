The four scoped figures support the teaching argument, and I found **no consequential mathematical error, incorrect plotted value, broken validity path or unreadable scoped figure** in the supplied desktop renders. I support a bounded positive visual-adequacy recommendation. This is AI review, not human acceptance or hardware validation.

All **98 entries in `inputs.sha256` passed**. The four standalone SVGs also match their page-embedded copies byte for byte.

**Findings and optional improvements**

- In [Figure 7.2](/tmp/vp-g3-review/images/tracking-transfer-budget.png), explicitly label the lower panel’s **vertical axis as logarithmic**. Its ticks correctly implement that scale, but only the horizontal axis declares it.
- In [Figure 7.1](/tmp/vp-g3-review/images/tracking-loop.png), clarify that \(k(e+n)\), rad/s, is the command **inside the combined gain/oscillator block, after multiplication by \(k\)**. The connection entering that block carries \(e+n\), rad. The equations are correct; the annotation’s placement could confuse a reader tracing units.
- Mark the two RMS criterion crossings and label the existing 10 and 100 Hz example dots. This would connect the curve, table and feasible interval more directly.
- In [Figure 9.2](/tmp/vp-g3-review/images/relative-phase-state-sequence.png), add “all checks pass” beside the downward progression and a nearby reference to the separate acquisition/instrument tests. The existing caption and surrounding protocol already supply the necessary distinction.
- The pilot measurement equation extends substantially into the right gutter in `pilot-state/crop-09.png`. It remains visible, but a multiline equation would improve layout.

These are presentation improvements, not demonstrated failures of the scoped models.

**Independent mathematics and numerical checks**

Starting from
\[
s\widehat\Theta=k(\Theta+N-\widehat\Theta),
\]
with zero initial conditions,
\[
T=\frac{k}{s+k},\qquad E=\frac{s}{s+k}=1-T.
\]
Consequently,
\[
\widehat\Theta=T\Theta+TN,\qquad
e=E\Theta-TN,\qquad
e+n=E\Theta+EN.
\]

Thus detector noise enters the true residual with a **negative filtered contribution**, while its direct contribution remains in the detector reading. Adding the estimate to the true residual reconstructs \(\theta\); adding the detector reading reconstructs \(\theta+n\).

For \(k>0\), the pole is \(-k\). The phase-step response \(\Delta e^{-kt}\), constant-rate steady error \(\Omega/k\), and initial-condition solution all agree with the manuscript. Nonzero initial conditions require the additional transient.

With \(r=|f|/f_c\), \(f_c=k/(2\pi)\),
\[
|T|=\frac1{\sqrt{1+r^2}},\qquad
|E|=\frac r{\sqrt{1+r^2}}.
\]
The upper transfer plot has the correct limits and crossing: both magnitudes equal \(1/\sqrt2\) at \(r=1\). The complementary identities are \(T+E=1\) and \(|T|^2+|E|^2=1\); the magnitudes themselves do not sum to one.

At 1 Hz with \(f_c=100\) Hz, I obtain:

| Wanted-phase output | Amplitude gain |
|---|---:|
| True residual | 0.00999950004 |
| Estimate | 0.999950004 |

The residual removes approximately 99% of the wanted amplitude. Wanted and nuisance phase entering the same input receive the same transfer.

For the declared two-sided detector-noise PSD,
\[
v_n=2S_0\int_0^B\frac{df}{1+(f/f_c)^2}
=2S_0f_c\arctan(B/f_c).
\]
This equals the manuscript’s \(S_0k\,\arctan(2\pi B/k)/\pi\). Independently implemented Simpson integration reproduced the analytic variances at 10 and 100 Hz to displayed floating-point precision.

For \(S_0=10^{-6}\) rad²/Hz, \(B=1000\) Hz and \(\Omega=\pi\) rad/s:
\[
R(f_c)=\sqrt{2S_0f_c\arctan(1000/f_c)+(0.5/f_c)^2}.
\]

| \(f_c\) | Centered noise SD | Deterministic bias | Combined RMS |
|---|---:|---:|---:|
| 10 Hz | 0.005587122 rad | 0.050000 rad | 0.050311191 rad |
| 100 Hz | 0.017153004 rad | 0.005000 rad | 0.017866884 rad |

The 0.02 rad crossings are **28.27159454 and 134.33399559 Hz**, consistent with the rounded figure and caption. Over that interval, 1 Hz residual retention is only approximately **0.03535–0.007444**. No joint wanted-signal feasibility follows without a retention requirement.

The limiting cases also check:

- \(B/f_c\to\infty\): \(v_n\to S_0k/2\).
- One-sided transfer integral: \(k/4\) Hz; two-sided integral: \(k/2\) Hz.
- At fixed finite \(B\), \(f_c\to\infty\): \(v_n\to2BS_0\), rather than growing indefinitely.
- For detector noise alone, detector-reading variance is \(2BS_0-v_n\), further demonstrating its difference from true-residual variance.

For the nonlinear model \(\dot e=\Omega-k\sin e\), equilibria satisfy \(\sin e=\Omega/k\). At \(\Omega/k=0.5\), the plotted equilibria are correctly located at \(\pi/6\) and \(5\pi/6\), with normalized slopes \(-0.8660254\) and \(+0.8660254\): stable and unstable respectively. At equality,
\[
e=\pi/2+\delta\quad\Rightarrow\quad
\dot\delta=k(1-\cos\delta)\simeq k\delta^2/2,
\]
giving attraction from below and departure above. At ratio 1.5, normalized rate remains between 0.5 and 2.5, so no equilibrium exists. Negative offsets give the corresponding reflected cases.

For holdover,
\[
|e(t)|\le e_{\max}+2\pi\int_0^t|\Delta f(u)|\,du.
\]
The declared bounds yield \(0.02+2\pi(0.1)t\), reaching 0.1 rad at **0.1273239545 s** and 0.145663706 rad at 0.2 s. A frequency-rate bound adds \(\pi\dot f_{\max}t^2\). This is a conditional worst-case guarantee; exceeding its horizon does not prove that an actual trajectory has failed.

For delayed feedback,
\[
s+ke^{-sL}=0.
\]
Setting \(s=j\omega\) gives the first crossing at \(\omega=k\), \(kL=\pi/2\), hence
\[
L_{\rm crit}=\frac1{4f_c}.
\]
The displayed 25 ms at 10 Hz and 2.5 ms at 100 Hz are correct. The crossing moves toward instability as latency increases. Equality supplies no practical stability margin.

The ramp-rate particular solution and the \(5/k\) initial-condition contribution also check; the latter is **0.000673795 rad** for the stated initial bound.

**Validity-path review**

The state diagram and [pilot protocol](/tmp/vp-g3-review/book/relative-phase-stability.qmd:533) provide the following paths:

| Invalidation | Route to gated data |
|---|---|
| Failed settling/coarse acquisition | Acquisition-stage failure branch → invalidation bus → INVALID |
| Unresolved phase branch | Branch/calibration-stage failure branch → bus → INVALID |
| Failed model or validity checks | Respective checking-stage branch → bus → INVALID |
| Changed operating state | Valid-use monitoring → bus → INVALID; renewed state recorded |
| Stale calibration | Calibration-age monitoring → explicit stale-calibration invalid gate |
| Amplitude/reference loss | Explicit bus condition → INVALID |

The return arrow goes to the initial state-recording stage and then passes through acquisition, branch resolution, applicable calibration, held-out checking and renewed validity evidence. There is no depicted shortcut directly back to valid use.

Held-out frequency/time data test the fit’s predictive adequacy. They cannot independently establish acquisition/instrument accuracy. The surrounding protocol correctly requires a separate comparison at Q1/Q2, its own uncertainty and cross-covariance, and recognizes that shared errors can survive agreement. Internal amplitude, continuity, innovation and headroom indicators alone do not establish independent instrument validity.

**Pixels, accessibility and teaching contribution**

I visually opened all **24 raster files**:

- Standalones: `tracking-loop.png`, `tracking-transfer-budget.png`, `tracking-nonlinear-holdover.png`, `relative-phase-state-sequence.png`.
- Complete pages: `pages/chapter7/image.png` and `pages/pilot-state/image.png`.
- Every Chapter 7 crop: `crop-00.png` through `crop-05.png`.
- Every pilot crop: `crop-00.png` through `crop-11.png`.

The complete pages established placement and continuity; readable crops supported detailed inspection of equations, labels, captions and surrounding prose. **Chapter 7 crop-05 is a blank 1425×26-pixel trailing strip**, not readable content evidence. Other crops cover the content. No image-opening or decoding failure occurred.

Scoped figures have intact labels, captions and paths. Distinct dash patterns and filled/hollow equilibrium markers supplement color. Colored text against white has calculated contrast ratios of approximately 5.48–7.59:1. The embedded figures have meaningful HTML alt text; standalone SVG descriptions are generic and could better describe their specific content. Responsive layouts, screen-reader behavior and grayscale output were not tested.

The figures contribute distinct explanations: physical feedback actions, signal-retention versus noise tradeoff, separation of three failure models, and explicit invalidation/requalification sequencing. Other pilot figures remain unchanged context and await their own intervention group; this review neither requires nor implies their completion.

**Limits and exposure**

I read the manuscripts and derived the mathematics before examining generator code. I subsequently inspected the generator and supplied SVG/HTML sources; I did not execute the author generator or edit files.

Capture metadata exposed original source-path strings, and supplied source notes/manuscript text incidentally exposed backward-looking correction/check statements. I did not follow those paths or use earlier assertions as evidence. No outside files, repository history/status, connectors or delegation were accessed.

The checks establish consistency under the declared models. RMS/SD is not an instantaneous bound, settling time is not acquisition reliability, and marginal latency is not practical stability margin. Empirical applicability, representative acquisition performance, reader effectiveness and human acceptance remain unestablished.