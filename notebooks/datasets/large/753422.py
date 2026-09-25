import re

def procesar_texto(texto):
    palabras = set()  # Usamos un set para almacenar palabras únicas
    buffer = ""  # Para manejar palabras que continúan en la siguiente línea

    for linea in texto:
        linea = linea.strip()  # Eliminamos espacios al inicio y al final
        # Si hay una palabra cortada por un guion al final
        if linea.endswith("-"):
            buffer += linea[:-1]  # Quitamos el guion y agregamos al buffer
        else:
            buffer += linea  # Añadimos la línea completa
            # Dividimos las palabras por espacios, considerando mayúsculas y guiones
            palabras_linea = re.findall(r"[a-zA-Z-]+", buffer.lower())
            palabras.update(palabras_linea)  # Añadimos palabras únicas al set
            buffer = ""  # Limpiamos el buffer después de procesar la línea

    return sorted(palabras)  # Devolvemos las palabras ordenadas alfabéticamente


# Leer todas las líneas de entrada
if __name__ == "__main__":
    try:
        # Leer hasta EOF, manejando en sistemas como pruebas locales o archivos
        import sys
        texto = sys.stdin.read().splitlines()

        # Procesar el texto
        resultado = procesar_texto(texto)

        # Imprimir las palabras únicas en orden alfabético
        print("\n".join(resultado))
    except Exception as e:
        print(f"Error: {e}")
