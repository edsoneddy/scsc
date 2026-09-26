n=int(input())
for i in range(1,n+1):
    cad=input()
    bai=""
    sw=0
    for i in range(0,len(cad)):
        if(cad[i]==' '):
            bai+=cad[i]
        else:
            if(sw==0):
                bai+=cad[i].upper()
                sw=1
            else:
                bai+=cad[i].lower()
                sw=0
    print(bai)    
