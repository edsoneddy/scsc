n=int(input())
i=1
a=0
while i<=n:
    x=int(input())
    c=0
    if x>9:
        while x>9:
            p=1
            while x>0:
                d=x%10
                p=p*d
                x=x//10
            x=p
            c+=1
        else:
            print(c,"pasos")
    else:
        print(a,"pasos")
    i+=1