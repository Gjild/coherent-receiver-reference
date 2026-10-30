# Physical-noise source examination — 2026-10-30

Actual web full-text extraction examined the following primary manufacturer texts.
No device performance, equation-image inspection or empirical confirmation follows.

- [Analog Devices MT-047](https://www.analog.com/media/en/training-seminars/tutorials/MT-047.pdf),
  *Op Amp Noise*, Rev. 0, 10/08: pp. 1–3, voltage/current equivalent sources,
  resistor RMS formula, junction shot-noise density and compensated-input caution.
  Supports those selective source models. Source bandwidth convention maps to
  one-sided 4kTR / 2qI; manuscript explicitly uses real two-sided 2kTR / qI.
  Its approximate op-amp independence is not imported as an RF-array assertion.
- [Walt Kester, MT-007](https://www.analog.com/media/en/training-seminars/tutorials/MT-007.pdf),
  Rev. A, 10/08: pp. 3–4, slope-error explanation and equations (1)–(6).
  Supports input-slope dependence and isolated-sine jitter limit. Source's RSS
  statement is restricted here to independent contributions. It does not establish
  the manuscript's broadband/correlated-clock spectral model.
- [Analog Devices mixer-noise article](https://www.analog.com/en/resources/technical-articles/specifications-and-measurement-of-local-oscillator-noise-in-integrated-circuit-base-station-mixers.html),
  displayed June 18, 2003: Abstract, Introduction, Mixer Noise Model, Effective
  Noise Floor of LO Driver. Prose supports blocker/LO reciprocal mixing and
  internal-buffer contribution. Equation images and device examples not examined;
  no normalization, current standard or part guarantee imported.

Thermal power/envelope translation, resistive source decomposition and loaded
matrix, active cross-term, shot-source Poisson derivation, finite blocker
convolution and complete-waveform timing models are locally derived. Numerical
values, spectra, loads, targets and clock component are synthetic. Positive
semidefinite matrices prove only second-moment admissibility, not hardware validity.
An actual array needs impedance/embedded response/active-noise/environment data;
an actual blocker or clock conclusion needs spectra and the observation chain.
