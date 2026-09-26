def contar_vocales_consonantes(cadena):
    vocales = "aeiouAEIOU"
    letras = [c for c in cadena if c.isalpha()]
    total_v = sum(1 for c in letras if c in vocales)
    total_c = len(letras) - total_v
    return total_v, total_c

texto = input()
nv, nc = contar_vocales_consonantes(texto)
salida = f"{nv} {nc}"
print(salida)
