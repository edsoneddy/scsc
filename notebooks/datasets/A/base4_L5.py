def sumar_digitos(numero):
    return sum(int(c) for c in str(numero))

def calcular_raiz(numero):
    while numero >= 10:
        numero = sumar_digitos(numero)
    return numero

valor = int(input())
print(calcular_raiz(valor))
