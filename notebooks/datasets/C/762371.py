def generar_parentecis(n):
    def backtrack(s, izq, der):
        if len(s) == 2 * n:
            r.append(s)
            return
        if izq < n:
            backtrack(s + '(', izq + 1, der)
        if der < izq:
            backtrack(s + ')', izq, der + 1)
 
    r = []
    backtrack('', 0, 0)
    return r
 
try:
    while True:
        n = int(input())
        if 1 <= n <= 10:
            v = generar_parentecis(n)
            for seq in v:
                print(seq)
except EOFError:
    pass
 
 