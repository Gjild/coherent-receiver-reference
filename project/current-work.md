# Current Work: authorized K05–K07 foundational batch

Owner authorized sequential bounded K05, K06 and K07 teaching units, each with
source examination, mathematical checks, fresh read-only AI review, corrections,
canonical integration and a local checkpoint. Stop after connected integration
review; no K08, experiments or human acceptance follows automatically.

Repository reconciliation: inspected all 15 staged files; no unstaged or unrelated
changes found. Preserved their exact bytes and history in baseline `3b669a7`.
ADR-0006 manuscript hash matches; 13 foundation and 19 pilot checks passed.
A clean Git archive rendered successfully (8 HTML pages). Python 3.12.3,
Quarto 1.10.18, codex-cli 0.165.0; pytest remains absent.

Bounded outcomes, from accepted technical coverage and annotated contents:

- K05 / Chapter 5: infer phase intercept and delay from finite frequency samples;
  derive likelihood/least squares, local precision and nuisance identifiability,
  then expose wrapping and model mismatch. No full estimator catalogue.
- K06 / Chapter 7: first-order continuous phase tracking, wanted/nuisance transfer,
  noise/dynamic tradeoff and bounded acquisition/holdover/recovery reasoning.
  Nonlinear capture guarantees and complete sampled/remote implementations excluded.
- K07 / Chapter 6: covariance-aware propagation, nonlinear failure, numerical
  convergence and model discrepancy for a receiver decision. No full uncertainty
  accreditation, system allocations or evidence-policy treatment.

K05 completed as a checked provisional draft after separate AI review and
reassessment; [review](../reviews/phase-delay-inference.md). Three new checks and
nine-page HTML render passed. K06 and K07 not started.

Maintain existing local conventions, not book-wide authority. K02–K04 remain
checked provisional drafts. Human specialist, reader and physical evidence pending.

---

# Current Work: K02–K04 demonstration batch complete

**2026-10-29:** Owner authorized the consolidation implementation and sequential
bounded K02–K04 teaching units. All three are now checked provisional drafts,
with separate-context AI review, corrections and reassessment. No human technical
acceptance, specialist validation, reader effectiveness or physical validation is
claimed. Existing ADR-0002–0006 and U-01–U-10 qualifications remain in force.

| Unit / canonical teaching home | Review and corrections | Local checkpoint |
|---|---|---|
| [K02 / Chapter 2](../book/scalar-stochastic-phase.qmd) | [Review](../reviews/scalar-stochastic-phase.md): dependent signal-frame noise, joint-Gaussian bridge, defined transfer problem and small-noise conditions | `a154d83` |
| [K03 / Chapter 3](../book/observation-weighted-coherence.qmd) | [Review](../reviews/observation-weighted-coherence.md): coherence stationarity, filter domain, Gaussian derivations and worked coherent-power calculation | `b564ead` |
| [K04 / Chapter 4](../book/covariance-quadratic-forms.qmd) | [Review](../reviews/covariance-quadratic-forms.md): singular-value scaling, centered-noise/bias assumptions and rank bridge | `151f9db` |

Thirteen foundation unittest checks and nineteen existing pilot checks passed.
Scaffold/whitespace and eight-page HTML rendering passed; 152 local HTML links
and fragments, 52 Markdown links, IDs and math presence were checked mechanically.
All 16 protected baseline artifacts are unchanged. pytest is absent. Browser pixel review,
PDF, reader trials, qualified specialist review and hardware tests were not performed.
No dependency installation, push or external publication occurred.

## Operational result and checkpoint boundaries

codex-cli 0.165.0 supports the chosen fresh `codex exec` reviewer arrangement.
Configured target and explicit reviewer requests: gpt-6.1-sol / high; exact runtime
routing is not independently introspectable. Review sessions received frozen inputs,
accepted requirements and sources without author history or correctness assertions.
Each returned findings and was resumed by explicit ID for reassessment before the
next unit began. Native agents were unnecessary; no runner or platform was added.

Initial runtime startup failed in the parent read-only filesystem environment.
Approved execution outside that parent sandbox succeeded while the nested reviewer
retained its own read-only shell: exclusive-create probe returned EROFS. Runtime
permission remains environment-dependent. Quarto needed XDG_CACHE_HOME in /tmp.
The CLI sequence worked but review latency and same-model correlated errors remain
limitations; no throughput or independent physical-validation claim follows.

The three commits checkpoint new unit/source/review files and tests; K02 also
checkpoints clean workflow files. Shared book configuration, bibliography, standards,
strategy, current-work and validation updates remain in the working tree because
they already carried owner changes. Existing staged entries are preserved. The
Review-link portability closeout: `00eb2c1`. These
commits alone are not a clean checkout of the pre-existing accepted working-tree
baseline. No unrelated changes were swept into a checkpoint.

## Owner decisions and stopping boundary

The owner authorized explicit local convention reuse; no book-wide convention was
adopted. Canonical pilot and phase-comparison bytes and accepted architecture are
preserved. The new units do not complete K02–K04 or their chapters; detailed matrix
inference, physical noise networks and application mappings retain their homes.

No unresolved critical finding remains from these bounded AI reviews. Human
technical acceptance, specialist/reader evaluation, book-wide conventions and any
next development batch remain owner decisions. Do not begin K05 automatically.
The repeatable arrangement and exact CLI invocation are in the existing strategy;
AGENTS.md defines autonomous responsibilities and escalation rules.

---

## Historical closeouts (prior stopping instructions superseded for this batch)

# Current Work: First Chapter 1 Unit Provisionally Accepted and Closed

**2026-10-29:** The owner provisionally accepts the unchanged
[phase-comparison manuscript](../book/phase-comparison.qmd) as a mathematically
checked, bounded textbook teaching draft for continued development under
[ADR-0006](decisions/ADR-0006-provisional-phase-comparison-acceptance.md).
Acceptance is limited to its declared idealized signal/receiver model, stated
local conventions, checked derivations and illustrative example. It does not
complete Chapter 1/K01 or establish independent specialist validation, actual
reader effectiveness, physical receiver performance or publication readiness.

The [review record](../reviews/phase-comparison.md) retains executed checks and
limitations. ADR-0006 records three nonblocking editorial obligations: later
sampled-observation linkage, consideration of reference/orientation diagrams,
and reuse of the canonical introductory derivation without unnecessary duplication.
No speculative rewriting, book-wide convention adoption or new technical review
occurs. The [strategy](sustained-authoring-strategy.md) remains the approved method.

Closeout changes administrative records only. Manuscript/architecture/pilot byte
preservation, index preservation, scaffold integrity and link/table/whitespace
checks are recorded in [validation](../docs/VALIDATION.md). Earlier mathematical
checks and five-page rendering are historical evidence, not rerun here.

**Next task: scalar stochastic phase reasoning — selected K02 / Chapter 2
material — not yet started.** Stop after this administrative closeout. No next
manuscript, bench campaign, installation, commit or publication begins.

Historical stage records below retain their evidence and stopping context.

---

# Current Work: First Technical Pilot Provisionally Accepted and Closed

**2026-10-29:** The project owner provisionally accepts the corrected dual-channel
relative-phase-stability pilot for **analytical teaching and technical-authoring
workflow development** under [ADR-0005](decisions/ADR-0005-provisional-relative-phase-pilot-acceptance.md).
This is the owner's stated decision, following focused AI-assisted review,
corrections and numerical checks; no independent specialist approval is asserted.

The [pilot brief](pilots/relative-phase-stability.md) records completed scope,
outcomes and canonical destinations. The [review record](../reviews/relative-phase-pilot.md)
retains correction dispositions and evidence limitations. ADR-0005 identifies
the unchanged accepted working-tree artifacts by SHA-256; the contextual HEAD
does not contain the staged additions.

Acceptance excludes physical-model validation for particular hardware,
experimental confirmation, educational effectiveness, general receiver-design
applicability and product compliance. Hardware parameter/fixture/acquisition/
settling evidence, specialist examination, reader trials and browser visual
inspection remain outstanding. Full pytest is unavailable because dependencies
are absent. Local conventions are not adopted book-wide.

## Closeout checks and repository observations

- Reran 19 standard-library pilot tests: passed; reproducible example completed.
- Scaffold integrity passed (13 required paths); Quarto 1.10.18 HTML render passed
  on four pages using a writable temporary cache. Python version: 3.12.3.
- Full pytest command attempted: pytest absent. NumPy import also failed; original
  NumPy-based tests remain unexecuted. PDF and browser pixel inspection were not
  performed in this closeout; the prior browser limitation remains open.
- Final audit passed: 52 local Markdown links resolve across the seven closeout
  files; 27 Markdown table rows have consistent column counts; four rendered
  HTML pages have 32 resolving internal fragment links with no duplicate IDs
  or unresolved references. Both SVG assets parse. Whitespace checks passed.
- All six accepted artifact hashes match the unchanged start-of-closeout bytes.
  Eleven protected charter/inventory/architecture/ADR files and all standards,
  source notes, publishing configuration and computational files are unchanged.
  The Git index is unchanged. Six existing administrative/status files and
  ADR-0005 are the only task edits; no new checker was added to the repository.
- Starting state contained staged pilot/standards work and staged archives with
  additional unstaged changes. The corrected six-artifact set matched its staged
  bytes. The owner subsequently removed changes.patch and changes.zip, confirmed in the
  working tree; their staged entries remain because the index was preserved;
  this task does not restore those files or alter the index.
- README's obsolete “pilot not started” statement is corrected. No technical
  manuscript, calculation, test, standard or accepted architecture is rewritten.
  No new source passage, human specialist review, learner trial or measurement is
  claimed. No commit, tag, dependency installation or publishing deployment occurs.

## Next activity and stopping boundary

**Post-pilot development-method assessment and sustained authoring preparation —
not yet started.** The pilot development stage is closed for its limited accepted
use. Stop after this administrative closeout; do not start assessment, subsequent
chapters, reference designs or a bench campaign. ADR-0002–0004 and outstanding
U-01–U-10 qualifications remain in force.

The record below is historical architecture-stage closeout; its “not yet started”
statements describe that earlier stage, not current pilot status.

---

# Current Work: Provisional Book Architecture Stage Closed

**Closed stage:** provisional book architecture, annotated table of contents and intellectual organization. **State:** provisionally accepted by the project owner on 2026-10-29 as suitable for guiding textbook development under [ADR-0004](decisions/ADR-0004-provisional-book-architecture-acceptance.md), following external AI-assisted review. This is planning acceptance only.

**Subsequent work — not yet started:** technical authoring standards development, publishing validation and the initial dual-channel relative-phase-stability technical pilot. These are future bounded tasks requiring separate authorization; no work on them begins in this closeout.

## Accepted book-planning package

- [Book architecture](book-architecture.md): five proposed parts and 32 chapters, organizational alternatives, learning/reference routes, boundaries and review decisions.
- [Annotated contents](annotated-toc.md): chapter objectives, prerequisites, canonical ownership, 128 substantive section annotations, work/evidence expectations and technical appendices.
- [Book coverage](book-coverage.md): canonical location assignments, all 45 capability outputs/dimensions, dependency/cohesion audits, staged reference designs and seven application/five failure-probe routes.

These organize the accepted knowledge requirements into a provisionally accepted textbook plan. They do not replace the canonical architecture or constitute manuscript content. Counts describe the provisional organization; they are not quality targets, fixed boundaries or adequacy evidence. The four ADR-0003 qualifications are preserved. All substantive source research, derivations, models, solved designs and educational/engineering validation remain future work.

## Earlier baseline and accepted technical package

The [charter](charter.md) governs mission and audience. The [competence inventory](competence-inventory.md) remains the provisional 45-capability baseline governed by [ADR-0002](decisions/ADR-0002-provisional-competence-baseline.md). Historical next-stage statements in that ADR and the inventory describe their earlier closeout; this record gives subsequent status without expanding their acceptance scope.

The accepted planning package consists of:

- [Technical architecture](architecture.md): reader bridges, progression, relationships, reference routes and readiness gate.
- [Technical coverage](technical-coverage.md): canonical treatment specifications, dependencies, capability traceability and gap dispositions.
- [Reference-design plan](reference-design-plan.md): provisional design briefs, example progression and paper stress tests.

ADR-0003 records the accepted Git revision and each document's SHA-256 before administrative closeout edits. Capability definitions, canonical treatment specifications and reference-design briefs are unchanged.

## Acceptance qualifications and outstanding work

1. Learning prerequisites and application treatment requirements must allow motivating examples before full quantitative methods are taught.
2. K02–K07 mathematical bridges must be developed for the declared RF-engineer baseline without hidden specialist prerequisites.
3. Interferometry, vector antenna/polarization models and application-processing scope require further boundary review; essential coherent-receiver reasoning must remain internal.
4. Educational and engineering adequacy must be tested through actual textbook development, including the later dual-channel relative-phase-stability pilot.

Inventory U-01–U-10, technical coverage §6 dispositions, unresolved mathematical conventions, claim-level source work and specialist review obligations remain open. Planning acceptance does not independently validate any derivation, physical model, engineering method, simulation, measurement or hardware-performance claim, nor establish system compliance. No independent specialist approval or unprovided external AI review findings are asserted.

## Historical book-planning checks and evidence boundaries

Checks actually performed on 2026-10-29 for this draft:

- `python3 scripts/check_repo.py`: passed; 13 required scaffold files present.
- One-off read-only audit, kept outside the repository: 32 ordered chapter headings and 128 section headings; explicit referenced section endpoints exist; all 33 K/A treatment identifiers have canonical rows; all 45 capability rows retain the accepted dimensions and evaluated-output audit text.
- The same audit checked consistent table columns in the three new documents, local Markdown link resolution across the three documents and this record, and byte-for-byte preservation against HEAD of the competence inventory, accepted three-document package and ADR-0002/0003. All 25 local links resolve after the status update.
- `git diff --check`: passed after the status update. The one-off audit also checked the new, untracked documents for trailing whitespace and final newlines.
- Authorial inspection of prerequisite/refinement/conditional routes, canonical boundaries, analog alternatives, all seven P routes and five X probes is recorded in book coverage §3–§4. This is an editorial audit, not independent technical review or proof of learning adequacy.

No software tests or book render were run: no engineering code, manuscript or publishing configuration changed. No source passages were newly examined; no derivation, numerical allocation, engineering model, physical measurement or learner assessment was performed. Existing source evidence remains limited to its recorded claims. The new documents and this status record are the only repository changes intended by this stage.

## Historical architecture-closeout checks and evidence boundaries

The 2026-10-28 architecture pass recorded scaffold integrity, in-memory capability/dimension/treatment/link/table audits, an ordering check on a manually transcribed dependency table, authorial paper-route review and `git diff --check`. Those historical checks support planning traceability only; they were not independent technical review, calculations, physical validation or learner assessment.

Closeout checks actually performed on 2026-10-29:

- `python3 scripts/check_repo.py`: passed; 13 required scaffold files present. The initial `python` invocation could not run because that command is unavailable; the installed `python3` was used.
- One-off in-memory audit: all three accepted-package SHA-256 values match their bytes at the recorded Git revision; architecture §§1–4, technical coverage §§1–5 and reference-design plan §§1–4 are byte-for-byte unchanged; the competence inventory and ADR-0002 are unchanged in full.
- One-off in-memory audit: all 43 local Markdown links resolve and Markdown table column counts are consistent across the seven closeout files. No checker or metadata framework was added.
- `git diff --check`: passed. Diff review confirms changes are limited to acceptance/status, qualifications, issue disposition and closeout records.

These are repository consistency checks, not technical validation. Software tests and book renders were not run because no implementation or manuscript changed. No source passages are newly examined and no technical results are independently validated by this closeout.

## Book-architecture acceptance qualifications and closeout

ADR-0004 preserves four review findings: Chapters 1–7 must connect foundations to meaningful receiver questions and consequential calculations early; all four anchors must become continuous engineering developments with justified iteration and production implications; part/chapter/section boundaries remain flexible; and all earlier technical qualifications remain in force. The exact accepted pre-closeout bytes are identified by SHA-256 in that decision, because the planning files were staged additions rather than contents of the recorded HEAD revision.

Acceptance does not establish mathematical correctness, physical-model validity, educational effectiveness, experimental verification or receiver-performance compliance. No new source examination, technical review by an independent specialist, measurement or learner assessment is asserted. Existing U-01–U-10, mathematical conventions, specialist boundaries and evidence gaps remain open. No additional issue blocking this administrative stage closure has been identified; they may restrict subsequent technical uses.

Closeout checks actually performed on 2026-10-29:

- `python3 scripts/check_repo.py`: passed; 13 required scaffold files present.
- One-off read-only audit outside the repository: all three ADR-0004 hashes match both the captured pre-closeout bytes and the existing staged artifacts. The recorded HEAD is context, not a false claim that it contains those additions.
- Preservation audit: the annotated contents after its status paragraph is byte-for-byte unchanged; book architecture and book coverage §§1–4 are unchanged. Protected competence, canonical treatment, reference-design and earlier decision documents are unchanged. All 32 chapter/128 section headings, 33 K/A identifiers and 45 capability dimensions/evaluated-output targets are retained.
- Link/table/whitespace audit: all 50 local Markdown links resolve across the seven closeout files; table columns, final newlines and trailing whitespace are consistent. `git diff --check` passed.
- Scope review: changes are confined to ADR-0004 and administrative status, acceptance, qualification, issue and closeout records in the six authorized existing documents. Existing staged work was preserved; no commit, tag or index update was performed. An unrelated, initially untracked `changes.zip` disappeared during the turn; this task did not edit or remove it, and it was excluded from the final repository-file preservation audit.

These are repository and planning-consistency checks, not mathematical or physical validation. No software tests or book render were run because no engineering implementation, manuscript or publishing configuration changed. No new source passages were examined. The later authoring standards, publishing validation and technical pilot were not executed.

## Stopping boundary

The book-architecture stage is closed for the owner's stated provisional use. Stop here. Technical authoring standards, publishing validation and the initial relative-phase-stability pilot are subsequent work, not yet started. Do not begin manuscript drafting, substantial mathematical derivations, computational modeling, solved designs or publishing infrastructure. Eventual pilot assessment must test actual educational and engineering adequacy, including consequential calculations and changed assumptions, not merely coverage.
