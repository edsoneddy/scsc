import sys
import re

def main():
    palabras = set()  # Usamos un conjunto para evitar duplicados
    buffer = ""  # Para almacenar las líneas que terminan con un guion

    for line in sys.stdin:
        line = line.rstrip()  # Eliminar espacios en blanco al final
        if line.endswith('-'):
            buffer += line[:-1]  # Agregar la línea sin el guion
        else:
            buffer += line  # Agregar la línea completa
            # Dividir las palabras en el buffer
            palabras.update(re.findall(r'\b\w[\w-]*\w\b|\b\w\b', buffer.lower()))  # Agregar palabras al conjunto
            buffer = ""  # Limpiar el buffer

    # Si hay contenido en el buffer después del último salto de línea
    if buffer:
        palabras.update(re.findall(r'\b\w[\w-]*\w\b|\b\w\b', buffer.lower()))

    # Ordenar y convertir el conjunto en una lista
    lista_palabras = sorted(palabras)

    # Imprimir cada palabra en una línea
    print("\n".join(lista_palabras))

if __name__ == "__main__":
    main()
