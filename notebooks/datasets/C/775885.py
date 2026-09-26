t = int(input())

for _ in range(t):
    n = int(input())  

    pasos = 0

    while n >= 10:
        producto = 1
        for digito in str(n):
            producto *= int(digito)
        n = producto
        pasos += 1

    print(f"{pasos} pasos")