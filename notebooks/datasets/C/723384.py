def multiplicar_digitos(n):
    if n < 10:
        return 0
    else:
        producto = 1
        for digito in str(n):
            producto *= int(digito)
        return 1 + multiplicar_digitos(producto)

num_casos = int(input())
for _ in range(num_casos):
    n = int(input())
    print(f"{multiplicar_digitos(n)} pasos")
