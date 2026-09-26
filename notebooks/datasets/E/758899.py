import sys
import re

def procesar_texto(entrada):
    texto = entrada.strip().splitlines()
    palabras = []
    palabra_actual = ""
    for linea in texto:
        linea = linea.strip()
        if palabra_actual:
            # Si había una palabra previa que continúa, añadir esta línea
            linea = palabra_actual + linea
            palabra_actual = ""
        if linea.endswith("-"):
            palabra_actual = linea[:-1]  # Guardar palabra sin el guion
        else:
            palabras.extend(re.findall(r"[a-zA-Z-]+", linea))  # Extraer palabras
    if palabra_actual:
        palabras.append(palabra_actual)
    palabras_unicas = set(palabra.lower() for palabra in palabras)
    return sorted(palabras_unicas)

entrada = sys.stdin.read()
resultado = procesar_texto(entrada)
print("\n".join(resultado))
