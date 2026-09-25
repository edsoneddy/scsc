casos_prueba = int(input())
for _ in range(casos_prueba):
    n = int(input())    
    vector_A = list(map(int, input().split()))    
    vector_B = list(map(int, input().split()))    
    producto_escalar = sum(a * b for a, b in zip(vector_A, vector_B))    
    print(producto_escalar)