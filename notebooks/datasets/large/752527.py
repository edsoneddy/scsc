import sys
import re

def leer_archivo():
    palabras = set()
    palabra_actual = ""
    
    for linea in sys.stdin:
        linea = linea.strip()
        if linea.endswith('-'):
            palabra_actual += linea[:-1] 
        else:
            palabra_actual += linea
            matches = re.findall(r'[a-zA-Z]+(?:-[a-zA-Z]+)?', palabra_actual)
            for palabra in matches:
                palabras.add(palabra.lower())
            palabra_actual = ""  

    return palabras

def main():
    palabras = leer_archivo()
    palabras_ordenadas = sorted(palabras)
    for palabra in palabras_ordenadas:
        print(palabra)

if __name__ == '__main__':
    main()
