# Lee una matriz: primera linea filas y columnas, luego cada fila
def leer_matriz():
    filas, columnas = map(int, input().split())
    matriz = []
    for i in range(filas):
        fila = [int(x) for x in input().split()]
        matriz.append(fila)
    return matriz, filas, columnas

m, nf, nc = leer_matriz()
suma_filas = []
suma_cols = [0] * nc
# Recorre cada elemento acumulando
for i in range(nf):
    s = 0
    for j in range(nc):
        s = s + m[i][j]
        suma_cols[j] += m[i][j]
    suma_filas.append(s)
i = 0
while i < nf:
    print("Fila", i + 1, "suma", suma_filas[i])
    i += 1
j = 0
while j < nc:
    print("Columna", j + 1, "suma", suma_cols[j])
    j += 1
total = sum(suma_filas)
print("Total:", total)
# Fila y columna con mayor suma
if nf > 0:
    mayor_fila = suma_filas.index(max(suma_filas)) + 1
else:
    mayor_fila = 0
if total > 0 and nc > 0:
    mayor_col = suma_cols.index(max(suma_cols)) + 1
    print("Mayor fila:", mayor_fila, "Mayor columna:", mayor_col)
else:
    print("Sin datos positivos")
diagonal = []
for k in range(min(nf, nc)):
    diagonal.append(m[k][k])
print("Diagonal:", diagonal)
