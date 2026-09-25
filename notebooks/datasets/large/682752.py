t = int(input().strip())

resultados = []

for _ in range(t):
    n = int(input().strip())

    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    prodscl = sum(A[i] * B[i] for i in range(n))

    resultados.append(prodscl)

for resultado in resultados:
    print(resultado)
