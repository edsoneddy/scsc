import sys
import re


palabras = set()
current_line = ""
    
# Leer desde la entrada estándar
for line in sys.stdin:
    line = line.rstrip()  # Quitar los espacios en blanco al final
    if line.endswith('-'):  
    # Si la línea termina con un guion
        current_line += line[:-1]  # Agregar la línea sin el guion
    else:
        current_line += line  # Agregar la línea normalmente
            
        # Extraer palabras usando una expresión regular
        words = re.findall(r'[a-zA-Z-]+', current_line)
        for word in words:
            palabras.add(word.lower())  # Almacenar en minúsculas
            
        current_line = ""  # Resetear current_line
    
# Procesar cualquier texto que haya quedado en current_line
if current_line:
    words = re.findall(r'[a-zA-Z-]+', current_line)
    for word in words:
        palabras.add(word.lower())
    
# Convertir el conjunto a una lista y ordenarla
palabras_ordenadas = sorted(palabras)
    
# Imprimir las palabras en orden
for palabra in palabras_ordenadas:
    print(palabra)

