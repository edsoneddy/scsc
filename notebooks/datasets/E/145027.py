cas=int(input())
while cas>0:
    n=int(input())
    a=tuple(map(int,input().split()))
    b=tuple(map(int,input().split()))
    s=0
    for i in range(n):
        s=s+a[i]*b[i]
    print(s)
    cas-=1
