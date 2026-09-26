def contar_pasos(n):
    pasos = 0
    while n >= 10:
        producto = 1
        for digito in str(n):
            producto *= int(digito)
        n = producto
        pasos += 1
    return pasos

casos = int(input())
for _ in range(casos):
    n = int(input())
    if n == 0:
        print("0 pasos")
    else:
        print(f"{contar_pasos(n)} pasos")
