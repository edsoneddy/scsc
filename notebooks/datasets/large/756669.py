import sys
import re

def procesar_diccionario():
    # Usamos un set para almacenar las palabras únicas
    palabras_unicas = set()

    # Leer toda la entrada
    texto = sys.stdin.read()
    
    # Reemplazar líneas nuevas por espacios, y unir palabras si un guion termina la línea
    texto = re.sub(r'(\S)-\s*\n', r'\1', texto)  # Unir palabras terminadas en guion
    texto = texto.replace('\n', ' ')  # Reemplazar saltos de línea por espacio

    # Usar regex para encontrar palabras, permitiendo guiones
    palabras = re.findall(r'\b[a-zA-Z-]+\b', texto)

    # Añadir palabras en minúsculas al conjunto
    palabras_unicas.update(map(str.lower, palabras))

    # Convertir el conjunto a una lista, ordenarla y imprimir
    lista_palabras = sorted(palabras_unicas)

    for palabra in lista_palabras:
        print(palabra)

if __name__ == "__main__":
    procesar_diccionario()