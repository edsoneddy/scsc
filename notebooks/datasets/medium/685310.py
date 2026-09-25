def convertir_a_bailarina(cadena):
    nueva_cadena = ""
    mayuscula = True
    for letra in cadena:
        if letra.isalpha():
            if mayuscula:
                nueva_cadena += letra.upper()
            else:
                nueva_cadena += letra.lower()
            mayuscula = not mayuscula
        else:
            nueva_cadena += letra
    return nueva_cadena
T = int(input(""))
for _ in range(T):
    cadena = input("")
    print(convertir_a_bailarina(cadena))
