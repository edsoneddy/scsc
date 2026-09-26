def generar_parentesis(abiertos, cerrados, total, secuencia):
    if abiertos == total and cerrados == total:
        print(secuencia)
        return

    if abiertos < total:
        generar_parentesis(abiertos + 1, cerrados, total, secuencia + "(")

    if cerrados < abiertos:
        generar_parentesis(abiertos, cerrados + 1, total, secuencia + ")")

try:
    while True:
        entrada = input().strip()
        if entrada == "":
            break
        cantidad = int(entrada)
        generar_parentesis(0, 0, cantidad, "")
except EOFError:
    pass
