import os, sys, openpyxl
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib import colors
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)

OUT = '/home/user/Task8/data_room/TRN416_nonclinical_study_summary.pdf'
SP, AS = 'Client (proprietary)', 'TRN-416'

ss = dict(
 H1=ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13, leading=16, spaceBefore=12, spaceAfter=5),
 H2=ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=10, leading=13, spaceBefore=9, spaceAfter=3),
 P =ParagraphStyle('P',  fontName='Times-Roman', fontSize=9.2, leading=12.4, spaceAfter=5, alignment=TA_JUSTIFY),
 S =ParagraphStyle('S',  fontName='Times-Roman', fontSize=8.2, leading=10.6, spaceAfter=3),
 T =ParagraphStyle('T',  fontName='Helvetica-Bold', fontSize=18, leading=22, spaceAfter=3),
 ST=ParagraphStyle('ST', fontName='Helvetica', fontSize=11, leading=15, spaceAfter=2),
)

def P(t, s='P'): return Paragraph(t, ss[s])
def H1(t): return Paragraph(t, ss['H1'])
def H2(t): return Paragraph(t, ss['H2'])

def kv(pairs, w=(52*mm, 118*mm)):
    rows = [[Paragraph(f'<b>{k}</b>', ss['S']), Paragraph(str(v), ss['S'])] for k, v in pairs]
    t = Table(rows, colWidths=w)
    t.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'), ('TOPPADDING',(0,0),(-1,-1),1.6),
        ('BOTTOMPADDING',(0,0),(-1,-1),1.6), ('LEFTPADDING',(0,0),(-1,-1),2),
        ('LINEBELOW',(0,0),(-1,-2),0.25,colors.HexColor('#DDDDDD'))]))
    return t

def grid(head, body, widths):
    rows = [[Paragraph(f'<b>{h}</b>', ss['S']) for h in head]]
    rows += [[Paragraph(str(c), ss['S']) for c in r] for r in body]
    t = Table(rows, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'), ('TOPPADDING',(0,0),(-1,-1),1.6),
        ('BOTTOMPADDING',(0,0),(-1,-1),1.6),
        ('LINEBELOW',(0,0),(-1,0),0.6,colors.black),
        ('LINEBELOW',(0,1),(-1,-1),0.25,colors.HexColor('#DDDDDD'))]))
    return t

def onpage(c, d):
    c.saveState()
    c.setFont('Helvetica', 7)
    c.setFillColor(colors.HexColor('#555555'))
    c.drawString(20*mm, 287*mm, f'Non-clinical study summary  |  {AS}  |  TRN-DOC-0416-07  Rev 3  |  Client proprietary')
    c.drawRightString(190*mm, 12*mm, f'Page {c.getPageNumber()}')
    c.drawString(20*mm, 12*mm, 'Confidential — client proprietary')
    c.setStrokeColor(colors.HexColor('#999999')); c.setLineWidth(0.4)
    c.line(20*mm, 285*mm, 190*mm, 285*mm)
    c.restoreState()

F = []
A = F.append

# ---------------------------------------------------------------- title
A(Spacer(1, 16*mm))
A(Paragraph('Non-clinical Study Summary', ss['T']))
A(Paragraph(f'Test article {AS} — in vitro pharmacology, binding and selectivity', ss['ST']))
A(Spacer(1, 7*mm))
A(kv([('Document number','TRN-DOC-0416-07'),('Revision','3'),
      ('Sponsor','Client. Sponsor identity withheld as proprietary.'),
      ('Compiled for','Programme review'),('Document owner','Non-clinical Sciences'),
      ('Test article',f'{AS} (anti-human TNFRSF1B monoclonal antibody)'),
      ('Studies covered','TRN416-FC-002 to FC-008, FC-012A, FC-012B, EL-012C, AR-012D, MB-012E, RS-001, BP-009, BP-010, BP-011'),
      ('Donor consent protocol','HS-2019-114'),
      ('Animal use protocol','IACUC-2016-041'),
      ('Scope','Methods and conditions as performed. Tabulated results are held in the accompanying data files.')]))
A(Spacer(1, 5*mm))

# ---------------------------------------------------------------- 1
A(H1('1. Test article identity'))
A(kv([('Designation', AS),
 ('Target','Human tumour necrosis factor receptor superfamily member 1B (TNFRSF1B, TNFR2)'),
 ('Species of origin','Mouse. Hybridoma raised in BALB/c.'),
 ('Isotype','IgG1, kappa'),
 ('Immunogen','Recombinant fragment of the human TNFR2 extracellular region spanning amino acids 50 to 122, followed by boosting with the whole exterior portion of the human TNFR2 protein.'),
 ('Immunisation schedule','Intravenous and subcutaneous administration on at least five occasions before splenic harvest. Tail bleed titres were checked by ELISA; animals reaching a titre between 1:30,000 and 1:100,000 were carried forward to hybridoma generation.'),
 ('Hybridoma history','Generated at a contract hybridoma facility. Supernatants were screened first; subclones retaining activity were purified. Clones of the IgM isotype were discarded.'),
 ('Purification','Protein A affinity chromatography followed by buffer exchange into phosphate-buffered saline.'),
 ('Purity','Greater than 95% by sodium dodecyl sulfate polyacrylamide gel electrophoresis and size-exclusion chromatography.'),
 ('Endotoxin','Determined with the Endosafe-PTS system and Endosafe PTS cartridges. Levels were below 1 EU/mg for every lot released to in vitro testing.'),
 ('Concentration determination','Absorbance at 280 nm, calculated with an extinction coefficient of 205,500 M<super>-1</super> cm<super>-1</super> (1.0 mg/ml = A280 1.40).'),
 ('Storage','Phosphate-buffered saline, pH 7.4, at 4 C for working stocks and -80 C for archive aliquots. Working stocks were not subjected to more than three freeze-thaw cycles.'),
 ('Lots used','TRN416-L07, TRN416-L09, TRN416-L11')]))

# ---------------------------------------------------------------- 2
A(H1('2. Intervention agents'))
A(P('The following agents were added to cultures in one or more of the studies described below. Each entry gives the identity of the agent and the molecular interaction through which it acts.'))
A(kv([
 ('Recombinant human IL-2','Interleukin-2, purchased from a commercial supplier. Binds the interleukin-2 receptor. Signalling proceeds through the IL-2 receptor beta chain (CD122) and the common gamma chain (CD132), activating JAK1 and JAK3 and phosphorylating STAT5.'),
 ('Recombinant human TNF','Tumour necrosis factor, purchased from a commercial supplier. A soluble trimer that binds both TNFR1 (TNFRSF1A) and TNFR2 (TNFRSF1B). TNFR1 carries an intracellular death domain and recruits TRADD; TNFR2 lacks a death domain and recruits TRAF2-containing complexes.'),
 ('Anti-CD3 monoclonal antibody, clone HIT3a','Mouse IgG2a against the epsilon chain of the human CD3 complex. Binding cross-links the CD3 complex associated with the T cell receptor and initiates proximal T cell receptor signalling through LCK and ZAP-70.'),
 ('Anti-CD3 monoclonal antibody, clone OKT3','Mouse IgG2a against the epsilon chain of the human CD3 complex, used plate-bound. Acts through the same proximal T cell receptor signalling route as clone HIT3a.'),
 ('Cross-linking anti-rodent IgG, clone ab9165','Polyclonal antibody raised against rodent immunoglobulin G. Binds the Fc portion of murine IgG and multimerises murine antibody that is already bound to its antigen.'),
 (f'{AS}','See section 1. Binds the human TNFR2 extracellular region at the sites given in section 12.'),
]))

# ---------------------------------------------------------------- 3
A(H1('3. Donor material and cell isolation'))
A(P('Peripheral whole blood was drawn into K2-EDTA (purple top) tubes. Donors provided written informed consent under protocol HS-2019-114. Donor material is described in each study section as nondiabetic blood donors or as donors with type 1 diabetes.'))
A(H2('3.1 CD4+ T cell isolation'))
A(P('Whole blood was washed twice with 1x Hanks’ balanced salt solution containing 2% fetal bovine serum. CD4+ T cells were isolated by immunomagnetic negative selection using the EasySep Direct Human CD4+ T Cell Isolation Kit, following the instructions of the manufacturer. In brief, 1200 microlitres of Isolation Cocktail and 1200 microlitres of RapidSpheres were combined with 24 ml of whole blood in a 50 ml centrifuge tube and incubated for 5 minutes at room temperature. Twenty-four millilitres of calcium- and magnesium-free phosphate-buffered saline were added and the tube was placed in an Easy 50 EasySep magnet, immobilising the unwanted cells against the wall of the tube. After 10 minutes the enriched suspension was transferred to a fresh tube and the magnetic separation was repeated for 5 minutes with fresh RapidSpheres. The suspension was transferred again and purified a third time in the magnet.'))
A(P('The purity of the final CD4+ T cell preparation was greater than 95% as assessed by flow cytometry. Cell recovery was counted on a hemocytometer with trypan blue exclusion; viability was above 92% in all preparations released to study.'))
A(H2('3.2 Peripheral blood mononuclear cells'))
A(P('Where peripheral blood mononuclear cells were required, they were collected on the day of venipuncture by density gradient separation over Ficoll-Hypaque Plus, centrifuged at 400 g for 30 minutes at room temperature with the brake disengaged, washed twice at 300 g for 10 minutes, cryopreserved in 10% dimethyl sulfoxide in fetal bovine serum and held at -80 C.'))

# ---------------------------------------------------------------- 4
A(H1('4. General culture conditions'))
A(P('Isolated CD4+ cells were cultured in RPMI GlutaMAX supplemented with 10% fetal bovine serum and 1x penicillin-streptomycin. Cells were seeded in 96-well round-bottom plates at 0.2 to 1 x 10<super>6</super> cells per well, treated with the agents stated for each study, and incubated for up to 72 hours at 37 C in 5% CO<sub>2</sub>. All cell culture experiments included low-level IL-2 at 200 U/ml in the media. Culture conditions specific to an individual study are given in that study’s section and take precedence over this paragraph.'))

# ---------------------------------------------------------------- 5
A(H1('5. Flow cytometry: staining panel and gating'))
A(kv([
 ('Instrument','BD FACSCalibur, four-colour configuration'),
 ('Preparation kit','Human Treg cell Flow Kit, used according to the instructions of the manufacturer'),
 ('Surface stain','Phycoerythrin-conjugated anti-human CD25, clone BC96, detected in FL2'),
 ('Intracellular stain','Alexa Fluor 488-conjugated anti-human FoxP3, clone 259D, detected in FL1, applied after fixation and permeabilisation'),
 ('Suppression assay stains','Carboxyfluorescein succinimidyl ester in FL1 and allophycocyanin-conjugated anti-human CD8, clone SK1, in FL4'),
 ('Conjugation','Where antibodies or fragments were conjugated in house, the Lightning-Link APC conjugation kit was used according to the instructions of the manufacturer'),
 ('Resuspension','1x Hanks’ balanced salt solution'),
 ('Gating, population reported as Treg','Events within the CD4+ preparation that are CD25 high and FoxP3 positive, assessed on an FL2 against FL1 plot'),
 ('Gating, population reported as Teff','Events within the CD4+ preparation that are CD25 high and FoxP3 negative, assessed on the same plot'),
 ('Quadrant placement','Set on unstained and single-stained aliquots of the same preparation, run at the start of each acquisition session'),
 ('Events acquired','A minimum of 30,000 events within the lymphocyte light-scatter region per sample'),
 ('Analysis software','FlowJo version 10.0.8'),
]))

# ---------------------------------------------------------------- 6
A(H1('6. Dose-response studies by flow cytometry'))
A(P('Five studies are reported in this group. Each used freshly isolated CD4+ cells prepared as in section 3.1 and cultured as in section 4. In every study each donor preparation was divided across all of the conditions listed for that study, cultured for 48 hours, then stained and acquired as in section 5. The reported quantity in every study in this group is the percentage of CD4+ events falling in the CD25 high, FoxP3 positive gate. Results are summarised as the mean with the standard error of the mean across donor preparations and are tabulated in the accompanying data files.'))

A(H2('6.1 Study TRN416-FC-002'))
A(kv([('Donor material','Nondiabetic blood donors, freshly isolated CD4+'),
 ('Samples (n)','13'),
 ('Conditions', f'{AS} at 0, 0.0008, 0.004, 0.02, 0.1, 0.5, 2.5, 5, 12.5 and 25 ug/ml. Media as in section 4, including IL-2 at 200 U/ml in every well.'),
 ('Incubation','48 hours'),('Summary statistic','Mean with SEM'),('Units','Percent of CD4+ events')]))

A(H2('6.2 Study TRN416-FC-003'))
A(kv([('Donor material','Donors with type 1 diabetes, freshly isolated CD4+'),
 ('Samples (n)','11'),
 ('Conditions', f'{AS} at 0, 0.0008, 0.004, 0.02, 0.1, 0.5, 2.5, 5, 12.5 and 25 ug/ml. Media as in section 4, including IL-2 at 200 U/ml in every well.'),
 ('Incubation','48 hours'),('Summary statistic','Mean with SEM'),('Units','Percent of CD4+ events')]))

A(H2('6.3 Study TRN416-FC-004'))
A(kv([('Donor material','Nondiabetic blood donors, freshly isolated CD4+'),
 ('Samples (n)','3'),
 ('Conditions', f'{AS} at 0, 0.0008, 0.004, 0.02, 0.1, 0.5, 2.5, 5, 12.5 and 25 ug/ml. Recombinant human TNF at 20 ng/ml was added to every well, including the well receiving no {AS}. Media as in section 4, including IL-2 at 200 U/ml in every well.'),
 ('Incubation','48 hours'),('Summary statistic','Mean with SEM'),('Units','Percent of CD4+ events')]))

A(H2('6.4 Study TRN416-FC-005'))
A(kv([('Donor material','Nondiabetic blood donors, freshly isolated CD4+'),
 ('Samples (n)','7'),
 ('Conditions','Recombinant human IL-2 added at 0, 2, 10, 50, 200, 1000 and 5000 U/ml. No test article was added to any well. Doses are the quantity of IL-2 added to the well.'),
 ('Incubation','48 hours'),('Summary statistic','Mean with SEM'),('Units','Percent of CD4+ events')]))

A(H2('6.5 Study TRN416-FC-006'))
A(kv([('Donor material','Nondiabetic blood donors, freshly isolated CD4+'),
 ('Samples (n)','8'),
 ('Conditions','Recombinant human TNF added at 0, 0.02, 0.1, 0.5, 2.5, 10, 20, 40, 80 and 100 ng/ml. No test article was added to any well. Doses are the quantity of TNF added to the well.'),
 ('Incubation','48 hours'),('Summary statistic','Mean with SEM'),('Units','Percent of CD4+ events')]))

# ---------------------------------------------------------------- 7
A(H1('7. Study TRN416-FC-007: absolute cell enumeration'))
A(kv([('Donor material','Nondiabetic blood donors, freshly isolated CD4+'),
 ('Samples (n)','11'),
 ('Conditions', f'{AS} at 0, 0.0008, 0.004, 0.02, 0.1, 0.5, 2.5, 5, 12.5 and 25 ug/ml. Media as in section 4, including IL-2 at 200 U/ml in every well.'),
 ('Incubation','48 hours'),
 ('Enumeration','Cells were harvested, stained as in section 5, and counted on a hemocytometer with trypan blue exclusion. Four corner squares were counted per chamber and two chambers were counted per sample.'),
 ('Reported quantity','Absolute number of CD25 high, FoxP3 positive cells per well'),
 ('Summary statistic','Mean with SEM'),('Units','Cells')]))

# ---------------------------------------------------------------- 8
A(H1('8. Study TRN416-FC-008: suppression of CD8+ T cell division'))
A(kv([
 ('Responder cells','Autologous peripheral blood mononuclear cells prepared as in section 3.2, thawed on the day before assembly and rested overnight in RPMI 1640 with 1% fetal bovine serum and IL-2 at 10 U/ml. Responders were CD8+ T cells from donors with type 1 diabetes.'),
 ('Responder labelling','Carboxyfluorescein succinimidyl ester at 1 micromolar'),
 ('Responder input','5 x 10<super>4</super> cells per well'),
 ('Added cells', f'CD4+ cultures expanded with {AS} at 2.5 ug/ml for 48 hours. The cells added in every ratio were expanded in this way.'),
 ('Ratios assembled','Responder to Treg at 0:1, 1:1, 2:1 and 4:1'),
 ('Stimulation','Soluble anti-CD3 monoclonal antibody, clone HIT3a, with IL-2 at 50 U/ml in 10% fetal bovine serum RPMI'),
 ('Incubation','4 days'),('Samples (n)','7, from normal blood donors'),
 ('Readout','Percentage of CD8+-gated responder cells that underwent division, read from carboxyfluorescein succinimidyl ester dilution'),
 ('Suppression index','Calculated as (Treg cell proliferation without Treg − Tresp proliferation with Treg) / Tresp proliferation without Treg cell'),
 ('Summary statistic','Mean with SEM'),('Units','Percent of CD8+-gated events'),
]))

# ---------------------------------------------------------------- 9
A(H1('9. Study TRN416-RS-001: transcript abundance by RNA sequencing'))
A(H2('9.1 Cell preparation and culture'))
A(P('CD4+ T cells were isolated from peripheral blood by immunomagnetic negative selection using the EasySep Direct Human CD4+ T Cell Isolation Kit as described in section 3.1, following the instructions of the manufacturer. The purity of the CD4+ preparation was greater than 95%.'))
A(P(f'Cells were cultured at 37 C in 24-well tissue culture plates at 3 x 10<super>6</super> cells per well in 1 ml of RPMI with GlutaMAX, fetal bovine serum at 2% (v/v) and human recombinant IL-2 at 50 U/ml, with or without {AS} at a concentration of 2.5 ug/ml. Cells were then harvested and washed twice with phosphate-buffered saline, pH 7.4, calcium and magnesium free. Various incubation times were studied from 6 to 24 hours. The incubation time for the samples reported here was 10 hours.'))
A(kv([('Arms', f'Each donor preparation was split into two wells. One well received IL-2 at 50 U/ml and no test article. The other well received IL-2 at 50 U/ml and {AS} at 2.5 ug/ml.'),
      ('Samples (n)','12 donor preparations'),
      ('Donor material','Nondiabetic blood donors')]))
A(H2('9.2 Sample handling'))
A(grid(['Step','Condition'], [
  ['Harvest time after addition of test article','10 h'],
  ['Interval from harvest to RNA stabilisation','1 h'],
  ['Wash','Two washes in calcium- and magnesium-free phosphate-buffered saline, 300 g for 5 min'],
  ['RNA isolation','RNeasy Plus Mini Kit, following the instructions of the manufacturer'],
  ['Quantification','NanoDrop spectrophotometer'],
  ['Storage','-80 C until processed for RNA sequencing'],
  ['Integrity','Agilent 2100 Bioanalyzer, RNA integrity number recorded per sample'],
], (52*mm, 118*mm)))
A(H2('9.3 Library preparation and sequencing'))
A(P('RNA sequencing was performed at two sites: the Calder Genomics Center and the Westmoor Sequencing Facility. Poly-A selection was performed using NEBNext Poly(A) mRNA Magnetic Isolation Modules, following the instructions of the manufacturer. The resulting mRNA was used for library preparation using NEBNext Ultra Directional RNA Library Prep Kits for Illumina at the Calder Genomics Center, and NEBNext Ultra II Directional RNA Library Prep Kits at the Westmoor Sequencing Facility, following the instructions of the manufacturer.'))
A(P('Libraries were run on high-sensitivity DNA chips on the Agilent 2100 Bioanalyzer and the functional concentration of each library was determined by quantitative polymerase chain reaction using KAPA Biosystems Illumina Library Quantification Kits. Libraries to be sequenced were pooled at a concentration of 2 nM, then denatured and diluted to a final concentration of 2 pM, and loaded onto an Illumina NextSeq 500.'))
A(P('The data were normalized for each sequencing laboratory separately using DESeq, part of the R-Bioconductor package.'))
A(H2('9.4 Alignment, normalization and reporting'))
A(kv([('Alignment reference','Human genome assembly HG19'),
 ('Aligner','TopHat'),('Transcript assembly','Cufflinks'),
 ('Normalization software','DESeq, part of the R-Bioconductor package'),
 ('Normalization scope','Raw reads were normalized for subjects separately.'),
 ('Units','Normalized reads'),
 ('Induction criterion applied','Transcripts were counted as induced where the increase over the paired wells with/without treatment reached 1200 normalized reads or more.'),
 ('Analysis environment','Ingenuity Pathway Analysis software, the R Statistical Programming language and Microsoft Excel'),
 ('Reported transcripts','The 70 transcripts listed in Appendix A.')]))

# ---------------------------------------------------------------- 10
A(H1('10. Study TRN416-BP-009: binding kinetics by surface plasmon resonance'))
A(kv([('Service provider','Contract biophysics laboratory'),
 ('Instrument','Biacore 3000'),('Sensor chip','BioCap'),
 ('Analyte','Recombinant human TNFR2 extracellular domain'),
 ('Ligand preparation', f'{AS} was biotinylated at 5:1 stoichiometry with biotinyl-LC-LC-NHS in phosphate-buffered saline. Excess biotinylating reagent was removed by centrifugation chromatography.'),
 ('Capture surface','Streptavidin surface at 3000 RU'),
 ('Capture level','Biotinylated antibody captured to a level of 100 RU. Antibody was injected at a concentration of 1 ng/ml to reach the final capture of 100 RU.'),
 ('Theoretical maximum signal','26 RU at that level of antibody capture. That signal was reached in a preliminary experiment using 500 nM TNFR2 in the running buffer.'),
 ('Flow rate','60 microlitres per minute'),
 ('Injections','2 minute association injections; dissociation followed for 10 minutes'),
 ('Analyte series','50, 25, 12.5, 6.25, 3.125 and 1.5625 nM'),
 ('Regeneration','10 mM glycine-hydrochloride, pH 1.7, for 30 seconds'),
 ('Reference channel','An identical level of streptavidin with no captured ligand'),
 ('Referencing','The double reference method was used for analysis'),
 ('Temperature','25 C'),('Fit model','1:1 Langmuir, global fit'),
 ('Evaluation software','BIAevaluation 4.1.1'),
 ('Dissociation constant','The K<sub>D</sub> was 1.2(2) nM.')]))

# ---------------------------------------------------------------- 11
A(H1('11. Study TRN416-BP-010: receptor counter-screen by ELISA'))
A(kv([('Format','Direct-binding enzyme-linked immunosorbent assay, 96-well'),
 ('Plates','Immulon 4HBX flat bottom microtiter plates'),
 ('Antigens coated','Recombinant human TNFR2 full ectodomain; the human TNFR2 fragment spanning amino acids 50 to 122; recombinant human TNFR1 full ectodomain; bovine serum albumin'),
 ('Coating','1 microgram of antigen per well in carbonate coating buffer, overnight at 4 C'),
 ('Primary antibody', f'{AS}, eight-point 1:3 serial titration from 10 ug/ml'),
 ('Secondary antibody','Horseradish peroxidase-conjugated antibody against rodent immunoglobulin G, 1:5000'),
 ('Substrate','3,3′,5,5′-tetramethylbenzidine, stopped with 2 N sulfuric acid'),
 ('Reader','SpectraMax 190 absorbance plate reader, 450 nm'),
 ('Analysis software','SoftMax Pro 6.3'),
 ('Replicates','Triplicate wells in each of three independent runs'),
 ('Reported quantity','Mean optical density at 450 nm')]))

# ---------------------------------------------------------------- 12
A(H1('12. Study TRN416-BP-011: epitope mapping'))
A(P('Linear epitope mapping on the TNFR2 external membrane protein sequence was performed by enzyme-linked immunosorbent assay. Peptides were purchased from a commercial supplier, diluted in coating buffer and placed on Immulon 4HBX flat bottom microtiter plates at a concentration of 1 mg per well. Primary monoclonal antibody at 0.1 mg per well was incubated with the substrates. Secondary antibodies against rodent immunoglobulin G were used to label the primary antibody. Absorbance was measured using the SpectraMax 190 absorbance plate reader and analysed with SoftMax Pro 6.3.'))
A(P('Three-dimensional peptide mapping was performed using Chemically Linked Peptides on Scaffolds (CLIPS) technology. The target protein was converted into a library of up to 10,000 overlapping linear peptides, which were then bound to a solid support and shaped into a matrix of CLIPS constructs. The affinity of the antibody to the various peptide conformations was used to determine the precise discontinuous epitopes.'))
A(kv([('Linear peptide lengths','15-mer and 18-mer, tiled at an offset of one residue'),
 ('Single-loop CLIPS construct length','17-mer'),
 ('Double-loop CLIPS construct length','22-mer'),
 ('Primary antibody concentration','1 ug/ml, incubated overnight at 4 C'),
 ('Detection','Peroxidase-conjugated antibody against mouse immunoglobulin G with 2,2′-azino-bis(3-ethylbenzothiazoline-6-sulfonic acid) substrate'),
 ('Reader','Charge-coupled device camera at 620 nm'),
 ('Reported quantity','Arbitrary binding units, mean of duplicate arrays'),
 ('Binding sites identified', f'The CRD1 and CRD2 discontinuous TNFR2 binding sites were QMCCSKCSPGQH, CSSDQVET, and NRICTCRP.')]))

# ---------------------------------------------------------------- 13
A(H1('13. Ancillary functional studies'))
A(H2("13.1 Study TRN416-FC-012A: F(ab′)2 fragment"))
A(kv([('Test article', f"F(ab′)2 fragments of {AS}, prepared using the Pierce F(ab′)2 Preparation Kit according to the instructions of the manufacturer and verified by size-exclusion chromatography"),
 ('Donor material','Peripheral human CD4+ cells'),('Samples (n)','5'),
 ('Conditions', "F(ab′)2 at 0, 0.001, 0.0073, 0.1, 0.37, 0.91, 1.8, 2.5, 10 and 18.3 ug/ml. Media as in section 4."),
 ('Incubation','48 hours'),('Readout','Percent of CD4+ events in the CD25 high, FoxP3 positive gate'),
 ('Summary statistic','Mean with SEM')]))
A(H2('13.2 Study TRN416-FC-012B: cross-linking antibody'))
A(kv([('Cross-linking reagent','Antibody against rodent immunoglobulin G, clone ab9165, at 2.5 ug/ml'),
 ('Test article', f'{AS} at 0.0008, 0.004, 0.02, 0.1, 0.5, 2.5, 12.5 and 25 ug/ml, with the cross-linking reagent present in every well'),
 ('Donor material','Peripheral human CD4+ cells'),('Samples (n)','3'),
 ('Timepoints examined','24, 48 and 72 hours'),('Timepoint tabulated','48 hours'),
 ('Readout','Percent of CD4+ events in the CD25 high, FoxP3 positive gate'),
 ('Summary statistic','Mean with SEM')]))
A(H2('13.3 Study TRN416-EL-012C: soluble TNFR2'))
A(kv([('Assay','Quantikine enzyme-linked immunosorbent assay kit for human soluble TNFR2, with modifications'),
 ('Matrix','Cell culture supernatant'),
 ('Culture conditions', f'CD4+ cells incubated with IL-2 at 200 U/ml alone, or with TNF at 20 ng/ml, or with {AS} at 12.5 ug/ml'),
 ('Collection window','Supernatants were collected after 24 to 42 hours of incubation'),
 ('Capture','Either the commercial plates or custom plates coated with 2 ug per well of TNFR2-directed antibodies'),
 ('Reader','SpectraMax 190 absorbance plate reader, 450 nm, analysed with SoftMax Pro 6.3'),
 ('Samples (n)','10'),('Units','pg/ml')]))
A(H2('13.4 Study TRN416-AR-012D: NF-kB pathway array'))
A(kv([('Platform','Applied Biosystems TaqMan Array Human NF-kB Pathway plates, used per the instructions of the manufacturer'),
 ('Culture conditions', f'Fresh human CD4+ T cells cultured with {AS} at 2.5 ug/ml, alongside wells of the same donor preparation receiving IL-2 only'),
 ('Incubation','6 hours'),('Samples (n)','7'),
 ('Gene families on the plate','The panel of assays on this plate targets genes encoding the proteins of the Rel/NF-kB family signalling pathways (NFKB1, NFKB2, RELA, RELB and REL) associated with regulatory proteins, including I-kappa-B, I-kappa-B kinase, Toll-like receptors, TNF and the TNF receptors, and TRAF; and those associated with NF-kB functions in apoptosis, immune and inflammation responses, as well as chemokines and cytokines.'),
 ('Reported quantity','Relative quantitation against the wells of the same donor preparation receiving IL-2 only, which are set to 1.000'),
 ('Wells without amplification','Reported as undetermined where no amplification occurred within 40 cycles')]))
A(H2('13.5 Study TRN416-MB-012E: itaconate'))
A(kv([('Matrix','Culture supernatant'),
 ('Culture conditions', f'Fresh human CD4+ T cells cultured with {AS} at 0, 0.1, 0.5 and 2.5 ug/ml in 96-well plates at 100,000 cells per well. Each well in each 96-well plate yielded 50 microlitres of culture sample.'),
 ('Incubation','6 hours'),
 ('Donors','Supernatants were harvested from numerous normal blood donors treated in the dose-specific manner (n = 6 donors).'),
 ('Analysis','Samples were sent to Metabolon Inc, Research Triangle Park, North Carolina, for the analysis of itaconate levels.'),
 ('Samples (n)','12'),('Units','Scaled intensity')]))

# ---------------------------------------------------------------- 14
A(H1('14. Statistical methods'))
A(kv([('Comparisons between two conditions','Student’s t test, two tailed, unequal variance, computed in Microsoft Excel or GraphPad Prism 8'),
 ('Comparisons across more than two conditions','One-way analysis of variance with Tukey’s multiple comparison test'),
 ('Dose-response trend','Linear mixed-effects modelling with participant-level random effects'),
 ('Expression comparisons','Paired Student’s t test, two tailed'),
 ('Summary measure','Mean with the standard error of the mean, unless otherwise stated in the study section'),
 ('Software versions','GraphPad Prism 8; FlowJo 10.0.8; SoftMax Pro 6.3; BIAevaluation 4.1.1; R 3.6.1 with Bioconductor 3.9')]))

# ---------------------------------------------------------------- Appendix
A(H1('Appendix A. Transcripts reported in study TRN416-RS-001'))
ws = openpyxl.load_workbook('/home/user/Task8/data_room/TRN416_expression_normalized_reads.xlsx', data_only=True).active
genes = sorted({r[0] for r in ws.iter_rows(min_row=2, values_only=True) if r[0]})
A(P(f'The following {len(genes)} transcripts were reported. Transcripts are listed in alphabetical order.'))
cols = 6
rowsn = -(-len(genes) // cols)
body = [[genes[c*rowsn + r] if c*rowsn + r < len(genes) else '' for c in range(cols)] for r in range(rowsn)]
t = Table(body, colWidths=[28*mm]*cols)
t.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'Times-Roman'),('FONTSIZE',(0,0),(-1,-1),8),
  ('TOPPADDING',(0,0),(-1,-1),1),('BOTTOMPADDING',(0,0),(-1,-1),1)]))
A(t)
A(Spacer(1, 4*mm))
A(Paragraph('End of document. TRN-DOC-0416-07 Rev 3.', ss['S']))

doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm,
                      topMargin=22*mm, bottomMargin=18*mm,
                      title='Non-clinical Study Summary TRN-416', author=SP)
doc.addPageTemplates([PageTemplate(id='n',
    frames=[Frame(20*mm, 18*mm, 170*mm, 262*mm, id='f')], onPage=onpage)])
doc.build(F)
print('wrote', OUT, os.path.getsize(OUT), 'bytes,', len(genes), 'genes listed')
