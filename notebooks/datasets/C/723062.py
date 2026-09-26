m= int(input())
for _ in range(m):
    n = int(input())
    iteraciones = 0  
    while n >= 10:
        producto = 1  
        while n > 0:
            digito = n % 10  
            producto *= digito  
            n //= 10  

        n = producto  
        iteraciones += 1  
    print(iteraciones,"pasos")
 