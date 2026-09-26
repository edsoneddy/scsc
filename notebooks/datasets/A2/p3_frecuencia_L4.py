import re

# Convierte el texto en lista de palabras en minuscula
def obtener_palabras(texto):
    palabras = re.findall(r"[a-zA-Z]+", texto)
    resultado = []
    for p in palabras:
        resultado.append(p.lower())
    return resultado

def contar(lista):
    frecuencia = {}
    # Cuenta cada palabra
    for palabra in lista:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

def mas_larga(lista):
    largo = ""
    for palabra in lista:
        if len(palabra) > len(largo):
            largo = palabra
    return largo

texto = input()
lista = obtener_palabras(texto)
frecuencia = contar(lista)
# Ordena por frecuencia descendente y luego alfabeticamente
items = sorted(frecuencia.items(), key=lambda par: (-par[1], par[0]))
print("Palabras totales:", len(lista))
print("Palabras distintas:", len(frecuencia))
for palabra, cuenta in items:
    print(palabra + ": " + str(cuenta))
# Palabra mas comun
if len(items) > 0:
    print("Mas comun:", items[0][0])
    print("Mas larga:", mas_larga(lista))
