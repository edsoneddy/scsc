n = int(input())
while n!=0:
    a = int(input())
    c = 0
    while a >=10:
        y = 1
        while a!=0:
            d = a%10
            y*=d
            a = a//10
        a = y
        c+=1
    print(f"{c} pasos")
    n-=1