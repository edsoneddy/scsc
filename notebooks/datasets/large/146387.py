n=int(input())
for i in range(n):
    s=int(input())
    a=tuple(input().split())
    b = tuple(input().split())
    m=1
    r=0
    for i in range(0,s,1):
        m=int(a[i])*int(b[i])
        r=r+m
    print(r)