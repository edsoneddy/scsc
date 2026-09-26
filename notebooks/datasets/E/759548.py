import sys
import re

def procesar_texto():
    palabras_unicas = set()
    palabra_actual = ""
    
    for linea in sys.stdin:
        linea = linea.strip()
        
        # Si la palabra actual tiene un guion al final, eliminar el guion y concatenar con la nueva línea
        if palabra_actual and palabra_actual.endswith("-"):
            palabra_actual = palabra_actual[:-1] + linea
        else:
            palabra_actual += (" " + linea if palabra_actual else linea)
        
        # Procesar palabras completas de la línea actual
        palabras = re.findall(r"[a-zA-Z-]+", palabra_actual)
        
        for i, palabra in enumerate(palabras):
            if palabra.endswith("-") and i == len(palabras) - 1:
                # Si la palabra tiene un guion al final y es la última palabra, se guarda para la próxima línea
                palabra_actual = palabra
            else:
                # Convertir a minúsculas y agregar al conjunto
                palabras_unicas.add(palabra.lower())
                palabra_actual = ""
    
    # Retornar el conjunto de palabras únicas
    return sorted(palabras_unicas)

if __name__ == "__main__":
    resultado = procesar_texto()
    for palabra in resultado:
        print(palabra)
