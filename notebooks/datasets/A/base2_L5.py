POTENCIA = 2

def suma_cuadrados(numero_str):
    total = 0
    for pos in range(len(numero_str)):
        digito = int(numero_str[pos])
        total = total + digito ** POTENCIA
    return total

casos = int(input())
for i in range(casos):
    numero_str = str(input())
    suma = 0
    for _ in range(1000):
        suma = suma_cuadrados(numero_str)
        if len(str(suma)) == 1:
            break
        numero_str = str(suma)
    if suma == 1:
        print("Feliz")
    else:
        print("Triste")
