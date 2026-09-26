import re

def procesar_texto():
    palabras = set()
    palabra_actual = ""
    
    try:
        while True:
            linea = input().strip()
            if linea.endswith('-'):
                palabra_actual += linea[:-1]
            else:
                palabra_actual += linea
                palabras_en_linea = re.findall(r'[a-zA-Z\-]+', palabra_actual)
                for palabra in palabras_en_linea:
                    palabras.add(palabra.lower())
                palabra_actual = ""
    except EOFError:
        pass
    
    for palabra in sorted(palabras):
        print(palabra)

procesar_texto()
