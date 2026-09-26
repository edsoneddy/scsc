casos=int(input())
while casos > 0:
    casos-=1
    cad=str(input())
    sw=1
    for i in range(0,len(cad)):
        if cad[i]==" ":
           print(cad[i],end="")
        else:
            if sw == 1:
               print(cad[i].upper(),end="")
               sw=0
            elif sw==0:
               print(cad[i].lower(),end="")
               sw=1
    print()
