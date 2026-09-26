def generar_parentesis(n, apertura=0, cierre=0, secuencia="", resultado=None):
    if resultado is None:
        resultado = []
    
    if apertura == n and cierre == n:
        resultado.append(secuencia)
        return
    
    if apertura < n:
        generar_parentesis(n, apertura + 1, cierre, secuencia + '(', resultado)
    
    if cierre < apertura:
        generar_parentesis(n, apertura, cierre + 1, secuencia + ')', resultado)
    
    return resultado

def main():
    import sys
    for line in sys.stdin:
        n = int(line.strip())
        resultados = generar_parentesis(n)
        for secuencia in resultados:
            print(secuencia)

if __name__ == "__main__":
    main()
