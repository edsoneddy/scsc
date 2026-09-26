def cont_pasos(num):
    cont = 0
    while num > 9:
        producto = 1
        while num > 0:
            digito = num % 10
            producto *= digito
            num //= 10
        num = producto
        cont += 1
    return cont

casos = int(input())
for _ in range(casos):
    num = int(input())
    print(f"{cont_pasos(num)} pasos")