import math

# Devuelve True si n es primo
def es_primo(n):
    if n < 2:
        return False
    d = 2
    while d <= int(math.sqrt(n)):
        if n % d == 0:
            return False
        d += 1
    return True

# Descompone n en factores primos
def factorizar(n):
    factores = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        else:
            divisor = divisor + 1
    return factores

numero = int(input())
if es_primo(numero):
    print(numero, "es primo")
else:
    print(numero, "no es primo")
    if numero > 1:
        fs = factorizar(numero)
        print("Factores:", fs)
        # Formato con exponentes
        partes = []
        for p in sorted(set(fs)):
            partes += ["{}^{}".format(p, fs.count(p))]
        print("Forma:", " * ".join(partes))
