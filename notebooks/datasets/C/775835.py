t = int(input())
for _ in range(t):
    n = int(input())
    contador = 0

    while n >= 10:  
        producto = 1
        for digito in str(n):  
            producto *= int(digito)  
        n = producto 
        contador += 1

    print(f"{contador} pasos")
