def producto_escalar(vector1, vector2):
    if len(vector1) != len(vector2):
        return None  
    
    producto = 0
    for i in range(len(vector1)):
        producto += vector1[i] * vector2[i]
    
    return producto
 
casos = int(input())
 
for _ in range(casos):
 
    n = int(input())
 
    vector1 = list(map(int, input().split()))
 
    vector2 = list(map(int, input().split()))
 
    resultado = producto_escalar(vector1, vector2)
 
    print(resultado)