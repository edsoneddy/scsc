t = int(input())
for _ in range(t):
    n = input().strip()
    if len(n) == 1:
        print("0 pasos")
        continue

    pasos = 0
    while len(n) > 1:
        prod = 1
        for d in n:
            prod *= int(d)
        n = str(prod)
        pasos += 1

    print(f"{pasos} pasos")