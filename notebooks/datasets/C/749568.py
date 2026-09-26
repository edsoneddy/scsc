def generar_parentesis(n, apertura=0, cierre=0, secuencia='', resultados=[]):
    if len(secuencia) == 2 * n:
        resultados.append(secuencia)
        return

    if apertura < n:
        generar_parentesis(n, apertura + 1, cierre, secuencia + '(', resultados)

    
    if cierre < apertura:
        generar_parentesis(n, apertura, cierre + 1, secuencia + ')', resultados)

def main():
    import sys
    input = sys.stdin.read
    datos = input().strip().splitlines()
    
    for linea in datos:
        n = int(linea)
        resultados = []
        generar_parentesis(n, resultados=resultados)
        for secuencia in resultados:
            print(secuencia)

if __name__ == "__main__":
    main()