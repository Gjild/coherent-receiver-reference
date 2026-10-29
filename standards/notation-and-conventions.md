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

## Relative-phase pilot conventions (local selection; review pending)

These explicit local choices permit a reviewable draft; they are not accepted
book-wide defaults. Human mathematical/engineering review remains outstanding.

- `v(t)=Re{z(t) exp(j 2π fc t)}`; z has peak-voltage scaling. For a constant
  envelope into a declared resistance R, power is `|z|²/(2R)`.
- Relative phase is channel 2 relative to 1: `arg(z2 conj(z1))`.
- Use the proposed Fourier pair above. Define centered correlation
  `Rxy(τ)=E[(x(t+τ)-μx) conj(y(t)-μy)]` and its transform `Sxy`.
  Thus `Sxy` corresponds to `X conj(Y)` and `Syx=conj(Sxy)`.
- Derivations use two-sided spectra over all real offset frequencies, in
  rad²/Hz for phase. State band limits explicitly. Imported one-sided spectra
  require an explicit conversion; no universal L(f) conversion is selected.
- A physical delay has transfer `exp(-j 2π f τ)`; group delay is the negative
  phase derivative with respect to angular frequency. State RF versus offset f.
- Unwrapped residuals require continuity and amplitude/SNR conditions; otherwise
  use circular quantities and report slips, gaps and invalid intervals.
- Noise spectra describe centered processes. Deterministic drift, spurs and
  restart-state mixtures are kept separate. Positive time error here means an
  advance, `φ/(2π fc)`; a physical delay has the opposite phase sign.

General normalization, nonstationary/distributional spectral theory and unrelated
convention choices remain unresolved. Translate each source rather than silently
importing its normalization.
