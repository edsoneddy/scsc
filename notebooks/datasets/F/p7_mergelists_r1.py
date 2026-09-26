def combinar(x, y):
    salida = []
    p = 0
    q = 0
    while p < len(x) and q < len(y):
        if x[p] <= y[q]:
            salida.append(x[p])
            p += 1
        else:
            salida.append(y[q])
            q += 1
    salida.extend(x[p:])
    salida.extend(y[q:])
    return salida

primera = list(map(int, input().split()))
segunda = list(map(int, input().split()))
resultado = combinar(primera, segunda)
print(' '.join(map(str, resultado)))
