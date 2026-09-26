for _ in range(int(input())):
    n = input()
    c = 0
    while len(n) > 1:
        p = 1
        for d in n: p *= int(d)
        n = str(p)
        c += 1
    print(f"{c} pasos")    