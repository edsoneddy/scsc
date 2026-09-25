import sys
import re

def procesar_texto(texto):
    palabras = set()  # Usaremos un conjunto para almacenar palabras únicas
    buffer = ""  # Para manejar palabras que continúan con un guion

    # Iterar sobre cada línea del texto
    for linea in texto:
        linea = linea.strip()  # Eliminar espacios en blanco al inicio y final
        
        # Si la línea termina en guion, acumular en el buffer sin el guion
        if linea.endswith('-'):
            buffer += linea[:-1]
        else:
            # Añadir la línea completa al buffer si hay texto acumulado
            buffer += linea

            # Extraer palabras del buffer usando una expresión regular
            for palabra in re.findall(r'[a-zA-Z\-]+', buffer):
                # Convertir a minúsculas y añadir al conjunto de palabras
                palabras.add(palabra.lower())

            # Reiniciar el buffer para la próxima línea
            buffer = ""

    return sorted(palabras)  # Devolver las palabras ordenadas alfabéticamente

def main():
    texto = sys.stdin.read().splitlines()  # Leer todo el texto de la entrada estándar
    resultado = procesar_texto(texto)
    
    # Imprimir las palabras una por línea
    for palabra in resultado:
        print(palabra)

if __name__ == "__main__":
    main()
