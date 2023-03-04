# Write a program to find the sum of first n natural numbers using while loop

import sys

N = int(input("Enter a natural number: "))

answer=0

i=1
while i<=N:
	answer = answer + i
	i=i+1

print(answer)