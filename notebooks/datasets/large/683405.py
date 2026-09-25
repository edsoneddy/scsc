n=int(input())
for i in range(1,n+1,1):
    s=0
    a=int(input())
    v1=list(map(int, input().split()))
    v2=list(map(int, input().split()))
    for j in range(a):
        m=v1[j]*v2[j]
        s=s+m
    print(s)