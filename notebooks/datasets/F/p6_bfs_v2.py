def construir_grafo(aristas):
    g = {}
    for a, b in aristas:
        g.setdefault(a, set()).add(b)
        g.setdefault(b, set()).add(a)
    return g


def distancia_minima(grafo, origen, destino):
    if origen == destino:
        return 0
    frontera = {origen}
    visitados = {origen}
    pasos = 0
    while frontera:
        pasos += 1
        siguiente_frontera = set()
        for nodo in frontera:
            for vecino in grafo.get(nodo, ()):
                if vecino == destino:
                    return pasos
                if vecino not in visitados:
                    visitados.add(vecino)
                    siguiente_frontera.add(vecino)
        frontera = siguiente_frontera
    return -1


vertices, num_aristas = map(int, input().split())
lista_aristas = []
for _ in range(num_aristas):
    u, v = map(int, input().split())
    lista_aristas.append((u, v))
o, d = map(int, input().split())

g = construir_grafo(lista_aristas)
print(distancia_minima(g, o, d))
