# Paso 1: Leer el número de casos de prueba
num_casos = int(input())
 
# Paso 2: Para cada caso de prueba
for _ in range(num_casos):
    # Leer el número de elementos en los vectores A y B
    n = int(input())
 
    # Leer los elementos del vector A
    vector_A = list(map(int, input().split()))
 
    # Leer los elementos del vector B
    vector_B = list(map(int, input().split()))
 
    # Calcular el producto escalar
    producto_escalar = sum(a * b for a, b in zip(vector_A, vector_B))
 
    # Imprimir el producto escalar
    print(producto_escalar)
 
 
 
