import sys

num_casos = int(sys.stdin.readline().strip())

for _ in range(num_casos):
    # Leer el número de elementos de los vectores
    n = int(sys.stdin.readline().strip())
    
    # Leer los elementos del vector A
    A = list(map(int, sys.stdin.readline().strip().split()))
    
    # Leer los elementos del vector B
    B = list(map(int, sys.stdin.readline().strip().split()))
    
    # Calcular el producto escalar
    escalar = sum(a * b for a, b in zip(A, B))
    
    print(escalar)
