casos=int(input())
for j in range(casos):
    cadena=input()
    newcad=""
    sw=True
    for i in range(len(cadena)):
        if cadena[i]==" ":
            newcad+=" "
            continue
        elif sw: newcad+= cadena[i].upper()
        else: newcad+= cadena[i].lower()
        sw = not sw
    print(newcad)