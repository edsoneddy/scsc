def g(n):
    def b(s, l, r):
        if len(s) == 2 * n:
            res.append(s)
            return
        if l < n:
            b(s + '(', l + 1, r)
        if r < l:
            b(s + ')', l, r + 1)
 
    res = []
    b('', 0, 0)
    return res
 
try:
    while True:
        n = int(input())
        if 1 <= n <= 10:
            seqs = g(n)
            for seq in seqs:
                print(seq)
except EOFError:
    pass
