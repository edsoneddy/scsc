n=int(input())
for i in range(1,n+1):
    s=0
    m=int(input())
    l=list(map(int,input().split()))
    k=list(map(int,input().split()))
    for j in range(m):
        d=l[j]*k[j]
        s=s+d
    print(s)
    s=0
