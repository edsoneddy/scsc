import sys
import re

def ent():
    palabras = []
    palabra_actual = ""
    
    for linea in sys.stdin:
        linea = linea.strip()
   
        if linea.endswith("-"):
            palabra_actual += linea[:-1]
        else:
            palabra_actual += linea
            
            
            nuevas_palabras = re.findall(r"[a-zA-Z\-]+", palabra_actual)
            palabras.extend(nuevas_palabras)
            palabra_actual = ""

    palabras_unicas = sorted(set(palabra.lower() for palabra in palabras))
    return palabras_unicas


resultado = ent()

print("\n".join(resultado))
