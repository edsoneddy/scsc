n=int(input())
for j in range(1,n+1):
    cad=input()
    bl=""
    sw=0 #Mayusculas 0 Min 1
    for i in range(0,len(cad)):
        if (cad[i]==" ") :
            bl=bl+cad[i]
        else:
            if sw==0:
                bl=bl+cad[i].upper();sw=1
            else:
                bl=bl+cad[i].lower()
                sw=0
    print(bl)