a= int(input())
for _ in range(a):
    n = input().strip() 
    pasos = 0  
    while len(n) > 1:
        producto = 1
        for digito in n:
            producto *= int(digito)
        n = str(producto)
        pasos = pasos+1  
    print(f"{pasos} pasos")