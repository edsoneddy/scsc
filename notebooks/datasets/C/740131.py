def generar_secuencias(abiertos, cerrados, n, secuencia):
    if abiertos == n and cerrados == n:
        print(secuencia)
        return
    if abiertos < n:
        generar_secuencias(abiertos + 1, cerrados, n, secuencia + "(")
    if cerrados < abiertos:
        generar_secuencias(abiertos, cerrados + 1, n, secuencia + ")")
 
while True:
    try:
        n = int(input())
        generar_secuencias(0, 0, n, "")
    except EOFError:
        break
 