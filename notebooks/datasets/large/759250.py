import sys
import heapq

def procesar_operaciones(operaciones):
    stack = []
    queue = []
    priority_queue = []
    
    es_pila = True
    es_cola = True
    es_cola_prioridad = True
    
    for operacion in operaciones:
        tipo, x = operacion
        if tipo == 1:
            stack.append(x)
            queue.append(x)
            heapq.heappush(priority_queue, -x)  # Usamos -x para simular una cola de prioridad max-heap
        elif tipo == 2:
            if es_pila:
                if not stack or stack.pop() != x:
                    es_pila = False
            if es_cola:
                if not queue or queue.pop(0) != x:
                    es_cola = False
            if es_cola_prioridad:
                if not priority_queue or -heapq.heappop(priority_queue) != x:
                    es_cola_prioridad = False
    
    if es_pila and not es_cola and not es_cola_prioridad:
        return "stack"
    elif not es_pila and es_cola and not es_cola_prioridad:
        return "queue"
    elif not es_pila and not es_cola and es_cola_prioridad:
        return "priority queue"
    elif not es_pila and not es_cola and not es_cola_prioridad:
        return "impossible"
    else:
        return "not sure"

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    i = 0
    while i < len(data):
        n = int(data[i])
        i += 1
        operaciones = []
        for _ in range(n):
            tipo, x = map(int, data[i].split())
            operaciones.append((tipo, x))
            i += 1
        resultado = procesar_operaciones(operaciones)
        print(resultado)

if __name__ == "__main__":
    main()