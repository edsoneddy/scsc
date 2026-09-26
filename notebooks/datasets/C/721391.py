def contar_pasos_para_un_digito(n):
    if n < 10:
        return 0

    pasos = 0
    while n >= 10:
        producto = 1
        for digito in str(n):
            producto *= int(digito)
        n = producto
        pasos += 1
    return pasos


def resolver_casos_de_prueba():
    t = int(input())

    for _ in range(t):
        numero = int(input())
        pasos = contar_pasos_para_un_digito(numero)
        print(f"{pasos} pasos")


resolver_casos_de_prueba()
