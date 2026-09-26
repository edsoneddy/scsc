def clasificar(cadena):
    vocales = set("aeiouAEIOU")
    total_vocales = sum(1 for letra in cadena if letra.isalpha() and letra in vocales)
    total_consonantes = sum(1 for letra in cadena if letra.isalpha() and letra not in vocales)
    return total_vocales, total_consonantes


linea = input()
nv, nc = clasificar(linea)
print(f"{nv} {nc}")
