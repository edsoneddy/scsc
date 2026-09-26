import heapq

def procesar_operaciones(operaciones):
    max_heap = []
    resultados = []

    for operacion in operaciones:
        if operacion.startswith("S "):
            partes = operacion.split(" ")
            x = int(partes[1])
            heapq.heappush(max_heap, -x)
        elif operacion == "A":
            if max_heap:
                resultados.append(str(-max_heap[0]))
            else:
                resultados.append("Error")
        elif operacion == "R":
            if max_heap:
                heapq.heappop(max_heap)
            else:
                resultados.append("Error")
        elif operacion.startswith("I "):
            if max_heap:
                partes = operacion.split(" ")
                x = int(partes[1])
                max_val = -heapq.heappop(max_heap)
                heapq.heappush(max_heap, -(max_val + x))
            else:
                resultados.append("Error")
        elif operacion.startswith("D "):
            if max_heap:
                partes = operacion.split(" ")
                x = int(partes[1])
                max_val = -heapq.heappop(max_heap)
                heapq.heappush(max_heap, -(max_val - x))
            else:
                resultados.append("Error")
        elif operacion == "T":
            break

    return resultados

def main():
    operaciones = []
    while True:
        linea = input().strip()
        operaciones.append(linea)
        if linea == "T":
            break

    resultados = procesar_operaciones(operaciones)
    for resultado in resultados:
        print(resultado)

main()
