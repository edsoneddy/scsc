import sys
import re

def procesar_texto(texto):
    texto_completo = []  
    palabra_actual = ""  

    for linea in texto:
        linea = linea.strip()
        if linea.endswith('-'):  
            palabra_actual += linea[:-1]  
        else:
            palabra_actual += linea  
            texto_completo.append(palabra_actual)  
            palabra_actual = "" 
    palabras = re.findall(r'[a-zA-Z\-]+', " ".join(texto_completo).lower())
    palabras_unicas = sorted(set(palabras)) 
    return palabras_unicas
entrada = sys.stdin.read().splitlines()
resultado = procesar_texto(entrada)
for palabra in resultado:
    print(palabra)
