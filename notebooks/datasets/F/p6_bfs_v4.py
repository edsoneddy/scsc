import heapq

def leer_grafo(cant_aristas):
    adyacencia = {}
    for _ in range(cant_aristas):
        u, v = map(int, input().split())
        adyacencia.setdefault(u, []).append(v)
        adyacencia.setdefault(v, []).append(u)
    return adyacencia

nv, ne = map(int, input().split())
adj = leer_grafo(ne)
src, dst = map(int, input().split())

heap = [(0, src)]
mejor = {src: 0}
resultado = -1
while heap:
    costo, nodo = heapq.heappop(heap)
    if nodo == dst:
        resultado = costo
        break
    if costo > mejor.get(nodo, float('inf')):
        continue
    for vecino in adj.get(nodo, []):
        nuevo_costo = costo + 1
        if nuevo_costo < mejor.get(vecino, float('inf')):
            mejor[vecino] = nuevo_costo
            heapq.heappush(heap, (nuevo_costo, vecino))

print(resultado)
