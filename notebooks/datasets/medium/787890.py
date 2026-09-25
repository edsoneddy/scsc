n=int(input())
for i in range(n):
    cadena=input()
    nueva_cadena=""
    mayuscula = True
    for char in cadena:

        if char==" ":
            nueva_cadena=nueva_cadena+" "
        elif mayuscula:
            nueva_cadena=nueva_cadena+char.upper()
            mayuscula=False
        else:
            mayuscula = True
            nueva_cadena=nueva_cadena+char.lower()
    print(nueva_cadena)
