# TRN-416 — QA triage (task qu50cce7 v1)

17 findings, 7 jobs, chain completed 2026-11-14 06:36 UTC, after the last run finished. Version tagged
**Failed QA**.

## The filter applied

The FA reports reasoning and method failures. A finding about how the grader distributed credit is not one:
the grade is not a delivery article, and the skill's own rule is that grader flags never produce grader
edits. Tooling and environment friction is not a mode either. That removes nine of the seventeen outright,
and a further four on the writer's adjudication below.

**Writer's adjudication, 2026-11-15, recorded as settled.** The composition-ceiling comments are overly
prescriptive and the intended golden is within scope. Findings 1, 5, 9 and 11 are closed on that basis.
This resolves the one open question in the previous version and it resolves it in the direction that
helps: the requirement basis for M1 and M2 is secured rather than contested.

## What survives, and why

| # | Finding | Why it survives | What it does |
|---|---|---|---|
| 2 | Rubric penalises flagging genuine biophysical inconsistencies | **Evidentiary, not a grading complaint.** A grader confirmed the inconsistencies are real | Guard. The runs that discounted the SPR, selectivity and epitope package were reasoning correctly. Writing that up would be writing up a grading defect as a model failure |
| 13 | Three records required to be accepted as clean contradict themselves, verified by reading the room | **Evidentiary.** Names the three: FC-007's enumeration method, BP-009's Rmax column and global-fit label, BP-011's construct lengths | Same guard, with the specifics. Also closed in the golden, which now flags the Rmax column and the CLIPS geometry and proceeds |
| 4 | Disclosed external reference crosscheck via `/opt/refdbs` | **Not grade-bearing.** It is a question about whether runs stayed inside the stated evidence boundary | Became M5. Thin, and your call. Also a room-design item: the mount exposes sequences the task did not anticipate |
| 17 | Guidance concedes the records carry repeated or implausible values | **Weakly evidentiary.** Corroborates that the repeats are known to the author | Was the basis of M4. **M4 is retracted**, so this now does nothing. See `error_modes.md` |

## Closed on the writer's adjudication

| # | Finding |
|---|---|
| 1 | Composition-ceiling chain dominates scoring; prompt never asks for it |
| 5 | "Ground truth" instruction conflicts with self-contradictory files |
| 9 | Open-ended grading expectations not stated |
| 11 | Prompt never mentions timepoints or composition ceilings — the check that rebuts finding 1 |

## Ignored: grade-bearing only

| # | Finding |
|---|---|
| 12 | Rubric makes the recommendation's position immaterial, overriding "lead with it on the first line" |
| 14 | Same, from the problem linter |
| 15 | Guidance makes the go/no-go direction neutral. All 16 runs held anyway |
| 16 | Guidance requires every number right but states no reference values or file names |

Worth doing before any rerun, not before this submission. The golden now carries the reference figures, so
16 is cheap to write.

## Ignored: environment and tooling

| # | Finding |
|---|---|
| 3 | Contrived saturation of planted flaws; reads as an error hunt |
| 6 | `/opt/refdbs` availability differs between rollouts |
| 7 | Reference mount contents differ between runs |
| 8 | Missing PDF and archive utilities in every environment; workarounds existed |
| 10 | Reference-DB tool incompatibilities (snpEff wrapper, Perl Storable cache) |

Difficulty has to live in the problem, not the toolchain. Task notes only.

## Coverage gap

Every ClaudeScope cluster names Opus hashes, all eight of them, and no Fable hash anywhere. That check saw
one of the two jobs, so its silence about Fable carries no information. Its `itemCount` is 10 against a
`findingCount` of 14, which the export does not explain. The two `difficulty` jobs returned nothing, and
the earlier of them started before the Fable panel finished.

## Net

No blocker. Nothing requires a prompt or room edit before the FA can be written. Two findings reached the
golden and are closed. One standing guard: do not write up the biophysical package, or FC-007's enumeration
method on its own, as a model failure.
