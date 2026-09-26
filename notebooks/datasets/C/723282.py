def multiplicar_digitos(n):
    resultado = 1
    while n > 0:
        resultado *= n % 10
        n //= 10
    return resultado

casos = int(input())
for _ in range(casos):
    numero = input().strip()
    if numero == "0":
        print("0 pasos")
        continue

    iteraciones = 0
    while len(numero) > 1:
        numero = str(multiplicar_digitos(int(numero)))
        iteraciones += 1

    print(f"{iteraciones} pasos")
