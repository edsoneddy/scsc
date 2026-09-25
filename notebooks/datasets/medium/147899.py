n=int(input())
for j in range(n):
    a=str(input())
    s=""
    g=0
    for i in range(len(a)):
        if a[i]!=" ":
            g=g+1
        if g%2!=0:
            s=s+a[i].upper()
        else:
            s=s+a[i].lower()
    print(s)


