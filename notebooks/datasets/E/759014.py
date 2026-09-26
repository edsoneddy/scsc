import sys
import re

def procesar_texto(texto):
    palabras = []
    buffer = ""

    for linea in texto:
        linea = linea.strip()  # Eliminar espacios al inicio y final
        if linea.endswith("-"):  # Si la línea termina en guion
            buffer += linea[:-1]  # Añadir la línea sin el guion al buffer
        else:
            buffer += linea
            # Extraer palabras y añadirlas a la lista
            palabras.extend(re.findall(r"[a-zA-Z]+(?:-[a-zA-Z]+)?", buffer))
            buffer = ""  # Reiniciar el buffer

    # Convertir palabras a minúsculas y eliminar duplicados
    palabras = {palabra.lower() for palabra in palabras}
    
    # Ordenar palabras alfabéticamente
    return sorted(palabras)

# Leer entrada desde stdin
def main():
    texto = sys.stdin.read().splitlines()
    resultado = procesar_texto(texto)
    print("\n".join(resultado))

if __name__ == "__main__":
    main()
