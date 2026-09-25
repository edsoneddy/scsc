n=int(input())
for i in range(1,n+1):
    cad=input()
    baile="";
    sw=0
    for j in range(0, len(cad)):
        if(cad[j]==' '):
            baile=baile+cad[j]
        else:
            if(sw==0):
                baile=baile+cad[j].upper()
                sw=1
            else:
                baile = baile + cad[j].lower()
                sw = 0
    print(baile)