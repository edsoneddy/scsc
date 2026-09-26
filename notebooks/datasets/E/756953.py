import sys
import re

def process_input():
    text = sys.stdin.read()  # Leer toda la entrada
    text = text.lower()      # Convertir todo a minúsculas
    lines = text.splitlines()  # Dividir por líneas

    words = []
    current_word = ""

    for line in lines:
        line = line.strip()
        
        # Si la línea termina con un guion, unirla con la siguiente línea
        if line.endswith("-"):
            current_word += line[:-1]  # Agregar sin el guion final
        else:
            current_word += line
            words += re.findall(r"[a-zA-Z-]+", current_word)  # Extraer palabras válidas
            current_word = ""  # Reiniciar la palabra actual

    # Eliminar duplicados, ordenar las palabras y devolverlas
    unique_words = sorted(set(words))
    return unique_words

def main():
    unique_words = process_input()

    for word in unique_words:
        print(word)

if __name__ == "__main__":  # Corregir el nombre del main
    main()
