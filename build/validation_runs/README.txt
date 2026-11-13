VALIDATION RUNS. Build-time evidence only. NOT the panel run, and NOT failure-analysis material.

WHAT THESE ARE
Three solve attempts and two document audits produced during the build, to test whether the room
supports the forcing chain and whether the documents agree with each other. Each solver worked from
an isolated copy of the room with no access to the prompt's companion material, the golden, the
grader, the brief, or the build directory.

ceiling_solve.txt        Solver given the prompt verbatim plus a nudge to analyse properly rather
                         than quickly. Reached nine of the ten route-necessary legs. Missed the
                         kinetics bound and the ten-hour reclassification, which is the decisive leg
                         and the primary pre-registered mode.
floor_solve_A.txt        Same prompt, same isolation, no deep-analysis nudge.
floor_solve_B.txt        Same again, independent sample.
audit_golden_vs_room.txt Adversarial check of the golden against the mounted files.
audit_grader_and_prompt.txt  Consistency check across prompt, grader and golden.

WHY THEY ARE NOT RUN DATA FOR THE FAILURE ANALYSIS
Panel geometry requires sixteen independent samples. These three were spawned from one parent
context with near-identical harness wording, so they share latent conditioning and are not
independent in the sense the FA needs. They are also not Taiga trajectories: there is no grader
score, no trajectory ID, and no record of tool use against the mounted room as the platform would
capture it.
The FA must be written from the actual panel transcripts. These files are evidence that the ceiling
is reachable and that the floor is low, which is a pre-submission check, not an analysis of model
behaviour.

WHAT THEY ARE GOOD FOR
Showing a reviewer why the ceiling and floor claims are believed.
Three defects in the room were found by these runs rather than by the builder: three impossible
SEMs in the F(ab')2 table, the implausible between-donor CV on the itaconate, and the murine test
article being absent from the golden. All three are fixed.
