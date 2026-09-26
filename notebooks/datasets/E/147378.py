cp=int(input())
y=0
c=0
for i in range (cp):
	a=int(input())
	v=list(map(int,input().split()))
	w=list(map(int,input().split()))
	for j in range(a):
		y=y+(v[j]*w[j])
		c=c+1
	print(y)
	if c > (a-1):
		y=0
		c=0