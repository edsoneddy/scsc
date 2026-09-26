num_casos = int(input())
for _ in range(num_casos):
    n = int(input())
    vector_a = list(map(int, input().split()))
    vector_b = list(map(int, input().split()))
    producto_escalar = 0
    for i in range(n):
        producto_escalar += vector_a[i] * vector_b[i]
    print(producto_escalar)