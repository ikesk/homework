# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input
import sys
import math

# accept input and initialize values list
cmd_values = sys.argv[1:]
num_list = []

# make sure the command line values contain numbers
for val in cmd_values:
	try:
		num_list.append(float(val))
	except:
		print(f'Value error: cannot convert {val} to a number', file=sys.stderr)
		raise

# make sure the probabilities add to 1.0
try:
	assert (math.isclose(sum(num_list), 1.0))
except:
	print("Assertion error: values do not add up to 1")
	raise

# calculate entropy
entropy = 0
for val in num_list:
	entropy += -(val * math.log2(val))
print(f'{entropy:.3f}')

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
