def generar_parentesis(n, secuencia="", abiertos=0, cerrados=0):
    if len(secuencia) == 2 * n:
        print(secuencia)
        return
    if abiertos < n:
        generar_parentesis(n, secuencia + "(", abiertos + 1, cerrados)
    if cerrados < abiertos:
        generar_parentesis(n, secuencia + ")", abiertos, cerrados + 1)
import sys
for linea in sys.stdin:
    if linea.strip():
        n = int(linea.strip())
        generar_parentesis(n)
