import sys
import re

def process_input():
    text = sys.stdin.read()  # Leer toda la entrada
    text = text.lower()      # Convertir todo a minúsculas
    lines = text.splitlines()  # Dividir por líneas

    # Lista para almacenar palabras procesadas
    words = []
    current_word = ""

    for line in lines:
        # Si la línea termina con "-", es una palabra que continúa
        if line.endswith("-"):
            current_word += line[:-1]  # Agregar sin el guion final
        else:
            current_word += line
            words += re.findall(r"[a-z-]+", current_word)
            current_word = ""  # Reiniciar la palabra actual

    unique_words = sorted(set(words))
    return unique_words

def main():
    unique_words = process_input()

    for word in unique_words:
        print(word)

if __name__ == "__main__":
    main()
