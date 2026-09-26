w=int(input())
for v in range (1,w+1):
    a=input()
    x=0
    z=" pasos"
    while(1>0):
        c=1
        a=int(a)
        if(a<10):
            x=str(x)
            y=x+z
            print(y)
            break
        else:
            a=str(a)
            for b in a:
                b=int(b)
                c=c*b
                a=c
            x=x+1
