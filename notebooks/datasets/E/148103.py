casos = int(input())
for i in range(casos):
    t = int(input())
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    p = 0
    for j in range(t):
        p += (a[j] * b[j])
    print(p)