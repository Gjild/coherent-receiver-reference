# Notation and Conventions

**Status:** initial proposal; canonical conventions must be reviewed before substantive mathematical chapters.

## Proposed conventions to confirm
- Continuous-time Fourier transform: `X(f) = ∫ x(t) exp(-j 2π f t) dt` and inverse with `+j 2π f t`.
- Angular frequency `ω = 2π f`, frequency `f` in hertz.
- Real physical waveforms vs complex analytical signals/envelopes must carry explicit scaling and carrier-sign conventions.
- Unwrapped phase and circular/angle-valued statistics are distinct; specify the one used.
- Spectral densities: explicitly state one-/two-sided definition, variable, units, domain and cross-spectrum ordering.
- Time and phase reference planes, trigger/reset state, bandwidth/filter and observation interval must accompany consequential phase measures.
- Clearly distinguish power and amplitude ratios in dB, and RMS vs peak conventions.

## Unresolved choices
General complex-envelope normalization, default PSD convention, phase-noise `L(f)` normalization, cross-spectrum sign/order, treatment of distributional/nonstationary spectra. Do **not** silently resolve these by defaulting to whatever an external source uses.
