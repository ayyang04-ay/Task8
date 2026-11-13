import sys, os, openpyxl
from openpyxl.styles import Font
sys.path.insert(0, os.path.dirname(__file__))
import anchors as A

SRC = '/root/.claude/uploads/ec75e3b9-b9a4-527a-87ca-4c7d9f339112/dec12f9f-aba9600_data_file_s1.xlsx'
OUT = '/home/user/Task8/data_room'
os.makedirs(OUT, exist_ok=True)
B = Font(bold=True)

def hdr(ws, rows):
    for r in rows:
        ws.append(r)
    for c in ws[1]:
        c.font = B

def meta(ws, pairs):
    for k, v in pairs:
        ws.append([k, v])
    ws.append([])

# ---------------------------------------------------------------- record 1
def rec1():
    wb0 = openpyxl.load_workbook(SRC, data_only=True)
    ws0 = wb0['Sheet 1']
    rows = list(ws0.iter_rows(min_row=1, max_row=87, values_only=True))
    spans = [(10, 44), (47, 66), (69, 83), (86, 87)]
    recs = []
    for a, z in spans:
        for i in range(a, z + 1):
            r = rows[i - 1]
            if r[0]:
                recs.append((r[0], list(r[1:25])))
    recs.sort(key=lambda x: x[0])                      # flatten: destroys block grouping
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'normalized_reads'
    head = ['Gene']
    for d in A.DONORS:
        head += [f'{d}_IL2_only', f'{d}_IL2_plus_TRN416']
    ws.append(head)
    for c in ws[1]: c.font = B
    for g, vals in recs:
        ws.append([g] + [None if v in (None, '') else float(v) for v in vals])
    ws.freeze_panes = 'B2'
    wb.save(f'{OUT}/TRN416_expression_normalized_reads.xlsx')
    return len(recs)

# ------------------------------------------------------- records 2,3,4 (flow)
def flow_dose(fn, sheet, study, pop, n, data, extra):
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = sheet
    ws.append(['Study code', study]); ws.append(['Sponsor', A.SPONSOR])
    ws.append(['Test article', A.ASSET]); ws.append(['Donor material', pop])
    ws.append(['Incubation', '48 h']); ws.append(['Samples (n)', n])
    for k, v in extra: ws.append([k, v])
    ws.append(['Readout', 'CD25hi FoxP3+ events as percent of CD4+ events'])
    ws.append(['Summary statistic', 'mean with SEM'])
    ws.append([])
    r = ws.max_row + 1
    ws.append([f'{A.ASSET} (ug/ml)', 'Treg (%) mean', 'Treg (%) SEM'])
    for c in ws[r]: c.font = B
    for d, m, s in zip(A.DOSE_AB, data['mean'], data['sem']):
        ws.append([d, m, s])
    wb.save(f'{OUT}/{fn}')

# ------------------------------------------------------- records 5,6 (cytokine)
def flow_cytokine(fn, sheet, study, agent, unit, doses, data):
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = sheet
    ws.append(['Study code', study]); ws.append(['Sponsor', A.SPONSOR])
    ws.append(['Donor material', 'Nondiabetic blood donors, freshly isolated CD4+'])
    ws.append(['Incubation', '48 h']); ws.append(['Samples (n)', data['n']])
    ws.append(['Added agent', agent])
    ws.append(['Readout', 'CD25hi FoxP3+ events as percent of CD4+ events'])
    ws.append(['Summary statistic', 'mean with SEM'])
    ws.append([])
    r = ws.max_row + 1
    ws.append([f'{agent} added ({unit})', 'Treg (%) mean', 'Treg (%) SEM'])
    for c in ws[r]: c.font = B
    for d, m, s in zip(doses, data['mean'], data['sem']):
        ws.append([d, m, s])
    wb.save(f'{OUT}/{fn}')

# ---------------------------------------------------------------- record 7
def rec7():
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'counts'
    ws.append(['Study code', 'TRN416-FC-007']); ws.append(['Sponsor', A.SPONSOR])
    ws.append(['Test article', A.ASSET])
    ws.append(['Donor material', 'Nondiabetic blood donors, freshly isolated CD4+'])
    ws.append(['Incubation', '48 h']); ws.append(['Samples (n)', A.R7['n']])
    ws.append(['Enumeration', 'Hemocytometer, trypan blue exclusion'])
    ws.append(['Reported quantity', 'Absolute CD25hi FoxP3+ cells per well'])
    ws.append(['Summary statistic', 'mean with SEM']); ws.append(['Units', 'cells'])
    ws.append([])
    r = ws.max_row + 1
    ws.append([f'{A.ASSET} (ug/ml)', 'Treg count mean', 'Treg count SEM'])
    for c in ws[r]: c.font = B
    for d, m, s in zip(A.DOSE_AB, A.R7['mean'], A.R7['sem']):
        ws.append([d, m, s])
    wb.save(f'{OUT}/TRN416_treg_absolute_counts.xlsx')

# ---------------------------------------------------------------- record 8
def rec8():
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'suppression'
    ws.append(['Study code', 'TRN416-FC-008']); ws.append(['Sponsor', A.SPONSOR])
    ws.append(['Responder cells', 'Autologous CD8+ T cells, CFSE 1 uM'])
    ws.append(['Added cells', f'CD4+ cultures expanded with {A.ASSET} 2.5 ug/ml for 48 h, all arms'])
    ws.append(['Stimulation', 'Soluble anti-CD3 clone HIT3a; IL-2 50 U/ml'])
    ws.append(['Incubation', '4 days']); ws.append(['Samples (n)', A.R8['n']])
    ws.append(['Readout', 'Percent of CD8+-gated events that underwent division'])
    ws.append(['Summary statistic', 'mean with SEM'])
    ws.append([])
    r = ws.max_row + 1
    ws.append(['Responder:Treg ratio', 'Added cells per well',
               'CD8+ division (%) mean', 'CD8+ division (%) SEM'])
    for c in ws[r]: c.font = B
    added = [0, 12500, 25000, 50000]
    for rt, ad, m, s in zip(A.R8_RATIOS, added, A.R8['mean'], A.R8['sem']):
        ws.append([rt, ad, m, s])
    wb.save(f'{OUT}/TRN416_suppression_cd8_division.xlsx')

# ---------------------------------------------------------------- record 9
def rec9():
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'kinetics'
    S = A.SPR
    for k, v in [('Study code','TRN416-BP-009'), ('Sponsor', A.SPONSOR),
        ('Test article', A.ASSET), ('Analyte','Recombinant human TNFR2, extracellular domain'),
        ('Instrument', S['instrument']), ('Sensor chip', S['chip']),
        ('Capture surface', f"Streptavidin, {S['streptavidin_RU']} RU"),
        ('Ligand immobilisation', f"{A.ASSET} biotinylated 5:1 with biotinyl-LC-LC-NHS, captured to {S['capture_RU']} RU"),
        ('Ligand injection concentration','1 ng/ml'),
        ('Running buffer','HBS-EP+, pH 7.4'),
        ('Flow rate', f"{S['flow_ul_min']} ul/min"),
        ('Association injection', f"{S['inj_min']} min"),
        ('Dissociation', '10 min'),
        ('Regeneration','10 mM glycine-HCl pH 1.7, 30 s'),
        ('Reference channel','Streptavidin at identical level, no captured ligand'),
        ('Referencing','Double reference (reference channel and buffer blank)'),
        ('Theoretical Rmax at this capture level', f"{S['Rmax_RU']} RU"),
        ('Rmax confirmation','26 RU observed with 500 nM analyte in running buffer'),
        ('Fit model','1:1 Langmuir, global'),
        ('Temperature','25 C'),
        ('Evaluation software','BIAevaluation 4.1.1')]:
        ws.append([k, v])
    ws.append([])
    r = ws.max_row + 1
    ws.append(['Analyte (nM)','Capture level (RU)','Rmax observed (RU)','ka (1/Ms)','kd (1/s)','KD (M)','Chi2 (RU2)'])
    for c in ws[r]: c.font = B
    series = [(50,101.4,25.6,4.82e5,5.79e-4,1.20e-9,0.118),
              (25,99.8,25.1,4.77e5,5.73e-4,1.20e-9,0.104),
              (12.5,100.6,24.7,4.91e5,5.88e-4,1.20e-9,0.097),
              (6.25,100.1,24.2,4.68e5,5.71e-4,1.22e-9,0.089),
              (3.125,99.5,23.8,4.74e5,5.64e-4,1.19e-9,0.081),
              (1.5625,100.9,23.1,4.80e5,5.82e-4,1.21e-9,0.076)]
    for row in series: ws.append(list(row))
    ws.append([])
    ws.append(['Global fit KD (nM)', S['KD_nM']])
    ws.append(['Global fit KD standard error (nM)', 0.2])
    wb.save(f'{OUT}/TRN416_spr_binding_kinetics.xlsx')

# --------------------------------------------------------------- record 10
def rec10():
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'counterscreen'
    for k, v in [('Study code','TRN416-BP-010'), ('Sponsor', A.SPONSOR),
        ('Test article', A.ASSET), ('Format','Direct-binding ELISA, 96-well'),
        ('Plates','Immulon 4HBX flat bottom'),
        ('Coating','1 ug per well antigen in carbonate coating buffer, overnight 4 C'),
        ('Primary','TRN-416, 8-point 1:3 serial titration from 10 ug/ml'),
        ('Secondary','HRP-conjugated anti-mouse IgG, 1:5000'),
        ('Substrate','TMB, stopped with 2 N H2SO4'),
        ('Reader','SpectraMax 190, absorbance 450 nm'),
        ('Analysis software','SoftMax Pro 6.3'),
        ('Replicates','Triplicate wells, 3 independent runs'),
        ('Reported quantity','Mean OD450 across replicate wells')]:
        ws.append([k, v])
    ws.append([])
    r = ws.max_row + 1
    ws.append(['TRN-416 (ug/ml)','TNFR2 full ectodomain OD450','TNFR2 aa 50-122 OD450',
               'TNFR1 full ectodomain OD450','Bovine serum albumin OD450'])
    for c in ws[r]: c.font = B
    rows = [(10,2.541,2.188,0.062,0.048),(3.33,2.402,2.051,0.059,0.047),
            (1.11,2.013,1.702,0.058,0.046),(0.370,1.404,1.173,0.055,0.045),
            (0.123,0.812,0.661,0.054,0.046),(0.0412,0.371,0.298,0.052,0.044),
            (0.0137,0.164,0.131,0.051,0.045),(0.00457,0.089,0.074,0.050,0.044),
            (0,0.047,0.046,0.048,0.043)]
    for row in rows: ws.append(list(row))
    wb.save(f'{OUT}/TRN416_elisa_receptor_counterscreen.xlsx')

# --------------------------------------------------------------- record 11
def rec11():
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'clips_mapping'
    for k, v in [('Study code','TRN416-BP-011'), ('Sponsor', A.SPONSOR),
        ('Test article', A.ASSET),
        ('Target','Human TNFR2 extracellular region'),
        ('Platform','Chemically Linked Peptides on Scaffolds (CLIPS)'),
        ('Library','Overlapping linear peptides tiled across the target sequence, up to 10000 constructs'),
        ('Linear peptide lengths','15-mer and 18-mer, offset 1 residue'),
        ('Looped constructs','Single-loop CLIPS, 17-mer; double-loop CLIPS, 22-mer'),
        ('Detection','Peroxidase-conjugated anti-mouse IgG, ABTS substrate'),
        ('Reader','Charge-coupled device camera, 620 nm'),
        ('Reported quantity','Arbitrary binding units, mean of duplicate arrays'),
        ('Incubation','Overnight 4 C, primary at 1 ug/ml')]:
        ws.append([k, v])
    ws.append([])
    r = ws.max_row + 1
    ws.append(['Construct ID','Peptide sequence','Construct type','Residue span','Binding (AU)'])
    for c in ws[r]: c.font = B
    rows = [
      ('C-0141','QMCCSKCSPGQH','double-loop CLIPS','44-55',2874),
      ('C-0142','MCCSKCSPGQHA','double-loop CLIPS','45-56',1960),
      ('C-0139','TPYAPEPGSTCQ','double-loop CLIPS','42-53',212),
      ('C-0207','CSSDQVET','single-loop CLIPS','98-105',2655),
      ('C-0208','SSDQVETQ','single-loop CLIPS','99-106',1411),
      ('C-0205','RCSSDQVE','single-loop CLIPS','97-104',884),
      ('C-0263','NRICTCRP','single-loop CLIPS','116-123',2413),
      ('C-0264','RICTCRPG','single-loop CLIPS','117-124',1197),
      ('C-0261','QNNRICTC','single-loop CLIPS','114-121',640),
      ('L-0088','SVCPQGKYIHPQNNSI','15-mer linear','29-44',188),
      ('L-0154','EMGQVEISSCTVDRDT','15-mer linear','72-87',151),
      ('L-0301','GTRSQNTVCTCEEGWH','15-mer linear','150-165',143),
      ('N-0001','scrambled control','18-mer linear','n/a',96),
    ]
    for row in rows: ws.append(list(row))
    wb.save(f'{OUT}/TRN416_epitope_mapping_clips.xlsx')

# --------------------------------------------------------------- record 12
def rec12():
    wb = openpyxl.Workbook()
    ws = wb.active; ws.title = 'fab2_fragment'
    for k,v in [('Study code','TRN416-FC-012A'),('Sponsor',A.SPONSOR),
        ('Test article',"F(ab')2 fragment of TRN-416, Pierce F(ab')2 Preparation Kit"),
        ('Donor material','Peripheral human CD4+ cells'),('Incubation','48 h'),
        ('Samples (n)',A.R12A['n']),
        ('Readout','CD25hi FoxP3+ events as percent of CD4+ events'),
        ('Summary statistic','mean with SEM')]: ws.append([k,v])
    ws.append([]); r=ws.max_row+1
    ws.append(["F(ab')2 (ug/ml)",'Treg (%) mean','Treg (%) SEM'])
    for c in ws[r]: c.font=B
    for d,m,s in zip(A.DOSE_FAB, A.R12A['mean'], A.R12A['sem']): ws.append([d,m,s])

    ws = wb.create_sheet('cross_linking')
    for k,v in [('Study code','TRN416-FC-012B'),('Sponsor',A.SPONSOR),
        ('Test article','TRN-416'),
        ('Cross-linking reagent','Anti-rodent IgG clone ab9165, 2.5 ug/ml'),
        ('Donor material','Peripheral human CD4+ cells'),
        ('Timepoints assessed','24 h, 48 h, 72 h'),('Tabulated timepoint','48 h'),
        ('Samples (n)',A.R12B['n']),
        ('Readout','CD25hi FoxP3+ events as percent of CD4+ events'),
        ('Summary statistic','mean with SEM')]: ws.append([k,v])
    ws.append([]); r=ws.max_row+1
    ws.append(['TRN-416 (ug/ml)','Treg (%) mean','Treg (%) SEM'])
    for c in ws[r]: c.font=B
    for d,m,s in zip(A.DOSE_XL, A.R12B['mean'], A.R12B['sem']): ws.append([d,m,s])

    ws = wb.create_sheet('stnfr2_supernatant')
    for k,v in [('Study code','TRN416-EL-012C'),('Sponsor',A.SPONSOR),
        ('Assay','Quantikine human sTNFR2 ELISA, R&D Systems'),
        ('Matrix','Cell culture supernatant'),
        ('Collection window','24 to 42 hours of incubation'),
        ('Capture plates','Commercial plates and custom plates coated with 2 ug per well anti-TNFR2'),
        ('Reader','SpectraMax 190, absorbance 450 nm'),
        ('Samples (n)',A.R12C_N),('Units','pg/ml'),
        ('Summary statistic','mean')]: ws.append([k,v])
    ws.append([]); r=ws.max_row+1
    ws.append(['Condition','sTNFR2 mean (pg/ml)','Samples (n)'])
    for c in ws[r]: c.font=B
    for k,v in A.R12C.items(): ws.append([k, v, A.R12C_N])

    ws = wb.create_sheet('nfkb_array')
    for k,v in [('Study code','TRN416-AR-012D'),('Sponsor',A.SPONSOR),
        ('Platform','TaqMan Array Human NF-kB Pathway 96-well plate, Applied Biosystems'),
        ('Treatment','TRN-416 2.5 ug/ml'),('Incubation','6 h'),
        ('Paired wells','IL-2 only, same donor preparation, same plate'),
        ('Samples (n)',7),
        ('Reported quantity','Relative quantitation, IL-2-only wells set to 1.000'),
        ('Lower limit of reported range','0.75')]: ws.append([k,v])
    ws.append([]); r=ws.max_row+1
    ws.append(['Gene','IL-2 only (RQ)','TRN-416 (RQ)','Flag'])
    for c in ws[r]: c.font=B
    for g,v in A.R12D:
        ws.append([g, 1.000, v, 'at or below lower limit of reported range' if v==A.FLOOR else None])

    ws = wb.create_sheet('itaconate_supernatant')
    for k,v in [('Study code','TRN416-MB-012E'),('Sponsor',A.SPONSOR),
        ('Matrix','Culture supernatant'),
        ('Culture format','96-well plates, 100000 cells per well, 50 ul sample per well'),
        ('Incubation','6 h'),('Analysis','Metabolon Inc, Research Triangle Park, NC'),
        ('Samples (n)',6),('Units','scaled intensity'),
        ('Summary statistic','mean with SEM')]: ws.append([k,v])
    ws.append([]); r=ws.max_row+1
    ws.append(['TRN-416 (ug/ml)','Itaconate mean','Itaconate SEM'])
    for c in ws[r]: c.font=B
    for d,m,s in zip(A.DOSE_ITA, A.R12E['mean'], A.R12E['sem']): ws.append([d,m,s])

    wb.save(f'{OUT}/TRN416_ancillary_functional_assays.xlsx')

n = rec1()
flow_dose('TRN416_flow_treg_dose_control_donors.xlsx','dose_response','TRN416-FC-002',
          'Nondiabetic blood donors, freshly isolated CD4+', A.R2['n'], A.R2,
          [('Analysis of trend','Linear mixed-effects model with participant-level random effects')])
flow_dose('TRN416_flow_treg_dose_t1d_donors.xlsx','dose_response','TRN416-FC-003',
          'Type 1 diabetes donors, freshly isolated CD4+', A.R3['n'], A.R3,
          [('Analysis of trend','Linear mixed-effects model with participant-level random effects')])
flow_dose('TRN416_flow_treg_dose_with_tnf.xlsx','dose_response','TRN416-FC-004',
          'Nondiabetic blood donors, freshly isolated CD4+', A.R4['n'], A.R4,
          [('Added agent','Recombinant human TNF, 20 ng/ml, all wells')])
flow_cytokine('TRN416_flow_treg_il2_dose.xlsx','dose_response','TRN416-FC-005',
              'IL-2','U/ml', A.DOSE_IL2, A.R5)
flow_cytokine('TRN416_flow_treg_tnf_dose.xlsx','dose_response','TRN416-FC-006',
              'TNF','ng/ml', A.DOSE_TNF, A.R6)
rec7(); rec8(); rec9(); rec10(); rec11(); rec12()
print('record 1 rows:', n)
print(sorted(os.listdir(OUT)))
