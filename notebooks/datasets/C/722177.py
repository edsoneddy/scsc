n_c = int(input())
for _ in range(n_c):
    n = int(input())
    interacccion = 0
    while n >= 10:
        product = 1
        for dig in str(n):
            product *= int(dig)
        n = product
        interacccion += 1
    print(f"{interacccion} pasos")