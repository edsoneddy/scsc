def mcd(p, q):
    if q == 0:
        return p
    return mcd(q, p % q)

m, n = map(int, input().split())
resultado = mcd(m, n)
print(resultado)
