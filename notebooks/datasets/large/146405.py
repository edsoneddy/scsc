k=int(input())
for k in range(k):
    n=int(input())
    a=input().split()
    b=input().split()
    s=0
    for i in range(n):
        y=int(a[i])*int(b[i])
        s=s+y
    print(s)