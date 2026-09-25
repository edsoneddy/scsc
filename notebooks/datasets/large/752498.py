import sys
import re

def procesar_segundo_diccionario():
    # Inicializar variables
    palabras_unicas = set()
    palabra_continua = ""

    for linea in sys.stdin:
        linea = linea.strip()  # Remover espacios en blanco al inicio y final

        if palabra_continua:
            # Si hay una palabra que continúa, combinarla con la nueva línea
            linea = palabra_continua + linea
            palabra_continua = ""

        if linea.endswith("-"):
            # Si la línea termina con "-", quitarlo y marcar para continuación
            palabra_continua = linea[:-1]
        else:
            # Dividir en palabras, transformar a minúsculas y agregar al conjunto
            palabras = re.findall(r'[a-zA-Z-]+', linea.lower())
            palabras_unicas.update(palabras)

    # Ordenar alfabéticamente las palabras únicas y mostrarlas
    for palabra in sorted(palabras_unicas):
        print(palabra)

if __name__ == "__main__":
    procesar_segundo_diccionario()
