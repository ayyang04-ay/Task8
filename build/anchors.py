# Values digitized at 400 dpi from the build-time source figures.
# Nothing in this file is mounted; it is build input only.

SPONSOR = "Torenia Biosciences"
ASSET   = "TRN-416"
DONORS  = [f"DN-{i:02d}" for i in range(1, 13)]

# ---- Record 2: Treg % by asset dose, control donors, 48 h, n=13
DOSE_AB = [0, 0.0008, 0.004, 0.02, 0.1, 0.5, 2.5, 5, 12.5, 25]
R2 = dict(n=13,
  mean=[10.622,11.042,11.361,11.076,11.782,12.840,13.849,13.899,14.101,13.765],
  sem =[0.706,0.521,0.756,0.672,0.756,0.790,1.076,1.244,1.092,0.908])

# ---- Record 3: Treg % by asset dose, T1D donors, 48 h, n=11
R3 = dict(n=11,
  mean=[10.902,10.968,10.653,10.869,11.847,13.158,14.368,14.302,14.385,14.866],
  sem =[0.481,0.464,0.415,0.415,0.448,0.415,0.680,1.658,0.514,0.597])

# ---- Record 4: Treg % by asset dose with added TNF 20 ng/ml, 48 h, n=3
R4 = dict(n=3,
  mean=[10.290,12.201,12.382,12.053,11.147,12.843,14.343,14.293,14.507,14.936],
  sem =[1.120,1.186,0.115,0.791,1.400,1.911,2.010,2.026,1.631,2.076])

# ---- Record 5: Treg % by IL-2 dose, 48 h, n=7
DOSE_IL2 = [0, 2, 10, 50, 200, 1000, 5000]           # U/ml, exogenously added
R5 = dict(n=7,
  mean=[4.553,7.106,7.106,7.085,7.064,7.085,7.106],
  sem =[0.830,0.319,0.319,0.298,0.298,0.298,0.319])

# ---- Record 6: Treg % by TNF dose, 48 h, n=8
DOSE_TNF = [0, 0.02, 0.1, 0.5, 2.5, 10, 20, 40, 80, 100]   # ng/ml
R6 = dict(n=8,
  mean=[8.660,9.472,8.745,9.664,10.263,11.395,10.818,11.011,11.182,11.438],
  sem =[0.598,0.748,0.492,0.513,0.449,0.470,0.449,0.534,1.154,0.855])

# ---- Record 7: absolute Treg counts by asset dose, 48 h, n=11 (hemocytometer)
R7 = dict(n=11,
  mean=[2029,2088,2139,2104,2369,2698,2965,2775,2944,2842],
  sem =[96,70,80,78,83,80,88,61,99,110])

# ---- Record 8: % CD8 division by responder:Treg ratio, 4 days, n=7
R8_RATIOS = ["1:0", "4:1", "2:1", "1:1"]
R8 = dict(n=7, mean=[83.66,73.01,64.09,49.41], sem=[9.71,8.52,11.29,10.73])

# ---- Record 12a: F(ab')2 fragment dose series, 48 h, n=5
DOSE_FAB = [0, 0.001, 0.0073, 0.1, 0.37, 0.91, 1.8, 2.5, 10, 18.3]
R12A = dict(n=5,
  mean=[0.16,0.16,0.84,8.94,8.63,13.37,11.55,12.00,9.35,8.24],
  sem =[0.55,0.51,0.88,3.27,1.86,1.63,3.45,3.00,4.22,5.69])

# ---- Record 12b: asset + cross-linking anti-rodent IgG (2.5 ug/ml), 48 h, n=3
DOSE_XL = [0.0008, 0.004, 0.02, 0.1, 0.5, 2.5, 12.5, 25]
R12B = dict(n=3,
  mean=[9.24,10.07,10.34,11.73,12.67,12.14,12.40,12.91],
  sem =[0.16,None,None,0.13,None,0.12,0.56,None])

# ---- Record 12c: sTNFR2 in culture supernatant, per-donor, n=10 per arm (pg/ml)
R12C = {
 "IL-2 200 U/ml":      [5.9,16.8,23.0,34.8,59.5,88.0,90.4,195.6,279.2,318.8],
 "TNF 20 ng/ml":       [59.8,105.0,113.3,124.5,166.3,215.3,283.5,313.5,318.2,359.6],
 "TRN-416 12.5 ug/ml": [180.2,208.6,221.3,240.8,277.9,370.2,390.6,429.6,445.0,471.6],
}

# ---- Record 12d: NF-kB pathway array, 6 h, n=7, relative quantitation vs IL-2-only wells
R12D = [("RPLP0",1.124),("HMBS",1.086),("BIRC2",1.291),("BIRC3",2.099),("CHUK",1.447),
 ("IKBKB",0.909),("IKBKE",1.607),("IKBKG",1.318),("JUN",1.107),("LTA",2.656),
 ("MAP3K1",None),("MAP3K11",0.786),("MAP3K12",None),("MAP3K14",1.628),("MAP3K2",1.164),
 ("MAP3K3",1.021),("MAP3K4",1.151),("MAP3K5",1.023),("MAP3K7",None),("MAP3K8",2.012),
 ("MAP3K9",1.250),("MAPK8",0.831),("MAPK9",0.928),("NFKB1",1.504),("NFKB2",1.877),
 ("NFKBIA",2.006),("NFKBIB",1.493),("NFKBIE",1.820),("REL",1.710),("RELA",1.225),
 ("RELB",2.573),("TANK",2.683),("TBK1",1.291),("TNF",0.852),("TNFAIP3",None),
 ("TNFRSF1B",0.894),("TRAF1",1.417),("TRAF2",1.187),("TRAF3",None)]

# ---- Record 12e: itaconate in culture supernatant, 6 h (scaled intensity)
DOSE_ITA = [0, 0.5, 2.5]
R12E = dict(mean=[614601,642714,700373], sem=[1850,2400,1100])

# ---- Record 9: SPR
SPR = dict(KD_nM=1.2, capture_RU=100, streptavidin_RU=3000, Rmax_RU=26,
           flow_ul_min=60, inj_min=2, chip="BioCap", instrument="Biacore 3000")

# ---- Record 11: CLIPS binding sequences
CLIPS = ["QMCCSKCSPGQH", "CSSDQVET", "NRICTCRP"]
