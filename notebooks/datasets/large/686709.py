import sys
import re
 
def procesar_entrada(texto_entrada):
    lineas = texto_entrada.split('\n')
    palabras = []
    palabra_actual = ""
    
    for linea in lineas:
        linea = linea.strip()
        if linea.endswith('-'):
            palabra_actual += linea[:-1]
        else:
            palabra_actual += linea
            palabras.extend(re.sub(r'[^\w-]', ' ', palabra_actual).split())
            palabra_actual = ""
    
    palabras_unicas = set(palabra.lower() for palabra in palabras)
    
    palabras_ordenadas = sorted(palabras_unicas)
    
    return palabras_ordenadas
 
def principal():
    texto_entrada = sys.stdin.read()
    palabras_salida = procesar_entrada(texto_entrada)
    
    for palabra in palabras_salida:
        print(palabra)
 
if __name__ == "__main__":
    principal()
