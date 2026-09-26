def multiplicar_digitos(num):
    pasos = 0
    while num >= 10:  
        producto = 1
        while num > 0:
            digito = num % 10  
            producto *= digito  
            num //= 10  
        num = producto  
        pasos += 1  
    return pasos    

casos=int(input())
for i in range (casos):
    num = int(input()) 
    resultado = multiplicar_digitos(num)
    print(f"{resultado} pasos")  
