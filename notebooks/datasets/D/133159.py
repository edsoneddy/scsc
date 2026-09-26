casos=int(input())
for i in range(casos):
    n=input()
    c=1
    f=""
    for a in n:
        if a!=" ":
            if n=="":
                break
            if c%2==1:
                p=a.upper()
            if c%2==0:
                p=a.lower()
            c=c+1
            f=f+p
        else:
            f=f+" "
    print(f)