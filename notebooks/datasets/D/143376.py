def cambio(cad):
    c=-1
    s=""
    for i in range (len(cad)):
        if(cad[i]!=" "):
            if(c==-1):
                s=s+(cad[i].upper())
                c=c*(-1)
            else:
                s=s+(cad[i].lower())
                c=c*(-1)
        else:
            s=s+" "
    print(s)
n=int(input(""))
for i in range(n):
    cad=str(input(""))
    cambio(cad)
