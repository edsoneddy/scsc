def generar_parentesis(n):
    resultado = []
    stack = []

    def backtrack(apertura, cierre):
        if apertura == n and cierre == n:
            resultado.append(''.join(stack))
            return
        
        if apertura < n:
            stack.append('(')
            backtrack(apertura + 1, cierre)
            stack.pop()

        if cierre < apertura:
            stack.append(')')
            backtrack(apertura, cierre + 1)
            stack.pop()

    backtrack(0, 0)
    return resultado

def main():
    import sys
    for line in sys.stdin:
        n = int(line.strip())
        resultados = generar_parentesis(n)
        print('\n'.join(resultados))

if __name__ == "__main__":
    main()
