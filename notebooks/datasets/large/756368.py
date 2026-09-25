import re
from collections import defaultdict


import sys
input = sys.stdin.read
text = input().strip()

# Convertir el texto a minúsculas y manejar guiones
words = text.lower().split()
unique_words = set()
current_word = []

for word in words:
    # Si la palabra termina con un guion, continuamos la palabra
    if word.endswith("-"):
        current_word.append(word[:-1])  # Eliminar el guion
    else:
        current_word.append(word)
        # Limpiar caracteres no alfabéticos
        cleaned_word = re.sub(r"[^a-z-]", "", "".join(current_word))
        if cleaned_word:
            unique_words.add(cleaned_word)
        current_word = []

# Ordenar alfabéticamente y mostrar las palabras
for word in sorted(unique_words):
    print(word)

