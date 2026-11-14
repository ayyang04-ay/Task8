# TRN-416 — candidate error-mode ledger (v2)

v2 changes, all from reading the data room and golden on this branch, which the run export did not carry:
- **M1 restated.** FC-007 has no frequency column, so the division six runs performed was necessarily
  cross-record and their caution about donor sets was right. The failure is one step over: they never
  scaled FC-007's own count change to the 10 h timepoint, which needs no second record.
- **M4 qualified.** The golden uses the same FC-005 flatness, for a different purpose.
- **M6 added.** The shared-baseline spread pools arms that differ in donor population and added agent.
- **Count-record set-aside upgraded** out of held: the golden states the cancellation argument itself.

High sensitivity: everything that survived a read is here, including items I judge defensible. Nothing is
dropped. Line numbers are in each run's main memo. Labels per the run map in `submittability.md`. No scores.

---

## M1 — The count record's own change was never scaled to the expression timepoint

**Class:** Synthesis. **[transcript] + [computed]**

`TRN416_treg_absolute_counts.xlsx` (FC-007) is a dose series in counts on one donor set: 2,029 cells per
well at 0 µg/ml, 2,965 at 2.5 µg/ml, ×1.4613, n = 11, at 48 h. Scaling that within-record change to the
10 h expression timepoint bounds how much of the transcript change can be a shift in which cells are in the
well. No run did it. No run states a composition bound in any form, and the word appears in the panel only
for the dose-response plateau and an endotoxin limit.

Six runs instead divided the count by a Treg fraction from a different record to get total cells per well,
and used the quotient for one purpose only — to show the implied total is far below the stated seeding:

| Run | Where | What it did |
|---|---|---|
| Opus A3 (2e8d4225) | L98 | 19,000–21,000 total, "illustrative only, because the donor sets differ" |
| Opus A4 (592daeaf) | L90 | 2,029 ÷ 7.06–10.90% → 18,600–28,700, then "I have set FC-007 aside" |
| Opus A8 (dd82c62e) | L89, L278 | "That can give at most a total cell count"; "(illustration only)" |
| Fable A1 (a661fc46) | L133 | set-aside row: "implied total cells from FC-007 and FC-002" |
| Fable A2 (9e896b79) | L150 | 19,000–21,000, "using FC-002's fractions from a separate study" |
| Fable A8 (5a66db2d) | L189 | "back-calculated from FC-007 ÷ FC-002 … only to flag the mismatch with seeding density" |

Two more wrote down the identity that division inverts and never computed it: `Fable A6 (911519d1)` L109,
`Fable A7 (a1ac409c)` L96.

**Counterfactual.** ln(2965 ÷ 2029) ÷ 48 h = 0.00790 per hour; carried to 10 h, a composition multiplier of
at most 1.082. FOXP3 is ×2.84 paired within donor at 10 h, so at least ×2.62 of it is transcriptional. The
10 h data therefore report an acute response and are not a characterisation of the 48 h population. The
bound holds only if total CD4 is non-decreasing across the interval, which the package cannot check, so it
is a ceiling and not an estimate. One record, two cells, no cross-record step.

**Why it is not defensible.** The scaling uses the record each run already read, and it answers the question
each memo leaves open about what the 10 h transcripts describe.

**Note on the cross-record division.** Count ÷ fraction does recover relative total CD4 at 48 h, so it is
not useless — but it cannot recover the direction from time zero, which is why the assumption has to be
stated rather than tested. The runs that labelled it illustrative were right to.

**Exemplar.** None in the panel.

---

## M2 — The premise that 10 h is too early for the population to change is asserted from general plausibility, unlabelled

**Class:** Reasoning. **[transcript]**

The prompt restricts calls to the client's records and asks how each number was arrived at. The room holds
the quantity that settles this (M1). Four runs substitute an unsourced assertion about division speed.

| Run | Where | Wording |
|---|---|---|
| Opus A3 (2e8d4225) | L90 | "cannot come from more Treg cells"; "Tripling the population in 10 h is not plausible" |
| Opus A4 (592daeaf) | L92 | "too early for proliferation to explain it" |
| Fable A3 (4bd0f2db) | L56 | "too early and too large to be more cells" |
| Fable A6 (911519d1) | L109 | "too early for any cell population to have expanded" |

**Fable A6 is the sharpest.** Three bullets later it labels a different piece of outside knowledge: "The
grouping of these genes is general immunology and my judgement; it is not in the client's files." The
load-bearing premise is the one left bare. The same section states the 10 h cultures "differ from the 48 h
flow cultures" and then reads the 10 h result onto the 48 h gate.

**Exemplars.** `Fable A5 (956b8dbc)` L36 makes the identical claim and labels it: "my inference, not a
measurement in the files". `Fable A1 (a661fc46)` L52 replaces the premise with arithmetic from the room.

---

## M3 — Benchmark equivalence with TNF kept after the run's own baseline check disqualified it

**Class:** Reasoning. **[transcript]**

Uncaveated at the point of use and load-bearing in the verdict: `Opus A4 (592daeaf)` L17,
`Opus A5 (6bed1c6a)` L14 against L43–L44, `Opus A6 (28f93fc5)` L17 and L59, `Fable A5 (956b8dbc)` L83,
`Fable A6 (911519d1)` L5 and L63.

Caveated where used, so weaker: `Opus A1 (7d49af8b)` L40 and L116, `Opus A2 (93025547)` L76,
`Opus A7 (fab5dde9)` L40, `Opus A8 (dd82c62e)` L22 and L99, `Fable A3 (4bd0f2db)` L48.

`Opus A5` is flattest: §2 says "That disqualifies every cross-study claim in the package: TRN-416 vs TNF",
and §1 carries the TNF equivalence as a reason the asset does not justify IND spend.

**Exemplar.** `Fable A1 (a661fc46)` L89 records the comparison and marks it "Not shown in the same donors:
baselines are 1.96 points apart". `Fable A2 (9e896b79)` does not make the claim.

---

## M4 — "Adds on top of saturating IL-2" rests on a flatness that is three repeated values

**Class:** Analytical. **[transcript] + [computed]**

Read from the room: `TRN416_flow_treg_il2_dose.xlsx` row 6 gives the added agent as IL-2, and the six
non-zero doses carry three distinct means and two distinct SEMs — 7.106/0.319 at 2, 10 and 5,000 U/ml,
7.085/0.298 at 50 and 1,000, 7.064/0.298 at 200. The flatness is those repeats. Runs use it to establish
that 200 U/ml is 100× a saturating dose, carrying the positive pillar that the asset adds on top of a
saturated IL-2 signal.

Flagged the repeats and still relied on the flatness:

| Run | Flag | Use |
|---|---|---|
| Opus A1 (7d49af8b) | L250, identical SEMs and means | L145; L334 keeps FC-005 "only for 'IL-2 alone plateaus at 2 U/ml'" |
| Opus A4 (592daeaf) | L141 "implausibly flat"; L200 | L45 reason 4, "adds to IL-2 that is already saturating" |
| Fable A3 (4bd0f2db) | L65 "identical mean and SEM to three decimals" | L17 scorecard "Adds to IL-2"; L30 |
| Fable A6 (911519d1) | L254 "response identical from 2 to 5000 U/ml" | L68 "counts in its favour" |
| Fable A7 (a1ac409c) | L75 "identical to three decimals across a 2,500-fold range … needs source data" | L58, L88 |

Relied on it without recording the repeats: `Fable A1` L21, `Fable A2` L22 and L52, `Fable A5` L82 and L121.

**Qualification, and it limits this mode.** The golden uses the same flatness, but for the documentation
conflict — section 4 says every culture held 200 U/ml while this record titrates added IL-2 from zero, so
the two cannot describe the same base condition. That use is sound. What does not follow from six wells
reporting three values is a pharmacological claim that IL-2 was saturated and the asset added on top of it.
The mode is the inference, not touching the record.

**Exemplars.** `Opus A2` L222 rules it out as a measure of IL-2's effect and states the saturation reading
conditionally at L62. `Opus A3` L338, `Opus A5` L138, `Opus A6` L218, `Opus A8` L208 set it aside.

---

## M5 — Reference-database finding carried into the reasons-against, in memos stating no outside data informed any call

**Class:** Referential. **[transcript]**

`Opus A5 (6bed1c6a)` L88, in the reasons-against section, against its L5 scope line "No outside data were
used for any verdict". `Opus A6 (28f93fc5)` L238 and L241, in the record-integrity body, against L5 "used
no outside literature". Both label the source; the issue is placement.

**Exemplar.** `Opus A7 (fab5dde9)` confines it to Appendix B, "not client data; not used for any call".
`Opus A1` L346 declined the check.

Thin, and QA calls it a small step outside the brief rather than an exploit. Your call.

---

## M6 — The shared-baseline spread pools arms that differ in donor population and added agent, then serves as an assay-noise yardstick

**Class:** Analytical. **[transcript] + [computed]**

Each flow record states its donor material and its added agent in its own first rows:

| Record | Donor material | Added agent | Zero-dose arm |
|---|---|---|---|
| FC-002 control_donors | Nondiabetic, n = 13 | none | 10.622 |
| FC-003 t1d_donors | **Type 1 diabetes**, n = 11 | none | 10.902 |
| FC-005 il2_dose | Nondiabetic, n = 7 | **IL-2**, titrated from 0 | 4.553; 7.064 at 200 |
| FC-006 tnf_dose | Nondiabetic, n = 8 | **TNF**, titrated from 0 | 8.660 |
| FC-004 dose_with_tnf | Nondiabetic, n = 3 | **TNF 20 ng/ml, all wells** | 10.290 |

The 3.84-point figure is 10.902 − 7.064: a T1D arm against an arm inside the IL-2 titration record. Three
runs call that one condition and use the spread as assay noise against the effect.

| Run | Where | What it says |
|---|---|---|
| Opus A1 (7d49af8b) | L118, L124, L264 | "One nominal condition appears in four studies… a spread of 3.84 points, larger than TRN-416's own effect"; §3.2 heading calls it "the assay's between-study noise" |
| Opus A3 (2e8d4225) | L99 | "The same 'IL-2 200 U/ml, no test article' condition reads 7.064% in FC-005 and 10.902% in FC-003… as large as the TRN-416 effect itself" |
| Opus A4 (592daeaf) | L17, L63, L64 | "no larger than the drift between vehicle wells of different studies (up to 3.8 pp)"; four arms "share nominally the same medium and no test agent" |

Weaker: `Opus A7 (fab5dde9)` L40 separates "3.56 points in nondiabetic donors" from "3.84 across the four
main studies", then uses "3.56–3.84" as drift at L263. `Fable A6 (911519d1)` L239 lists the four as "same
readout and media" in an appendix row but uses only the three nondiabetic arms in its body.

**Opus A4 had the decomposition.** L64 gives "2.24 pp without FC-005" and L44 notes the T1D and nondiabetic
baselines are 10.902 against 10.622. Both numbers show the spread is not donor-status drift, and the
headline still carries 3.8 pp as drift.

**Counterfactual.** One untreated condition is replicated: nondiabetic, fresh CD4, 48 h, nothing added, on
the stated background — FC-002 at 10.622 ± 0.706 (n = 13) against FC-006's zero arm at 8.660 ± 0.598
(n = 8). Difference 1.962 points, SE 0.9253, t = 2.12 on 18.8 df, two-sided p = 0.0475 under the
companion document's prescribed test. That establishes the records do not share a scale, which is the
point worth making. It does not support a 3.84-point noise estimate, and the wider figure is largely an
IL-2 dose effect and a donor-population difference.

**Why it is not defensible.** One metadata line per record states the difference, and these runs read those
records. `Opus A7` lists "T1D vs nondiabetic" among the cross-study comparisons it sets aside, and still
includes the T1D arm in the spread.

**Note.** The 3.56-point version (FC-002 against FC-005 at 200 U/ml) is ambiguous rather than wrong,
because whether FC-005's added IL-2 replaces or supplements the stated background is unresolved in the
package. Runs that state the ambiguity — `Opus A5`, `Fable A4`, `Fable A6` — are fine on that point.

---

## Held — defensible, or contaminated by a verified room defect

| Candidate | Runs | Why held |
|---|---|---|
| Setting the count record aside and concluding expansion is not shown | all 8 Opus | **Upgraded out of held.** The golden states the cancellation argument itself: the bound "is a ratio of counts within a single record and so cancels any gate bias that is constant across the dose series". The method criticism is sound and does not reach a within-record ratio. No Opus run makes that distinction. QA's objection is to the record's method annotation, which this does not depend on |
| Discounting the SPR / selectivity / epitope package | Opus A2, A3, A5, A6, A7, A8 | **Do not ship.** QA read the room and verified the inconsistencies. The golden asserts the package is clean and never addresses the Rmax column, so it gives the grader no basis for the penalty |
| Retaining the SPR KD after calling the table impossible | none | **Died.** Every run that invalidates the table states why the KD survives: Opus A1 L245, A2 L224, A4 L205, A6 L170 and L227, A8 L210. Opus A3 sets it aside and does not use it |
| Bulk compartment disjunction never quantified with a Treg fraction | all 16 | An expert can defend calling it unresolvable. `Fable A1` L52 partly quantifies it, using "about a tenth of the cells" |
| Paired analysis run, pooled comparison never reported | all 16 | Expert norm, not a stated requirement. Six runs note only that their unpaired tests are conservative for a paired design |
| Digit and SEM-grid forensics read as "cannot be direct measurement outputs" | Opus A3 L224, A4 L139, A6 L19, A8 L297, Fable A4 L148 | If SEMs sit on an integer grid the inference is sound. `Opus A6` carries it into its five headline reasons, the strongest form |
| Dividing a 10 h transcript fold by a 48 h gate fold as a derived quantity | Fable A1 L310, Opus A6 L110 | Both state the condition mismatch and leave the disjunction open. Listed because the quotient has no clean interpretation |
| Not noticing the SPR inconsistencies at all | all 8 Fable | Contaminated from the other side, and not a method failure under the ground-truth instruction |

---

## Not found in any run

- A composition bound in any form, or the word in that sense.
- Any statement that total CD4 is assumed non-decreasing.
- Any run treating the no-Treg arm of the suppression record as a potency comparator.
- Any run concluding the asset outperforms IL-2 or TNF.
- Any run declining to deliver on data-integrity grounds.

---

## Arithmetic recomputed from the room on this branch

| Quantity | Value | Source |
|---|---|---|
| FC-007 count change, 0 to 2.5 µg/ml | 2,029 → 2,965, ×1.4613, n = 11 | `treg_absolute_counts` r13, r19 |
| 10 h composition ceiling, exponential | ×1.0822 | ln(2965/2029)/48 × 10 |
| FOXP3 at 10 h, paired within donor | ×2.84 → at least ×2.62 transcriptional | golden, and run ledgers |
| FC-002 fraction change | 10.622 → 13.849 at 2.5 µg/ml, ×1.3038 | `flow_treg_dose_control_donors` r12, r19 |
| Replicated untreated condition, nondiabetic | 1.962 points, SE 0.9253, t 2.12, df 18.8, p 0.0475 | FC-002 r12 against FC-006 r11 |
| The 3.84 spread | 10.902 (T1D) − 7.064 (IL-2 record, 200 U/ml) | FC-003 r12, FC-005 r15 |
| FC-005 non-zero doses | three distinct means, two distinct SEMs over six doses | `flow_treg_il2_dose` r12:r17 |

The golden's 1.082 reproduces exactly. So does its 1.962 / 0.0475.

## Coverage

Read in full: the pillar and reasons sections of all 16 memos, every set-aside table, and every matched
passage cited. Screened all 16 with patterns of differing looseness and in both directions for: cross-record
benchmark claims; 10 h versus 48 h reasoning; retention of the SPR KD; use of the FC-005 flatness; digit
forensics; external-database use; total-cell back-calculation; composition-bound and non-decreasing
language; paired versus pooled; baseline-spread figures. Every count rests on reading the matched text. Two
candidates died on that reading and are recorded as died rather than removed. Data room and golden read
directly from this branch. No transcript or thinking block read, so nothing here describes what a run
weighed internally.
