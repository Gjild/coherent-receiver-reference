# Visual inspection retest after temporary inotify adjustment — 2026-10-30

Status: live limit 512 verified; private-pipe captures and author pixel inspection
succeeded. Separate-context read-only pixel review and a fresh-session
workflow test also completed successfully. No human visual/technical acceptance or illustration production.

The owner reported applying a temporary resource change. Codex made no host,
security, permission or software-installation change. The original diagnosis,
visual audit and review findings remain intact. This record supersedes their
historical blocked capability status only where a successful test is recorded.

## Controlled comparison

| Test | Before (128) | After (512) |
|---|---|---|
| inotify allocation | EMFILE inside and outside Codex sandbox | OK inside and outside |
| Codex sandbox SO_PASSCRED | EPERM | EPERM; no browser launched by preflight |
| Ordinary-user host minimal Brave CLI screenshot | 20.066 s timeout, no PNG, inotify errors | 20.067 s timeout, no PNG; inotify errors absent |
| Existing smoke script, CLI backend | preflight exit 2 | host browser timeout at 30.069 s; script exit 1 |
| GPU-disable hypothesis | not required for this comparison | 25.067 s timeout, no PNG |
| Direct private-pipe capture, same browser | not tested | actual PNG produced, no security bypass |

Effective `fs.inotify.max_user_instances=512`, max_user_watches=65536. The
inotify adjustment removed the measured allocation failure but was insufficient
to repair the CLI screenshot route. A GPU initialization message motivated one
`--disable-gpu` trial; it did not fix capture. A successful Quarto capture later
emitted the same transient GPU message, so it is not by itself a failure criterion.
The precise upstream cause of Brave's CLI capture hang remains unresolved.

A private DevTools-pipe diagnostic independently established browser responsiveness,
local document execution, layout and successful Page.captureScreenshot. It opened
no network debugging port and preserved browser sandboxing. No arbitrary flag
sweep was performed. See Chrome's [headless documentation](https://developer.chrome.com/docs/automation-and-testing/headless)
and the [Page protocol](https://chromedevtools.github.io/devtools-protocol/tot/Page/).

## Repeatable route and actual observations

The existing Python smoke/capture command now uses one small Node-built-ins-only
helper, `scripts/visual_capture.mjs`, for the demonstrated pipe interface. The old
CLI route remains explicitly selectable with `--backend cli` for diagnosis;
it is not the supported capture path on this installation. Both probes run before
launch. The Python process enforces a total timeout and terminates only its own
capture process group on timeout. The helper waits for page completion, MathJax
startup if present, fonts and decoded images, measures the full content rectangle,
captures PNG pixels, closes the browser and records browser status. No framework
or packages were installed. Existing installed Node 24.14.0 is used.

Commands, as the ordinary host user through scoped approved execution:

```bash
python3 scripts/visual_inspection.py --output /tmp/coherent-inspection-retest/pipe-smoke
python3 scripts/visual_inspection.py --source book/figures/relative-phase-reference-planes.svg --width 1400 --height 600 --output /tmp/coherent-inspection-retest/pipe-svg
python3 scripts/visual_inspection.py --source /tmp/coherent-html-retest.TFrOHy/repo/book/_book/publishing-pilot.html --width 1440 --height 2200 --wait-ms 10000 --timeout 40 --output /tmp/coherent-inspection-retest/pipe-page
```

Those are evidence paths, not required future profile locations. The canonical
procedure uses configurable/new paths. Original identical CLI comparison:

```bash
/opt/brave.com/brave/brave --headless --user-data-dir=/tmp/coherent-inspection-diagnosis/host-brave-512/profile --window-size=1000,700 --screenshot=/tmp/coherent-inspection-diagnosis/host-brave-512/image.png file:///tmp/coherent-inspection-diagnosis/minimal.html
```

| Pipe test | Exit / seconds | PNG dimensions | Author actual-image examination |
|---|---|---|---|
| Smoke | 0 / 1.219 | 1000 × 700 | Heading, ordinary text, blue circle and Radius 60 px legible; no clipping |
| Existing reference-plane SVG | 0 / 1.270 | 1400 × 600 | Full figure, signal/LO paths and labels visible; L2 arrow overlaps label |
| Complete rendered publishing pilot | 0 / 2.975 | 1440 × 2200 | Typeset identity/aligned derivation, table, figure, caption and bottom navigation visible |

Author called the actual `view_image` tool on all three PNGs. The full-page image
was opened at original detail. The reference-plane product reads p = z2 z1*,
consistent with channel 2 relative to 1; neither a common reference nor the diagram
proves deterministic phase. Dark blue lines/text on white/pale blue have clear
contrast. The LO vertical line crosses the second fixture line without an explicit
junction disposition; P2 lies close to this crossing. L2 is overprinted by its
injection arrow. These are existing presentation concerns, not capture failures.
The page has repeated generated labels “Equation Equation 8.1”, “table Table 8.1”
and “Figure Figure 8.1”; its diagram labels are smaller than in standalone view.
No fixes were made because illustration/manuscript remediation is outside this
retest. The caption correctly limits the publishing demonstration's validity.

Fresh scratch-copy Quarto render exited 0 and produced eleven pages. The captured
page's document was complete, with four math elements and four MathJax containers,
and a loaded figure; actual pixels show equations rather than raw TeX. The content
rectangle and PNG both span 1440 × 2200, and the bottom navigation is visible.
The large lower whitespace is the tall viewport's page layout, not missing content.
This does not establish offline MathJax availability or all chapter layouts.

## Least privilege and proposed persistence

The working route is a scoped approved invocation of this capture script outside
the parent Codex sandbox, as UID 1000, retaining the browser sandbox. All profiles,
XDG config/data/cache/runtime and temp files are private to each capture. Protocol
traffic uses inherited private pipes; no debugging listener, unrestricted shell
approval, root execution, global sandbox weakening or personal profile is needed.
This is the least-privileged reliable route demonstrated in these tests, not a
proof that all alternative policies have been excluded. Do not repeat browser
launches inside the demonstrably incompatible sandbox.

Minimum proposed persistent resource setting: owner-managed new file
`/etc/sysctl.d/90-coherent-visual-inspection.conf` containing only
`fs.inotify.max_user_instances = 512`. Do not change max_user_watches or security
settings. This retains the now-demonstrated resource headroom; it alone does not
repair the CLI path. Potential kernel-memory use rises with permitted instances.
Owner-only application and rollback are in the canonical procedure. Codex has not
installed the file; persistence across reboot and sustained peak workload are
unverified. The exact smallest sufficient value below 512 has not been measured.

## Separate review and fresh-session evidence

Fresh ephemeral independent reviewer `01a18bee-7561-77d2-a913-a008e4e36528`
requested GPT-6.1 Sol / high with an enforced `-s read-only` shell. The CLI launched
through scoped host approval and exited 0. Actual smoke, standalone-figure and
complete-page PNGs were attached with three `-i` arguments; source SVG, rendered
HTML/assets, manuscript model and accepted requirement files were frozen and
hashed in an isolated packet. No author findings, conversation, active project
state, prior reviews or dispositions were supplied. The reviewer reports actual
viewing as attachments and through the image viewer, independently verified all
34 manifest entries and decoded the PNGs. Concrete observations include the circle's
120-pixel diameter/RGB(20,100,180), arrow directions, L1 crossing, L2 overlap,
repeated reference names, aligned mathematics, caption and bottom navigation.
The first dimension command used absent `python`; the reviewer corrected it to
`python3`. No prohibited exposure, edits, delegation or connectors were reported.
Exact backend model/effort routing was not independently introspected.

[Unedited reviewer findings](visual-inspection-evidence/retest-512/pixel-review-findings.md),
[input manifest](visual-inspection-evidence/retest-512/pixel-review-inputs.sha256),
[prompt](visual-inspection-evidence/retest-512/pixel-review-prompt.txt) and
[session metadata](visual-inspection-evidence/retest-512/sessions.json) are preserved.
Author disposition is separate: accept the observed presentation defects/concerns;
defer their corrections to the paused illustration/editorial initiative. None
prevents using the inspection capability, and none grants visual adequacy. The
mathematical atan2 reassessment from the prior task remains completed and unchanged.

Fresh author-workflow session `01a18bef-d3b4-7003-8121-6c13cf312264` was launched
with no conversation, using only repository instructions and a bounded smoke-test
request. It found root AGENTS.md/the canonical procedure, used a fresh output
directory, reported the ordinary sandbox's preflight failure without browser
launch, obtained scoped approval for the same command, captured a new 1000 × 700
image in 1.219 s (script/browser exit 0), and reported actual pixel examination.
It independently rehashed the PNG; its hash equals the managing author's smoke
image hash. CLI exit was 0. [Fresh findings](visual-inspection-evidence/retest-512/fresh-session-findings.md)
and the separate fresh sandbox/host environment/result/image artifacts are
preserved. No repository edit, installation, host change or delegation occurred.
The CLI JSON exposes command events and final reports but does not expose every
Code Mode image-tool call; no claim of independently instrumented image-tool
telemetry is made. Actual images were also explicitly attached to and examined
by the isolated independent reviewer above.

Invocation forms: `codex exec --ephemeral --skip-git-repo-check -C PACKET
-m gpt-6.1-sol -c model_reasoning_effort='"high"' -s read-only
-i PACKET/smoke.png -i PACKET/figure.png -i PACKET/page.png --json -o OUTPUT -`
for the reviewer, with the preserved prompt on stdin; fresh workflow used
`codex exec --ephemeral -C REPOSITORY -m gpt-6.1-sol
-c model_reasoning_effort='"high"' --approve-for-me --json -o OUTPUT PROMPT`.
These are new contexts, not resumed/forked author contexts.

## Closeout and limits

All requested inspection capabilities are demonstrated for the tested environment:
SVG-to-PNG, actual author raster viewing, complete rendered Quarto-page inspection,
fresh read-only reviewer receiving/examining actual raster attachments, and
fresh repository-only discovery/execution/inspection. The canonical procedure
was updated and its root AGENTS.md instruction remains mandatory. The new helper
is justified by the demonstrated CLI-entry failure; it introduces no framework.

Syntax checks (`python3 -m py_compile scripts/visual_inspection.py` and
`node --check scripts/visual_capture.mjs`), `python3 scripts/check_repo.py`, and
`git diff --check` passed. Smoke, SVG, HTML and fresh-session captures exited 0.
Existing manuscript, accepted architecture, figures, visual audit and prior
independent findings were preserved. No physics regression, hardware test, new
source-claim review or human acceptance is inferred from these checks.

Remaining: upstream Brave CLI screenshot hang; reboot persistence of the temporary
512 setting; sustained resource-load behavior; other browsers/versions/OSs; offline
MathJax; PDF, mobile/responsive layouts and other chapter pixels; and correction/
acceptance of the identified presentation defects. The technical inspection
blocker is cleared for the tested private-pipe route while resource headroom is
available. The owner requested stopping after verification: no 26 interventions,
new chapters, commits, pushes or publications were started.
