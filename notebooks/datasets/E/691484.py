import sys
import re

def normalizar_palabra(palabra):
    return re.sub(r'[^a-zA-Z-]', '', palabra).lower()

def procesar_texto(texto):
    palabras = []
    palabra_actual = ""
    for linea in texto:
        linea = linea.strip()
        if linea.endswith('-'):
            palabra_actual += linea[:-1]
        else:
            palabra_actual += linea
            palabras.extend(palabra_actual.split())
            palabra_actual = ""
    
    palabras_normalizadas = set(normalizar_palabra(palabra) for palabra in palabras)
    palabras_ordenadas = sorted(palabras_normalizadas)
    
    return palabras_ordenadas


texto = sys.stdin.read().splitlines()
palabras_ordenadas = procesar_texto(texto)

for palabra in palabras_ordenadas:
    print(palabra)