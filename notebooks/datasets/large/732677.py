def producto_escalar(A, B):
    return sum(a * b for a, b in zip(A, B))

casos_prueba = int(input())

for _ in range(casos_prueba):
    n = int(input())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(producto_escalar(A, B))