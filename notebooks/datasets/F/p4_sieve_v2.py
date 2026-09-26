def es_primo(numero):
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True

limite = int(input())
lista_primos = []
for candidato in range(limite + 1):
    if es_primo(candidato):
        lista_primos.append(str(candidato))

print(' '.join(lista_primos))
