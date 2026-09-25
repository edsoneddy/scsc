import sys
import re

def crear_diccionario():
    palabras_unicas = set()  # Usaremos un conjunto para evitar repeticiones
    palabra_continua = ""    # Almacena palabras que continúan en la siguiente línea

    for linea in sys.stdin:
        linea = linea.strip()  # Elimina espacios al inicio y final
        
        # Si hay una palabra en continuación, la unimos con la línea actual
        if palabra_continua:
            linea = palabra_continua + linea
            palabra_continua = ""
        
        # Si la línea termina con un guion "-", la marcamos para continuación
        if linea.endswith("-"):
            palabra_continua = linea[:-1]
        else:
            # Extraemos palabras válidas con una expresión regular y las normalizamos a minúsculas
            palabras = re.findall(r"[a-zA-Z-]+", linea.lower())
            palabras_unicas.update(palabras)
    
    # Convertimos el conjunto a una lista, ordenamos alfabéticamente e imprimimos cada palabra
    for palabra in sorted(palabras_unicas):
        print(palabra)

if __name__ == "__main__":
    crear_diccionario()
