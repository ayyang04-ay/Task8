import openpyxl, math
from itertools import combinations

P='/home/user/Task8/data_room/TRN416_expression_normalized_reads.xlsx'
ws=openpyxl.load_workbook(P,data_only=True).active
rows=list(ws.iter_rows(values_only=True))
head=rows[0]
data={}
for r in rows[1:]:
    g=r[0]; vals=r[1:]
    pairs=[(vals[2*i],vals[2*i+1]) for i in range(12)]
    data.setdefault(g,[]).append(pairs)

def binom_p_two(k,n):
    c=lambda n,k: math.comb(n,k)
    tot=2**n
    def tail(x): return sum(c(n,i) for i in range(0,x+1))
    lo=min(k,n-k)
    return min(1.0, 2*tail(lo)/tot)

def stats(g, idx=0):
    pairs=[p for p in data[g][idx] if p[0] not in (None,'') and p[1] not in (None,'')]
    n=len(pairs)
    ratios=[b/a for a,b in pairs if a]
    gm=math.exp(sum(math.log(x) for x in ratios)/len(ratios))
    up=sum(1 for x in ratios if x>1)
    pooled=sum(b for a,b in pairs)/sum(a for a,b in pairs)
    return n,gm,up,binom_p_two(up,n),pooled,ratios

print(f"{'gene':10s} {'n':>3} {'paired_gm':>10} {'up/n':>7} {'sign_p':>8} {'pooled':>8}")
for g in ['FOXP3','IL10','IL4','CTLA4','PDCD1','TGFB1','ETS1','IL7R','MDH2','GLS2','IL2','CPT1B','IL2RA','EP300','CREB','IKZF2','TNFRSF18']:
    if g not in data: print(g,'MISSING'); continue
    for i in range(len(data[g])):
        n,gm,up,p,pooled,_=stats(g,i)
        tag=g if len(data[g])==1 else f'{g}#{i+1}'
        print(f'{tag:10s} {n:3d} {gm:10.4f} {up:3d}/{n:<3d} {p:8.4f} {pooled:8.4f}')

n,gm,up,p,pooled,rat=stats('MDH2')
print('\nMDH2 per-donor ratios:', [round(x,3) for x in rat])
print('MDH2 max ratio donor index:', rat.index(max(rat))+1, round(max(rat),3))

# threshold check: absolute induction >=1200 normalized reads
print('\nGenes meeting >=1200 absolute mean induction (IL2-only -> TRN-416):')
hits=[]
for g,sets in data.items():
    for pr in sets:
        pp=[x for x in pr if x[0] not in (None,'') and x[1] not in (None,'')]
        d=sum(b-a for a,b in pp)/len(pp)
        if d>=1200: hits.append((g,round(d,1)))
for h in sorted(hits,key=lambda x:-x[1]): print('  ',h)

# BDNF duplicate
print('\nBDNF entries:',len(data['BDNF']))
for i,pr in enumerate(data['BDNF']): print('  set',i+1,pr[:3])
# missing
for g,sets in data.items():
    for pr in sets:
        m=[j+1 for j,x in enumerate(pr) if x[0] in (None,'') or x[1] in (None,'')]
        if m: print(f'\nMISSING {g}: donor slots {m}')
print('\ntotal rows',sum(len(v) for v in data.values()),'unique genes',len(data))
