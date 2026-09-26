# Función para calcular el producto escalar de dos vectores
def producto_escalar(A, B):
    return sum(a * b for a, b in zip(A, B))

# Leer el número de casos de prueba
casos_prueba = int(input())

# Para cada caso de prueba
for _ in range(casos_prueba):
    # Leer el tamaño de los vectores
    n = int(input())
    
    # Leer los elementos de los vectores A y B
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # Calcular y imprimir el producto escalar
    print(producto_escalar(A, B))