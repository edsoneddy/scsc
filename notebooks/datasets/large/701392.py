t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    v = list(map(int,input().split()))[:n]
    v1 = list(map(int,input().split()))[:n]
    sum=0
    for i in range(n):
        sum=v[i]*v1[i]+sum            
    print(sum)
