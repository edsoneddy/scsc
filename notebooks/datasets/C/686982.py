def generar_secuencias_par(n, secuencia="", abiertos=0, cerrados=0):
    if len(secuencia) == 2 * n:
        print(secuencia)
        return
    if abiertos < n:
        generar_secuencias_par(n, secuencia + '(', abiertos + 1, cerrados)
    
    if cerrados < abiertos:
        generar_secuencias_par(n, secuencia + ')', abiertos, cerrados + 1)
while True:
    try:
        n = int(input())
        generar_secuencias_par(n)
    except EOFError:
        break