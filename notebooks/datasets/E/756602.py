import sys
import re

def procesar_diccionario():
    palabras = set() 
    palabra_continua = "" 

    for linea in sys.stdin:
        linea = linea.strip()

        if palabra_continua:  
            linea = palabra_continua + linea
            palabra_continua = ""  

        if linea.endswith("-"):
            palabra_continua = linea[:-1].lower()  
            continue

        palabras_en_linea = re.findall(r"[a-zA-Z]+(?:-[a-zA-Z]+)?", linea.lower())
        palabras.update(palabras_en_linea)  

    palabras_ordenadas = sorted(palabras)

    for palabra in palabras_ordenadas:
        print(palabra)


if __name__ == "__main__":
    procesar_diccionario()

