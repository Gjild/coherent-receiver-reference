# Observation-weighted coherence: source examination

2026-10-29; Codex examiner; human review pending.
Examined web PDF text of Oppenheim and Verghese, Signals, Systems and Inference,
MIT 6.011 Spring 2010, Chapter 10, printed pp. 183–184, equations (10.1)–(10.3).
https://ocw.mit.edu/courses/6-011-introduction-to-communication-control-and-signal-processing-spring-2010/8075041184d566103ce7c3f69afc5e75_MIT6_011S10_chap10.pdf
Supports correlation-transform PSD, integrated expected power and LTI |H|² weighting.
Translation: source uses omega and 1/(2 pi) measure, real uncentered correlation;
unit uses f in Hz and centered phase correlation. S_local(f)=S_source(j2 pi f)
for the centered process. No physical hardware or estimator claim is imported.

Finite observation weighting, exponential-covariance example, increment/coherence
identities, Gaussian integral, finite sample and fourth-moment expansions are
explicit authorial derivations. Gaussian fourth-moment factorization is a stated
specialization to check independently; not attributed to the examined chapter.
Elementary delay specialization is a scoped introductory restatement; general
pilot results remain owned by book/relative-phase-stability.qmd. All numbers are
synthetic. No radar performance or experimental validation is claimed.

## Visual bridge additions (2026-10-30)

Complex-filter order figure uses the pilot's local AM/PM model. The finite-input
remainder bound is an original mathematical specialization: split
`r=(exp(j phi)-1-j phi)+alpha(exp(j phi)-1)` and apply the exponential integral
remainders for real alpha/phi. Convolution norm bounds require absolutely
integrable normalized response (finite sums for taps). No new external source
passage or empirical support is attributed to this addition. Figure inputs and
other numerical visual models are synthetic and preserved in the figure generator.
