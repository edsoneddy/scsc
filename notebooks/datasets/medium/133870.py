a=int(input())
for c in range (1,a+2):
    d=input()
    d=d.lower()
    x=0
    y=""
    for b in d:
        x=x+1
        if b==" ":
            x=x-1
        elif x%2!=0:
            b=b.upper()
        y=y+b
    print(y)