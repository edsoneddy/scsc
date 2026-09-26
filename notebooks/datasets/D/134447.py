c=int(input())
for i in range(c):
    a=input()
    s=""
    b=0
    x=0
    for j  in a:
        if j==" ":
            b=b+1
            x=x+1
        else:
            b=0
        if x==0 or x%2==0:
            d=j.upper()
            s=s+d
        else:
            d=j.lower()
            s=s+d
        x=x+1
    print(s)