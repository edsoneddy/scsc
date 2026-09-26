t = int(input())
for _ in range(t):
    n = input().strip()
    c = 0
    if len(n) == 1:
        print(f"{c} pasos")
        continue
    while len(n) > 1:
        p = 1
        for d in n:
            p *= int(d)
        n = str(p)
        c += 1
    print(f"{c} pasos")
