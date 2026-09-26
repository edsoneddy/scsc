# ALE
import sys
import re

def read_input():
    """
    Lee todo el texto desde la entrada estándar (stdin).
    :return: Texto completo como una cadena.
    """
    return sys.stdin.read()

def join_lines_with_hyphen(input_text):
    """
    Une líneas del texto teniendo en cuenta los guiones al final de las líneas.
    Si una línea termina con un guion, se une con la siguiente.
    :param input_text: Texto completo dividido en líneas.
    :return: Texto unificado como una sola cadena.
    """
    lines = input_text.splitlines()  # Dividir el texto en líneas
    joined_text = ""  # Variable para construir el texto unificado
    for line in lines:
        if line.endswith("-"):  # Si la línea termina con un guion
            joined_text += line[:-1]  # Agregar la línea sin el guion
        else:
            joined_text += line + " "  # Agregar la línea con un espacio al final
    return joined_text

def extract_words(text):
    """
    Extrae palabras del texto usando expresiones regulares.
    Una palabra se define como una secuencia de letras y guiones.
    :param text: Texto completo como una cadena.
    :return: Lista de palabras extraídas.
    """
    return re.findall(r"[a-zA-Z-]+", text)

def process_words(words):
    """
    Procesa una lista de palabras: las convierte a minúsculas, elimina duplicados y las ordena.
    :param words: Lista de palabras.
    :return: Lista de palabras únicas y ordenadas alfabéticamente.
    """
    words_lowercase = [word.lower() for word in words]  # Convertir a minúsculas
    return sorted(set(words_lowercase))  # Eliminar duplicados y ordenar

def print_words(words):
    """
    Imprime cada palabra de la lista en una línea nueva.
    :param words: Lista de palabras.
    """
    for word in words:
        print(word)

def process_text():
    """
    Función principal que orquesta todo el procesamiento del texto.
    """
    # Leer la entrada
    input_text = read_input()

    # Unir líneas considerando los guiones
    joined_text = join_lines_with_hyphen(input_text)

    # Extraer palabras
    words = extract_words(joined_text)

    # Procesar palabras
    unique_words = process_words(words)

    # Imprimir palabras
    print_words(unique_words)

# Llamar a la función principal
process_text()
