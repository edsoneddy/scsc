num_casos = int(input().strip())

for _ in range(num_casos):
    n = int(input().strip())
    vector_a = list(map(int, input().strip().split()))
    vector_b = list(map(int, input().strip().split()))
    producto_escalar = sum(a * b for a, b in zip(vector_a, vector_b))
    print(producto_escalar)
