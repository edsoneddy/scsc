def convertir_a_bailarina(cadena):
    resultado = ""
    mayuscula = True  # Indica si la próxima letra debe ser mayúscula
    
    for letra in cadena:
        if letra.isalpha():
            if mayuscula:
                resultado += letra.upper()
            else:
                resultado += letra.lower()
            
            # Cambiar el valor de mayuscula para la siguiente letra
            mayuscula = not mayuscula
        else:
            resultado += letra
    
    return resultado

# Leer el número de casos de prueba
T = int(input())

# Procesar cada caso de prueba
for _ in range(T):
    cadena = input()
    print(convertir_a_bailarina(cadena))
