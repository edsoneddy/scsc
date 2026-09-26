n=int(input())
for _ in range(n):
    x=int(input())
    pas=0
    while(x>9):
        pro=1
        while(x!=0):
            d=x%10
            x=x//10
            pro=pro*d
        x=pro
        pas=pas+1
    print(pas,"pasos")