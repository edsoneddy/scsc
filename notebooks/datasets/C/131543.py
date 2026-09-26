n=int(input())
for i in range (n):
    x=int(input())
    a=x
    d=1
    sw=0
    c=0
    if x==0 and x<10:
        sw=1
    else:
        if x<=10:
            c=c+1
            sw=1
        else:
            while sw==0:
                while a!=0:
                    dig=a%10
                    d = d * dig
                    a=a//10
                c=c+1
                if d>=10:
                    a=d
                    d=1
                else:
                    sw=1
    print(c,'pasos')