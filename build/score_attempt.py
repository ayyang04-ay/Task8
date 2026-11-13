"""Scores a solver attempt against the anchors and the grader A/B items.
Objective part only: which anchor values were recovered, which were missed,
and which penalised moves are textually detectable. The judgment part is a read."""
import re, sys, math

ANCHORS = [
 ("expansion ratio, record 2",            1.3038, 0.004, ["1.30","1.31"]),
 ("count ratio, record 7",                1.4613, 0.004, ["1.46"]),
 ("growth rate per hour",                 0.007903, 0.0002, ["0.0079","0.00790","0.0079"]),
 ("composition ceiling at 10 h",          1.082, 0.012, ["1.08","1.09"]),
 ("zero-dose spread",                     2.333, 0.03, ["2.33","2.3"]),
 ("Treg frequency denominator",           10.622, 0.05, ["10.62"]),
 ("FOXP3 paired geometric mean",          2.8383, 0.01, ["2.84","2.838"]),
 ("transcriptional floor",                2.62, 0.03, ["2.62","2.6"]),
 ("conventional-cell branch percent",     21.8, 0.4, ["21.8","22"]),
 ("ETS1 paired",                          1.0703, 0.01, ["1.07"]),
 ("ETS1 sign-test p",                     0.146, 0.004, ["0.146","0.15"]),
 ("IL7R paired",                          0.5184, 0.01, ["0.518","0.52"]),
 ("MDH2 pooled",                          1.2187, 0.01, ["1.219","1.22"]),
 ("MDH2 paired",                          0.8537, 0.01, ["0.854","0.85"]),
 ("DN-04 leverage",                       7.394, 0.02, ["7.39"]),
 ("K_D nM",                               1.2, 0.01, ["1.2"]),
]
LEGS = {
 "L1 expansion real, counts as well as frequency": r"(absolute count|2029|2965|cell number)",
 "L2 records do not share a scale":               r"(4\.553|2\.33|do not share|different baseline|incommensur|not comparable across)",
 "L3 composition ceiling derived":                r"(0\.0079|ceiling|upper bound|at most 1\.0|composition multiplier)",
 "L4 10 h is acute, not the 48 h population":     r"(acute|different timepoint|10[ -]hour.{0,80}48[ -]hour|cannot characteri[sz]e the)",
 "L5 compartment not assignable from bulk":       r"(bulk|cannot assign|which compartment|conventional CD4|Tconv)",
 "L6 per-cell potency unmeasured":                r"(per[- ]cell|every arm|all arms|no non-asset|only.{0,40}Treg dose|potency.{0,30}unmeasured)",
 "L7 effectors oppose identity markers":          r"(IL10|IL-10).{0,200}(IL4|IL-4)|effector.{0,60}(down|decreas|opposite)",
 "L8 biophysics clean":                           r"(1\.2 ?nM|K ?D|TNFR1.{0,40}(no|absent|background)|selectiv)",
 "L9 panel cannot discriminate":                  r"(TBX21|GATA3|RORC|proliferation marker|Ki-?67|MKI67|panel.{0,60}(cannot|lacks|no))",
 "L10 paired analysis applied":                   r"(paired|within[- ]donor|sign test|Wilcoxon)",
}
PENALTIES = {
 "B unresolved compartment resolved anyway": r"(confirms|demonstrates|shows) that (the )?Tregs",
 "B FOXP3 up means Tregs up":                r"FOXP3.{0,60}(confirm|demonstrat|prov)",
 "B asset beats IL-2":                       r"(superior to|outperform|better than|greater than).{0,40}IL-?2",
 "B 1:0 treated as comparator":              r"1:0.{0,60}(control|comparator|baseline arm)",
 "B pooled estimator":                       r"(pooled|across all donors).{0,40}(mean|ratio|fold)",
}

t = open(sys.argv[1]).read()
nums = set(re.findall(r'\d+\.?\d*', t.replace(',','')))
def near(v, tol):
    for n in nums:
        try:
            if abs(float(n)-v) <= tol: return n
        except ValueError: pass
    return None

hit=0
print("ANCHOR RECOVERY")
for name, val, tol, _ in ANCHORS:
    f = near(val, tol)
    if f: hit+=1
    print(f"  {'HIT ' if f else 'miss'} {name:42s} want {val:<10} found {f or '-'}")
print(f"  {hit} of {len(ANCHORS)} anchors recovered\n")

print("ROUTE-NECESSARY LEGS (textual probe, confirm by reading)")
L=0
for name, pat in LEGS.items():
    m = re.search(pat, t, re.I|re.S)
    if m: L+=1
    print(f"  {'present' if m else 'ABSENT ':8s} {name}")
print(f"  {L} of {len(LEGS)} legs probe positive\n")

print("PENALISED MOVES (textual probe, confirm by reading)")
for name, pat in PENALTIES.items():
    m = re.search(pat, t, re.I)
    print(f"  {'FIRED  ' if m else 'clear  '} {name}" + (f"   -> '{m.group(0)[:60]}'" if m else ""))
print(f"\nwords: {len(t.split())}")
