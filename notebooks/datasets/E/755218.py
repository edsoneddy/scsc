import re

palabras = set()
palabra_actual = ''

try:
    while True:
        linea = input().strip().lower()
        if linea.endswith('-'):
            palabra_actual += linea[:-1]
        else:
            palabra_actual += linea
            for palabra in re.findall(r'[a-z\-]+', palabra_actual):
                palabras.add(palabra)
            palabra_actual = ''

except EOFError:
    palabras_ordenadas = sorted(palabras)
    for palabra in palabras_ordenadas:
        print(palabra)
