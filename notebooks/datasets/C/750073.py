def generar_secuencias_par(n):
    def backtrack(s='', abiertos=0, cerrados=0):
        if len(s) == 2 * n:
            secuencias.append(s)
            return
        if abiertos < n:
            backtrack(s + '(', abiertos + 1, cerrados)
        if cerrados < abiertos:
            backtrack(s + ')', abiertos, cerrados + 1)

    secuencias = []
    backtrack()
    return secuencias

import sys

# Leer entrada
input = sys.stdin.read
datos = input().split()

# Generar y mostrar secuencias de paréntesis
for dato in datos:
    n = int(dato)
    secuencias = generar_secuencias_par(n)
    for secuencia in secuencias:
        print(secuencia)
