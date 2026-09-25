times=int(input())
for i in range(times):
    min_may=True
    cadena=input()
    nueva_cadena=""
    for caracter in cadena:
        if caracter.isalpha():
            if min_may:
                nueva_cadena+=caracter.upper()
                min_may=False
            else:
                nueva_cadena+=caracter.lower()
                min_may=True
        else:
            nueva_cadena+=caracter
    print(nueva_cadena)
