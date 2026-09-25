def convertir_a_bailarina(cadena):
    # Resultado para la cadena bailarina
    resultado = []
    
    # Bandera para alternar entre mayúscula y minúscula, comenzando con mayúscula
    es_mayuscula = True
    
    for char in cadena:
        if char.isalpha():  # Verifica si el carácter es una letra
            if es_mayuscula:
                resultado.append(char.upper())
            else:
                resultado.append(char.lower())
            es_mayuscula = not es_mayuscula  # Alterna la bandera
        else:
            resultado.append(char)  # Mantiene caracteres no alfabéticos como están
    
    return ''.join(resultado)

# Leer el número de casos de prueba
num_cases = int(input())

# Procesar cada caso de prueba
for _ in range(num_cases):
    # Leer la cadena de texto
    case = input()
    
    # Convertir la cadena a bailarina
    cadena_bailarina = convertir_a_bailarina(case)
    
    # Imprimir el resultado
    print(cadena_bailarina)