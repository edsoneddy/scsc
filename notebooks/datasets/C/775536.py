def multiplicar_digitos(num):
    producto = 1
    for digito in str(num):
        producto *= int(digito)
    return producto

def contar_pasos(num):
    if num == 0:
        return 0
    pasos = 0
    while num >= 10:
        num = multiplicar_digitos(num)
        pasos += 1
    return pasos

casos = int(input())
resultados = []

for _ in range(casos):
    num = int(input())
    pasos = contar_pasos(num)
    resultados.append(f"{pasos} pasos")

for resultado in resultados:
    print(resultado)