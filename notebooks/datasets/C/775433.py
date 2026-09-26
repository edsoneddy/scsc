def multiplicar_digitos(n):
    producto = 1
    while n > 0:
        producto *= n % 10  
        n //= 10  
    return producto
def contar_pasos(n):
    pasos = 0
    while n >= 10:
        n = multiplicar_digitos(n)  
        pasos += 1
    return pasos
t = int(input())  
for _ in range(t):
    n = int(input())  
    if n < 10:
        print(f"0 pasos")
    else:
        pasos = contar_pasos(n)
        print(f"{pasos} pasos")