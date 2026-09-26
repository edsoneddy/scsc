num_casos = int(input())

for _ in range(num_casos):
    longitud = int(input())
    vector_a = list(map(int, input().split()))
    vector_b = list(map(int, input().split()))
    producto_escalar = sum(a * b for a, b in zip(vector_a, vector_b))
    print(producto_escalar)