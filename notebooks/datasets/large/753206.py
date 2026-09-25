import sys
import re

def procesar_texto(entrada):
    texto_unido = ""
    for linea in entrada:
        linea = linea.rstrip()  # Quita espacios en blanco finales
        if linea.endswith('-'):
            # Si la línea termina en '-', une con la siguiente línea
            texto_unido += linea[:-1]
        else:
            texto_unido += linea + " "
    
    # Encuentra todas las palabras válidas
    palabras = re.findall(r'[a-zA-Z\-]+', texto_unido)
    
    # Normalizar palabras a minúsculas y eliminar duplicados
    palabras_normalizadas = set(palabra.lower() for palabra in palabras)
    
    # Ordenar las palabras alfabéticamente
    palabras_ordenadas = sorted(palabras_normalizadas)
    
    return palabras_ordenadas

# Leer entrada desde el stdin (o archivo)
entrada = sys.stdin.read().splitlines()

# Procesar el texto
resultado = procesar_texto(entrada)

# Imprimir cada palabra en una línea
for palabra in resultado:
    print(palabra)
