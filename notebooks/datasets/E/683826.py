def producto_escalar(vector1, vector2):
    assert len(vector1) == len(vector2), "Los vectores deben tener la misma longitud"
    producto = sum(vector1[i] * vector2[i] for i in range(len(vector1)))
    
    return producto
num_casos = int(input())
for _ in range(num_casos):
    n = int(input())
    vector1 = list(map(int, input().split()))
    vector2 = list(map(int, input().split()))
    print(producto_escalar(vector1, vector2))