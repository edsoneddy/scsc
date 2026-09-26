def convertir_a_bailarina(cadena):
    resultado = []
    mayuscula = True  # La primera letra es mayúscula
    for char in cadena:
        if char.isalpha():
            if mayuscula:
                resultado.append(char.upper())
            else:
                resultado.append(char.lower())
            mayuscula = not mayuscula  # Alternar entre mayúscula y minúscula
        else:
            resultado.append(char)  # Mantener caracteres no alfabéticos sin cambios
    return ''.join(resultado)

# Leer datos de entrada
import sys

input_data = sys.stdin.read().strip().split('\n')
T = int(input_data[0])
resultados = []

for i in range(1, T + 1):
    cadena = input_data[i]
    resultado = convertir_a_bailarina(cadena)
    resultados.append(resultado)

# Imprimir resultados, una línea por cada caso de prueba
for resultado in resultados:
    print(resultado)
