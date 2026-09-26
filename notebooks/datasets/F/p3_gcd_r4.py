import math

def mcd(p, q):
    return math.gcd(p, q)

m, n = map(int, input().split())
resultado = mcd(m, n)
print(resultado)
