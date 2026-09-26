n=int(input())
for i in range(n):
    cad=input()
    x=len(cad)
    i=0
    s=""
    y=0
    while i<x:
        if(cad[i]!=" "):
            if (y==0):
                v=cad[i].upper()
                s=s+v
                y=1
            else:
                v=cad[i].lower()
                s=s+v
                y=0
        else:
            v=" "
            s=s+v
        i=i+1
    print (s)
    i=0
    s=""