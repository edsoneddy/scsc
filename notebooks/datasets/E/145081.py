n=int(input())
for i in range(n):
    p=int(input())
    s=0
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(p):
        s=s+a[i]*b[i]
    print(s)