import sys
import re
def procesar_texto():
    palabras = set()
    buffer_palabra = ""
    for linea in sys.stdin:
        linea = linea.strip().lower()  
        if linea.endswith('-'):
            buffer_palabra += linea[:-1]  
        else:
            buffer_palabra += linea
            for palabra in re.findall(r'\b[a-z-]+\b', buffer_palabra):
                palabras.add(palabra)
            buffer_palabra = ""  
    palabras_ordenadas = sorted(palabras)    
    for palabra in palabras_ordenadas:
        print(palabra)
if __name__ == "__main__":
    procesar_texto()
