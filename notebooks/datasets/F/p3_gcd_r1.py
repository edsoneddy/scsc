def mcd(p, q):
    while q != 0:
        resto = p % q
        p = q
        q = resto
    return p

m, n = map(int, input().split())
print(mcd(m, n))
