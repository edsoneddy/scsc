n=int(input())
for i in range(n):
    m=int(input())
    r=0
    for y in range(1):
        a=input().split()
        b=input().split()
        for x in range(m):
            r=int(a[x])*int(b[x])+r
        print(r)