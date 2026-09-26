# Leer el número de casos de prueba
t = int(input().strip())

# Iterar a través de cada caso de prueba
for _ in range(t):
    # Leer el número de elementos del vector
    n = int(input().strip())
    
    # Leer los elementos del vector A
    A = list(map(int, input().split()))
    
    # Leer los elementos del vector B
    B = list(map(int, input().split()))
    
    # Calcular el producto escalar
    producto_escalar = sum(a * b for a, b in zip(A, B))
    
    # Imprimir el resultado
    print(producto_escalar)