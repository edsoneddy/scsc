x=int(input())
for i in range (x):
    n=int(input())
    s=0
    cont=0
    a=n
    x=1
    if n==0 and n<10:
        s=1
    else:
        if n<=10:
            cont=cont+1
            s=1
        else:
            while s==0:
                while a!=0:
                    g=a%10
                    x=x*g
                    a=a//10
                cont=cont+1
                if x>=10:
                    a=x
                    x=1
                else:
                    s=1
    print(cont,"pasos")