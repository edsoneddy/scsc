def generar_parentesis(n):
    def backtrack(s='', abiertos=0, cerrados=0):
        if len(s) == 2 * n:
            print(s)
            return
        if abiertos < n:
            backtrack(s + '(', abiertos + 1, cerrados)
        if cerrados < abiertos:
            backtrack(s + ')', abiertos, cerrados + 1)

    backtrack()

# Leer múltiples casos de prueba hasta EOF
import sys

for line in sys.stdin:
    n = int(line.strip())
    generar_parentesis(n)