import math

# Devuelve True si n es primo
def comprobar_primo(x):
    if x < 2:
        return False
    for candidato in range(2, int(math.sqrt(x)) + 1):
        if x % candidato == 0:
            return False
    return True

# Descompone n en factores primos
def descomponer(x):
    lista_f = []
    div = 2
    while x > 1:
        if x % div == 0:
            lista_f.append(div)
            x = x // div
        else:
            div += 1
    return lista_f

valor = int(input())
if comprobar_primo(valor):
    print(valor, "es primo")
else:
    print(valor, "no es primo")
    if valor > 1:
        resultado = descomponer(valor)
        print("Factores:", resultado)
        # Formato con exponentes
        trozos = []
        for primo in sorted(set(resultado)):
            trozos.append("{}^{}".format(primo, resultado.count(primo)))
        print("Forma:", " * ".join(trozos))
