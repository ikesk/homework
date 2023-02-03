# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'
anti = ''

for i in dna:
    if i == 'A':
        anti = 'T' + anti
    elif i == 'C':
        anti = 'G' + anti
    elif i == 'G':
        anti = 'C' + anti
    elif i == 'T':
        anti = 'A' + anti

print(anti)

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
