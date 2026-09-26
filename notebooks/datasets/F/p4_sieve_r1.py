def criba(limite):
    es_primo = [True] * (limite + 1)
    es_primo[0] = False
    if limite >= 1:
        es_primo[1] = False
    for i in range(2, int(limite ** 0.5) + 1):
        if es_primo[i]:
            for j in range(i * i, limite + 1, i):
                es_primo[j] = False
    salida = []
    for i in range(limite + 1):
        if es_primo[i]:
            salida.append(i)
    return salida

tope = int(input())
lista_primos = criba(tope)
print(' '.join(map(str, lista_primos)))
