All 18 manifest entries verified before and after execution; `SHA256SUMS` itself remained unchanged. No files were edited.

Independent calculations recovered:

- Loaded voltage: \(35.3553390593274+j\,3.53553390593274\) µV.
- Loaded power: \(1.2625\times10^{-11}\) W.
- Matched thermal power: \(4.0038821\times10^{-16}\) W.
- LO-density limit: \(3.162277660168379\times10^{-13}\) rad²/Hz, from the −115 dBm allocation, \(10^{-7}\) W blocker and 100 kHz bandwidth.

Power, rotated-voltage and LO-limit comparisons normalize to one. Their rounding thresholds are approximately \(5\times10^{-13}\), \(5\times10^{-13}\) and \(5\times10^{-11}\), respectively. Each rejected scaling factors 0, 0.01, 0.1, 0.5, 2, 10 and 100.

`python3 -B -m unittest discover -s tests -p test_physical_models_stdlib.py -v` completed: **19 tests, 0.523 s, OK; exit 0**, including the SVG-coordinate fixture.

No consequential defect found within this numerical scope. Exposure comprised packet requirements, accepted-scope documents, manuscript conditions, code and SVG coordinates; scope-document acceptance metadata was incidentally visible. No actual-pixel, physical or human acceptance is claimed.