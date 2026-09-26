# Número de casos de prueba
T = int(input())

# Procesar cada caso
for _ in range(T):
    cadena = input()  # Leer la cadena
    bailarina = ""  # Resultado de la cadena bailarina
    es_mayuscula = True  # Estado inicial, debe comenzar en mayúscula

    for c in cadena:
        if c.isalpha():  # Procesar solo letras
            if es_mayuscula:
                bailarina += c.upper()  # Convertir a mayúscula
            else:
                bailarina += c.lower()  # Convertir a minúscula
            es_mayuscula = not es_mayuscula  # Alternar el estado
        else:
            bailarina += c  # Mantener caracteres no alfabéticos

    print(bailarina)  # Mostrar la cadena bailarín resultante
