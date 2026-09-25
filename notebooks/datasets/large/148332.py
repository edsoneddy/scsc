caso_prueba = int(input())


for i in range(caso_prueba):
	elementos = int(input())
	sum = 0
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))

	for k in range(elementos):
		sum = sum + (A[k]*B[k])
	print(sum)
