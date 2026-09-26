n=int(input())
for i in range(n):
    dat=int(input())
    c=0
    while dat>9:
        k=dat
        mult=1
        while k>0:
            d=k%10
            mult*=d
            k//=10
        dat=mult
        c+=1
    print (f"{c} pasos")