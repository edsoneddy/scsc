m = int(input(""))

for _ in range(m):
    n = int(input(""))
    iteraciones = 0

    while n >= 10:
        producto = 1
        while n > 0:
            producto *= n % 10
            n //= 10
        n = producto
        iteraciones += 1

    print(f"{iteraciones} pasos")