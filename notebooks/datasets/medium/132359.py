n=int(input())
for i in range(n):
    k=str(input())
    k=k.lower()
    s=''
    j=0
    for i in k:

        if j%2==0 and i!=' ':
            s=s+i.upper()
            j=j+1
        elif i==' ':
            s=s+i
        else:
            s=s+i
            j=j+1
    print(s)