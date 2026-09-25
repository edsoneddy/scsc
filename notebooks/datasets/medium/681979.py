def make_dancing_string(s):
    result = []
    capitalize = True
    for char in s:
        if char.isalpha():
            if capitalize:
                result.append(char.upper())
            else:
                result.append(char.lower())
            capitalize = not capitalize
        else:
            result.append(char)
    return ''.join(result)

# Leer el número de casos de prueba
num_cases = int(input())

# Procesar cada caso de prueba
for _ in range(num_cases):
    # Leer la cadena de texto
    text = input()
    
    # Convertir la cadena a una cadena bailarina
    dancing_string = make_dancing_string(text)
    
    # Imprimir el resultado
    print(dancing_string)
