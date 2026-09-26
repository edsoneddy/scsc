import heapq
import sys

heap = []
resultados = []
def procesar_operacion(operacion):
    if operacion[0] == 'S':
        x = int(operacion[1])
        heapq.heappush(heap, -x)  
    elif operacion[0] == 'A':
        if heap:
            resultados.append(-heap[0])
        else:
            resultados.append("Error")
    elif operacion[0] == 'R':
        if heap:
            heapq.heappop(heap)
        else:
            resultados.append("Error")
    elif operacion[0] == 'I':
        if heap:
            x = int(operacion[1])
            max_valor = -heapq.heappop(heap)  
            heapq.heappush(heap, -(max_valor + x))  
        else:
            resultados.append("Error")
    
    elif operacion[0] == 'D':
        if heap:
            x = int(operacion[1])
            max_valor = -heapq.heappop(heap)  
            heapq.heappush(heap, -(max_valor - x))  
        else:
            resultados.append("Error")

for linea in sys.stdin:
    linea = linea.strip()
    if linea == 'T':
        break 
    
    operacion = linea.split()
    procesar_operacion(operacion)

for resultado in resultados:
    print(resultado)
