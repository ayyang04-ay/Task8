# TRN-416 (task qu50cce7 / 1665bc436cf34a3389385f7fcc62f278, v1) — submittability

v2: the data room and golden on this branch closed the two Phase 0 gaps. Verdict unchanged; the golden
edits are narrower than v1 proposed, and six modes now clear instead of one. See `error_modes.md`.

## Verdict

**Submittable after golden edits.** Six modes clear, across both models, none resting on a QA-flagged
record. One candidate must not ship: the runs that discounted the biophysical package were right.

## Checks

| Check | Result | Reason |
|---|---|---|
| QA fixability | pass, with a deferred room item | Every QA flag that matters is grader-side or room-side and does not stop the FA. The three self-contradicting records are real (env_linter read them in `/tmp/world/filesystem`) but their **values** are in the room, so nothing a correct answer needs is missing |
| Golden derivability | pass, one narrow edit | Read on this branch. Its composition bound (1.082) and its baseline test (1.962 points, p 0.0475) both reproduce from the room. It does not address the Rmax column |
| At least one mode | pass | Six, in `error_modes.md`. M1 and M6 are the strongest |

## Mode that cleared

**Benchmark comparison kept after its own baseline check disqualified it**

Runs: `Opus A4 (592daeaf)`, `Opus A5 (6bed1c6a)`, `Opus A6 (28f93fc5)`, `Fable A5 (956b8dbc)`,
`Fable A6 (911519d1)`.

Each run measures the spread in the replicated untreated arm (10.622 / 8.660 / 7.064 % in FC-002, FC-006,
FC-005), states that the spread is as large as the drug effect and that comparisons between records
therefore fail, and then states in its headline reasons that TNF moves the same gate by the same amount —
with no caveat at the point of use, and as a reason the effect is unimpressive.

Where it is visible:

| Run | Claim made | Its own disqualifying finding |
|---|---|---|
| Opus A4 | summary bullet, "modest against the package's own benchmarks" | vehicle-arm list later in the same section |
| Opus A5 | §1 "The answer in brief", bullet 2 | §2 bullet: "That disqualifies every cross-study claim in the package: TRN-416 vs TNF" |
| Opus A6 | item 3 of the not-established list; §3.1 heading | the same §3.1 heading also sets the effect against the between-study drift |
| Fable A5 | bolded bullet in the supporting case | three differing baselines given earlier in the memo |
| Fable A6 | framing paragraph under the recommendation; repeated "for scale" | later bullet: every comparison between studies "fails on this" |

Same pattern but **caveated where it is used**, so weaker and your call whether to include:
`Opus A1 (7d49af8b)`, `Opus A2 (93025547)`, `Opus A7 (fab5dde9)`, `Opus A8 (dd82c62e)`,
`Fable A3 (4bd0f2db)`. `Fable A1 (a661fc46)` and `Fable A2 (9e896b79)` do not do it at all.

## Golden edits required

Narrower than v1 proposed, because the golden already handles the count record correctly.

| Location | What changes | Why |
|---|---|---|
| ~~The paragraph calling format, selectivity and proximal signalling "all clean"~~ | **Done.** The Rmax column is now a fourth flagged-and-not-pursued item in the set-aside section, with the drift, the regression, what it reaches (the rate constants) and what it does not (the KD and the selectivity call). The "all clean" conclusion is kept and now rests on the per-concentration KD stability | `build/validation_runs/audit_golden_vs_room.txt` FINDING 15 had already raised this at build time and the golden was never updated |
| ~~The CLIPS header, and the epitope spans~~ | **Done.** Added as a fifth flagged-and-not-pursued item: the construct lengths, that sequence length and span agree row by row so the three regions stand, and that thirteen rows from a library of up to 10,000 with no stated cutoff means an absent region is not a tested negative. The PDF's 1 mg and 0.1 mg per well went into the companion-document conflicts paragraph | The spans-outside-the-fragment objection in `ceiling_solve.txt` does **not** hold: section 1 of the companion document says immunisation continued with the whole exterior portion of the protein, so an epitope outside aa 50-122 is expected. The golden now says so |
| The two "TNFR2" linear peptides reported as TNFR1 sequences | **left out deliberately.** Only reachable through an external sequence database, which the golden may not rest on | Three Opus runs found it via the `/opt/refdbs` mount and quarantined it. It stays a room-design question, not golden content |
| No change needed on FC-007 | — | The golden already states the cancellation: the bound "is a ratio of counts within a single record and so cancels any gate bias that is constant across the dose series." That is what makes the Opus mode safe to ship |

## Held — your call

| Item | Why held |
|---|---|
| Composition-ceiling chain missing in all 16 runs | ClaudeScope raises it as an **unstated requirement**; the data-quality check rebuts that. QA contradicts itself. M1 restates it as what the runs did with the record rather than as a required derivation, which is the form I would defend |
| Opus runs discarding the count record (all 8 Opus; no Fable run) | **Out of held.** The golden states the cancellation argument independently, so this no longer rests on my reading alone |
| Runs discounting the SPR / selectivity / epitope package | **Do not ship.** QA verified the inconsistencies are real and calls the penalty a grading misalignment, not an agent error |
| Bulk compartment disjunction never quantified (all 16) | An expert can defend saying it is unresolvable and moving on |
| Paired analysis run, pooled comparison never made (all 16) | A run that correctly chooses paired does not obviously owe the pooled contrast. Expert norm, not a stated requirement |

## Deferred

- Recommendation position: prompt demands line 1, grader guidance says position is immaterial twice. Probe showed 0.88 for a buried recommendation against 0.85 for a leading one. Grader item, after submission.
- Grader guidance carries no reference values or file names for the quantities it requires to be correct.
- Grader guidance makes the direction of the call neutral, so "commit now" is unpenalised.
- `/opt/refdbs` contents differ between rollouts; some runs could check the epitope peptides against real TNFR1/TNFR2 sequences and others could not. Environment, not a mode.
- Missing PDF and archive utilities in every run. Tooling note.

## Phase 0 manifest

| Row | Result |
|---|---|
| Run export located | pass — two jobs, `bf8a192e` (Opus 5.5) and `7e7a0a3c` (Fable 5.2) |
| Export complete | pass — both `export_selection` carry outputs, transcripts, grading; `task_files` and `grader_files` excluded in both |
| Clusters present | n/a — no `task_files/_ERROR.txt`; the room was excluded by selection, not failed download |
| Run map | pass, 16 rows, below |
| Run count and status | pass — 8 + 8, all completed, none refused, none truncated |
| QA report | pass — fresh, chain completed 2026-11-14 06:36, after the last run finished 22:23 the previous day. 17 findings / 7 jobs. ClaudeScope `itemCount` 10 against `findingCount` 14, unexplained. Version tagged **Failed QA**. The two `difficulty` jobs ran at 22:15 and 22:23, so the earlier one preceded the end of the Fable panel; both returned nothing |
| Golden | **fail** — not in the export, and no rubric or grader files either |
| Data room | **fail** — excluded by export selection. I worked from the deliverables and the grader rationales; env_linter read the room directly, so its file-level claims are usable |
| Grading document | pass — writer-authored `grader_guidance`, A/B/C. Identical across both jobs, as is the prompt. **Graded mode, context only** |
| Stats availability | not yet needed |
| Thinking channel | not yet read |
| Deliverable present | pass — all 16, one main memo each |

## Run map

| Label | Short hash | Model | Attempt |
|---|---|---|---|
| Opus A1 | 7d49af8b | Opus 5.5 | 1 |
| Opus A2 | 93025547 | Opus 5.5 | 2 |
| Opus A3 | 2e8d4225 | Opus 5.5 | 3 |
| Opus A4 | 592daeaf | Opus 5.5 | 4 |
| Opus A5 | 6bed1c6a | Opus 5.5 | 5 |
| Opus A6 | 28f93fc5 | Opus 5.5 | 6 |
| Opus A7 | fab5dde9 | Opus 5.5 | 7 |
| Opus A8 | dd82c62e | Opus 5.5 | 8 |
| Fable A1 | a661fc46 | Fable 5.2 | 1 |
| Fable A2 | 9e896b79 | Fable 5.2 | 2 |
| Fable A3 | 4bd0f2db | Fable 5.2 | 3 |
| Fable A4 | f2892b68 | Fable 5.2 | 4 |
| Fable A5 | 956b8dbc | Fable 5.2 | 5 |
| Fable A6 | 911519d1 | Fable 5.2 | 6 |
| Fable A7 | a1ac409c | Fable 5.2 | 7 |
| Fable A8 | 5a66db2d | Fable 5.2 | 8 |

## Task note

`job_info.json` for the Fable job reports `clears_gate: false` against a `max_avg_score` of 0.55. Under
current guidance there is no score gate, so this is noise, but it will show in Studio.

## Coverage

Read in full: the five deliverable sections carrying the cleared mode, in Opus A4, A5, A6 and Fable A5, A6,
plus the surrounding baseline sections. Screened all 16 deliverables for the mode with four patterns of
differing looseness and in both directions, then read every match. No transcript read yet — the mode is
visible in the deliverables. Nothing here rests on a score.
