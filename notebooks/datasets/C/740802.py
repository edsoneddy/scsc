def gen(a, c, n, s):
    if a == n and c == n:
        print(s)
        return
    if a < n:
        gen(a + 1, c, n, s + "(")
    if c < a:
        gen(a, c + 1, n, s + ")")
try:
    while True:
        x = input().strip()
        if x == "":
            break
        enie = int(x)
        gen(0, 0, enie, "")
except EOFError:
    pass