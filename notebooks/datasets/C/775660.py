def multiplicar_digitos(n):
    pasos = 0
    while len(str(n)) > 1:
        producto = 1
        for digito in str(n):
            producto *= int(digito)
        n = producto
        pasos += 1
    return pasos
t = int(input()) 
for i in range(t):
    num = int(input())
    pasos = multiplicar_digitos(num)
    print(f"{pasos} pasos")