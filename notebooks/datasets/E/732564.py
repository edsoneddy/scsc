t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = sum(A[i] * B[i] for i in range(n))
    print(result)
