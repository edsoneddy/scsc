import sys
import re

def procesar_texto():
    texto = sys.stdin.read()
    
    # Combinar líneas con palabras que terminan en guión
    lineas = texto.splitlines()
    texto_procesado = ""
    for i, linea in enumerate(lineas):
        if linea.endswith("-"):
            texto_procesado += linea[:-1]  # Eliminar el guion
        else:
            texto_procesado += linea + " "

    # Extraer palabras usando una expresión regular
    palabras = re.findall(r"[a-zA-Z]+(?:-[a-zA-Z]+)?", texto_procesado)

    # Convertir palabras a minúsculas y eliminar duplicados usando un conjunto
    palabras_unicas = set(palabra.lower() for palabra in palabras)

    # Ordenar las palabras alfabéticamente
    palabras_ordenadas = sorted(palabras_unicas)

    # Imprimir palabras en orden alfabético
    for palabra in palabras_ordenadas:
        print(palabra)

# Ejecutar el programa si se llama desde la línea de comandos
if __name__ == "__main__":
    procesar_texto()
