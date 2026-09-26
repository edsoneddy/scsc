import sys
import re

def procesar_texto(entrada):
    texto = []
    buffer = ""
    for linea in entrada:
        linea = linea.strip()
        if linea.endswith('-'):
            buffer += linea[:-1]
        else:
            buffer += linea
            texto.append(buffer)
            buffer = ""
    if buffer:
        texto.append(buffer)
    return " ".join(texto)

def extraer_palabras(texto):
    palabras = re.findall(r"[a-zA-Z-]+", texto)
    palabras_procesadas = {palabra.lower() for palabra in palabras}
    return sorted(palabras_procesadas)

def main():
    entrada = sys.stdin.read().splitlines()
    texto = procesar_texto(entrada)
    palabras = extraer_palabras(texto)
    print("\n".join(palabras))

if __name__ == "__main__":
    main()
