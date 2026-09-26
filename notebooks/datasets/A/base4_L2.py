def calcular_raiz(numero):
    while numero >= 10:
        suma = 0
        while numero > 0:
            suma += numero % 10
            numero //= 10
        numero = suma
    return numero

valor = int(input())
print(calcular_raiz(valor))
