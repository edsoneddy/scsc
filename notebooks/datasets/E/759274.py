import sys
import re

def procesar_texto():
    texto = sys.stdin.read()  # Lee todo el texto de entrada
    lineas = texto.splitlines()  # Divide el texto en líneas
    palabras = []  # Lista para almacenar las palabras
    
    palabra_actual = ""  # Palabra temporal para manejar guiones al final de línea
    
    for linea in lineas:
        # Elimina caracteres no alfabéticos excepto guiones
        linea = re.sub(r"[^a-zA-Z\- ]", " ", linea)
        palabras_linea = linea.split()  # Divide la línea en palabras
        
        for palabra in palabras_linea:
            if palabra.endswith('-'):  # Si la palabra termina en guion
                palabra_actual += palabra[:-1]  # Quita el guion y acumula
            else:
                palabra_actual += palabra  # Completa la palabra
                palabras.append(palabra_actual.lower())  # Añade la palabra completa en minúsculas
                palabra_actual = ""  # Reinicia la palabra temporal
    
    # Elimina duplicados y ordena alfabéticamente
    palabras_unicas = sorted(set(palabras))
    for palabra in palabras_unicas:
        print(palabra)

# Llama a la función si se ejecuta como script
if __name__ == "__main__":
    procesar_texto()
