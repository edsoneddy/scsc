def generaParen(abierto, cerrado, n, sec, resultados):
    if abierto == cerrado == n:
        resultados.append(sec)
        return
    if abierto < n:
        generaParen(abierto + 1, cerrado, n, sec + '(', resultados)
    if cerrado < abierto:
        generaParen(abierto, cerrado + 1, n, sec + ')', resultados)
while True:
    try:
        n = int(input())
        resultados = []
        generaParen(0, 0, n, '', resultados)
        resultados.sort()
        for sec in resultados:
            print(sec)
    except EOFError:
        break
