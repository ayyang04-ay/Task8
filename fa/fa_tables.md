# TRN-416 — per-run attribution tables

Reformat of `error_modes.md`. No new analysis. Cells are clipped on purpose: a cell that reads as a
finished sentence gets pasted, and pasted prose is what the overlap check catches. Locations are line
numbers in each run's main memo.

---

## 1. Count record's own change never scaled to the expression timepoint

**Runs:** Opus A3, Opus A4, Opus A8, Fable A1, Fable A2, Fable A8. Also Fable A6, Fable A7 one step earlier.

**What they did.** Divided the gated count by a Treg fraction from a different record. Used the quotient
only against the stated seeding density.

| Run | The number or claim it produced | Where |
|---|---|---|
| Opus A3 | "19,000–21,000 total cells per well"; "illustrative only, because the donor sets differ" | :98 |
| Opus A4 | "18,600–28,700 CD4+ cells per well"; "1.9–14% of input"; "I have set FC-007 aside" | :90 |
| Opus A8 | "That can give at most a total cell count"; ledger "(illustration only)" | :89, :278 |
| Fable A1 | set-aside row, "implied total cells from FC-007 and FC-002" | :133 |
| Fable A2 | "roughly 19,000–21,000 total cells per well"; "using FC-002's fractions from a separate study" | :150 |
| Fable A8 | set-aside row, "back-calculated from FC-007 ÷ FC-002"; "only to flag the mismatch with seeding density" | :189 |
| Fable A6 | "it is total cells multiplied by the same gate fraction" — identity stated, never divided | :109 |
| Fable A7 | "must be a total count multiplied by the same gate fraction" — identity stated, never divided | :96 |

**The figures.** `TRN416_treg_absolute_counts.xlsx` r13 and r19: 2,029 and 2,965 cells per well, 0 and
2.5 µg/ml, n = 11, 48 h. ln(2965 ÷ 2029) ÷ 48 = 0.00790 per hour. At 10 h, 1.082. FOXP3 ×2.84 paired
within donor. At least ×2.62 transcriptional. One record, two cells.

**Why not a defensible call.** The scaling uses the record each run read, and the counts are a within-record
dose series, so no cross-record step is needed. FC-007 carries no frequency column, so the division these
runs performed was necessarily cross-record and labelling it illustrative was correct.

**Exemplar.** None.

**Limit to carry.** The bound holds only if total CD4 is non-decreasing across the interval, which the
package cannot check. It is a ceiling, not an estimate.

---

## 2. Timepoint premise asserted from general plausibility, unlabelled

**Runs:** Opus A3, Opus A4, Fable A3, Fable A6.

**What they did.** Settled whether the 10 h transcript rise was per-cell or more cells on an unsourced claim
about division speed, in memos restricted to the client's records.

| Run | The number or claim it produced | Where |
|---|---|---|
| Opus A3 | "Tripling the population in 10 h is not plausible"; "cannot come from more Treg cells" | :90 |
| Opus A4 | "At 10 h the change is per cell, not more cells"; "too early for proliferation to explain it" | :92 |
| Fable A3 | "too early and too large to be more cells" | :56 |
| Fable A6 | "too early for any cell population to have expanded" | :109 |

**Fable A6, same section.** Labels a different outside-knowledge claim at :109 onward — "general immunology
and my judgement; it is not in the client's files" — and states at :109 that the 10 h cultures "differ from
the 48 h flow cultures".

**Exemplars.** Fable A5 :36, identical claim, labelled "my inference, not a measurement in the files".
Fable A1 :52, premise replaced with arithmetic from the room.

---

## 3. Benchmark equivalence kept after the run's own baseline check disqualified it

**Runs:** Opus A4, Opus A5, Opus A6, Fable A5, Fable A6.

**What they did.** Measured the between-record baseline problem, wrote that comparisons between records
fail, and carried a TNF equivalence into the headline reasons uncaveated.

| Run | The claim it produced | Where | Its own disqualifying line |
|---|---|---|---|
| Opus A4 | "the same size as what TNF itself does in the same assay format" | :17 | :63 |
| Opus A5 | "the same relative size as the one TNF … gives on its own" | :14 | :43, :44 |
| Opus A6 | "TNF gives the same ≈1.3-fold shift"; section heading "the same size as TNF's" | :17, :59 | :65 |
| Fable A5 | "moves the gate the same way by a similar amount" | :83 | :26 |
| Fable A6 | "TNF and IL-2 each move the same readout by a similar amount" | :5, :63 | :65 |

**Opus A5 is flattest.** :44 reads "That disqualifies every cross-study claim in the package: TRN-416 vs
TNF". :14 sits in "The answer in brief".

**Caveated where used, weaker:** Opus A1 :40, :116. Opus A2 :76. Opus A7 :40. Opus A8 :22, :99.
Fable A3 :48.

**Exemplar.** Fable A1 :89, "Not shown in the same donors: baselines are 1.96 points apart". Fable A2 does
not make the claim.

---

## 4. Saturating-IL-2 pillar rests on three repeated values

**Runs, flagged then relied on it:** Opus A1, Opus A4, Fable A3, Fable A6, Fable A7.
**Runs, relied on it without recording the repeats:** Fable A1, Fable A2, Fable A5.

**What they did.** Took the flatness of the IL-2 titration as evidence that 200 U/ml is a saturating
background, carrying the positive pillar that the asset adds on top of it.

| Run | Flag it recorded | Where | Use it made | Where |
|---|---|---|---|---|
| Opus A1 | "identical SEMs at three doses each" | :250 | "a saturating concentration"; keeps FC-005 "only for 'IL-2 alone plateaus at 2 U/ml'" | :145, :334 |
| Opus A4 | "the plateau is implausibly flat" | :141, :200 | reason 4, "adds to IL-2 that is already saturating" | :45 |
| Fable A3 | "identical mean and SEM to three decimals" | :65 | scorecard "Adds to IL-2" | :17, :30 |
| Fable A6 | "response identical from 2 to 5000 U/ml" | :254 | "counts in its favour" | :68 |
| Fable A7 | "identical to three decimals across a 2,500-fold range … needs source data" | :75 | "already saturated at 2 U/ml" | :58, :88 |
| Fable A1 | — | — | "the effect sits on top of saturating IL-2" | :21 |
| Fable A2 | — | — | "More IL-2 does not reproduce it" | :22, :52 |
| Fable A5 | — | — | "Extra IL-2 would not reproduce it" | :82, :121 |

**The figures.** `TRN416_flow_treg_il2_dose.xlsx` r12:r17. Six non-zero doses, three distinct means
(7.106 three times, 7.085 twice, 7.064 once) and two distinct SEMs (0.319 three times, 0.298 three times).

**Limit to carry.** The same flatness is sound evidence for the documentation conflict — section 4 puts
200 U/ml in every culture while this record titrates added IL-2 from zero. The mode is the pharmacological
inference, not touching the record.

**Exemplars.** Opus A2 :222, rules it out as a measure of IL-2's effect; :62 states the saturation reading
conditionally. Opus A3 :338, Opus A5 :138, Opus A6 :218, Opus A8 :208 set it aside.

---

## 5. Reference-database finding placed in the reasons-against

**Runs:** Opus A5, Opus A6.

| Run | What it produced | Where | Its own scope line |
|---|---|---|---|
| Opus A5 | external peptide check, in the reasons-against section | :88 | :5, "No outside data were used for any verdict" |
| Opus A6 | external peptide check, in the record-integrity body | :238, :241 | :5, "used no outside literature" |

Both label the source. Placement is the issue.

**Exemplar.** Opus A7, Appendix B, "not client data; not used for any call". Opus A1 :346 declined the check.

Thin. QA calls it a small step outside the brief rather than an exploit.

---

## 6. Baseline spread pooled across donor populations and added agents, then used as assay noise

**Runs:** Opus A1, Opus A3, Opus A4.

| Run | The number or claim it produced | Where |
|---|---|---|
| Opus A1 | "One nominal condition appears in four studies"; "a spread of 3.84 points, larger than TRN-416's own effect"; heading "the assay's between-study noise" | :118, :124, :116 |
| Opus A3 | "The same 'IL-2 200 U/ml, no test article' condition reads 7.064% in FC-005 and 10.902% in FC-003"; "as large as the TRN-416 effect itself" | :99 |
| Opus A4 | "no larger than the drift between vehicle wells of different studies (up to 3.8 pp)"; four arms "share nominally the same medium and no test agent" | :17, :63 |

**What each record states, in its own first rows.**

| Record | Donor material | Added agent | Zero-dose arm |
|---|---|---|---|
| control_donors | Nondiabetic, n = 13 | none | 10.622 |
| t1d_donors | Type 1 diabetes, n = 11 | none | 10.902 |
| il2_dose | Nondiabetic, n = 7 | IL-2, titrated from 0 | 4.553; 7.064 at 200 |
| tnf_dose | Nondiabetic, n = 8 | TNF, titrated from 0 | 8.660 |
| dose_with_tnf | Nondiabetic, n = 3 | TNF 20 ng/ml, all wells | 10.290 |

The 3.84 figure is 10.902 − 7.064: a T1D arm against an arm inside the IL-2 titration record.

**Opus A4 had the decomposition.** :64 gives "2.24 pp without FC-005"; :44 gives the T1D and nondiabetic
baselines as 10.902 against 10.622.

**The replicated condition.** control_donors r12, 10.622 ± 0.706, n = 13, against tnf_dose r11,
8.660 ± 0.598, n = 8. Difference 1.962 points, SE 0.9253, t = 2.12 on 18.8 df, p = 0.0475 under the test
section 14 prescribes.

**Why not a defensible call.** One metadata line per record states the difference. Opus A7 lists "T1D vs
nondiabetic" among the comparisons it sets aside, and includes the T1D arm in the spread.

**Weaker:** Opus A7 :40, :263 separates "3.56 points in nondiabetic donors" from "3.84 across the four main
studies". Fable A6 :239, appendix row only; the body uses the three nondiabetic arms.

**Limit to carry.** The 3.56 version (control_donors against il2_dose at 200 U/ml) is ambiguous rather than
wrong, because whether the added IL-2 replaces or supplements the stated background is unresolved. Opus A5,
Fable A4 and Fable A6 state that ambiguity.

---

## Closing line, if used

Any "everything else was right in all sixteen" sentence needs its exceptions verified run by run, not taken
from a grader. I have not done that sweep. Ask for it before writing such a line.
