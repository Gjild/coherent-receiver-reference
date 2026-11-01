# Operational-metrology evidence examination — 2026-11-01

Fresh examination of original NIST TN1297 online1994edition sections5.1–5.2,
AppendixA.1–A.5, B.1–B.3 and D.4.1: measurement-process inputs/covariance,
correction versus uncertainty, independence and first-order/coverage applicability,
and explicitly method-defined measurands. Our correlated-record quadratic-form
DOF is derived locally, not imported as the AppendixB independent-component rule.
Custom observation is not a standardized-method conformance claim.
https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty
https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty
https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-b-coverage-factors
https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d4-measurand-defined-measurement-method

Original JCGM VIM3 online2.41 definition and notes1–5 examined: result-level
reference/calibration/uncertainty chain and no implication of fitness for purpose.
https://jcgm.bipm.org/vim/en/2.41.html

Original Anritsu10450-00040RevAE online Receiver Calibration Uncertainties subsection
examined in full (29web text lines). Source-power calibration, mismatch, linearity,
trace noise, plane/configuration and interpolation limits are setup dependent.
Typical amplitude numbers are not guarantees or phase specifications; none is
imported as a device capability. Broader manual/datasheet and figure pixels not
examined. https://dl.cdn-anritsu.com/en-us/test-measurement/ohs/10450-00040AE/Calibration_and_Measurement/MG_Ch08_RcvrCals.13.6.html

All local loading/correlation/noise/uncertainty/floor/range values and CSV records
are supplied synthetic teaching inputs. Seed2201, stationary first-order Gaussian
processes and two configurations do not demonstrate hardware. Fixed correction
knowledge terms are independent by assumption, shared between configurations;
phase readings within each record are correlated. Independent-reference case is
an analytical changed condition, not additional measured data. Loading/level/state
and reference characterization, certificates and actual traceability remain absent.
