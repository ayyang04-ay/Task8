"""Recomputes every golden-relevant quantity reading ONLY the shipped data room."""
import openpyxl, math, os
R='/home/user/Task8/data_room'
def load(f): return openpyxl.load_workbook(os.path.join(R,f),data_only=True)
def table(ws):
    rows=list(ws.iter_rows(values_only=True))
    i=next(k for k,r in enumerate(rows) if r[0] and str(r[0]).lower().startswith(('trn-416 (','il-2 added','tnf added','responder:','f(ab')))
    return [r for r in rows[i+1:] if r[0] is not None]

print('='*74); print('A. EXPANSION, VEHICLE-CONTROLLED'); print('='*74)
t2=table(load('TRN416_flow_treg_dose_control_donors.xlsx').active)
d0,d25=t2[0],[r for r in t2 if r[0]==2.5][0]
print(f'  record 2 (n=13): 0 ug/ml = {d0[1]}%   2.5 ug/ml = {d25[1]}%   ratio = {d25[1]/d0[1]:.4f}')
t7=table(load('TRN416_treg_absolute_counts.xlsx').active)
c0,c25=t7[0],[r for r in t7 if r[0]==2.5][0]
print(f'  record 7 (n=11): 0 ug/ml = {c0[1]} cells  2.5 ug/ml = {c25[1]} cells  ratio = {c25[1]/c0[1]:.4f}')

print('\n'+'='*74); print('B. KINETICS BOUND (records 2 + 7)'); print('='*74)
rate=math.log(c25[1]/c0[1])/48
print(f'  exponential rate from 0->48 h   = {rate:.6f} /h')
for h in (6,10,24):
    print(f'  implied multiplier at {h:>2} h       = {math.exp(rate*h):.4f}')
print(f'  BAND for the 10 h timepoint     = 1.00 (any lag) to {math.exp(rate*10):.3f}')

print('\n'+'='*74); print('C. CROSS-RUN SCALE: zero-dose / no-added-agent condition'); print('='*74)
ctrl={}
for f,lab in [('TRN416_flow_treg_dose_control_donors.xlsx','rec2 asset dose, nondiabetic, n=13'),
              ('TRN416_flow_treg_dose_with_tnf.xlsx','rec4 asset dose + TNF, n=3'),
              ('TRN416_flow_treg_il2_dose.xlsx','rec5 IL-2 dose, n=7'),
              ('TRN416_flow_treg_tnf_dose.xlsx','rec6 TNF dose, n=8')]:
    v=table(load(f).active)[0][1]; ctrl[lab]=v; print(f'  {v:>7.3f}%   {lab}')
lo,hi=min(ctrl.values()),max(ctrl.values())
print(f'  spread = {hi:.3f} / {lo:.3f} = {hi/lo:.4f}x')
print(f'  effect being compared against it (record 2) = {d25[1]/d0[1]:.4f}x')

print('\n'+'='*74); print('D. COMPOSITION DENOMINATOR AND THE DISJUNCTION'); print('='*74)
fr=d0[1]/100
print(f'  Treg fraction at 0 ug/ml = {d0[1]}%')
print(f'  If the whole FOXP3 change is Treg-intrinsic: per-Treg rise needed = 2.8383x')
print(f'  If it sits in conventional cells: they must reach '
      f'{(2.8383-1)*fr/(1-fr)*100:.1f}% of the per-Treg level to produce the same bulk change')

print('\n'+'='*74); print('E. PAIRED EXPRESSION (record 1)'); print('='*74)
ws=load('TRN416_expression_normalized_reads.xlsx').active
rows=list(ws.iter_rows(values_only=True))[1:]
D={}
for r in rows:
    if r[0]: D.setdefault(r[0],[]).append([(r[1+2*i],r[2+2*i]) for i in range(12)])
def sign_p(k,n): return min(1.0, 2*sum(math.comb(n,i) for i in range(min(k,n-k)+1))/2**n)
def st(g,i=0):
    pr=[p for p in D[g][i] if p[0] not in (None,'') and p[1] not in (None,'')]
    rt=[b/a for a,b in pr]
    gm=math.exp(sum(map(math.log,rt))/len(rt)); up=sum(1 for x in rt if x>1)
    return len(pr),gm,up,sign_p(up,len(pr)),sum(b for a,b in pr)/sum(a for a,b in pr)
print(f"  {'gene':9s} {'n':>3} {'paired GM':>10} {'up/n':>7} {'sign p':>8} {'pooled':>8}")
for g in ['FOXP3','IL10','IL4','CTLA4','PDCD1','TGFB1','ETS1','IL7R','MDH2','GLS2','IL2','CPT1B']:
    n,gm,up,p,po=st(g); print(f'  {g:9s} {n:3d} {gm:10.4f} {up:3d}/{n:<3d} {p:8.4f} {po:8.4f}')
n,gm,up,p,po=st('MDH2')
rt=[b/a for a,b in D['MDH2'][0]]
print(f'  MDH2 reversal: pooled {po:.4f} vs paired {gm:.4f}; leverage donor DN-{rt.index(max(rt))+1:02d} at {max(rt):.3f}x')

print('\n'+'='*74); print('F. ABSOLUTE 1200-READ CRITERION APPLIED CONSISTENTLY'); print('='*74)
meets=[]; fails=[]
for g,sets in D.items():
    pr=[p for p in sets[0] if p[0] not in (None,'') and p[1] not in (None,'')]
    delta=sum(b-a for a,b in pr)/len(pr); gm=math.exp(sum(math.log(b/a) for a,b in pr)/len(pr))
    (meets if delta>=1200 else fails).append((g,delta,gm))
print(f'  genes meeting the criterion: {len(meets)} of {len(D)}')
print('  excluded despite a large paired ratio:')
for g,dl,gm in sorted(fails,key=lambda x:-x[2])[:5]:
    print(f'    {g:9s} paired GM {gm:.3f}  mean absolute induction {dl:9.1f}')
print('  included but failing the paired sign test:')
for g,dl,gm in meets:
    n,gmm,up,p,po=st(g)
    if p>0.05: print(f'    {g:9s} absolute induction {dl:9.1f}  paired GM {gmm:.3f}  {up}/{n}  p={p:.3f}')

print('\n'+'='*74); print('G. SUPPRESSION ARMS (record 8)'); print('='*74)
ws8=load('TRN416_suppression_cd8_division.xlsx').active
for r in ws8.iter_rows(values_only=True):
    if r[0] in ('Added cells','Samples (n)'): print(f'  {r[0]}: {r[1]}')
t8=table(ws8); print('  ratio    added cells   % CD8 division')
for r in t8: print(f'  {r[0]:<8} {r[1]:>10}    {r[2]} +/- {r[3]}')
print('  every ratio uses asset-expanded cells; the only contrast is Treg dose')

print('\n'+'='*74); print('H. PANEL CONTENT (record 1)'); print('='*74)
P=set(D)
print(f'  unique genes: {len(P)}')
print(f'  competing-lineage TF present: {P & {"TBX21","GATA3","RORC","BCL6","EOMES"} or "none"}')
print(f'  proliferation marker present: {P & {"MKI67","PCNA","CCNB1","TOP2A","CDK1"} or "none"}')
