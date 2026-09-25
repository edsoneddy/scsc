T = int(input())
for i in range(T):
    cadena = input()
    nueva_cadena = ""
    usar_mayuscula = True

    for letra in cadena:
        if letra.isalpha():
            if usar_mayuscula:
                nueva_cadena += letra.upper()
            else:
                nueva_cadena += letra.lower()
            usar_mayuscula = not usar_mayuscula
        else:
            nueva_cadena += letra

    print(nueva_cadena)