def transponer(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    salida = [[0] * filas for _ in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            salida[j][i] = matriz[i][j]
    return salida

nf, nc = map(int, input().split())
matriz = []
for _ in range(nf):
    matriz.append(list(map(int, input().split())))

resultado = transponer(matriz)
for fila in resultado:
    print(' '.join(map(str, fila)))
