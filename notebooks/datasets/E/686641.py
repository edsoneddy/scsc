import sys
import re

def main():
    # Leer toda la entrada hasta EOF
    input_lines = sys.stdin.read().splitlines()
    
    # Unir las líneas con un espacio para procesar los guiones que indican continuación de palabra
    combined_text = " ".join(input_lines)
    
    # Remover guiones que indican continuación de palabra
    processed_text = re.sub(r"-\s+", "", combined_text)
    
    # Usar una expresión regular para encontrar todas las palabras
    words = re.findall(r"[a-zA-Z]+(?:-[a-zA-Z]+)?", processed_text)
    
    # Convertir todas las palabras a minúsculas
    words = [word.lower() for word in words]
    
    # Usar un conjunto para eliminar duplicados
    unique_words = set(words)
    
    # Ordenar las palabras en orden alfabético
    sorted_words = sorted(unique_words)
    
    # Imprimir cada palabra en una línea
    for word in sorted_words:
        print(word)

if __name__ == "__main__":
    main()
