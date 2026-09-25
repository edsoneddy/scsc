n=int(input())
for i in range(1,n+1):
    cad=input()
    bailarina=""
    sw=0
    for i in range(0,len(cad)):
        if cad[i]==' ':
            bailarina=bailarina+cad[i]
        else:
            if sw==0:
                bailarina=bailarina+cad[i].upper()
                sw=1
            else:
                bailarina=bailarina+cad[i].lower()
                sw=0
    print(bailarina)