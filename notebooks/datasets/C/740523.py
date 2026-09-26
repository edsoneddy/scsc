def generar_parentesis(abiertos, cerrados, n, secuencia):
    if abiertos == n and cerrados == n:
        print(secuencia)
        return

    if abiertos < n:
        generar_parentesis(abiertos + 1, cerrados, n, secuencia + "(")

    if cerrados < abiertos:
        generar_parentesis(abiertos, cerrados + 1, n, secuencia + ")")

try:
    while True:
        entrada = input().strip()
        if entrada == "":
            break
        n = int(entrada)

        generar_parentesis(0, 0, n, "")
except EOFError:
    pass