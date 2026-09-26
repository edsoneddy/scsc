n=int(input())
for i in range (n):
    num=int(input())
    s=0
    contador=0
    nn=num
    d=1
    if num==0 and num<10:
        s=1
    else:
        if num<=10:
            contador=contador+1
            s=1
        else:
            while s==0:
                while nn!=0:
                    digito=nn%10
                    d = d * digito
                    nn=nn//10
                contador=contador+1
                if d>=10:
                    nn=d
                    d=1
                else:
                    s=1
    print(contador,'pasos')
