def contar_pasos(n):
    if n < 10:
        return 0
    pasos = 0
    while n >= 10:
        producto = 1
        for d in str(n):
            producto *= int(d)
        n = producto
        pasos += 1
    return pasos

t = int(input())

for _ in range(t):
    n = int(input())
    print(f"{contar_pasos(n)} pasos")