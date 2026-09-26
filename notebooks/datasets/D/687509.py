def convertir_bailarina(cadena):
    resultado = ""
    mayuscula = True
    
    for i, caracter in enumerate(cadena):
        if caracter.isalpha():
            if mayuscula:
                resultado += caracter.upper()
            else:
                resultado += caracter.lower()
            mayuscula = not mayuscula
        else:
            resultado += caracter
    
    return resultado

# Leer el número de casos de prueba
T = int(input())

# Procesar cada caso de prueba
for _ in range(T):
    cadena = input()
    cadena_bailarina = convertir_bailarina(cadena)
    print(cadena_bailarina)