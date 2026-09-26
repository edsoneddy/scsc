def generar_parentesis(n, apertura=0, cierre=0, secuencia='', resultados=None):
    if resultados is None:
        resultados = []

    if apertura == n and cierre == n:
        resultados.append(secuencia)
        return

    if apertura < n:
        generar_parentesis(n, apertura + 1, cierre, secuencia + '(', resultados)

    if cierre < apertura:
        generar_parentesis(n, apertura, cierre + 1, secuencia + ')', resultados)

    return resultados

# Código sin datos predefinidos
import sys

for line in sys.stdin:
    n = int(line.strip())
    secuencias = generar_parentesis(n)
    for secuencia in secuencias:
        print(secuencia)
