# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library

n = 5
rsum = 0
fac = 1

for i in range(1, n + 1):
	rsum += i
	fac *= i
print(n, rsum, fac)
"""
python3 22sumfac.py
5 15 120
"""
