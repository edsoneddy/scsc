def generar(n):
    def backtrack(s, I, D):
        if len(s) == 2 * n:
            v.append(s)
            return
        if I < n:
            backtrack(s + '(', I + 1, D)
        if D < I:
            backtrack(s + ')', I, D + 1)
 
    v = []
    backtrack('', 0, 0)
    return v
 
try:
    while True:
        n = int(input())
        if 1 <= n <= 10:
            s = generar(n)
            for seq in s:
                print(seq)
except EOFError:
    pass