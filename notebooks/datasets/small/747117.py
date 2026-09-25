import heapq
import sys

def coleccion_numeros():
    heap = []
    resultados = []

    while True:
        linea = input().strip()
        if linea == 'T':
            break
        operacion = linea.split()
        comando = operacion[0]

        if comando == 'S':
            x = int(operacion[1])
            heapq.heappush(heap, -x)

        elif comando == 'A':
            if heap:
                resultados.append(-heap[0])
            else:
                resultados.append("Error")

        elif comando == 'R':
            if heap:
                heapq.heappop(heap)
            else:
                resultados.append("Error")

        elif comando == 'I':
            if heap:
                x = int(operacion[1])
                max_actual = -heapq.heappop(heap)
                heapq.heappush(heap, -(max_actual + x))
            else:
                resultados.append("Error")

        elif comando == 'D':
            if heap:
                x = int(operacion[1])
                max_actual = -heapq.heappop(heap)
                heapq.heappush(heap, -(max_actual - x))
            else:
                resultados.append("Error")

    print("\n".join(map(str, resultados)))

coleccion_numeros()
