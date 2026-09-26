from collections import deque

def distancia_bfs(grafo, origen, destino):
    visitados = {origen}
    cola = deque([(origen, 0)])
    while cola:
        nodo, dist = cola.popleft()
        if nodo == destino:
            return dist
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((vecino, dist + 1))
    return -1

nv, na = map(int, input().split())
grafo = {}
for _ in range(na):
    u, v = map(int, input().split())
    grafo.setdefault(v, []).append(u)
    grafo.setdefault(u, []).append(v)
origen, destino = map(int, input().split())
resultado = distancia_bfs(grafo, origen, destino)
print(resultado)
