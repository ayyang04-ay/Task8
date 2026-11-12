import os, re, subprocess, openpyxl, sys
ROOM='/home/user/Task8/data_room'
fails=[]; notes=[]

def xlsx_text(p):
    out=[]
    wb=openpyxl.load_workbook(p,data_only=True)
    for ws in wb.worksheets:
        out.append(ws.title)
        for r in ws.iter_rows(values_only=True):
            for c in r:
                if c is not None: out.append(str(c))
    return '\n'.join(out)

files=sorted(os.listdir(ROOM))
texts={}
for f in files:
    p=os.path.join(ROOM,f)
    texts[f]= xlsx_text(p) if f.endswith('.xlsx') else subprocess.run(
        ['pdftotext',p,'-'],capture_output=True,text=True).stdout

allnames='\n'.join(files)
alltext='\n'.join(texts.values())
corpus=allnames+'\n'+alltext

# ---- A. no .md, no stray file types
if any(f.endswith('.md') for f in files): fails.append('A1 .md file in room')
print(f'A. {len(files)} files, extensions:', sorted({f.rsplit(".",1)[1] for f in files}))

# ---- B. provenance scrub (names AND contents)
BANNED = {
 'original clone code':[r'\bTY ?101[-– ]?10\b', r'\bTY101\b'],
 'accession':[r'\beaba9600\b', r'\baba9600\b', r'\bGSE\d+\b', r'\bPRJNA\d+\b', r'\bDRYAD\b', r'\bdoi\b'],
 'journal/publisher':[r'sciencemag', r'\bstke\b', r'Sci\.? ?Signal', r'Science Signaling', r'RESEARCH RESOURCE'],
 'supplementary conventions':[r'\bmmc\d', r'\bTable S\d', r'\bFig(?:ure)?\.? ?S\d', r'\bData file S\d',
                              r'\bSupplementary\b', r'\bSupplemental\b'],
 'figure back-reference':[r'\bFig(?:ure)?\.? ?\d', r'\bFigure \d'],
 'source authors/institutions':[r'\bTorrey\b', r'\bFaustman\b', r'\bDana[- ]Farber\b', r'\bDFCI\b',
                                r'\bBioMicro\b', r'Massachusetts Institute'],
 'original donor labels':[r'\bSubject \d', r'\bSubject\b'],
}
for label,pats in BANNED.items():
    for pat in pats:
        hits=[(f,m.group(0)) for f,t in texts.items() for m in re.finditer(pat,t,re.I)]
        hits+= [('<FILENAME>',m.group(0)) for m in re.finditer(pat,allnames,re.I)]
        if hits: fails.append(f'B [{label}] /{pat}/ -> {hits[:4]}')

# ---- C. renaming applied
if not re.search(r'TRN-416', alltext): fails.append('C1 asset name absent')
dn=set(re.findall(r'\bDN-\d\d\b', alltext))
notes.append(f'C donor IDs present: {sorted(dn) if dn else "none (record 1 uses column headers)"}')
hdr=openpyxl.load_workbook(f'{ROOM}/TRN416_expression_normalized_reads.xlsx').active[1]
cols=[c.value for c in hdr]
if not all(re.match(r'DN-\d\d_',c) for c in cols[1:]): fails.append('C2 record1 headers not renamed')
print('C. record1 header sample:', cols[:5])

# ---- D. companion document absence anchors
doc=texts['TRN416_nonclinical_study_summary.pdf']
ABSENCE = {
 'fold change / effect size':[r'\bfold\b', r'\d+(?:\.\d+)?[- ]fold', r'\bratio of\b', r'% ?change',
                              r'\bincreased by\b', r'\bdecreased by\b', r'\beffect size\b', r'\bmagnitude\b'],
 'purpose of an arm':[r'\bserved as\b', r'\bas a control\b', r'\bnegative control\b', r'\bpositive control\b',
                      r'\bvehicle control\b', r'\buntreated control\b', r'\bbaseline arm\b', r'\bin order to assess\b',
                      r'\bto determine whether\b', r'\bto confirm\b', r'\bto rule out\b', r'\bto assess the\b'],
 'comparator language':[r'\bcomparator\b', r'\bno comparator\b', r'\babsent\b', r'\bwas not included\b',
                        r'\blacking a\b', r'\bbenchmark\b'],
 'sorting flag':[r'\bnot sorted\b', r'\bwithout sorting\b', r'\bunsorted\b', r'\bno sorting\b',
                 r'\bsorted for\b', r'\bsorting\b', r'\bused directly\b',
                 r'(?:were|was) not [^.]{0,60}(?:select|sort|purif|enrich|isolat)',
                 r'(?:no|without) further [^.]{0,40}(?:select|sort|purif|enrich)'],
 'panel annotation':[r'\bsignature gene', r'\bpathway genes\b', r'\bglycolysis\b', r'\bglutaminolysis\b',
                     r'\bKrebs\b', r'\bfatty acid\b', r'\bmetabolic gene', r'\blineage\b', r'\bTreg signature',
                     r'\bpotent Treg\b', r'\bdoes not contain\b', r'\bpanel includes\b'],
 'Treg purity of sequenced material':[r'Treg.{0,30}purity', r'purity.{0,30}Treg'],
 'temporal / benchmark judgment':[r'\brapidly\b', r'\brobust', r'\bsuperior\b', r'\bmaximal', r'\bpotent\b',
                                  r'\bmarked\b', r'\bstriking\b', r'\bprofound\b', r'\bearly response\b'],
 'causal / inferential':[r'\bbecause\b', r'\btherefore\b', r'\bthus\b', r'\bsuggest', r'\bindicat',
                         r'\bdemonstrat', r'\bshows that\b', r'\bconsistent with\b', r'\bsupports\b',
                         r'\bresults in\b', r'\bleads to\b', r'\bdue to\b'],
 'cross-study relationship':[r'\bsame donors\b', r'\bsame donor set\b', r'\bdifferent donors\b',
                             r'\bthe same participants\b', r'\bas in study TRN416-(?:FC|RS)'],
 'timepoint bridging':[r'10 hours?.{0,60}48 hours?', r'48 hours?.{0,60}10 hours?'],
}
ALLOW = {'RapidSpheres','Rapid'}
for label,pats in ABSENCE.items():
    for pat in pats:
        hits=[m.group(0) for m in re.finditer(pat,doc,re.I) if m.group(0) not in ALLOW]
        hits=[h for h in hits if not (label=='temporal / benchmark judgment' and h.lower().startswith('rapid') and 'RapidSpheres' in doc)]
        if hits: fails.append(f'D [{label}] /{pat}/ -> {sorted(set(hits))[:4]}')

# ---- E. required source inconsistencies preserved
REQ = [('IL-2 200 vs 50 U/ml', [r'IL-2 at 200 U/ml', r'IL-2 at 50 U/ml']),
       ('normalization per-subject vs per-site', [r'normalized for subjects separately', r'for each sequencing laboratory separately']),
       ('itaconate n 6 vs 12', [r'n = 6 donors', r"'Samples \(n\)', ?'?12|Samples \(n\)\s*12"]),
       ('suppression responders T1D vs normal', [r'donors with type 1 diabetes', r'normal blood donors']),
       ('expression timepoint 1 h vs 10 h', [r'test article\s*1 h|Harvest time after addition of test article', r'incubation time for the samples reported here was 10 hours']),
       ('suppression index formula as printed', [r'Treg cell proliferation without Treg']),
       ('suppression ratio labels 0:1 vs 1:0', [r'0:1', ]),
      ]
for label,pats in REQ:
    missing=[p for p in pats if not re.search(p,doc,re.I)]
    if missing: fails.append(f'E [{label}] not found in companion doc: {missing}')

# record-level inconsistencies
r1=openpyxl.load_workbook(f'{ROOM}/TRN416_expression_normalized_reads.xlsx',data_only=True).active
g=[r[0] for r in r1.iter_rows(min_row=2,values_only=True) if r[0]]
if len(g)-len(set(g))!=1: fails.append(f'E duplicate gene row: expected 1, got {len(g)-len(set(g))}')
miss=[(r[0],j) for r in r1.iter_rows(min_row=2,values_only=True) if r[0] for j,v in enumerate(r[1:25]) if v in (None,'')]
if not miss: fails.append('E missing expression value absent')
notes.append(f'E duplicate gene = {[x for x in set(g) if g.count(x)>1]}; missing cells = {miss}')

# ---- F. panel absence anchors
PANEL=set(g)
comp={'TBX21','GATA3','RORC','RORA','BCL6','EOMES','AHR','STAT4','STAT6','RORGT'}
prolif={'MKI67','PCNA','CCNB1','CCND1','TOP2A','CDK1','AURKB','TYMS','BIRC5'}
if PANEL & comp: fails.append(f'F competing-lineage TF present: {PANEL&comp}')
if PANEL & prolif: fails.append(f'F proliferation marker present: {PANEL&prolif}')
notes.append(f'F panel = {len(PANEL)} unique genes; no competing-lineage TF; no proliferation marker')

print('\n--- NOTES ---'); [print(' ',n) for n in notes]
print('\n--- ASSERTIONS ---')
if fails:
    print(f'{len(fails)} FAILED:')
    for f in fails: print('  FAIL:', f)
else:
    print('ALL PASS')
sys.exit(1 if fails else 0)
