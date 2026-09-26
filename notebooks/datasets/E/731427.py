def producto_escalar(vector_a, vector_b):
    return sum(a * b for a, b in zip(vector_a, vector_b))

# Leer número de casos de prueba
num_casos = int(input())

for _ in range(num_casos):
    # Leer el número de elementos de los vectores
    n = int(input())
    
    # Leer los elementos del vector A
    vector_a = list(map(int, input().split()))
    
    # Leer los elementos del vector B
    vector_b = list(map(int, input().split()))
    
    # Calcular el producto escalar
    resultado = producto_escalar(vector_a, vector_b)
    
    # Imprimir el resultado
    print(resultado)
