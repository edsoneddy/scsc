import heapq
import sys

def procesar_comandos(comandos):
    max_heap = []  # Simularemos un max-heap usando valores negativos
    resultados = []
    
    for comando in comandos:
        partes = comando.split()
        operacion = partes[0]
        
        if operacion == 'S':
            # Guardar el valor en el heap
            x = int(partes[1])
            heapq.heappush(max_heap, -x)
        
        elif operacion == 'A':
            # Imprimir el número más grande
            if max_heap:
                resultados.append(-max_heap[0])
            else:
                resultados.append("Error")
        
        elif operacion == 'R':
            # Extraer el número más grande
            if max_heap:
                heapq.heappop(max_heap)
            else:
                resultados.append("Error")
        
        elif operacion == 'I':
            # Incrementar el número más grande en x
            if max_heap:
                x = int(partes[1])
                max_value = -heapq.heappop(max_heap)
                max_value += x
                heapq.heappush(max_heap, -max_value)
            else:
                resultados.append("Error")
        
        elif operacion == 'D':
            # Decrementar el número más grande en x
            if max_heap:
                x = int(partes[1])
                max_value = -heapq.heappop(max_heap)
                max_value -= x
                heapq.heappush(max_heap, -max_value)
            else:
                resultados.append("Error")
        
        elif operacion == 'T':
            break
    
    return resultados

# Lectura de entrada
comandos = []
for linea in sys.stdin:
    comandos.append(linea.strip())

# Procesar comandos y mostrar resultados
resultados = procesar_comandos(comandos)
for resultado in resultados:
    print(resultado)
