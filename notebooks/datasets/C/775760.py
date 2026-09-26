def contar_pasos(n):
    if n < 10:
        return 0

    pasos = 0
    while n >= 10:
        producto = 1
        for digito in str(n):
            producto *= int(digito)
        n = producto
        pasos += 1
    return pasos

C = int(input())
for _ in range(C):
    n = int(input())
    print(f"{contar_pasos(n)} pasos")