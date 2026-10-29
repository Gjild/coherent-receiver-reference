# Technical Authoring Standard

**Status:** provisional.

Write primarily for an experienced human RF engineer learning coherent receivers. Each substantial treatment should motivate an engineering question, develop relevant physics and mathematics, define assumptions, interpret results, demonstrate their engineering use, and disclose limitations. Different subjects need different structures: do not impose a mechanical template on all chapters.

- Develop prerequisites or add a targeted mathematical refresher where general RF expertise is insufficient.
- Use complete derivations for essential results; distinguish exact statements from approximations.
- Include system interactions, contrasting architectures and counterexamples where important.
- Use readable diagrams that correctly indicate signal paths, reference planes, directions and units.
- Integrate physical implementation, calibration and verification implications close to the relevant theory.
- Prefer a canonical result with sensible local exposition/cross-reference over copying conflicting derivations.
- Never invent numerical component data or use arbitrary design parameters without labeling them illustrative.
- A chapter's editorial completeness does not imply technical acceptance.

## Pilot-tested minimum obligations (2026-10-29; human acceptance pending)

For each consequential result supply the observable, reference planes, observation
operator, state, calibration history, physical model and stochastic assumptions.
Define symbols and units before use. Develop indispensable steps internally;
identify exact identities, modeling choices and approximations separately. Check
dimensions, limiting cases and error scales. A covariance is constructed from
physical sources and paths, not chosen merely to obtain a favorable budget.

Keep instantaneous phase variance, increments, calibrated residuals, restart
statistics and application performance distinct. Averaging phase and taking the
phase of an averaged complex product are different operations. Every integral
needs its spectral domain and convergence conditions. Preserve endpoint transfer
functions until a justified reduction is made.

A numerical example exposes inputs and their provenance, intermediate results,
uncertainty, decision and rejected alternative without requiring code execution.
Include a diagnostic counterexample and a transfer question that changes the
model. A design recommendation includes interface, implementation, calibration
access and evidence consequences. Introduce specialist mathematics in the reading
path from the RF baseline; a source citation cannot replace the bridge.

Keep general derivations in one home. The relative-phase pilot temporarily owns
its general results; its brief records their eventual chapter destinations.
