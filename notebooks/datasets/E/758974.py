import sys
import re

def procesar_diccionario(entrada):
    lineas = entrada.splitlines()
    palabras = []
    palabra_actual = ""

    for linea in lineas:
        linea = linea.strip()
        if palabra_actual:
            # Continuar palabra con guion
            linea = palabra_actual + linea
            palabra_actual = ""

        if linea.endswith("-"):
            # Palabra que continúa en la siguiente línea
            palabra_actual = linea[:-1]
        else:
            # Extraer palabras de la línea
            palabras.extend(re.findall(r"[a-zA-Z-]+", linea))

    # Procesar si queda una palabra colgante
    if palabra_actual:
        palabras.append(palabra_actual)

    # Convertir palabras a minúsculas y eliminar duplicados
    palabras_unicas = set(palabra.lower() for palabra in palabras)

    # Ordenar palabras alfabéticamente
    return sorted(palabras_unicas)

# Leer toda la entrada
entrada = sys.stdin.read()

# Procesar el texto para obtener el diccionario
resultado = procesar_diccionario(entrada)

# Imprimir el resultado
print("\n".join(resultado))
