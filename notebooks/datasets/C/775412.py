def multiplicar_digitos(n):
    producto = 1
    while n > 0:
        digito = n % 10
        producto *= digito
        n //= 10
    return producto

t = int(input())  
for _ in range(t):
    n = int(input())
    if n < 10:
        print("0 pasos")
        continue

    pasos = 0
    while n >= 10:
        n = multiplicar_digitos(n)
        pasos += 1
    print(f"{pasos} pasos")