def generar_parentesis(n, apertura=0, cierre=0, secuencia='', resultados=None):
    if resultados is None:
        resultados = []
    
    if apertura == n and cierre == n:
        resultados.append(secuencia)
        return
    
    if apertura < n:
        generar_parentesis(n, apertura + 1, cierre, secuencia + '(', resultados)
    
    if cierre < apertura:
        generar_parentesis(n, apertura, cierre + 1, secuencia + ')', resultados)
    
    return resultados

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    for line in data:
        n = int(line)
        resultados = generar_parentesis(n)
        for secuencia in resultados:
            print(secuencia)

if __name__ == "__main__":
    main()