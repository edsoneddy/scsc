casos=int(input())
for i in range(casos):

	n=int(input())
	pasos=0

	while n > 9:
		n2=n
		prod = 1
		while n2>0:
			dig=n2%10
			prod=prod*dig
			n2=n2//10

		pasos+=1
		n=prod

	print(f"{pasos} pasos")