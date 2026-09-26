def multiplicar_dígitos(n):
    res = 1
    while n > 0:
        res *= n % 10
        n //= 10
    return res
t = int(input())
for _ in range(t):
    n = int(input())
    if n < 10:
        print("0 pasos")
    else:
        pasos = 0
        while n >= 10:
            n = multiplicar_dígitos(n)
            pasos += 1
        print(f"{pasos} pasos")