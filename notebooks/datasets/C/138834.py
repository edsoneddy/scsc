t = int(input())
for i in range(t):
	n = int(input())
	ans = 0
	while(n>9):
		aux = 1
		ans += 1
		while(n>0):
			aux *= n%10
			n = n//10
		n = aux
	print(ans,'pasos')
