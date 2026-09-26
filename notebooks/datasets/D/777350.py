n=int(input())
for j in range(1,n+1):
    cad=input()
    ba=""
    sw=0
    for i in range (0, len(cad)):
        if (cad[i]==" "):
            ba=ba+cad[i]
        else:
            if (sw==0):
                ba=ba+cad[i].upper()
                sw=1
            else:
                ba=ba+cad[i].lower()
                sw=0
    print(ba)