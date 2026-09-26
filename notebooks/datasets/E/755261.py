import re

def procesar_texto(texto):
    palabras = set()
    buffer = ""

    for linea in texto:
        linea = linea.strip()
        if linea.endswith("-"):
            buffer += linea[:-1]
        else:
            buffer += linea
            palabras_linea = re.findall(r"[a-zA-Z-]+", buffer.lower())
            palabras.update(palabras_linea)
            buffer = ""

    return sorted(palabras)

if __name__ == "__main__":
    try:
        import sys
        texto = sys.stdin.read().splitlines()
        resultado = procesar_texto(texto)
        print("\n".join(resultado))
    except Exception as e:
        print(f"Error: {e}")
