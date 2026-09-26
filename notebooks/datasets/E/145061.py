x=int(input())
for k in range(x):
	c=int(input())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	s=0
	for i in range(c):
		s+=a[i]*b[i]
	print(s)