def multiplicar_digitos(n):
    """Multiplica los dígitos de un número hasta que quede un solo dígito."""
    pasos = 0
    while n >= 10:
        n = eval('*'.join(str(n)))
        pasos += 1
    return pasos

# Leer el número de casos de prueba
num_casos = int(input())
resultados = []

for _ in range(num_casos):
    n = int(input())
    pasos = multiplicar_digitos(n)
    resultados.append(f"{pasos} pasos")

# Imprimir los resultados
for resultado in resultados:
    print(resultado)