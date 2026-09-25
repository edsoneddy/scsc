import sys
import re

def procesar_entrada(entrada):
    texto_completo = ""
    lineas = entrada.splitlines()

    for i, linea in enumerate(lineas):
        if linea.endswith("-") and i < len(lineas) - 1:  
            texto_completo += linea[:-1] 
        else:
            texto_completo += linea + " "  

    
    texto_completo = texto_completo.replace("\n", " ")  
    texto_completo = texto_completo.lower()  
    palabras = re.findall(r'\b[a-záéíóúüñ\-]+\b', texto_completo)  

    return sorted(set(palabras))  

if __name__ == "__main__":
   
    entrada = sys.stdin.read()
    palabras_procesadas = procesar_entrada(entrada)
    for palabra in palabras_procesadas:
        print(palabra)
