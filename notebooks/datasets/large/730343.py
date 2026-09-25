t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=0
    for i in range(n):
        ans+=a[i]*b[i]
    print(ans)