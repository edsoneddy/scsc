def multiplicar_digitos(n):
    pasos = 0
    while n >= 10:
        producto = 1
        for digito in str(n):
            producto *= int(digito)
        n = producto
        pasos += 1
    return pasos

casos_prueba = int(input())
pasos_lista = []

for _ in range(casos_prueba):
    numero = int(input())
    if numero == 0:
        pasos_lista.append(f"{numero} pasos")
    else:
        pasos_lista.append(f"{multiplicar_digitos(numero)} pasos")

for pasos in pasos_lista:
    print(pasos)
