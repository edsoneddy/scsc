import sys
import re

def process_input(input_text):
    # Unir palabras que continúan en la siguiente línea
    lines = input_text.splitlines()
    new_text = ''
    for line in lines:
        if line.endswith('-'):
            new_text += line[:-1]  # Eliminar el guion al final de la línea
        else:
            new_text += line + ' '  # Añadir un espacio al final de la línea normal
    
    # Convertir todo el texto a minúsculas y encontrar las palabras
    words = re.findall(r'\b[a-zA-Z]+(?:-[a-zA-Z]+)?\b', new_text.lower())
    
    # Eliminar duplicados y ordenar las palabras alfabéticamente
    unique_words = sorted(set(words))
    
    return unique_words

# Leer la entrada desde stdin (entrada estándar)
input_text = sys.stdin.read()

# Procesar la entrada y obtener la lista de palabras únicas
unique_words = process_input(input_text)

# Imprimir las palabras únicas, una por línea
for word in unique_words:
    print(word)
