n=int(input())
for i in range (n):
	x=input()
	x1=len(x)
	aux=""
	z=0
	for j in range (x1):
		if (" "!=x[j]):
			if (z%2==0):
				aux+=(x[j].upper())
			else:
				aux+=(x[j].lower())
			z=z+1
		else:
			aux+=x[j]
	print(aux)
