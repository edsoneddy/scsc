def Secuencias(n, secuencia='', abiertos=0, cerrados=0):
    if len(secuencia) == 2 * n:
        print(secuencia)
        return
    if abiertos < n:
        Secuencias(n, secuencia + '(', abiertos + 1, cerrados)
    if cerrados < abiertos:
        Secuencias(n, secuencia + ')', abiertos, cerrados + 1)

while True:
    try:
        n = int(input())
        Secuencias(n)
    except EOFError:
        break