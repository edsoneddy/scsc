def multiplicar_digitos(n):
    p = 1
    while n > 0:
        p *= n % 10
        n //= 10
    return p

def contar_pasos(n):
    if n < 10:
        return 0
    p1 = 0
    while n >= 10:
        n = multiplicar_digitos(n)
        p1 += 1
    return p1

nc = int(input())
for _ in range(nc):
    n = int(input())
    p2 = contar_pasos(n)
    print(f"{p2} pasos")