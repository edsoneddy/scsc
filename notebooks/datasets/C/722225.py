def productos(n):
    if n == 0:
        return 0
    pasos = 0
    while n >= 10:
        producto = 1
        while n > 0:
            producto *= n % 10
            n //= 10
        n = producto
        pasos += 1
    return pasos

casos = int(input())
res = []
for _ in range(casos):
    num = int(input())
    pasos = productos(num)
    res.append(f"{pasos} pasos")
for resultado in res:
    print(resultado)