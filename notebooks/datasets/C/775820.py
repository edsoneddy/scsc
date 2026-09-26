t = int(input())
for _ in range(t):
    num = input().strip()
    if len(num) == 1:
        print("0 pasos")
    else:
        pasos = 0
        while len(num) > 1:
            prod = 1
            for d in num:
                prod *= int(d)
            num = str(prod)
            pasos += 1
        print(f"{pasos} pasos")
