def sumar_digitos(numero):
    limite = 10
    suma = 0
    while numero > 0:
        digito = numero % limite
        suma += digito
        numero //= limite
    return suma

def calcular_raiz(numero):
    limite = 10
    while numero >= limite:
        numero = sumar_digitos(numero)
    return numero

valor = int(input())
print(calcular_raiz(valor))
