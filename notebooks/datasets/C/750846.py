def generar_parentesis(n, abiertos=0, cerrados=0, secuencia="", resultados=None):
    if resultados is None:
        resultados = []
    

    if abiertos == n and cerrados == n:
        resultados.append(secuencia)
        return
    

    if abiertos < n:
        generar_parentesis(n, abiertos + 1, cerrados, secuencia + "(", resultados)
    

    if cerrados < abiertos:
        generar_parentesis(n, abiertos, cerrados + 1, secuencia + ")", resultados)
    
    return resultados


import sys

for line in sys.stdin:
    n = int(line.strip())
    resultados = generar_parentesis(n)
    for secuencia in resultados:
        print(secuencia)