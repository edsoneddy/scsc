from collections import deque
import heapq
import sys

def adivinar_estructura(operaciones):
    pila = []
    cola = deque()
    cola_prioridad = []
    es_pila = es_cola = es_cola_prioridad = True
    for tipo, x in operaciones:
        if tipo == 1:
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x)
        else:
            if pila and pila[-1] == x:
                pila.pop()
            else:
                es_pila = False
            if cola and cola[0] == x:
                cola.popleft()
            else:
                es_cola = False
            if cola_prioridad and -cola_prioridad[0] == x:
                heapq.heappop(cola_prioridad)
            else:
                es_cola_prioridad = False
    if es_pila + es_cola + es_cola_prioridad > 1:
        return 'not sure'
    elif es_pila:
        return 'stack'
    elif es_cola:
        return 'queue'
    elif es_cola_prioridad:
        return 'priority queue'
    else:
        return 'impossible'


resultados = []
lineas = sys.stdin.read().strip().splitlines() 
i = 0

while i < len(lineas):
    n = int(lineas[i])  
    operaciones = [list(map(int, lineas[i + j + 1].split())) for j in range(n)]
    resultados.append(adivinar_estructura(operaciones))
    i += n + 1  


print("\n".join(resultados))
