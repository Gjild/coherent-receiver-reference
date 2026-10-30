Two consequential teaching corrections remain. I found no consequential sign or numerical error in the checked examples. All **145 manifest entries pass SHA-256 verification**.

1. **Clarify the filtering approximation’s applicability — Figure 3.1.** [The adjoining text](/tmp/coherent-visual-g1-review/book/observation-weighted-coherence.qmd:71) does not define fractional AM perturbation α or develop the displayed linearization. Small input perturbations and \(H_0\ne0\) alone are insufficient: the filtered perturbation must satisfy \(|h*\delta z|\ll|AH_0|\). For example, \(h=(1+j1000,-j1000)\), \(H_0=1\), and inputs \((1.001,1)\) give an exact angle of **0.784898 rad**, versus **1 rad** from linearization. Add the local model and output-smallness condition. Replace “an imaginary normalized impulse response” with “the imaginary part of the normalized impulse response.”

2. **Separate legends from axis titles.** Visible crowding recurs in Figures **2.1, 2.2, 3.3, 3.4 and 3.7**. In [Figure 3.7](/tmp/coherent-visual-g1-review/images/finite-record-uncertainty.png), inspect the bands around \(y=140–166\) and \(525–551\). Separately, SVG inspection confirms only **13 units** between the second legend-row baseline and axis-title baseline—about **10 pixels** in the page rendering. Increase this clearance and recheck the page-sized figures.

Optional improvements:

- Replace literal mathematical prose such as `n_parallel`, `bar_phi` and the Gaussian characteristic-function calculation with properly rendered mathematics.
- Label the coincident ±0.7 curves directly in Figure 3.7’s lower panel; use clearer logarithmic ticks and mark \(N=100\) in Figure 2.2.
- Label both the noise displacement and resultant voltage in Figure 2.5. State a common numerical covariance normalization in Figure 2.3.

Independent checks reproduced:

| Relationship | Result |
|---|---|
| Lower/upper LO comparison | **40° / −26°** |
| Added 25 ps RF delay | **31° / −17°** |
| Common reference advanced 65° | Phasors **−53° / −13°**; difference remains **40°** |
| Mixed-model average, \(N=100\) | **0.01604494 rad RMS** |
| Coherent power, \(T/t_c=10\) | **0.45641013**; rejected substitution **0.83526945** |
| Shared-delay gain at normalized offset 0.1 | **0.38196601** |
| AR(1), \(N=100\), \(\rho=-0.7,0,+0.7\) | Mean SD **0.042581, 0.100000, 0.234758**; variance-estimator SD **0.240162, 0.141421, 0.240162** |

I also checked distribution/propriety counterexamples, circular averaging, peak-voltage power scaling, wrapping ambiguity, validity gaps, covariance and increment limits, two-sided PSD normalization, spectral weighting, and short/long observation limits. Time-domain and spectral average variances agreed within the bounded spectral-tail error; coherent-power quadrature agreed with an independent series calculation. These support the declared illustrative models.

Pixel coverage was **all 17 standalone PNGs, all three complete-page overviews, and all 29 readable overlapping crops**. Crop coordinates below are half-open; every crop matched its parent pixels exactly.

| Chapter | Page dimensions | Readable crop coverage |
|---|---:|---|
| 1 | 1425×10254 | \(x=[320,1140)\), full height |
| 2 | 1425×7617 | Full width and height |
| 3 | 1425×9430 | Full width and height |

Chapter 1’s outer columns were inspected only in the reduced overview. Separate source checks parsed all **36 supplied SVGs**, confirmed all 17 corresponding copies match, and inspected manuscript/model before author code. No image-access or SVG-parsing failures occurred. My earlier empty-SVG statement was incorrect.

Only supplied requirements, manuscript, HTML/SVG, PNGs, provenance notes and code were examined. Incidental exposure: provenance notes contained earlier Codex examination/check claims; I did not use those as independent evidence. No original repository, history, prior-review files, connectors or external sources were accessed. No files were changed. `python` and NumPy were unavailable; checks succeeded using `python3`, standard-library calculations and Pillow. No rebuild, hardware validation, reader trial or human acceptance is established.