def criba(limite):
    es_primo = [True] * (limite + 1)
    i = 2
    while i * i <= limite:
        if es_primo[i]:
            for j in range(i * i, limite + 1, i):
                es_primo[j] = False
        i += 1
    if limite >= 1:
        es_primo[1] = False
    es_primo[0] = False
    return [k for k in range(limite + 1) if es_primo[k]]

tope = int(input())
lista_primos = criba(tope)
resultado_texto = ' '.join(map(str, lista_primos))
print(resultado_texto)
