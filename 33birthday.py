# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list
import sys
import random

d = int(sys.argv[1])
p = int(sys.argv[2])

dup = 0

for reps in range(10000):
	year = []
	for person in range(p):
		x = random.randint(0, d - 1)
		if x in year:
			dup += 1
			break
		else:
			year.append(x)

print(f'{dup/10000:.3f}')

"""
python3 33birthday.py 365 23
0.571
"""

