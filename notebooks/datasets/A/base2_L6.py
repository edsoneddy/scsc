POTENCIA = 2

def suma_cuadrados(numero):
    total = 0
    while numero > 0:
        digito = numero % 10
        total += digito ** POTENCIA
        numero //= 10
    return total

def es_feliz(numero):
    vistos = set()
    while numero != 1 and numero not in vistos:
        vistos.add(numero)
        numero = suma_cuadrados(numero)
    return numero == 1

casos = int(input())
for _ in range(casos):
    numero_str = input()
    if es_feliz(int(numero_str)):
        print("Feliz")
    else:
        print("Triste")
