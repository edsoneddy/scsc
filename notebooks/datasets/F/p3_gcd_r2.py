def mcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p

m, n = map(int, input().split())
resultado = mcd(m, n)
print(resultado)
