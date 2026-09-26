import re

linea = input()
solo_letras = re.sub(r'[^a-zA-Z0-9]', '', linea).lower()

es_igual = True
tam = len(solo_letras)
indice = 0
while indice < tam // 2:
    if solo_letras[indice] != solo_letras[tam - indice - 1]:
        es_igual = False
        break
    indice = indice + 1

print("yes" if es_igual else "no")
