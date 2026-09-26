for _ in range(int(input())):
    n = input().strip()
    if len(n) == 1:
        print("0 pasos")
        continue
    p = 0
    while len(n) > 1:
        m = 1
        for i in n: m *= int(i)
        n = str(m)
        p += 1
    print(f"{p} pasos")