n=int(input())
for j in range(n):
    s=0
    m=int(input())
    l=list(map(int,input().split()))
    k=list(map(int,input().split()))
    for i in range(m):
        d=l[i]*k[i]
        s=s+d
    print(s)
    s=0