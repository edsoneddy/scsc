import sys
import heapq

input = sys.stdin.read
data = input().split()

def determinar_estructura(n, comandos):
    pila = []
    cola = []
    cola_prioridad = []
    
    es_pila = True
    es_cola = True
    es_cola_prioridad = True
    
    i = 0
    while i < len(comandos):
        comando = int(comandos[i])
        x = int(comandos[i + 1])
        i += 2
        
        if comando == 1:
            if es_pila:
                pila.append(x)
            if es_cola:
                cola.append(x)
            if es_cola_prioridad:
                heapq.heappush(cola_prioridad, -x)  # Usamos valores negativos para simular max-heap
        elif comando == 2:
            if es_pila:
                if pila and pila[-1] == x:
                    pila.pop()
                else:
                    es_pila = False
            if es_cola:
                if cola and cola[0] == x:
                    cola.pop(0)
                else:
                    es_cola = False
            if es_cola_prioridad:
                if cola_prioridad and -heapq.heappop(cola_prioridad) == x:
                    pass
                else:
                    es_cola_prioridad = False
    
    if es_pila and not es_cola and not es_cola_prioridad:
        return "stack"
    if not es_pila and es_cola and not es_cola_prioridad:
        return "queue"
    if not es_pila and not es_cola and es_cola_prioridad:
        return "priority queue"
    if not es_pila and not es_cola and not es_cola_prioridad:
        return "impossible"
    return "not sure"

index = 0
while index < len(data):
    n = int(data[index])
    index += 1
    comandos = data[index:index + 2 * n]
    index += 2 * n
    print(determinar_estructura(n, comandos))