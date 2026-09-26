# Lee una matriz: primera linea filas y columnas, luego cada fila
def cargar():
    nfilas, ncols = map(int, input().split())
    mat = []
    for r in range(nfilas):
        renglon = [int(v) for v in input().split()]
        mat.append(renglon)
    return mat, nfilas, ncols

grid, R, C = cargar()
sf = []
sc = [0] * C
# Recorre cada elemento acumulando
for r in range(R):
    acc = 0
    for c in range(C):
        acc += grid[r][c]
        sc[c] += grid[r][c]
    sf.append(acc)
for r in range(R):
    print("Fila", r + 1, "suma", sf[r])
for c in range(C):
    print("Columna", c + 1, "suma", sc[c])
gran_total = sum(sf)
print("Total:", gran_total)
# Fila y columna con mayor suma
mf = sf.index(max(sf)) + 1 if R > 0 else 0
if gran_total > 0 and C > 0:
    mc = sc.index(max(sc)) + 1
    print("Mayor fila:", mf, "Mayor columna:", mc)
else:
    print("Sin datos positivos")
diag = [grid[d][d] for d in range(min(R, C))]
print("Diagonal:", diag)
