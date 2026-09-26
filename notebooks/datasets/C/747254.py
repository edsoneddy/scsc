import heapq

def procesar_operaciones(operaciones):
    max_heap = [] 
    resultados = []

    for operacion in operaciones:
        if operacion.startswith("S "):
            _, x = operacion.split()
            heapq.heappush(max_heap, -int(x))
        elif operacion == "A":
            if max_heap:
                resultados.append(-max_heap[0])
            else:
                resultados.append("Error")
        elif operacion == "R":
            if max_heap:
                heapq.heappop(max_heap)
            else:
                resultados.append("Error")
        elif operacion.startswith("I "):
            if max_heap:
                _, x = operacion.split()
                max_val = -heapq.heappop(max_heap)
                heapq.heappush(max_heap, -(max_val + int(x)))
            else:
                resultados.append("Error")
        elif operacion.startswith("D "):
            if max_heap:
                _, x = operacion.split()
                max_val = -heapq.heappop(max_heap)
                heapq.heappush(max_heap, -(max_val - int(x)))
            else:
                resultados.append("Error")
        elif operacion == "T":
            break

    return resultados

operaciones = []
while True:
    linea = input().strip()
    if linea == "T":
        operaciones.append(linea)
        break
    operaciones.append(linea)
resultados = procesar_operaciones(operaciones)
for resultado in resultados:
    print(resultado)
