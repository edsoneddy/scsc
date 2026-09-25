import heapq
import sys

def procesar_instrucciones(instrucciones):
    max_heap = []
    resultados = []
    
    for instruccion in instrucciones:
        comando = instruccion[0]
        
        if comando == 'S':
            # Guardar el número x en el heap como negativo (para simular un max-heap)
            x = int(instruccion[1])
            heapq.heappush(max_heap, -x)
            
        elif comando == 'A':
            if max_heap:
                # Obtener el valor más grande (invertir el signo para mostrar el valor real)
                resultados.append(-max_heap[0])
            else:
                resultados.append("Error")
                
        elif comando == 'R':
            if max_heap:
                # Remover el número más grande (invertir el signo para obtener el valor real)
                heapq.heappop(max_heap)
            else:
                resultados.append("Error")
                
        elif comando == 'I':
            if max_heap:
                # Incrementar el número más grande
                x = int(instruccion[1])
                max_val = -heapq.heappop(max_heap)
                max_val += x
                heapq.heappush(max_heap, -max_val)
            else:
                resultados.append("Error")
                
        elif comando == 'D':
            if max_heap:
                # Decrementar el número más grande
                x = int(instruccion[1])
                max_val = -heapq.heappop(max_heap)
                max_val -= x
                heapq.heappush(max_heap, -max_val)
            else:
                resultados.append("Error")
                
        elif comando == 'T':
            break
    
    return resultados

# Lectura de entrada
instrucciones = []
for line in sys.stdin:
    instruccion = line.strip().split()
    instrucciones.append(instruccion)

# Procesar y mostrar resultados
resultados = procesar_instrucciones(instrucciones)
for resultado in resultados:
    print(resultado)
