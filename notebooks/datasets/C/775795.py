casos = int(input())

for _ in range(casos):
    numero = input().strip()
    if len(numero) == 1:
        print("0 pasos")
        continue

    pasos = 0
    while len(numero) > 1:
        prod = 1
        for digito in numero:
            prod *= int(digito)
        numero = str(prod)
        pasos += 1

    print(f"{pasos} pasos")

