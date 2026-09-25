n = int(input())
for _ in range(n):
    tam = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    producto_escalar = sum(a * b for a, b in zip(A, B))
    print(producto_escalar)
