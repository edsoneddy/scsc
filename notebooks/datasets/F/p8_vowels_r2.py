def contar_vocales_consonantes(cadena):
    vocales = "aeiouAEIOU"
    total_c = 0
    total_v = 0
    for letra in cadena:
        if letra.isalpha():
            if letra not in vocales:
                total_c += 1
            else:
                total_v += 1
    return total_v, total_c

texto = input()
nv, nc = contar_vocales_consonantes(texto)
salida = f"{nv} {nc}"
print(salida)
