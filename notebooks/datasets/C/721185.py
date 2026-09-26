def decompose(n):
	ans=1
	while n>0:
		ans=ans*(n%10)
		n=n//10
	return ans
for _ in range(int(input())):
	n=int(input())
	count=0
	while n>=10:
		count+=1
		n=decompose(n)
	print('{} pasos'.format(count))
