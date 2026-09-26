import sys
import heapq

def identificar_estructura(operaciones):
    stack = []
    queue = []
    priority_queue = []
    
    es_pila = True
    es_cola = True
    es_cola_prioridad = True
    
    for operacion, x in operaciones:
        if operacion == 1:  # Inserción
            stack.append(x)
            queue.append(x)
            heapq.heappush(priority_queue, -x)  # Usamos valores negativos para simular una cola de prioridad max
            
        elif operacion == 2:  # Extracción
            if es_pila:
                if stack and stack[-1] == x:
                    stack.pop()
                else:
                    es_pila = False
            
            if es_cola:
                if queue and queue[0] == x:
                    queue.pop(0)
                else:
                    es_cola = False
            
            if es_cola_prioridad:
                if priority_queue and -priority_queue[0] == x:
                    heapq.heappop(priority_queue)
                else:
                    es_cola_prioridad = False
    
    # Determinar el resultado
    posibles = [es_pila, es_cola, es_cola_prioridad]
    cantidad_verdaderos = posibles.count(True)
    
    if cantidad_verdaderos == 0:
        return "impossible"
    elif cantidad_verdaderos > 1:
        return "not sure"
    elif es_pila:
        return "stack"
    elif es_cola:
        return "queue"
    elif es_cola_prioridad:
        return "priority queue"

# Lectura de entrada
input = sys.stdin.read
datos = input().strip().splitlines()
indice = 0

while indice < len(datos):
    n = int(datos[indice])
    indice += 1
    operaciones = []
    
    for _ in range(n):
        operacion, x = map(int, datos[indice].split())
        operaciones.append((operacion, x))
        indice += 1
    
    # Identificar la estructura de datos
    print(identificar_estructura(operaciones))
