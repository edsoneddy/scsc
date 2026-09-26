class Matriz:
    def __init__(self, datos):
        self.datos = datos
        self.n_filas = len(datos)
        self.n_cols = len(datos[0]) if datos else 0

    def traspuesta(self):
        salida = []
        col = 0
        while col < self.n_cols:
            nueva_fila = []
            fila = 0
            while fila < self.n_filas:
                nueva_fila.append(self.datos[fila][col])
                fila += 1
            salida.append(nueva_fila)
            col += 1
        return salida


nr, nc = map(int, input().split())
contenido = [list(map(int, input().split())) for _ in range(nr)]
m = Matriz(contenido)
for fila in m.traspuesta():
    print(' '.join(str(x) for x in fila))
