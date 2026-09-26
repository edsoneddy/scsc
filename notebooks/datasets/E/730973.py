def producto_escalar(vector_a, vector_b):
    return sum(a * b for a, b in zip(vector_a, vector_b))

def leer_vector(n):
    return list(map(int, input().split()))
num_casos = int(input())

for _ in range(num_casos):
    n = int(input())
    
    vector_a = leer_vector(n)
    vector_b = leer_vector(n)
    
    resultado = producto_escalar(vector_a, vector_b)
    print(resultado)