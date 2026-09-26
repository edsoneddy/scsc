def transponer(matriz):
    return [list(fila) for fila in zip(*matriz)]

nf, nc = map(int, input().split())
matriz = []
for _ in range(nf):
    matriz.append(list(map(int, input().split())))

resultado = transponer(matriz)
lineas = []
for fila in resultado:
    lineas.append(' '.join(map(str, fila)))
print('\n'.join(lineas))
