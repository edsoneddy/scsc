def producto_escalar(A, B):
    if len(A) != len(B):
        return None  
    else:
        resultado = 0
        for i in range(len(A)):
            resultado += A[i] * B[i]
        return resultado

casos = int(input())


for _ in range(casos):
 
    longitud = int(input())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
  
    resultado = producto_escalar(A, B)
    print(resultado)
