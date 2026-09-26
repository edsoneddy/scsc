def transponer(matriz):
    columnas = len(matriz[0])
    filas = len(matriz)
    salida = [[matriz[i][j] for i in range(filas)] for j in range(columnas)]
    return salida

nf, nc = map(int, input().split())
matriz = []
for _ in range(nf):
    matriz.append(list(map(int, input().split())))

resultado = transponer(matriz)
lineas = []
for fila in resultado:
    lineas.append(' '.join(map(str, fila)))
print('\n'.join(lineas))
