import sys
import re

def generar_diccionario():
    palabras = set()
    buffer = ""  # Para manejar palabras con guion al final de la línea
    
    # Leer entrada hasta EOF
    for linea in sys.stdin:
        linea = linea.strip()  # Eliminar espacios al inicio y al final
        if linea.endswith("-"):  # Si la línea termina con guion
            buffer += linea[:-1]  # Guardar la parte antes del guion
        else:
            # Concatenar la línea actual al buffer y procesar
            linea = buffer + linea
            buffer = ""  # Resetear el buffer
            
            # Extraer palabras usando regex y agregar al conjunto
            for palabra in re.findall(r"[a-zA-Z-]+", linea):
                palabras.add(palabra.lower())
    
    # Ordenar palabras y mostrar
    for palabra in sorted(palabras):
        print(palabra)

# Llamar a la función principal
generar_diccionario()