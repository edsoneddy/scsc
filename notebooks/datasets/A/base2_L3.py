POTENCIA = 2
casos = int(input())  # cantidad de casos
for i in range(casos):
    numero_str = str(input())  # numero como texto
    terminado = 0
    longitud = len(numero_str)
    while terminado != 1:
        suma = 0
        for pos in range(longitud):
            digito = int(numero_str[pos])
            suma = suma + digito ** POTENCIA
        longitud = len(str(suma))
        if longitud == 1:
            terminado = 1
        else:
            numero_str = str(suma)
    if int(suma) == 1:
        print("Feliz")
    else:
        print("Triste")
