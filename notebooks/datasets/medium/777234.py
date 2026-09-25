n = int(input())
for i in range(1,n+1):
    cad = input(); bail = ""; sw = 0 #Si es 1, la letra es minuscula y 0 para mayusculas
    for i in range(0,len(cad)):
        if (cad[i] == ' '):
            bail = bail + cad[i]
        else:
            if (sw == 0):
                bail = bail + cad[i].upper()
                sw = 1
            else:
                bail = bail + cad[i].lower()
                sw = 0
    print(bail)