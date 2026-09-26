import math

# Devuelve True si n es primo
def es_primo(n):
    if not n >= 2:
        return False
    for d in range(2, int(math.sqrt(n)) + 1):
        if not n % d:
            return False
    return True

# Descompone n en factores primos
def factorizar(n):
    factores = []
    divisor = 2
    while not n <= 1:
        if n % divisor == 0:
            factores.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factores

numero = int(input())
if es_primo(numero):
    print(numero, "es primo")
else:
    print(numero, "no es primo")
    if 1 < numero:
        fs = factorizar(numero)
        print("Factores:", fs)
        # Formato con exponentes
        partes = []
        for p in sorted(set(fs)):
            partes.append("{}^{}".format(p, fs.count(p)))
        print("Forma:", " * ".join(partes))
