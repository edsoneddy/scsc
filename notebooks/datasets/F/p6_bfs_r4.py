import heapq

def distancia_bfs(grafo, origen, destino):
    mejor = {origen: 0}
    monticulo = [(0, origen)]
    while monticulo:
        dist, nodo = heapq.heappop(monticulo)
        if nodo == destino:
            return dist
        if dist > mejor.get(nodo, float('inf')):
            continue
        for vecino in grafo.get(nodo, []):
            nueva_dist = dist + 1
            if nueva_dist < mejor.get(vecino, float('inf')):
                mejor[vecino] = nueva_dist
                heapq.heappush(monticulo, (nueva_dist, vecino))
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
