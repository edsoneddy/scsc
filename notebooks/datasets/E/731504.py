# Leer el número de casos de prueba
num_casos = int(input())

# Procesar cada caso de prueba
for _ in range(num_casos):
    # Leer el número de elementos del vector
    n = int(input())
    
    # Leer los elementos del vector A
    A = list(map(int, input().split()))
    
    # Leer los elementos del vector B
    B = list(map(int, input().split()))
    
    # Calcular el producto escalar
    producto_escalar = sum(A[i] * B[i] for i in range(n))
    
    # Imprimir el resultado
    print(producto_escalar)
