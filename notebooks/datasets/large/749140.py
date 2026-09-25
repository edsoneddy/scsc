import sys
import heapq
from collections import deque

def procesar_operaciones(n, operaciones):
    es_pila = True
    es_cola = True
    es_prioridad = True

    pila = []
    cola = deque()
    cola_prioridad = []

    for operacion, x in operaciones:
        if operacion == 1:
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x)  # Almacenamos negativos para simular max-heap
        elif operacion == 2:
            if es_pila:
                if not pila or pila.pop() != x:
                    es_pila = False
            if es_cola:
                if not cola or cola.popleft() != x:
                    es_cola = False
            if es_prioridad:
                if not cola_prioridad or -heapq.heappop(cola_prioridad) != x:
                    es_prioridad = False

    if es_pila + es_cola + es_prioridad == 0:
        return "impossible"
    elif es_pila + es_cola + es_prioridad > 1:
        return "not sure"
    elif es_pila:
        return "stack"
    elif es_cola:
        return "queue"
    elif es_prioridad:
        return "priority queue"

def main():
    input = sys.stdin.read().strip().splitlines()
    index = 0
    resultados = []

    while index < len(input):
        n = int(input[index].strip())
        index += 1
        operaciones = []

        for _ in range(n):
            tipo, x = map(int, input[index].strip().split())
            operaciones.append((tipo, x))
            index += 1

        resultados.append(procesar_operaciones(n, operaciones))

    print("\n".join(resultados))

if __name__ == "__main__":
    main()
