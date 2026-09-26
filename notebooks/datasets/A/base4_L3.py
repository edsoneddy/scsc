def calcular_raiz(numero):
    limite = 10
    while numero >= limite:
        suma = 0
        while numero > 0:
            digito = numero % limite
            suma += digito
            numero //= limite
        numero = suma
    return numero

valor = int(input())
print(calcular_raiz(valor))
