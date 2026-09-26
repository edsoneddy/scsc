def calcular_raiz(numero):
    if numero == 0:
        return 0
    resto = numero % 9
    return 9 if resto == 0 else resto

valor = int(input())
print(calcular_raiz(valor))
