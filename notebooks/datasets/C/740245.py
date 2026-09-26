def generar_parentesis(n, abierto=0, cerrado=0, secuencia="", resultados=[]):
    if len(secuencia) == 2 * n:
        resultados.append(secuencia)
        return
    
    if abierto < n:
        generar_parentesis(n, abierto + 1, cerrado, secuencia + "(", resultados)
    
    if cerrado < abierto:
        generar_parentesis(n, abierto, cerrado + 1, secuencia + ")", resultados)

def imprimir_secuencias_parentesis(n):
    resultados = []
    generar_parentesis(n, 0, 0, "", resultados)
    for secuencia in resultados:
        print(secuencia)

if __name__ == "__main__":
    import sys
    for linea in sys.stdin:
        n = int(linea.strip())
        imprimir_secuencias_parentesis(n)
