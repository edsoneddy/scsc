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

casos = int(input())

for _ in range(casos):
    numero = int(input())
    pasos = contar_pasos(numero)
    print(f"{pasos} pasos")
