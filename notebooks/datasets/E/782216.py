t=int(input())
for i in range(t):
    m=int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    s=0
    for j in range(m):
        s=s+x[j]*y[j]
    print(s)