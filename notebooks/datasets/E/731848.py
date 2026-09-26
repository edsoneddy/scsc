# Función para calcular el producto escalar de dos vectores
def dot_product(A, B):
    return sum(a * b for a, b in zip(A, B))

# Leer el número de casos de prueba
num_cases = int(input())

# Procesar cada caso de prueba
for _ in range(num_cases):
    # Leer el número de elementos del vector
    n = int(input())
    
    # Leer los elementos del vector A
    A = list(map(int, input().split()))
    
    # Leer los elementos del vector B
    B = list(map(int, input().split()))
    
    # Calcular el producto escalar y mostrarlo
    print(dot_product(A, B))
