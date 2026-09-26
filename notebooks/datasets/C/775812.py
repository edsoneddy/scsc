def pasos(n):
    c = 0
    while n >= 10:
        p = 1
        for d in str(n):
            p *= int(d)
        n = p
        c += 1
    return c

t = int(input())
for _ in range(t):
    x = int(input())
    print(f"{pasos(x)} pasos")