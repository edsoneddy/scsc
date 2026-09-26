def pro_dig(n):
    cont = 0
    while n >= 10:
        pro = 1
        while n > 0:
            pro *= (n % 10)
            n = n // 10
        n = pro
        cont += 1

    return cont

casos=int(input())
for _ in range(casos):
    n = int(input())
    pasos = pro_dig(n)
    print(f'{pasos} pasos')