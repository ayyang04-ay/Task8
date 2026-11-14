# TRN-416 — QA triage (task qu50cce7 v1)

17 findings, 7 jobs, chain completed 2026-11-14 06:36 UTC. Fresh: QA ran against this version, and the two
auto-QA jobs that matter started 04:13, after the last run finished 22:23 the previous day. Version tagged
**Failed QA**.

**Coverage gap to know about.** Every ClaudeScope cluster names Opus hashes only — all eight of them, no
Fable hash anywhere. ClaudeScope saw one of the two jobs. Its `itemCount` is 10 against a `findingCount`
of 14, which the export does not explain. The two `difficulty` jobs ran at 22:15 and 22:23, so the earlier
one preceded the end of the Fable panel; both returned nothing.

Run labels substituted for hashes throughout.

## Triage

| # | Finding | Runs named | Type | Affects golden? | Action |
|---|---|---|---|---|---|
| 1 | Composition-ceiling chain dominates scoring; prompt never asks for it | Opus A5, A2, A7 | Ambiguity / undisclosed constraint | no | **Your call.** Self-contradicting with #11. M1 restates the same ground as what the runs did with the count record, which does not need the requirement to be stated. Option A: ship M1 in that form and leave the prompt alone. Option B: add one clause to the prompt and rerun, which is a blocker |
| 2 | Rubric penalises flagging genuine biophysical inconsistencies | Opus A3 | Factual issue in the golden | **yes** | **Done.** Rmax column added as a flagged-and-not-pursued item, with the drift, the regression and what it reaches. Runs that discounted the package must not be written up as a mode |
| 3 | Contrived saturation of planted data flaws; reads as an error hunt | Opus A4 | Prompt / data room | no | **Defer.** Room-design comment, not actionable on this version. No mode rests on it |
| 4 | Disclosed external reference crosscheck via `/opt/refdbs` | Opus A3, A5, A7 | ClaudeScope cluster, 2+ runs | no | **Sent to Phase 1** → became M5, thin. Also a room-design item: the mount exposes TNFR1/TNFR2 sequences the task did not anticipate |
| 5 | "Ground truth" instruction conflicts with self-contradictory files | Opus A5, A2 | Ambiguity | no | **Your call.** Every run resolved it the same way, treating the files as the record to audit. No mode turns on it. A one-line prompt change would close it and costs a rerun |
| 6 | `/opt/refdbs` availability differs between rollouts | Opus A7 | Tooling | no | **Ignore for the FA.** Environment item: rollouts should face the same mount |
| 7 | Reference mount contents differ between runs | Opus A4 | Tooling | no | **Ignore for the FA.** Same item as #6 |
| 8 | Missing PDF and archive utilities in every environment | Opus A1, A2 | Tooling | no | **Ignore for the FA.** Workarounds existed; no run failed on it. Task note only |
| 9 | Open-ended grading expectations not stated | Opus A3, A1, A8 | Ambiguity | no | **Your call**, same substance as #1 |
| 10 | Reference-DB tool incompatibilities (snpEff wrapper, Perl Storable) | Opus A3, A7 | Tooling | no | **Ignore for the FA.** Difficulty must live in the problem, not the toolchain |
| 11 | Prompt never mentions timepoints or composition ceilings | — | Ambiguity, self-rebutting | no | **Context for #1.** This check rebuts the ClaudeScope cluster: the quoted text is from grader guidance, not the files, and the open prompt invites the derivation. Note the contradiction when you settle #1 |
| 12 | Rubric makes recommendation position immaterial, overriding "first line" | — | Grader-only | check | **Defer, no grader edit.** Probe: buried recommendation 0.88 against leading 0.85. Golden leads with its recommendation, so nothing to revise there. Same issue as #14 |
| 13 | Records required to be accepted as clean contain internal contradictions | Opus A3 | Data room, with a golden-side fix | **yes** | **Done, in part.** Golden now flags the SPR Rmax column and the CLIPS construct geometry and proceeds. FC-007 needed nothing: the golden already states the cancellation. Still open as a room item if you want the records corrected — QA's fixes are flow-based enumeration, a relabelled Rmax column with one global rate pair, and a corrected CLIPS header |
| 14 | Prompt requires the recommendation on the first line, guidance says immaterial | — | Grader-only | no | **Defer.** Same as #12. Static analysis, no runs. Fix is one A-item plus one B-item, or drop the prompt line |
| 15 | Guidance makes the go/no-go direction neutral | — | Grader-only | no | **Defer.** All 16 runs landed on hold anyway, so it changed nothing on this panel. It would matter on a rerun |
| 16 | Guidance requires every number right but gives no reference values or file names | — | Grader-only | no | **Defer.** Worth doing before any rerun: the golden now carries the reference figures, so the block is cheap to write |
| 17 | Guidance says records carry repeated or implausible values, prompt says ground truth | — | Ambiguity | check | **Partly closed.** The repeated values are real and named: the IL-2 titration's three mean/SEM pairs over six doses. M4 is built on them. Whether to name them in the guidance is a grader item |

## What this leaves

| Bucket | Items |
|---|---|
| Done in the golden | 2, 13 (SPR Rmax, CLIPS geometry, document-versus-file loading quantities) |
| Your call, and the one that shapes the FA | 1, with 9, 11 and 5 as the same question |
| Deferred grader items, after submission | 12, 14, 15, 16, 17 |
| Environment, not FA material | 3, 6, 7, 8, 10 |
| Became a mode | 4 → M5 |

**No blocker.** Nothing on this list requires a prompt or room edit before the FA can be written. The two
findings that reach the golden are closed, and the modes that clear do not rest on a QA-flagged record.

## One standing caution

Findings 2 and 13 both say the panel was penalised for accurate, data-grounded flags. Two of the three
best-looking candidate modes sat exactly there. Anything written up about the biophysical package, or about
FC-007's enumeration method on its own, is writing up a grading defect as a model failure.
