def generador_parentesis(n):
    def backtrack(s, izq, der):
        if len(s) == 2 * n:
            resultado.append(s)
            return
        if izq < n:
            stack.append('(')
            backtrack(s + '(', izq + 1, der)
            stack.pop()
        if der < izq and stack:
            stack.pop()
            backtrack(s + ')', izq, der + 1)
            stack.append('(')

    resultado = []
    stack = []
    backtrack('', 0, 0)
    return sorted(resultado)


while True:
    try:
        n = int(input())
        secuencia = generador_parentesis(n)
        for sec in secuencia:
            print(sec)
    except EOFError:
        break