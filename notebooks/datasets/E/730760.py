def prodEsc(vx,vy,n):
    ps = 0
    for i in range(n):
        ps += vx[i]*vy[i]
    return ps

t = int(input())
for i in range(t):
    n = int(input())
    vx = list(map(int,input().split()))
    vy = list(map(int,input().split()))
    print(prodEsc(vx,vy,n))

