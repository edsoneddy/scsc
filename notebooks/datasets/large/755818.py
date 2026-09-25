import re


import sys

def procesar_texto():
    linea_previa = ""

    almacen_palabras = set()

    for texto in sys.stdin:
        texto = texto.strip()
        if texto.endswith("-"): 




            linea_previa += texto[:-1]
        else:
            linea_actual = linea_previa + texto




            linea_previa = ""
            palabras_detectadas = re.findall(r'[a-zA-Z]+(?:-[a-zA-Z]+)?', linea_actual.lower())
            almacen_palabras.update(palabras_detectadas)

    palabras_finales = sorted(almacen_palabras)

    for elemento in palabras_finales:
        print(elemento)

if __name__ == "__main__":
    procesar_texto()
