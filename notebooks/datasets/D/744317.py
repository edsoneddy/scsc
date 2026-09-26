def convertir_a_bailarina(cadena):
    if not cadena:
        return ""
    resultado = []
    mayuscula_siguiente = True
    for char in cadena:
        if char == ' ':
            resultado.append(char)
            continue
        if mayuscula_siguiente:
            resultado.append(char.upper())
        else:
            resultado.append(char.lower())
        mayuscula_siguiente = not mayuscula_siguiente
    return ''.join(resultado)



T = int(input())
for _ in range(T):
    cadena = input()
    resultado = convertir_a_bailarina(cadena)
    print(resultado)
