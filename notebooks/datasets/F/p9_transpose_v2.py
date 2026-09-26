def girar(m):
    return [list(fila) for fila in zip(*m)]


filas, columnas = [int(x) for x in input().split()]
datos = []
for _ in range(filas):
    linea = [int(x) for x in input().split()]
    datos.append(linea)

girada = girar(datos)
for f in girada:
    textos = [str(n) for n in f]
    print(" ".join(textos))
