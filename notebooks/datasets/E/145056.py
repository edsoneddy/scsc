rep = int(input())
for i in range(0,rep):
	n,prod = int(input()),0
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	for j in range(0,n):
		prod = prod+(a[j]*b[j])
	print(prod)