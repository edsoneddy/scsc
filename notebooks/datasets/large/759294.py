import sys
import re

def main():
    input_text = sys.stdin.read()  # Leer toda la entrada
    words = set()  # Usaremos un conjunto para evitar duplicados
    current_word = ""

    # Procesar línea por línea
    for line in input_text.splitlines():
        line = line.strip()  # Eliminar espacios en blanco alrededor de la línea
        if not line:
            continue

        # Combinar palabras con guión al final
        if line.endswith("-"):
            current_word += line[:-1]
        else:
            current_word += line
            # Dividir la línea en palabras utilizando regex
            tokens = re.findall(r"[a-zA-Z\-]+", current_word.lower())
            words.update(tokens)  # Agregar palabras al conjunto
            current_word = ""

    # Convertir el conjunto a una lista, ordenar e imprimir
    for word in sorted(words):
        print(word)

if __name__ == "__main__":
    main()