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
    terminado = 0
    longitud = len(numero_str)
    while terminado != 1:
        suma = suma_cuadrados(numero_str)
        longitud = len(str(suma))
        if longitud == 1:
            terminado = 1
        else:
            numero_str = str(suma)
    if int(suma) == 1:
        print("Feliz")
    else:
        print("Triste")
