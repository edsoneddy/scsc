dims = input().split()
alto = int(dims[0])
ancho = int(dims[1])

tabla = {}
for i in range(alto):
    valores = input().split()
    for j in range(ancho):
        tabla[(i, j)] = int(valores[j])

lineas_salida = []
for j in range(ancho):
    partes = []
    for i in range(alto):
        partes.append(str(tabla[(i, j)]))
    lineas_salida.append(" ".join(partes))

print("\n".join(lineas_salida))
