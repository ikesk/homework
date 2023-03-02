# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below
import sys
import random

cmd_values = sys.argv[1:]
genome_size = int(cmd_values[0])
read_num = int(cmd_values[1])
read_len = int(cmd_values[2])

coverage = []
for i in range(genome_size):
	coverage.append(0)

for i in range(read_num):
	start_pos = random.randint(0, genome_size - read_len)
	for j in range(start_pos, start_pos + read_len):
		coverage[j] += 1

min_cov = min(coverage[read_len:-read_len])
max_cov = max(coverage[read_len:-read_len])
avg_cov = sum(coverage[read_len:-read_len]) / len(coverage[read_len:-read_len])
print(min_cov, max_cov, avg_cov)

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
