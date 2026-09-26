def generar_parentesis(n):
    def backtrack(combinacion, abre, cierra):
        if len(combinacion) == 2 * n:
            r.append(combinacion)
            return
        if abre < n:
            backtrack(combinacion + '(', abre + 1, cierra)
        if cierra < abre:
            backtrack(combinacion + ')', abre, cierra + 1)

    r = []
    backtrack('', 0, 0)
    return r


import sys
for linea in sys.stdin:
    if linea == "\n":
        break
    n = int(linea)
    caminos = generar_parentesis(n)
    for i, camino in enumerate(caminos, 1):
        print(f"{camino}")