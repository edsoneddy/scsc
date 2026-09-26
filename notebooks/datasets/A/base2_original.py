n=int(input())
for i in range(n):
    x=str(input())
    m=len(x)
    r=0
    while r!=1:
        s=0
        for g in range(m):
            z=int(x[g])
            s=s+z**2
        m=len(str(s))
        if m==1:
            r=1
        else:
            x=str(s)
    if int(s)==1:
        print("Feliz")
    else:
        print("Triste")
