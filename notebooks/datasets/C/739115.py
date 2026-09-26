def generar_parentesis(n):
    def backtrack(s, abiertos, cerrados):
        if len(s) == 2 * n:
            secuencias.append(s)
            return
        if abiertos < n:
            backtrack(s + '(', abiertos + 1, cerrados)
        if cerrados < abiertos:
            backtrack(s + ')', abiertos, cerrados + 1)

    secuencias = []
    backtrack('', 0, 0)
    return secuencias

def main():
    import sys
    input = sys.stdin.read
    datos = input().split()
    
    for caso in datos:
        n = int(caso)
        secuencias = generar_parentesis(n)
        for secuencia in secuencias:
            print(secuencia)

if __name__ == "__main__":
    main()
