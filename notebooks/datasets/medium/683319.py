def convertir_a_bailarina(cadena):
    nueva_cadena = ""
    mayuscula = True
    for caracter in cadena:
        if caracter.isalpha():
            if mayuscula:
                nueva_cadena += caracter.upper()
            else:
                nueva_cadena += caracter.lower()
            mayuscula = not mayuscula
        else:
            nueva_cadena += caracter
    return nueva_cadena
T = int(input())
for _ in range(T):
    cadena = input()
    print(convertir_a_bailarina(cadena))