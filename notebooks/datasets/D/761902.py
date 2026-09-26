n1=int(input())    
lp=[]
for i in range(n1):
    cadena=input()
    newcad=""
    cont=0
    for i in range(len(cadena)):
        if (cadena[i]!=" "):
            if(cont==0):
                caracter=cadena[i].upper()
                newcad=newcad+caracter
                cont=1
            else:
                caracter=cadena[i].lower()
                newcad=newcad+caracter
                cont=0
        else:
            
            newcad=newcad+" "
    lp.append(newcad)

for linea in lp:
    print(linea)

