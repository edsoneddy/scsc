import sys
input = sys.stdin.read

def generar_parentesis(n, secuencia="", abiertos=0, cerrados=0, resultado=None):
    if resultado is None:
        resultado = []
    
    # Condición de parada: secuencia completa de longitud 2n
    if abiertos == n and cerrados == n:
        resultado.append(secuencia)
        return

    # Backtracking con pila: Agregamos `(` si quedan por abrir
    if abiertos < n:
        generar_parentesis(n, secuencia + "(", abiertos + 1, cerrados, resultado)
    
    # Agregamos `)` si cerrados < abiertos (para balancear)
    if cerrados < abiertos:
        generar_parentesis(n, secuencia + ")", abiertos, cerrados + 1, resultado)

    return resultado

def procesar_entrada():
    data = input().strip().splitlines()
    for linea in data:
        n = int(linea)
        combinaciones = generar_parentesis(n)
        print("\n".join(combinaciones))

procesar_entrada()
