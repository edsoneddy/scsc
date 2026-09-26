def contar_pasos(n):
    # Si el número ya es de un solo dígito, no se necesitan pasos
    if n < 10:
        return 0
    
    pasos = 0
    while n >= 10:
        producto = 1
        while n > 0:
            producto *= n % 10  # Multiplicamos cada dígito
            n //= 10  # Quitamos el último dígito
        n = producto
        pasos += 1
    return pasos

def resolver():
    # Leer número de casos
    num_casos = int(input())
    
    # Procesar cada caso
    for _ in range(num_casos):
        numero = int(input())
        pasos = contar_pasos(numero)
        print(f"{pasos} pasos")

# Ejecución
resolver()
