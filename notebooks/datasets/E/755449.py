import sys
import re

def main():
    words = set()  # Conjunto para almacenar palabras únicas
    buffer = ""  # Para manejar palabras divididas por guiones

    # Leer todas las líneas de entrada
    for line in sys.stdin:
        line = line.rstrip()  # Eliminar espacios en blanco al final de la línea

        if buffer:  # Si hay un fragmento de palabra pendiente, agrégalo a la línea actual
            line = buffer + line
            buffer = ""

        # Si la línea termina con un guion, se guarda el prefijo en el buffer
        if line.endswith("-"):
            buffer = line[:-1]  # Guardar la línea sin el guion final
            continue  # Esperar la siguiente línea para completar la palabra

        # Usar una expresión regular para extraer palabras válidas
        matches = re.findall(r"[a-zA-Z\-]+", line)
        for word in matches:
            words.add(word.lower())  # Convertir a minúsculas y agregar al conjunto

    # Ordenar y mostrar las palabras únicas
    for word in sorted(words):
        print(word)

if __name__ == "__main__":
    main()
