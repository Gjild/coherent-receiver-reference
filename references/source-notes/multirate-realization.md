# Multirate evidence examination — 2026-11-01

Original ADI MT085 Rev0 10/08 PDF pp2–4: accumulator/tuning relation, phase and
amplitude truncation, loading/update. Our NCO sign, fractional-word choices and
retune results are derived locally. DDS DAC restrictions/spectrum are not
imported as mixer feasibility or spurious guarantees. No source-curve pixels
inspected. https://www.analog.com/media/en/training-seminars/tutorials/MT-085.pdf

Original TI SLAA193 February2004 PDF pp3–4and8: a device-specific integer-rate
audio example, computing retained FIR outputs while retaining every input in
history. Does not establish asynchronous-clock estimation, our RF rates or
platform throughput. We do not copy its coefficients or device performance.
https://www.ti.com/lit/an/slaa193/slaa193.pdf

Original historical Xilinx PG149v7.0 March20,2013 PDF pp8–9,16–19,24–25,61–68:
configuration-dependent latency/limited resource characterization, optional
reset of history versus control, handshake and multirate metadata semantics,
MAC/symmetry/padding, coefficient scaling and precision/rounding. Current online
PG149 paths partly return404/401; primary search exposes some short sections,
but the complete PDF examination is explicitly historical. No current core,
FPGA configuration or achieved hardware schedule is qualified. Source diagrams
not pixel-inspected. https://docs.amd.com/api/khub/documents/kEmF~wSgDRbjAEDvn55_BQ/content

Original AMD current2026.1 FIRv7.2 performance page opening interpretation notes
examined: isolated out-of-context implementation and clock search, limitations
on repeatability in a larger design. No table row/number is selected or imported.
Actual whole-design tool reports and interface tests remain required external
evidence; calculated MAC capacity alone is not hardware feasibility.
https://download.amd.com/docnav/documents/ip_attachments/fir-compiler.html

All coefficient models, interpolation, integer/queue examples and timing-fault
records are local synthetic calculations. Host perf_counter timings are actual
software executions with recorded environment, not converter/link/FPGA or RF
measurements. No independent reader/specialist/experimental validation claimed.
