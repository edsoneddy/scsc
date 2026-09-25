x=int(input())
for i in range(x):
    c=0
    cad=input()
    s=cad[0].upper()
    for j in range(1,len(cad)):
        if cad[j]!=' ':
            c=c+1
            if c%2==1:
                s+=cad[j].lower()
            else:
                s+=cad[j].upper()
        else:
            s+=' '
    print(s)      