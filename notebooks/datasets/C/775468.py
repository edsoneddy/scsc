def multiplicar_digitos(num):
    producto = 1
    while num > 0:
        digito = num % 10
        producto *= digito
        num //= 10
    return producto

t = int(input())
for _ in range(t):
    n = int(input())
    pasos = 0
    while n >= 10:
        n = multiplicar_digitos(n)
        pasos += 1
    print(f"{pasos} pasos")
