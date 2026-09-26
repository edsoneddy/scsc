def generar_parentesis(n):
    def backtrack(s, abiertos, cerrados):
        if len(s) == 2 * n:
            resultados.append(s)
            return
        if abiertos < n:
            backtrack(s + '(', abiertos + 1, cerrados)
        if cerrados < abiertos:
            backtrack(s + ')', abiertos, cerrados + 1)
    
    resultados = []
    backtrack('', 0, 0)
    return resultados

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    for linea in data:
        n = int(linea)
        secuencias = generar_parentesis(n)
        for secuencia in secuencias:
            print(secuencia)

if __name__ == "__main__":
    main()