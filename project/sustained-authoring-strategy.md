**Current authorization (2026-10-30):** the owner provisionally accepted the
Chapters 1–7/pilot HTML visual milestone under
[ADR-0007](decisions/ADR-0007-provisional-html-visual-pedagogy-acceptance.md).
K08–K10 are the next authorized autonomous development batch, sequentially bounded
under the accepted architecture and full technical-and-visual procedure. This task
ends with administrative closeout; their manuscript development has not started.
[current-work.md](current-work.md) supplies the active boundary. Earlier task and
permission statements below retain their historical scope.

**Historical K05–K07 authorization:** owner approved the next sequential bounded K05–K07
batch and its connected integration review, including safe reconciliation and local
Git checkpoints. This supersedes earlier next-unit stopping instructions only for
this batch. Chapter 6 owns K07; Chapter 7 owns K06. Stop after batch integration.

**2026-10-29 authorization update:** Owner approved the consolidation plan and
sequential bounded K02–K04 batch, with fresh read-only CLI AI review, local
convention reuse and selective local unit commits. This supersedes the earlier
single-unit stopping boundary below for this batch only. No K05, installation,
external publication or AI technical acceptance is authorized. AGENTS.md and
current-work.md govern operational responsibilities and escalation. Earlier
method rationale and acceptance qualifications remain in force.

# Sustained textbook authoring strategy

**2026-10-29:** The owner approved the proposed method and authorized only the
first bounded Chapter 1 unit, with continuous textbook exposition as an explicit
qualification. This approval concerns method and scope, not technical acceptance.

## Evidence and lessons

Observed: ADR-0005 accepts the corrected relative-phase pilot for analytical
teaching/workflow use. Its review records nine corrections, nineteen passing
pilot tests and successful HTML generation. Distinct time/spectral and
source-coefficient formulations support conditional analytical consistency.
Source notes preserve narrow claim support. Independent specialist review,
reader trials, hardware evidence and successful browser inspection were absent.
The first draft's eight tests did not expose all consequential defects.

Inference: the main workflow weakness was connecting statistics and derivations
to acquisition, calibration, physical reference planes and operating timelines.
Static calibration/band confusion, a hidden regression reference and incomplete
snapshot timing show why end-to-end reasoning needs focused challenge. Symmetric
examples can hide defects. The corrected explanation is useful but dense; its
accessibility and full-book adequacy remain untested. Ten files required correction;
no measured effort or repeated-unit experience establishes sustainable throughput.
Repeated historical status prose increases maintenance burden.

Recommendation: keep the accepted intellectual architecture, existing tools and
small records. Develop one engineering outcome at a time, review its connections,
and integrate the reading path before starting the next unit. No new agents,
knowledge database, publishing infrastructure or comprehensive chapter schedule.

## CLI author/reviewer arrangement

Installed and tested 2026-10-29: codex-cli 0.165.0; user model configuration is
`gpt-6.1-sol` / `high`. Native multi_agent is enabled but subagents inherit
permissions. Prefer a fresh CLI context for enforced read-only shell review:

```sh
codex exec --ephemeral --skip-git-repo-check -C "$REVIEW_PACKET" \
  -m gpt-6.1-sol -c 'model_reasoning_effort="high"' \
  --sandbox read-only --json -
```

Pass neutral review instructions through stdin; keep reviewer output outside the
frozen inputs and retain relevant provenance in the unit review record. Do not
fork or resume author history. Capture the returned thread ID. For correction
reassessment use a fresh read-only context with newly frozen affected inputs,
requirements and actual PNGs, retaining the requested model/effort. Keep prior
findings and author dispositions separate from reviewer inputs. The current
[inspection procedure](../docs/VISUAL-INSPECTION.md) supplies the packet-only
invocation, including actual PNG attachments; set REVIEW_PACKET to the isolated
frozen input directory, not the author repository. No custom runner, agent platform or global config change is required.

This installation's runtime initialization failed inside the parent filesystem
sandbox; approved execution outside that parent sandbox worked while the nested
reviewer's exclusive-create probe failed with EROFS. Such runtime permission is
not permission to widen the reviewer's sandbox. Reviewer connectors and edits are
forbidden. Noninteractive failures require reporting, not inferred completion.
AI model/effort are requested settings; reviewer introspection did not independently
expose runtime identifiers. Same-model review retains correlated failure risks.

## Repeatable process

At the start of **every authoring batch**, execute a fresh environment smoke test
using [the existing private-pipe route](../docs/VISUAL-INSPECTION.md), inspect its
actual PNG and record paths/versions, command/exit, hashes and concrete observations.
Do this before manuscript/figure development; include the current smoke image in
the first separate-context technical/visual packet. A failed route preserves the
visual gate and exact continuation boundary. Diagnose specific host differences;
do not redesign the helper or repeat known failed invocations without new evidence.

1. Select by prerequisite value, coherence-specific consequence, practical use,
   reusable results and review difficulty; record K/A home and reader outcome.
2. Bound the engineering question, prerequisites, exclusions, supplied inputs,
   failure modes, evidence needs and intended completion claim.
3. Examine consequential source passages and translate conventions; distinguish
   imported results, original derivations, assumptions and missing evidence.
4. Develop observable, physical model, essential mathematics, interpretation and
   decision together with indispensable scientific diagrams and quantitative plots.
   Specify purpose, assumptions, planes, normalization and error prevented; reuse
   canonical figures where appropriate. Check signs, units, limits and interfaces.
5. Compute only where a distinct formulation, convergence or stochastic/numerical
   result materially improves confidence. Reuse existing mechanisms.
6. Write a continuous textbook argument with a worked decision, counterexample
   and changed-assumption assessment; essential explanation stays readable offline.
7. Independently verify consequential calculations and graphical mappings through
   distinct formulations, limits, asymmetric cases and coordinate/connectivity checks.
   Render affected HTML; inspect actual assets and complete pages with readable crops,
   equations, captions and alt text. Obtain fresh read-only separate-context AI technical
   and visual review on frozen requirements, source passages, manuscript/model/code and
   actual PNG attachments. Record image access and evidence limits; repeated AI reasoning
   never becomes independent physical evidence. Human review is recorded only when provided.
8. Correct consequential findings in dependent prose, calculations and figures;
   repeat affected checks and pixel inspection, freeze corrected inputs and obtain
   fresh targeted reassessment before advancing.
9. Integrate canonical placement, local bridges, notation and surrounding prose;
   create safe authorized local checkpoints and report the bounded outcome, actual
   evidence, optional polish and unresolved claims. Close the batch with connected
   technical/visual assessment. Checked provisional drafts remain distinct from
   independently specialist-validated engineering knowledge.

General results have one home. Do not migrate pilot derivations without updating
its references and assessing changed acceptance scope. Local introductory
explanations may restate definitions and scalar signs without superseding the
pilot's general analysis. Preserve four continuous design threads and the
independent application cases; do not let the convenient D-MET start replace them.

## Small development queue

| Order | Unit/home | Reason |
|---|---|---|
| 1 | Operational phase comparison/representations, K01, Chapter 1 | Signs, normalization and planes propagate everywhere; immediate useful calculation |
| 2 | Scalar stochastic phase reasoning, K02, Chapter 2 | Supply RF-baseline probability, covariance, wrapping and noise-to-phase bridges |
| 3 | Observation-weighted phase stability/coherence, K03, Chapter 3 | Reuse pilot time/spectral and unequal-path reasoning; distinguish consequential statistics |
| 4 | Covariance/quadratic forms, K04, Chapter 4 | Develop coupled reasoning and source/path construction before general budgets |
| 5 | Local phase/delay inference versus ambiguity, K05, Chapter 5 | Reuse asymmetric fitting and reference conversion; prepare calibration observability |

This order follows dependencies and error consequences, not chapter numbers.
Units 3–5 need stronger time-frequency/statistical/metrology review. Introduce an
unequal-delay D-RAD contrast at unit 3. Reassess the method after three delivered
units; no automatic queue execution is authorized.

## Completion and human decisions

A completed draft explains its bounded outcome. Checks establish named encoded
properties. Physical applicability assessment identifies mechanisms, domain and
missing evidence; laboratory tests are not universal prerequisites for theory.
Human technical review identifies the actual engineer and artifact. Provisional
acceptance identifies owner, use and qualifications. Publication integration adds
reading-path and rendered-presentation review without upgrading technical evidence.
These are separate claims, not an automatic status ladder.

The owner chose continued bounded provisional drafting while specialist/reader
review remains outstanding. Book-wide conventions still require human review.
Reference-design requirements, application/specialist boundaries and publication
format expectations remain human decisions. Risk: drafts may outpace review,
foundations may be too compressed and D-MET may dominate. Existing U-01–U-10 and
ADR-0002–0005 qualifications remain in force.

## First task and stopping boundary

Develop “Defining and tracking a two-channel phase comparison,” selected Chapter
1/K01 content, not a complete chapter. Derive physical/analytic/envelope relations,
peak-power scaling, explicit planes, lower/upper conversion orientation and a
continuous worked instrument comparison. Explain reference changes, wrapping,
nulls, offsets/frequency/delay and what repeated observations cannot establish.
Check by waveform reconstruction, direct extraction, reference changes and limits.
Keep conventions local. Exclude PSD theory, matrix statistics, calibration
algorithms, components and empirical performance claims. No new software module
is required. Acceptance requires text-only reproducibility and honest review limits.

Deliver manuscript, source provenance, checks and review record; preserve pilot
and accepted architecture. Stop after this unit. No next unit, bench campaign,
dependency installation, commit or publication follows automatically.
