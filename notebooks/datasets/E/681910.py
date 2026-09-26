t = int(input())
for _ in range(t):
    s = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    p = sum(x * y for x, y in zip(a, b))
    print(p)