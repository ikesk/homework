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
    r = random.randint(1, 100)
    if   r <= 30:
        dna += 'A'
    elif r > 30 and r <= 60:
        dna += 'T'
    elif r > 60 and r <= 80:
        dna += 'C'
    elif r > 80 and r <= 100:
        dna += 'G'

at_percent = (dna.count('A') + dna.count('T')) / len(dna)

print(len(dna), at_percent, dna)
      
"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
