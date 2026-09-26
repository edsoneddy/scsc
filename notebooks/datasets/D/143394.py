n=int(input())
for i in range(n):
    cad=input()
    s=""
    c=-1
    for j in range (len(cad)):
        if(cad[j]!=" "):
            if(c==-1):
                s=s+cad[j].upper()
            else:
                s=s+cad[j].lower()
            c=c*-1
        else:
            s=s+cad[j]
    print(s)