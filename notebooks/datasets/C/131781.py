n=int(input())
for i in range(n):
    b=int(input())
    p=0
    if b>9:
        while b>9:
            s=1
            while b>0:
                d=b%10
                s=s*d
                b=b//10
            b=s
            p=p+1
        else:
            print(p,"pasos")
    else:
        print("0 pasos")