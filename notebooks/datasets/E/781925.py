casos = int(input())

for i in range(casos):
    n = int(input())

    linea_a = input()
    A = linea_a.split()
    for j in range(n):
        A[j] = int(A[j])

    linea_b = input()
    B = linea_b.split()
    for j in range(n):
        B[j] = int(B[j])

    producto = 0
    for j in range(n):
        producto = producto + A[j] * B[j]

    print(producto)