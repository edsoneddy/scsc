def multiplicar_digitos(n):
    producto = 1
    while n > 0:
        digito = n % 10
        producto *= digito
        n //= 10
    return producto

num_casos = int(input())
for _ in range(num_casos):
    n = int(input())
    iteraciones = 0
    if n < 10:
        print(f"{n} pasos")
        continue

    while n >= 10:
        n = multiplicar_digitos(n)
        iteraciones += 1

    print(f"{iteraciones} pasos")