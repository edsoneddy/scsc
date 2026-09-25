import sys
import re

def process_text():
    input_lines = sys.stdin.read().splitlines()  # Leer todas las líneas de la entrada
    words = []
    current_word = ""

    for line in input_lines:
        line = line.strip()  # Eliminar espacios en blanco al inicio y al final
        if line.endswith("-"):  # Si la línea termina en un guion, es una palabra incompleta
            current_word += line[:-1]  # Agregar la palabra sin el guion final
        else:
            current_word += line  # Agregar el resto de la palabra
            words.extend(re.findall(r"[a-zA-Z-]+", current_word))  # Extraer palabras válidas
            current_word = ""  # Reiniciar la palabra actual

    # Si hay una palabra incompleta al final, agregarla
    if current_word:
        words.extend(re.findall(r"[a-zA-Z-]+", current_word))

    # Convertir todas las palabras a minúsculas y eliminar duplicados
    unique_words = sorted(set(word.lower() for word in words))
    
    # Imprimir palabras ordenadas
    print("\n".join(unique_words))

if __name__ == "__main__":
    process_text()