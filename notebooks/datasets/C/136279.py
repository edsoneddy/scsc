t=int(input())
for i in range(t):
	n=int(input())
	res=0
	while n>9:
		nn=n
		p=1
		res+=1
		while nn>0:
			p*=(nn%10)
			nn//=10
		n=p
	
	print(res,"pasos")
