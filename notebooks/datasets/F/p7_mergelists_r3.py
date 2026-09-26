def combinar(x, y):
    if not x:
        return list(y)
    if not y:
        return list(x)
    if x[0] <= y[0]:
        return [x[0]] + combinar(x[1:], y)
    return [y[0]] + combinar(x, y[1:])

primera = list(map(int, input().split()))
segunda = list(map(int, input().split()))
resultado = combinar(primera, segunda)
texto = ' '.join(map(str, resultado))
print(texto)
