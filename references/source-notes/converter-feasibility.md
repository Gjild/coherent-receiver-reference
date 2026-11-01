# Converter evidence examination — 2026-11-01

Kester MT007 RevA10/08 original ADI PDF, pp2–7: aperture delay versus jitter,
slope/sine derivation and SNR test including clock-generator uncertainty.
RSS is used locally only for explicitly uncorrelated sources; complete waveform,
discrete phase weights and shared/private sources are local derivations.
https://www.analog.com/media/en/training-seminars/tutorials/MT-007.pdf

Kester MT001 RevA10/08 original PDF, pp1–6: ideal code error, uniform approximation,
full-scale sine normalization and signal-correlated error/periodic spectral
content. No plotted numerical data imported. Conditional uniform non-subtractive
dither mean/variance and exact 64-sample example are local calculations.
https://www.analog.com/media/en/training-seminars/tutorials/MT-001.pdf

AD9643 RevG, April2024 verified revision historyp2. Original PDF text pp4–8
electrical conditions/min/typ/max; pp22–25 switched inputs/common-mode/clock
and dynamic duty-cycle behavior; pp26–27 pipeline, delayed overrange and
clock-relative synchronization. Supports separate interface/state obligations,
not our driver/noise/recovery envelopes. Output interleaving is a data format,
not evidence for our alternating-aperture model. No device selected; typical
entries are not temperature/state guarantees. Source curves not pixel-reviewed.
https://www.analog.com/media/en/technical-documentation/data-sheets/AD9643.pdf
