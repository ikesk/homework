# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane

import mcb185
import sys

# Kyte-Dolittle scores dictionary
kd_scores = {'I': 4.5, 'V': 4.2, 'L': 3.8, 'F': 2.8, 'C': 2.5,
             'M': 1.9, 'A': 1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
             'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
             'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5}

# Calculate KD:
def calculate_kd(seq):
    total_kd_score = 0
    for aa in seq:
        total_kd_score += kd_scores.get(aa, 0)
    return total_kd_score

# Determine whether sequence has a hydrophobic alpha helix:
def is_transmembrane_protein(seq):

    # Check for a signal peptide in the first 30 aa:
    has_signal_peptide = False
    for i in range(0, 30 - 8 + 1):
        window = seq[i:i + 8]
        if 'P' not in window:
            my_kd = calculate_kd(window)
            if my_kd > 2.5:
                has_signal_peptide = True
                break
            
    # Check for hydrophobic regions after the first 30 aa:
    has_hydrophobic_region = False
    for i in range(30, len(seq) - 11 + 1):
        window = seq[i:i + 11]
        if 'P' not in window:
            my_kd = calculate_kd(window)
            if my_kd > 2.0:
                has_hydrophobic_region = True
                break
            
    # If it has both, it is a transmembrane protein:
    if has_signal_peptide and has_hydrophobic_region:
        return True
    else:
        return False

# Run test on proteome:
fasta_file = sys.argv[1]
for defline, seq in mcb185.read_fasta(fasta_file):
    if is_transmembrane_protein(seq) == True:
        print(defline)

"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
