n=int(input())
for i in range (n):
    num=int(input())
    s=0
    c=0
    a=num
    d=1
    if num==0 and num<10:
        s=1
    else:
        if num<=10:
            c=c+1
            s=1
        else:
            while s==0:
                while a!=0:
                    dig=a%10
                    d = d * dig
                    a=a//10
                c=c+1
                if d>=10:
                    a=d
                    d=1
                else:
                    s=1
    print(c,'pasos')
