y=int(input())
for i in range (y):
    n=int(input())
    s=0
    cont=0
    b=n
    y=1
    if n==0 and n<10:
        s=1
    else:
        if n<=10:
            cont=cont+1
            s=1
        else:
            while s==0:
                while b!=0:
                    g=b%10
                    y=y*g
                    b=b//10
                cont=cont+1
                if y>=10:
                    b=y
                    y=1
                else:
                    s=1
    print(cont,"pasos")