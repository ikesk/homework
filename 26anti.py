# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'

rev = '' 

revcomp = ''

for i in dna:
    rev = i + rev

for i in rev:
    if i == 'A':
        revcomp += 'T'
    elif i == 'C':
        revcomp += 'G'
    elif i == 'G':
        revcomp += 'C'
    elif i == 'T':
        revcomp += 'A'

print(revcomp)
        


"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
