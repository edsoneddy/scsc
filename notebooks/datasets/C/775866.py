def multiplicar_digitos(n):
    producto = 1
    while n > 0:
        digito = n % 10
        producto *= digito
        n = n // 10
    return producto

def contar_pasos(n):
    pasos = 0
    while n >= 10:
        n = multiplicar_digitos(n)
        pasos += 1
    return pasos

casos = int(input())
for _ in range(casos):
    numero = int(input())
    pasos = contar_pasos(numero)
    print(f"{pasos} pasos")