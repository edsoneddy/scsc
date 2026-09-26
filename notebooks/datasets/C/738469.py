def generar_parentesis(n):
    def backtrack(s, abiertos, cerrados):
        if len(s) == 2 * n:
            print(s)
            return
        if abiertos < n:
            backtrack(s + '(', abiertos + 1, cerrados)
        if cerrados < abiertos:
            backtrack(s + ')', abiertos, cerrados + 1)
    backtrack('', 0, 0)


while True:
    try:
        n = int(input().strip())  
        generar_parentesis(n)
    except EOFError:  
        break
