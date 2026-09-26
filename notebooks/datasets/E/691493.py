import sys
import re

def Pal_Limpia(palabra):
    return re.sub(r'[^a-zA-Z-]', '', palabra).lower()

def Gen_Diccionario(texto):
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
    
    palabras_normalizadas = set(Pal_Limpia(palabra) for palabra in palabras)
    palabras_ordenadas = sorted(palabras_normalizadas)
    
    return palabras_ordenadas


texto = sys.stdin.read().splitlines()
palabras_ordenadas = Gen_Diccionario(texto)

for palabra in palabras_ordenadas:
    print(palabra)

