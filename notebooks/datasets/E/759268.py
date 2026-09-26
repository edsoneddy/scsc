import sys
import re

def procesar_texto(entrada):
    texto = " ".join(entrada)  # Combinar todas las líneas en un solo texto
    palabras = []
    palabra_actual = ""
    
    for palabra in texto.split():
        if palabra.endswith("-"):  # Si termina en guion, acumular sin el guion
            palabra_actual += palabra[:-1]
        else:
            palabra_actual += palabra  # Añadir la última parte de la palabra
            palabras.append(palabra_actual)
            palabra_actual = ""  # Reiniciar acumulador

    return palabras

def normalizar_y_ordenar(palabras):
    # Normalizar palabras (convertir a minúsculas y eliminar caracteres no deseados)
    palabras = [re.sub(r"[^a-zA-Z-]", "", palabra).lower() for palabra in palabras]
    palabras = [palabra for palabra in palabras if palabra]  # Eliminar vacías
    return sorted(set(palabras))  # Ordenar alfabéticamente y eliminar duplicados

if __name__ == "__main__":
    # Leer entrada desde stdin hasta EOF
    entrada = sys.stdin.read().splitlines()
    palabras = procesar_texto(entrada)
    resultado = normalizar_y_ordenar(palabras)

    # Imprimir palabras en orden alfabético
    for palabra in resultado:
        print(palabra)
