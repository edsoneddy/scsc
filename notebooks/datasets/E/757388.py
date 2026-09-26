import sys
import re

lineas = sys.stdin.read().splitlines()
texto = ""
for linea in lineas:
    if linea.endswith("-"):
        texto += linea[:-1]
    else:
        texto += linea + " "
palabras = re.findall(r"[a-zA-Z\-]+", texto.lower())
palabras_unicas = sorted(set(palabras))
print("\n".join(palabras_unicas))