def producto_escalar(vector_a, vector_b):
    return sum(a * b for a, b in zip(vector_a, vector_b))

num_casos = int(input())

for _ in range(num_casos):
    n = int(input())
    vector_a = list(map(int, input().split()))
    vector_b = list(map(int, input().split()))
    resultado = producto_escalar(vector_a, vector_b)
    print(resultado)