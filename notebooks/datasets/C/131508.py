n=int(input())
for i in range (n):
    x=int(input())
    x1=str(x)
    a=len(str(x))
    c=0
    while a>1:
        r = 1
        for d in range(0,a,1):
            t=(x1[d])
            r=r*int(t)
        c=c+1
        a=len(str(r))
        x1=str(r)
    print(c,"pasos")
