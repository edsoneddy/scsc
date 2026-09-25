n=int(input())
for i in range(n):
    R=0
    N=int(input())
    a=input().split()
    b=input().split()
    for y in range(N):
        r=int(a[y])*int(b[y])
        R=r+R
    print(R)