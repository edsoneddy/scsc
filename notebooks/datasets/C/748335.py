def generar_parentesis(n, abiertos, cerrados, secuencia_actual):
    if abiertos == 0 and cerrados == 0:
        print(secuencia_actual)
        return
    if abiertos > 0:
        generar_parentesis(n, abiertos - 1, cerrados, secuencia_actual + "(")
    if cerrados > abiertos:
        generar_parentesis(n, abiertos, cerrados - 1, secuencia_actual + ")")

try:
    while True:
        n = int(input().strip())
        generar_parentesis(n, n, n, "")
except EOFError:
    pass
