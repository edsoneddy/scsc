def calcular_pasos(num):
    cnt = 0
    while num > 9:
        sequence = 1
        while num > 0:
            dig = num % 10
            sequence *= dig
            num //= 10
        num = sequence
        cnt += 1
    return cnt

t = int(input())
for _ in range(t):
    num = int(input())
    pasos = calcular_pasos(num)
    print(pasos,"pasos")