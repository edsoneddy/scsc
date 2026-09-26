import re

# Convierte el texto en lista de palabras en minuscula
def extraer(cadena):
    tokens = re.findall(r"[a-zA-Z]+", cadena)
    salida = []
    for w in tokens:
        salida.append(w.lower())
    return salida

cadena = input()
todas = extraer(cadena)
contador = {}
# Cuenta cada palabra
for word in todas:
    if word in contador:
        contador[word] += 1
    else:
        contador[word] = 1
# Ordena por frecuencia descendente y luego alfabeticamente
ordenados = sorted(contador.items(), key=lambda pair: (-pair[1], pair[0]))
print("Palabras totales:", len(todas))
print("Palabras distintas:", len(contador))
for word, veces in ordenados:
    print(word + ": " + str(veces))
# Palabra mas comun
if len(ordenados) > 0:
    print("Mas comun:", ordenados[0][0])
    mayor = ""
    for word in todas:
        if len(word) > len(mayor):
            mayor = word
    print("Mas larga:", mayor)
