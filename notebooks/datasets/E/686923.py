import sys
import re

def procesarTexto(entrada):
    lineas = entrada.split('\n')
    conjuntoPAL = set()
    palabraCONT = ""

    for linea in lineas:
        linea = linea.strip()
        if linea.endswith('-'):
            palabraCONT += linea[:-1]
        else:
            palabraCONT += linea
            lineaPro = re.sub(r'[^\w-]', ' ', palabraCONT)
            for palabra in lineaPro.split():
                conjuntoPAL.add(palabra.lower())
            palabraCONT = ""

    palabrasORD = sorted(conjuntoPAL)
    return palabrasORD

if __name__ == "__main__":
    entrada = sys.stdin.read()
    resultado = procesarTexto(entrada)
    for palabra in resultado:
        print(palabra)
