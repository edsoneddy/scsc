import sys
import re

def procesar_texto():
    texto_completo = []
    palabra_actual = ""

    for linea in sys.stdin:
        linea = linea.rstrip() 
        if linea.endswith('-') and len(linea) > 1:
            palabra_actual += linea[:-1]
        else:
            palabra_actual += linea
            texto_completo.append(palabra_actual)
            palabra_actual = ""  
    texto = " ".join(texto_completo)

    palabras = re.findall(r"[a-zA-Z]+(?:-[a-zA-Z]+)?", texto.lower())

    palabras_unicas = sorted(set(palabras))

    for palabra in palabras_unicas:
        print(palabra)

procesar_texto()