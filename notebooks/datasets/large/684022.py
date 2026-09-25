def producto_escalar(vector_A, vector_B):
    # Verificar si ambos vectores tienen la misma longitud
    if len(vector_A) != len(vector_B):
        return "Los vectores deben tener la misma longitud"
    
    # Calcular el producto escalar
    resultado = sum(a * b for a, b in zip(vector_A, vector_B))
    return resultado

# Leer el número de casos de prueba
num_casos = int(input())

# Iterar sobre cada caso de prueba
for _ in range(num_casos):
    # Leer la longitud de los vectores
    n = int(input())
    
    # Leer los elementos de los vectores
    vector_A = list(map(int, input().split()))
    vector_B = list(map(int, input().split()))
    
    # Calcular y imprimir el producto escalar
    print(producto_escalar(vector_A, vector_B))