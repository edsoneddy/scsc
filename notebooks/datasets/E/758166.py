import sys
import re

def procesar_texto(entrada):
    # Almacenará las palabras procesadas
    palabras = set()
    buffer = ""

    for linea in entrada:
        linea = linea.strip()
        
        # Si la línea termina con un guion, concatenamos con la siguiente
        if linea.endswith('-'):
            buffer += linea[:-1]  # Elimina el guion al final
        else:
            # Agregar la línea al buffer y procesar las palabras
            buffer += linea
            # Separar las palabras usando regex, considerando solo letras y guiones intermedios
            palabras_en_linea = re.findall(r'[a-zA-Z]+(?:-[a-zA-Z]+)*', buffer)
            # Añadir las palabras al conjunto en minúsculas
            for palabra in palabras_en_linea:
                palabras.add(palabra.lower())
            buffer = ""  # Reiniciar el buffer para la siguiente línea

    # Si queda algo en el buffer, procesarlo
    if buffer:
        palabras_en_linea = re.findall(r'[a-zA-Z]+(?:-[a-zA-Z]+)*', buffer)
        for palabra in palabras_en_linea:
            palabras.add(palabra.lower())

    # Devolver las palabras ordenadas alfabéticamente
    return sorted(palabras)

if __name__ == "__main__":
    # Leer entrada desde stdin
    entrada = sys.stdin.readlines()
    resultado = procesar_texto(entrada)
    # Imprimir cada palabra en una nueva línea
    print("\n".join(resultado))
