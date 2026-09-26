class Grafo:
    def __init__(self):
        self.ady = {}

    def conectar(self, x, y):
        self.ady.setdefault(x, []).append(y)
        self.ady.setdefault(y, []).append(x)

    def camino_mas_corto(self, ini, fin):
        cola = [ini]
        dist = {ini: 0}
        indice = 0
        while indice < len(cola):
            actual = cola[indice]
            indice += 1
            if actual == fin:
                return dist[actual]
            for vecino in self.ady.get(actual, []):
                if vecino not in dist:
                    dist[vecino] = dist[actual] + 1
                    cola.append(vecino)
        return -1


n_nodos, n_aristas = [int(x) for x in input().split()]
grafo = Grafo()
for _ in range(n_aristas):
    p, q = [int(x) for x in input().split()]
    grafo.conectar(p, q)

inicio, final = [int(x) for x in input().split()]
print(grafo.camino_mas_corto(inicio, final))
