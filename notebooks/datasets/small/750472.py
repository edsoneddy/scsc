import sys
import heapq

def procesar_instrucciones(instrucciones):
    max_heap = []  # Cola de prioridad máxima usando valores negativos
    resultados = []

    for instruccion in instrucciones:
        operacion = instruccion[0]
        
        if operacion == "S":
            # Agregar el número x al heap
            x = int(instruccion[1])
            heapq.heappush(max_heap, -x)
        
        elif operacion == "A":
            # Imprimir el número más grande
            if max_heap:
                resultados.append(str(-max_heap[0]))
            else:
                resultados.append("Error")
        
        elif operacion == "R":
            # Extraer el número más grande
            if max_heap:
                heapq.heappop(max_heap)
            else:
                resultados.append("Error")
        
        elif operacion == "I":
            # Incrementar el número más grande en x
            x = int(instruccion[1])
            if max_heap:
                max_value = -heapq.heappop(max_heap)
                heapq.heappush(max_heap, -(max_value + x))
            else:
                resultados.append("Error")
        
        elif operacion == "D":
            # Decrementar el número más grande en x
            x = int(instruccion[1])
            if max_heap:
                max_value = -heapq.heappop(max_heap)
                heapq.heappush(max_heap, -(max_value - x))
            else:
                resultados.append("Error")
        
        elif operacion == "T":
            # Termina la entrada
            break

    return resultados

# Leer las entradas desde stdin y procesarlas
input = sys.stdin.read
instrucciones = [line.strip().split() for line in input().strip().splitlines()]
resultados = procesar_instrucciones(instrucciones)

# Imprimir los resultados
print("\n".join(resultados))