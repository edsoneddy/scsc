import heapq
from collections import deque
 
def identificar_estructura_operaciones(operaciones):
    es_pila = True
    es_cola = True
    es_cola_prioridad = True
    pila = []
    cola = deque()
    cola_prioridad = []
 
    for operacion, valor in operaciones:
        if operacion == 1:
            pila.append(valor)
            cola.append(valor)
            heapq.heappush(cola_prioridad, -valor)
        else:
            if not pila or pila.pop() != valor:
                es_pila = False
            if not cola or cola.popleft() != valor:
                es_cola = False
            if not cola_prioridad or -heapq.heappop(cola_prioridad) != valor:
                es_cola_prioridad = False
 
    opciones = [es_pila, es_cola, es_cola_prioridad]
    if sum(opciones) == 0:
        return "impossible"
    elif sum(opciones) > 1:
        return "not sure"
    elif es_pila:
        return "stack"
    elif es_cola:
        return "queue"
    elif es_cola_prioridad:
        return "priority queue"
 
while True:
    try:
        n = int(input())
        operaciones = []
        for _ in range(n):
            operacion, valor = map(int, input().split())
            operaciones.append((operacion, valor))
 
        resultado = identificar_estructura_operaciones(operaciones)
        print(resultado)
    except EOFError:
        break
