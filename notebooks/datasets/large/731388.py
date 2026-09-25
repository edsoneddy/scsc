t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    pe=0
    for i in range(n):
        pe+=a[i]*b[i]
    print(pe)