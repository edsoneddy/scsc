p=int(input())
for i in range(p):
	c=str(input())
	a=""
	n=0
	x=0
	for i in c:
		if i==" ":
			n=n+1
			x=x+1
		else:
			n=0
		if x==0 or x%2==n:
			y=str(i.upper())
			a=a+y
		else:
			y=str(i.lower())
			a=a+y
		x=x+1
	print(a)
					