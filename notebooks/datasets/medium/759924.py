n = int(input())
for i in range(n):
    cadena = input()
    resultado = ''
    contador = 0

    for letra in cadena:
        if letra != ' ':
            if contador % 2 == 0:
                resultado = resultado + letra.upper()
            else:
                resultado = resultado + letra.lower()
            contador = contador + 1
        else:
            resultado = resultado + ' '

    print(resultado)