import sys
import re

def process_text():
    """
    Procesa un texto ingresado desde la entrada estándar (stdin) para:
    1. Eliminar los saltos de línea y unir líneas separadas por guiones al final.
    2. Extraer palabras utilizando expresiones regulares.
    3. Convertir las palabras a minúsculas.
    4. Eliminar duplicados y ordenar las palabras alfabéticamente.
    5. Imprimir cada palabra única en orden alfabético.
    """
    # Leer todo el texto de entrada
    input_text = sys.stdin.read()

    # Paso 1: Unir las líneas teniendo en cuenta los guiones al final
    lines = input_text.splitlines()  # Dividir el texto en una lista de líneas
    joined_text = ""  # Variable para construir el texto unificado
    for line in lines:
        if line.endswith("-"):  # Si la línea termina con un guion
            joined_text += line[:-1]  # Agregar la línea sin el guion
        else:
            joined_text += line + " "  # Agregar la línea con un espacio al final

    # Paso 2: Extraer palabras usando expresiones regulares
    # Se consideran palabras como secuencias de letras (a-z, A-Z) y guiones
    words = re.findall(r"[a-zA-Z-]+", joined_text)

    # Paso 3: Convertir las palabras a minúsculas para evitar duplicados por mayúsculas
    words = [word.lower() for word in words]

    # Paso 4: Eliminar duplicados y ordenar las palabras alfabéticamente
    unique_words = sorted(set(words))

    # Paso 5: Imprimir cada palabra única
    for word in unique_words:
        print(word)

# Llamar a la función principal
process_text()
