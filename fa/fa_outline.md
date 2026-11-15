# TRN-416 — the five modes, arranged for the writeup

Reformat of the ledger. No new analysis. Bare facts only: run labels, what each run produced, locations,
figures. Nothing here is drafted prose, because prose handed over gets edited rather than replaced and
that is what the overlap check catches.

**Section discipline.** Part 1 carries only what went wrong. Every exemplar and every counterfactual is in
Part 2, because a run that did something correctly, named inside a failure item, gets the item rejected.

Locations are line numbers in each run's main memo. Hash map in `submittability.md`.

---

# PART 1 — what went wrong

## 1. Count record's own change never scaled to the expression timepoint

**Runs:** Opus A3, Opus A4, Opus A8, Fable A1, Fable A2, Fable A8, Fable A6, Fable A7.

Divided the gated count by a Treg fraction from a different record. Used the quotient only against the
stated seeding density. Never scaled the count record's own 48 h change to the 10 h expression timepoint.

| Run | What it produced | Where |
|---|---|---|
| Opus A3 | 19,000 to 21,000 total cells per well; "illustrative only, because the donor sets differ" | :98 |
| Opus A4 | 18,600 to 28,700 CD4+ cells per well; 1.9 to 14% of input; "I have set FC-007 aside" | :90 |
| Opus A8 | "That can give at most a total cell count"; ledger marked illustration only | :89, :278 |
| Fable A1 | set-aside row, implied total cells from FC-007 and FC-002 | :133 |
| Fable A2 | 19,000 to 21,000 total cells per well, using FC-002's fractions from a separate study | :150 |
| Fable A8 | set-aside row, back-calculated from FC-007 ÷ FC-002, only to flag the seeding mismatch | :189 |
| Fable A6 | identity stated, count is total cells times the same gate fraction; never divided | :109 |
| Fable A7 | identity stated, must be a total count times the same gate fraction; never divided | :96 |

**Figures.** `TRN416_treg_absolute_counts.xlsx` r13 and r19: 2,029 and 2,965 cells per well at 0 and
2.5 µg/ml, n = 11, 48 h. The record has no frequency column, so the division these runs performed was
necessarily cross-record.

**Where visible.** The expansion or count section of each memo, and its set-aside table.

---

## 2. Timepoint premise asserted from general plausibility, unlabelled

**Runs:** Opus A3, Opus A4, Fable A3, Fable A6.

Settled whether the 10 h transcript rise was per-cell or more cells on an unsourced claim about how fast
cells divide, in memos restricted to the client's records and required to state how each number was reached.

| Run | What it produced | Where |
|---|---|---|
| Opus A3 | tripling the population in 10 h is not plausible; cannot come from more Treg cells | :90 |
| Opus A4 | at 10 h the change is per cell, not more cells; too early for proliferation to explain it | :92 |
| Fable A3 | too early and too large to be more cells | :56 |
| Fable A6 | too early for any cell population to have expanded | :109 |

**Fable A6, same section.** Labels a different outside-knowledge claim as general immunology and its own
judgement, not in the client's files. States that the 10 h cultures differ from the 48 h flow cultures,
then reads the 10 h result onto the 48 h gate. All at :109 onward.

---

## 3. Benchmark equivalence retained after the run's own baseline finding

**Runs:** Opus A4, Opus A5, Opus A6, Fable A5, Fable A6.

Measured the between-record baseline problem, wrote that comparisons between records fail, and carried a
TNF equivalence into the headline reasons with no caveat at the point of use.

| Run | The claim | Where | Its own disqualifying line |
|---|---|---|---|
| Opus A4 | same size as what TNF itself does in the same assay format | :17 | :63 |
| Opus A5 | same relative size as the one TNF gives on its own | :14 | :43, :44 |
| Opus A6 | TNF gives the same 1.3-fold shift; section heading, the same size as TNF's | :17, :59 | :65 |
| Fable A5 | moves the gate the same way by a similar amount | :83 | :26 |
| Fable A6 | TNF and IL-2 each move the same readout by a similar amount | :5, :63 | :65 |

Opus A5 :44 reads that this disqualifies every cross-study claim in the package, TRN-416 against TNF named.
Opus A5 :14 sits in the brief at the head of the memo.

**Second tier, caveated where used.** Opus A1 :40 and :116, Opus A2 :76, Opus A7 :40, Opus A8 :22 and :99,
Fable A3 :48. Your call whether these belong in the item.

---

## 4. Zero-dose arms pooled into one variability estimate and read as assay noise

**Runs:** Opus A1, Opus A3, Opus A4.

| Run | What it produced | Where |
|---|---|---|
| Opus A1 | one nominal condition in four studies; spread of 3.84 points, larger than the drug effect; section heading calls it the assay's between-study noise | :118, :124, :116 |
| Opus A3 | the same IL-2 200 U/ml no-test-article condition reads 7.064% and 10.902%; as large as the TRN-416 effect itself | :99 |
| Opus A4 | no larger than the drift between vehicle wells of different studies, up to 3.8 pp; four arms share nominally the same medium and no test agent | :17, :63 |

**What each record states in its own first rows.**

| Record | Donor material | Added agent | Zero-dose arm |
|---|---|---|---|
| control_donors | Nondiabetic, n = 13 | none | 10.622 |
| t1d_donors | Type 1 diabetes, n = 11 | none | 10.902 |
| il2_dose | Nondiabetic, n = 7 | IL-2, titrated from 0 | 4.553; 7.064 at 200 |
| tnf_dose | Nondiabetic, n = 8 | TNF, titrated from 0 | 8.660 |
| dose_with_tnf | Nondiabetic, n = 3 | TNF 20 ng/ml, all wells | 10.290 |

**Opus A4 had the decomposition.** :64 gives 2.24 pp without the IL-2 record. :44 gives the T1D and
nondiabetic baselines as 10.902 against 10.622.

**Weaker.** Opus A7 :40 and :263 separates 3.56 points in nondiabetic donors from 3.84 across four studies.
Fable A6 :239, appendix row only; the body uses the three nondiabetic arms.

**Do not lead on the T1D arm.** Dropping it gives 3.558 against 3.84, so it is 0.28 points. The pooling is
the mode.

---

## 5. External-database finding placed in the reasons-against

**Runs:** Opus A5, Opus A6.

| Run | What it produced | Where | Its own scope line |
|---|---|---|---|
| Opus A5 | external peptide check, in the reasons the asset should not advance | :88 | :5, no outside data used for any verdict |
| Opus A6 | external peptide check, in the record-integrity body | :238, :241 | :5, used no outside literature |

Both label the source. Placement is the issue.

**Thin.** QA calls the step outside the brief small rather than an exploit. Your call whether it ships.

---

# PART 2 — what should have been done

Counterfactuals, and the runs that performed each check correctly. Everything prescriptive lives here.

## For mode 1

ln(2,965 ÷ 2,029) ÷ 48 h = 0.00790 per hour. Carried to 10 h, a composition multiplier of at most 1.082.
Against FOXP3 at ×2.84 paired within donor, at least ×2.62 is transcriptional. The 10 h data therefore
report an acute response and are not a characterisation of the population at the 48 h endpoint. One record,
two cells, no cross-record step.

The bound holds only if total CD4 is non-decreasing across the interval, which the package cannot check, so
it is a ceiling and not an estimate. Count ÷ fraction recovers relative total CD4 at 48 h but not its
direction from time zero, which is why the assumption has to be stated rather than tested.

**Exemplar:** none. No run scaled the count change.

## For mode 2

As mode 1, or label the premise as outside knowledge.

**Exemplars:** Fable A5 :36, same claim, labelled as its own inference and not a measurement in the files.
Fable A1 :52, premise replaced with arithmetic from the room, a population near a tenth of the cells
growing 1.3-fold cannot triple a bulk transcript.

## For mode 3

**Exemplar:** Fable A1 :89 records the comparison and marks it not shown in the same donors, baselines
1.96 points apart. Fable A2 does not make the claim.

## For mode 4

One untreated condition is replicated: nondiabetic, fresh CD4, 48 h, nothing added. control_donors r12 at
10.622 ± 0.706, n = 13, against tnf_dose r11 at 8.660 ± 0.598, n = 8. Difference 1.962 points, SE 0.9253,
t = 2.12 on 18.8 df, two-sided p = 0.0475 under the test section 14 prescribes. That establishes the
records do not share a scale. It does not yield a noise figure.

**Exemplars:** Opus A5, Fable A4 and Fable A6 state the unresolved question of whether the IL-2 record's
added doses replace or supplement the stated background.

## For mode 5

**Exemplar:** Opus A7 confines the check to an appendix marked not client data and not used for any call.
Opus A1 :346 declined it.

## Correct approaches whose absence was defensible, so not modes

These belong here and not in Part 1.

| Approach | Why it is not a failure |
|---|---|
| Quantifying a branch of the bulk compartment question with a Treg fraction and its complement | Calling it unresolvable is defensible. Fable A1 :52 partly quantifies it |
| Reporting where paired and pooled estimates of the expression data disagree | A run that correctly chooses paired does not owe the pooled contrast |
| Reading the IL-2 titration's repeated rows as undermining the saturation claim | The record carries three distinct non-zero means spanning 0.042 points, so the reading holds without them |
| Flagging the SPR Rmax column and the CLIPS geometry | The inconsistencies are real. Runs that flagged them were right, and the golden now does the same |

---

## Standing guard

Do not write up the biophysical package, or the count record's enumeration method on its own, as a model
failure. Both are verified room defects. The count record enters mode 1 through a within-record ratio,
where a constant gate bias cancels, which is the golden's own reasoning.
