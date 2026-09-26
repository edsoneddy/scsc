def multiplicar_digitos(n):
    producto = 1
    while n > 0:
        producto *= n % 10
        n //= 10
    return producto

n = int(input())  # Número de casos de prueba
for _ in range(n):
    num = int(input())
    pasos = 0
    while num >= 10:
        num = multiplicar_digitos(num)
        pasos += 1
    print(f"{pasos} pasos")