# Función para contar las iteraciones hasta que el número sea de un solo dígito
def contar_pasos(n):
    if n == 0:
        return 0
    
    pasos = 0
    while n >= 10:
        producto = 1
        while n > 0:
            producto *= n % 10  # Multiplicar los dígitos
            n //= 10
        n = producto
        pasos += 1
    
    return pasos

# Leer el número de casos de prueba
casos = int(input())

# Procesar cada caso
for _ in range(casos):
    numero = int(input())
    pasos = contar_pasos(numero)
    print(f"{pasos} pasos")
