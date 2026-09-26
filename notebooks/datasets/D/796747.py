n=int(input(""))
for i in range(0,n):
    cadena=input("")
    i=i+1
    contador=0
    cadnueva=""
    for letra in cadena:
        if letra != " ":
            if contador % 2 == 0:
                cadnueva+= letra.upper()
            else:
                cadnueva+=letra.lower()
            contador+=1
        else:
            cadnueva+=" "
    print(cadnueva)