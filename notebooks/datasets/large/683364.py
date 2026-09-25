nc = int(input())

for _ in range(nc):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    pe = sum(a * b for a, b in zip(A, B))
    print(pe)