n=int(input())
for i in range(n):
    s=0
    t=int(input())
    a=input().split()
    b=input().split()
    for j in range(t):
        s=s+(int(a[j])*int(b[j]))
    print(s)