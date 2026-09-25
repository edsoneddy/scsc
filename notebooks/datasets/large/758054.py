import sys
import re

def procesar_entrada(entrada):
    # Unir líneas para manejar palabras divididas por guiones al final de línea
    texto = " ".join(entrada).replace("\n", " ")
    # Manejar guiones de continuidad
    texto = re.sub(r"(\S)-\s", r"\1", texto)
    # Extraer palabras con regex
    palabras = re.findall(r"[a-zA-Z\-]+", texto)
    # Convertir palabras a minúsculas y eliminar duplicados
    palabras_unicas = sorted(set(palabra.lower() for palabra in palabras))
    return palabras_unicas

# Leer entrada desde stdin hasta EOF
if __name__ == "__main__":
    try:
        entrada = sys.stdin.read()
    except EOFError:
        entrada = ""
    palabras_ordenadas = procesar_entrada(entrada.splitlines())
    for palabra in palabras_ordenadas:
        print(palabra)
