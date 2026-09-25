#-------------------Adivine la Estructura--------------------#

from collections import deque
import heapq

def detectar_estructura(operaciones):
    pila = []
    cola = deque()
    cola_prioridad = []
    es_pila, es_cola, es_cola_prioridad = True, True, True

    for tipo, valor in operaciones:
        if tipo == 1:
            if es_pila:
                pila.append(valor)
            if es_cola:
                cola.append(valor)
            if es_cola_prioridad:
                heapq.heappush(cola_prioridad, -valor)
        elif tipo == 2:
            if es_pila:
                if pila and pila[-1] == valor:
                    pila.pop()
                else:
                    es_pila = False
            if es_cola:
                if cola and cola[0] == valor:
                    cola.popleft()
                else:
                    es_cola = False
            if es_cola_prioridad:
                if cola_prioridad and -cola_prioridad[0] == valor:
                    heapq.heappop(cola_prioridad)
                else:
                    es_cola_prioridad = False

    posible_estructuras = sum([es_pila, es_cola, es_cola_prioridad])
    if posible_estructuras == 0:
        return "impossible"
    if posible_estructuras > 1:
        return "not sure"
    if es_pila:
        return "stack"
    if es_cola:
        return "queue"
    if es_cola_prioridad:
        return "priority queue"

while True:
    try:
        n = int(input())
        operaciones = [tuple(map(int, input().split())) for _ in range(n)]
        print(detectar_estructura(operaciones))
    except EOFError:
        break
