def explorer(cadena):

    cad = ""

    i = -1

    for caracter in cadena:
        if caracter != ' ':
            i += 1

            if i % 2 == 0:
                cad = cad + caracter.upper()
            else:
                cad = cad + caracter.lower()

        else:
            cad = cad + ' '

    print(cad)


t = int(input())
for _ in range(t):
    cadena = input()
    explorer(cadena)
            
