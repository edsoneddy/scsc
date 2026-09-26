import sys
import re

def main():
    palabras = set() 
    buffer = ""  

    for line in sys.stdin:
        line = line.rstrip()  
        if line.endswith('-'):
            buffer += line[:-1]  # Agregar la línea sin el guion
        else:
            buffer += line 
            for palabra in re.findall(r'\b\w[\w-]*\w\b|\b\w\b', buffer):
                palabras.add(palabra.lower()) 
            buffer = "" 

    if buffer:
        for palabra in re.findall(r'\b\w[\w-]*\w\b|\b\w\b', buffer):
            palabras.add(palabra.lower())

    lista_palabras = sorted(palabras)

    for palabra in lista_palabras:
        print(palabra)

if __name__ == "__main__":
    main()
