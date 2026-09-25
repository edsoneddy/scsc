import sys
import re
 
def procesar_entrada(entrada_texto):
    lineas = entrada_texto.split('\n')
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
    entrada_texto = sys.stdin.read()
    palabras_salida = procesar_entrada(entrada_texto)
    
    for palabra in palabras_salida:
        print(palabra)
 
if __name__ == "__main__":
    principal()


# LA COMPLEJIADA  ALGORITMICA ES :
#la complejidad de este código es principalmente lineal 
#con un factor adicional de ordenamiento que es O(n log n), 
#donde n es el número total de palabras en el texto de entrada.