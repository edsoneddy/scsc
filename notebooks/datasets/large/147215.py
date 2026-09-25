
n = int(input())
for _ in range(n):
    lon = int(input())
    v1 = list(map(int,input().split()))
    v2 = list(map(int,input().split()))
    s = 0
    k = len(v1)
    for i in range(0,k,1):
         prod = v1[i]*v2[i]
         s = prod + s
    print(s)