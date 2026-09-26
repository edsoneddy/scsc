def contar_vocales_consonantes(cadena):
    vocales = "aeiouAEIOU"
    total_v = 0
    total_c = 0
    for letra in cadena:
        if letra.isalpha():
            if letra in vocales:
                total_v += 1
            else:
                total_c += 1
    return total_v, total_c

texto = input()
nv, nc = contar_vocales_consonantes(texto)
print(nv, nc)
