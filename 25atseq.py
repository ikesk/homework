# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers

import random

random.seed()

dna = ''

for i in range(1,31):
    r = random.randint(1, 10)
    if   r <= 3:
        dna += 'A'
    elif r > 3 and r <= 6:
        dna += 'T'
    elif r > 6 and r <= 8:
        dna += 'C'
    elif r > 8 and r <= 10:
        dna += 'G'

at_percent = (dna.count('A') + dna.count('T')) / len(dna)

print(len(dna), at_percent, dna)
      
"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
