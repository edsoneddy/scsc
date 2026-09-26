def combinar(x, y):
    salida = []
    q = 0
    p = 0
    while p < len(x) and q < len(y):
        if x[p] <= y[q]:
            salida.append(x[p])
            p += 1
        else:
            salida.append(y[q])
            q += 1
    salida.extend(y[q:])
    salida.extend(x[p:])
    return salida

primera = list(map(int, input().split()))
segunda = list(map(int, input().split()))
resultado = combinar(primera, segunda)
texto = ' '.join(map(str, resultado))
print(texto)
