n_c = int(input())
for _ in range(n_c):
    n = int(input())
    iteraciones = 0
    while n >= 10:
        producto = 1
        for digito in str(n):
            producto *= int(digito)
        n = producto
        iteraciones += 1
    print(f"{iteraciones} pasos")