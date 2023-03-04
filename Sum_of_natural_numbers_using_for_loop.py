# Write a program to find the sum of first n natural numbers using for loop.

import sys

N = int(input("Enter a natural number: "))

answer=0

for i in range(0,N+1):
	answer = answer + i;

print(answer)