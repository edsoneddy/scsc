cas=int(input())
for i in range(cas):
	c=str(input())
	v=""
	n=0
	x=0
	for i in c:
		if i==" ":
			n+=1
			x+=1
		else:
			n=0
		if x==0 or x%2==n:
			y=str(i.upper())
			v=v+y
		else:
			y=str(i.lower())
			v=v+y
		x+=1
	print(v)