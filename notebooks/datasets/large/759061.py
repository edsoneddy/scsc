import sys
import re

def analizar_texto():
    vocabulario = set()
    palabra_temporal = ""
    
    for linea in sys.stdin:
        linea = linea.strip().lower()
        if linea.endswith('-'):
            palabra_temporal += linea[:-1]
        else:
            palabra_temporal += linea
            for termino in re.findall(r'\b[a-z-]+\b', palabra_temporal):
                vocabulario.add(termino)
            palabra_temporal = ""
    
    lista_palabras = sorted(vocabulario)
    for termino in lista_palabras:
        print(termino)

if __name__ == "__main__":
    analizar_texto()
