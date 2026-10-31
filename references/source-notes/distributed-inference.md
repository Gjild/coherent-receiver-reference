# Distributed inference: claim-level examination — 2026-10-31

RFC5905, Mills/Martin/Burbank/Kasch, June2010 original RFC Editor HTML.
Examined §8 four-event definitions and offset/round-trip equations, pp28–30;
§6 pp12–14 timestamp diagram and 32-bit fraction; p29–30 difference-first
floating arithmetic discussion. Supports unity-rate algebra and exact field
resolution only. Affine-rate/asymmetry equations, binary64 example, bounds and
engineering decisions are local derivations. No NTP implementation, current
security guidance, hardware resolution/accuracy or picosecond service claim.
https://www.rfc-editor.org/rfc/rfc5905.html

NIST TWSTFT original HTML, created2016-05-10, updated2026-06-15.
Examined paragraphs on sequential/simultaneous transfer, reciprocity and distinct
equipment, equations1–2 and differenced clock expression retaining equipment,
propagation, relay and Sagnac contributions. Supports why path/equipment
asymmetries survive. Its satellite measurement conventions and published
performance are not imported into our terrestrial sequential model. Local
delays/signs are defined from timestamp event equations; no universal reciprocal
medium or cancellation of motion/relativistic corrections is assumed.
https://www.nist.gov/pml/time-and-frequency-division/time-distribution/two-way-satellite-time-and-frequency-transfer

NIST OneWayGNSS original HTML, created2016-05-17, updated2025-09-15.
Examined opening one-way delay/frequency distinction and geometry/medium/hardware
error discussion. Supports need for delay magnitude versus delay variation.
No GNSS performance, ionospheric model or navigation solution imported.
https://www.nist.gov/pml/time-and-frequency-division/time-services/one-way-gnss-time-transfer

All delays, asymmetry/calibration bounds, rate/drift/phase qualifications, baseline,
carrier and controller parameters are synthetic supplied envelopes. In particular,
the 0.01degree phase anchor is an additional required external input, not inferred
from the 100ps path or coarse timestamp example. Executed synthetic alignment and
validity logic are not device measurements, protocol compliance, physical proof,
reader testing or human acceptance. Original prose examined via web; reviewer
packets provide these notes/anchors, not independently authenticated originals.
