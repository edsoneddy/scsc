def generar_parentesis(abiertos, cerrados, actual, resultado):
    if abiertos == 0 and cerrados == 0:
        resultado.append(actual)
        return


    if abiertos > 0:
        generar_parentesis(abiertos - 1, cerrados, actual + '(', resultado)

    if cerrados > abiertos:
        generar_parentesis(abiertos, cerrados - 1, actual + ')', resultado)

def generar_todas_secuencias(n):
    resultado = []
    generar_parentesis(n, n, '', resultado)
    return resultado

import sys
for linea in sys.stdin:
    n = int(linea.strip())
    secuencias = generar_todas_secuencias(n)
    for secuencia in secuencias:
        print(secuencia)
