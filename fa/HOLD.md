# ON HOLD — out of scope under the small-molecule guidance

**Date:** 2026-11-17. **Reason:** project guidance narrowed to small molecules. TRN-416 is an antibody.

## Determination

| Evidence | Source |
|---|---|
| Mouse IgG1 kappa, raised in a BALB/c hybridoma, against a recombinant fragment of the human TNFR2 extracellular region spanning amino acids 50 to 122, purified on protein A | `data_room/TRN416_nonclinical_study_summary.pdf` §1 |
| Molar mass about 146,786 g/mol | derived from the stated extinction coefficient |
| SPR kinetics against the recombinant TNFR2 ectodomain, 1:1 Langmuir | `data_room/TRN416_spr_binding_kinetics.xlsx` |
| CLIPS peptide epitope mapping | `data_room/TRN416_epitope_mapping_clips.xlsx` |
| F(ab')2 and Fab fragments, Fc dependence, anti-rodent IgG cross-linker | `data_room/TRN416_ancillary_functional_assays.xlsx` |

Not a borderline case, and not reframeable. The asset is the antibody, the gating step in every proposed
route is a humanised or engineered derivative, and the binding package is antibody biophysics throughout.

## State at hold

Complete and verified. Nothing is mid-flight.

| Artefact | State |
|---|---|
| `fa/submittability.md` | submittable after golden edits; both edits made |
| `fa/error_modes.md` | five modes stand, v3. M4 retracted, M6 restated |
| `fa/fa_tables.md` | per-run attribution for the five modes |
| `fa/fa_outline.md` | Part 1 failure items, Part 2 counterfactuals and exemplars |
| `fa/qa_triage.md` | 17 findings triaged; four survive, three as evidentiary guards |
| `task/golden_response.txt` | SPR Rmax column and CLIPS construct geometry now flagged and proceeded past |

Written but never written up: the FA text itself, which is typed by hand in Studio.

## If the hold lifts

Nothing needs redoing. Two things to pick up:

1. Mode 5 (external-database finding in the reasons-against) was still your call on whether it ships.
2. Mode 3's second tier (Opus A1, A2, A7, A8, Fable A3 — caveated where used) was still your call.

Both are in `fa/fa_outline.md`.
