def ubicar(v, t):
    izq = 0
    der = len(v) - 1
    while True:
        if izq > der:
            return -1
        m = (izq + der) >> 1
        actual = v[m]
        if actual == t:
            return m
        izq, der = (m + 1, der) if actual < t else (izq, m - 1)


tam = int(input())
elementos = input().split()
elementos = [int(e) for e in elementos]
buscar_valor = int(input())
print(ubicar(elementos, buscar_valor))
