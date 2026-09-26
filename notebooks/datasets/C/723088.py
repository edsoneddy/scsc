def multiplicar_digitos(num):
    producto = 1
    for digito in str(num):
        producto *= int(digito)
    return producto

def contar_pasos(num):
    if num < 10:
        return 0
    pasos = 0
    while num >= 10:
        num = multiplicar_digitos(num)
        pasos += 1
    return pasos

t = int(input())

for _ in range(t):
    n = int(input())
    print(f"{contar_pasos(n)} pasos")