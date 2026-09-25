import sys

input = sys.stdin.read
data = input().strip().splitlines()

n_cases = int(data[0])
index = 1

resultados = []

for _ in range(n_cases):
    tamaño = int(data[index])
    index += 1
    A = list(map(int, data[index].split()))
    index += 1
    B = list(map(int, data[index].split()))
    index += 1

    producto_escalar = sum(a * b for a, b in zip(A, B))
    resultados.append(producto_escalar)

for resultado in resultados:
    print(resultado)
