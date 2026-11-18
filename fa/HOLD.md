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

## Relabelling was considered and rejected (2026-11-18)

Asked whether the brief could present the asset as a small molecule, or as a small peptide, with the data
essentially unchanged. It cannot. The modality is encoded in the measurements.

The decisive figure, so this does not need re-deriving: the package's concentrations yield the stated
nanomolar values only at about 147,000 g/mol. Back-solved from two independent cells, 152,632 and 147,059
against the recorded 146,786. "Potency matches affinity", the strongest positive evidence in the package,
requires the asset to weigh what an IgG weighs. At 500 g/mol the EC50 well reads 580 nM against a recorded
KD of 1.2 nM; at a 30-mer, 88 nM; at a 100-mer, which is no longer small, still 26 nM.

Also unreconcilable without rebuilding the records: the F(ab')2 fragment arm and the anti-rodent IgG
cross-linker (FC-012A, FC-012B); anti-mouse and anti-rodent detection secondaries (CLIPS, ELISA
counter-screen); protein A purification and the BALB/c hybridoma provenance in PDF section 1; a three-region
contact footprint spanning residues 44 to 123; and the humanisation pillar, which is a grader A-item with no
analogue in either alternative modality.

A relabel would also plant, at the centre of the asset, the same defect this version was penalised for at
its edges: records contradicting themselves, with runs that notice scoring worst.

**Pause stands.** If a compliant version is wanted, the route is new data against the same pillar
architecture. The five modes are modality-independent and already written, so they carry across as
pre-registration.
