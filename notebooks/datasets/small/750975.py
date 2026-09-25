import heapq
import sys

input = sys.stdin.read

def procesar_operaciones(data):
    max_heap = []
    resultados = []

    for line in data.strip().splitlines():
        comando = line.split()
        
        if comando[0] == 'S':
            # Insertar el número `-x` para simular un max-heap
            x = int(comando[1])
            heapq.heappush(max_heap, -x)
        
        elif comando[0] == 'A':
            # Mostrar el número más grande
            if max_heap:
                resultados.append(-max_heap[0])
            else:
                resultados.append("Error")
        
        elif comando[0] == 'R':
            # Extraer el número más grande
            if max_heap:
                heapq.heappop(max_heap)
            else:
                resultados.append("Error")
        
        elif comando[0] == 'I':
            # Incrementar el número más grande en `x`
            if max_heap:
                x = int(comando[1])
                max_element = -heapq.heappop(max_heap)
                heapq.heappush(max_heap, -(max_element + x))
            else:
                resultados.append("Error")
        
        elif comando[0] == 'D':
            # Decrementar el número más grande en `x`
            if max_heap:
                x = int(comando[1])
                max_element = -heapq.heappop(max_heap)
                heapq.heappush(max_heap, -(max_element - x))
            else:
                resultados.append("Error")
        
        elif comando[0] == 'T':
            # Terminar la entrada
            break
    
    # Imprimir los resultados de todas las operaciones
    print("\n".join(map(str, resultados)))

# Leer entrada desde el estándar
data = input()
procesar_operaciones(data)
