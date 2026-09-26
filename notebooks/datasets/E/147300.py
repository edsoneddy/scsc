cas=int(input())
while cas>0:
	l=int(input())
	s=0
	a=list(tuple(map(int,input().split())))
	b=list(tuple(map(int,input().split())))
	for i in range(l):
		s=s+a[i]*b[i]
	print(s)
	cas-=1