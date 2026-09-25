import sys
import re

def procesar_texto():
    palabras = set()
    palabra_actual = ""

    for linea in sys.stdin:
        linea = linea.strip()
        if linea.endswith("-"):
            palabra_actual += linea[:-1]
        else:
            palabra_actual += linea
            for palabra in re.findall(r"[a-zA-Z\-]+", palabra_actual):
                palabras.add(palabra.lower())
            palabra_actual = ""

    palabras_ordenadas = sorted(palabras)
    return palabras_ordenadas

if __name__ == "__main__":
    resultado = procesar_texto()
    for palabra in resultado:
        print(palabra)
