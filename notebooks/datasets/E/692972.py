import sys
import re

def process_text(input_text):
    # Inicializar variables
    lines = input_text.splitlines()
    full_text = ""
    current_word = ""
    
    # Procesar cada línea
    for line in lines:
        if line.endswith("-"):
            current_word += line[:-1]
        else:
            full_text += current_word + line + " "
            current_word = ""
    
    # Convertir a minúsculas
    full_text = full_text.lower()
    
    # Eliminar puntuación
    full_text = re.sub(r'[.,]', '', full_text)
    
    # Dividir en palabras
    words = full_text.split()
    
    # Crear conjunto de palabras únicas
    unique_words = set(words)
    
    # Ordenar palabras
    sorted_words = sorted(unique_words)
    
    # Imprimir cada palabra en una nueva línea
    for word in sorted_words:
        print(word)

if __name__ == "__main__":
    input_text = sys.stdin.read()
    process_text(input_text)
