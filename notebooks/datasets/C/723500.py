def producto_digitos(n):
    producto = 1
    while n > 0:
        producto *= n % 10
        n //= 10
    return producto

def contar_pasos(n):
    pasos = 0
    while n >= 10:
        n = producto_digitos(n)  
        pasos += 1  
    return pasos

num_casos = int(input())

for _ in range(num_casos):
    numero = int(input())
    pasos = contar_pasos(numero)
    print(f"{pasos} pasos")
