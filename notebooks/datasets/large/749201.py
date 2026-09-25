from sys import stdin
import heapq

def identificar_estructura(n, operaciones):
    # Inicializar estructuras de datos
    stack = []
    queue = []
    priority_queue = []
    
    # Flags para determinar posibles estructuras válidas
    es_pila = True
    es_cola = True
    es_cola_prioridad = True

    for comando, x in operaciones:
        if comando == 1:
            # Insertar elemento en cada estructura
            stack.append(x)
            queue.append(x)
            heapq.heappush(priority_queue, -x)  # Usar negativo para simular una cola de prioridad max

        elif comando == 2:
            # Verificar cada estructura al extraer
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

    # Determinar el tipo de estructura o la incertidumbre
    posibles = sum([es_pila, es_cola, es_cola_prioridad])
    if posibles == 0:
        return "impossible"
    elif posibles > 1:
        return "not sure"
    elif es_pila:
        return "stack"
    elif es_cola:
        return "queue"
    elif es_cola_prioridad:
        return "priority queue"

# Procesamiento de entrada y ejecución de cada caso de prueba
resultados = []
while True:
    try:
        n = int(input().strip())
        operaciones = [tuple(map(int, input().split())) for _ in range(n)]
        resultados.append(identificar_estructura(n, operaciones))
    except EOFError:
        break

# Imprimir todos los resultados
print("\n".join(resultados))

