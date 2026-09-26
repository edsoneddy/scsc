
while 1:
    nc=int(input())
    for j in range(nc):
        n=int(input())
        c=0
        if n>9:
            while 1:
                p=1
                while n>0:
                    ud=n%10
                    p=p*ud
                    n=n//10
                c+=1
                if p<10:
                   break
                else:
                    n=p

            print(c,"pasos")
        else:
            print(0, "pasos")




