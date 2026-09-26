t = int(input())
for _ in range(t):
    n = int(input())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    r = 0
    for i in range(n):
        r += v1[i] * v2[i]
    print(r)