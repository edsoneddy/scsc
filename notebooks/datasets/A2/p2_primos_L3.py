import math

# Devuelve True si n es primo
def es_primo(n):
    if n < 2:
        return False
    for d in range(2, int(math.sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

# Descompone n en factores primos
def factorizar(n):
    divisor = 2
    factores = list()
    while n > 1:
        if n % divisor == 0:
            factores.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factores

texto = input()
numero = int(texto)
if es_primo(numero):
    print(numero, "es primo")
else:
    print(numero, "no es primo")
    if numero > 1:
        fs = factorizar(numero)
        print("Factores:", fs)
        # Formato con exponentes
        partes = list()
        for p in sorted(set(fs)):
            partes.append("{}^{}".format(p, fs.count(p)))
        print("Forma:", " * ".join(partes))
