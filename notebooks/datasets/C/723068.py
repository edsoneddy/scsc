def multiplicar_digitos(n):
    producto = 1
    while n > 0:
        producto *= n % 10
        n //= 10
    return producto
def contar_pasos(n):
    if n < 10:
        return 0

    pasos = 0
    while n >= 10:
        n = multiplicar_digitos(n)
        pasos += 1
    return pasos
casos = int(input())
for _ in range(casos):
    n = int(input())
    pasos = contar_pasos(n)
    print(f"{pasos} pasos")
