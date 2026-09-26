import heapq
 
def procesar_operaciones(operaciones):
    heap = []
    for operacion in operaciones:
        if operacion[0] == 'S':
            heapq.heappush(heap, -int(operacion[2:]))
        elif operacion == 'A':
            if not heap:
                print("Error")
            else:
                print(-heap[0])
        elif operacion == 'R':
            if not heap:
                print("Error")
            else:
                heapq.heappop(heap)
        elif operacion[0] == 'I':
            if not heap:
                print("Error")
            else:
                x = int(operacion[2:])
                heapq.heapreplace(heap, -(-heap[0] + x))
        elif operacion[0] == 'D':
            if not heap:
                print("Error")
            else:
                x = int(operacion[2:])
                heapq.heapreplace(heap, -(-heap[0] - x))
        elif operacion == 'T':
            break
operaciones = []
while True:
    try:
        operacion = input().strip()
        if operacion == 'T':
            break
        operaciones.append(operacion)
    except EOFError:
        break
 
procesar_operaciones(operaciones)