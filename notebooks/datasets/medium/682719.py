def convertir_a_bailarina(cadena):
    nueva_cadena = ""
    es_mayuscula = True  # Empezamos con mayúscula
    for letra in cadena:
        if letra.isalpha():
            if es_mayuscula:
                nueva_cadena += letra.upper()
            else:
                nueva_cadena += letra.lower()
            es_mayuscula = not es_mayuscula
        else:
            nueva_cadena += letra  # Mantener otros caracteres sin cambios
    return nueva_cadena

# Leer el número de casos de prueba
T = int(input())

# Procesar cada caso de prueba
for _ in range(T):
    cadena = input()
    resultado = convertir_a_bailarina(cadena)
    print(resultado)
