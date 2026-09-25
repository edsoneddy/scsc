c=int(input())
for i in range(c):
    a=str(input())
    s=""
    n=0
    x=0
    for i in a:
        if i==" ":
            n=n+1
            x=x+1
        else:
            n=0
        if x==0 or x%2==n:
            y=str(i.upper())
            s=s+y
        else:
            y=str(i.lower())
            s=s+y
        x=x+1
    print(s)

