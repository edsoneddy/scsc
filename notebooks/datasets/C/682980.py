def generar_parentesis(balanceados, abiertos, cerrados, n, resultado):
    if len(balanceados) == 2 * n:
        resultado.append(balanceados)
        return
    
    if abiertos < n:
        generar_parentesis(balanceados + '(', abiertos + 1, cerrados, n, resultado)
    if cerrados < abiertos:
        generar_parentesis(balanceados + ')', abiertos, cerrados + 1, n, resultado)

def main():
    import sys
    input = sys.stdin.read
    datos = input().strip().split()
    
    for linea in datos:
        n = int(linea)
        resultado = []
        generar_parentesis("", 0, 0, n, resultado)
        resultado.sort()
        for secuencia in resultado:
            print(secuencia)

if __name__ == "__main__":
    main()
