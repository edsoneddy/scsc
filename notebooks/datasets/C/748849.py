import heapq
import sys
input = sys.stdin.read

def procesar_instrucciones(instrucciones):
    heap = []
    resultados = []
    for instruccion in instrucciones:
        partes = instruccion.split()
        operacion = partes[0]
        
        if operacion == "S":
            x = int(partes[1])
            heapq.heappush(heap, -x) 
            
        elif operacion == "A":
            if heap:
                resultados.append(-heap[0])
            else:
                resultados.append("Error")
                
        elif operacion == "R":
            if heap:
                heapq.heappop(heap)
            else:
                resultados.append("Error")
                
        elif operacion == "I":
            if heap:
                x = int(partes[1])
                maximo_actual = -heapq.heappop(heap) 
                heapq.heappush(heap, -(maximo_actual + x)) 
            else:
                resultados.append("Error")
                
        elif operacion == "D":
            if heap:
                x = int(partes[1])
                maximo_actual = -heapq.heappop(heap) 
                heapq.heappush(heap, -(maximo_actual - x))  
            else:
                resultados.append("Error")
                
        elif operacion == "T":
            break
    for resultado in resultados:
        print(resultado)
entrada = input().strip().splitlines()
procesar_instrucciones(entrada)
