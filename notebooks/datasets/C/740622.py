def generar_parentesis(n, apertura, cierre, secuencia, resultados):
    if apertura == n and cierre == n:
        resultados.append(secuencia)
        return
    
    if apertura < n:
        generar_parentesis(n, apertura + 1, cierre, secuencia + '(', resultados)
    if cierre < apertura:
        generar_parentesis(n, apertura, cierre + 1, secuencia + ')', resultados)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    for linea in data:
        n = int(linea)
        resultados = []
        generar_parentesis(n, 0, 0, '', resultados)
        
        for secuencia in resultados:
            print(secuencia)

if __name__ == "__main__":
    main()
