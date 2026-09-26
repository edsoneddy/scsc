def generar_parens(n, abiertos, cerrados, cadena):

    if abiertos == n and cerrados == n:
        print(cadena)
        return

    if abiertos < n:
        generar_parens(n, abiertos + 1, cerrados, cadena + "(")
 
    if cerrados < abiertos:
        generar_parens(n, abiertos, cerrados + 1, cadena + ")")

import sys
for linea in sys.stdin:
    n = int(linea.strip())
    generar_parens(n, 0, 0, "")
