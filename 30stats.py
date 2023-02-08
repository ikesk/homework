# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys
import sys

# accept arguments from cmd and populate numbers list
cmd_values = sys.argv[1:]
num_list = []
for val in cmd_values:
	num_list.append(float(val))

# calculate count
count = len(num_list)

# calculate standard deviation
std_dev = 0
numerator = 0
mean = sum(num_list) / count
for val in num_list:
	numerator += (val - mean) ** 2
std_dev = (numerator / count) ** 0.5

# calculate median
median = 0
num_list.sort()
if count % 2 == 0:
	median = (num_list[count // 2 - 1] + num_list[count // 2]) /2
else:
	median = (num_list[count // 2])

# print stats
print(f'{"Count: "} {count}')
print(f'{"Minimum: "} {min(num_list)}')
print(f'{"Maximum: "} {max(num_list)}')
print(f'{"Mean: "} {mean:.3f}')
print(f'{"Std. dev: "} {std_dev:.3f}')
print(f'{"Median "} {median:.3f}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
