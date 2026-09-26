# Función para calcular el producto escalar de dos vectores
def producto_escalar(A, B):
    return sum(a * b for a, b in zip(A, B))

# Leer el número de casos de prueba
num_casos = int(input())

# Procesar cada caso de prueba
for _ in range(num_casos):
    # Leer el tamaño de los vectores
    n = int(input())
    
    # Leer los elementos de los vectores A y B
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # Calcular el producto escalar e imprimirlo
    resultado = producto_escalar(A, B)
    print(resultado)
