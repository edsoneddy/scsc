n=int(input())
for i in range(n):
    cad=input()
    if (cad.isspace()):
        print (cad)
    else:
        contador=2
        for i in range (len(cad)):
            if (cad[i].isspace()):
                print(cad[i],end="")
            else:
                if (contador%2==0):
                    print(cad[i].upper(),end="")    
                    contador=contador+1
                else:
                    print(cad[i].lower(),end="")    
                    contador=contador+1
        print()