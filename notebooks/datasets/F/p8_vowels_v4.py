import re

palabra = input()
letras = re.findall(r'[A-Za-z]', palabra)
mapa_vocal = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}

vy = 0
co = 0
for l in letras:
    if mapa_vocal.get(l.lower()):
        vy = vy + 1
    else:
        co = co + 1

resultado = str(vy) + " " + str(co)
print(resultado)
