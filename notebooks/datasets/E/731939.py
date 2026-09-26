x = int(input())
for _ in range(x):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    res = 0
    for i in range(n):
        res = res + A[i] * B[i]
    print(res)