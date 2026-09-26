o=int(input())
for i in range(o):
	c=str(input())
	vacío=""
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
			vacío=vacío+y
		else:
			y=str(i.lower())
			vacío=vacío+y
		x+=1
	print(vacío)