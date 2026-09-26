import sys
import re

def principal():
    conjunto_palabras = set()
    acumulador = ""

    for linea in sys.stdin:
        linea = linea.rstrip()
        if linea.endswith('-'):
            acumulador += linea[:-1]
        else:
            acumulador += linea
            for palabra in re.findall(r'\b\w[\w-]*\w\b|\b\w\b', acumulador):
                conjunto_palabras.add(palabra.lower())
            acumulador = ""

    if acumulador:
        for palabra in re.findall(r'\b\w[\w-]*\w\b|\b\w\b', acumulador):
            conjunto_palabras.add(palabra.lower())

    lista_ordenada = sorted(conjunto_palabras)

    for palabra in lista_ordenada:
        print(palabra)

if __name__ == "__main__":
    principal()
