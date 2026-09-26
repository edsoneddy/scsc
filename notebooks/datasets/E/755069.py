import sys
import re

def procesar_entrada(texto):
    texto = texto.replace('\n', ' ') 
    palabras = []
    buffer = ""
    
    for palabra in texto.split():
        if palabra.endswith('-') and not palabra == '-': 
            buffer += palabra[:-1]  
        else:
            buffer += palabra
            palabras.append(buffer)  
            buffer = "" 

    return palabras
def extraer_palabras(texto):
    palabras = procesar_entrada(texto)
    palabras = [palabra.lower() for palabra in palabras]  
    palabras = [re.sub(r'[^a-zA-Z\-]', '', palabra) for palabra in palabras] 
    return sorted(set(palabra for palabra in palabras if palabra)) 
def main():
    entrada = sys.stdin.read()
    palabras_unicas = extraer_palabras(entrada)
    print("\n".join(palabras_unicas))

if __name__ == "__main__":
    main()