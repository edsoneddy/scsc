from collections import deque
import heapq
import sys
input = sys.stdin.read

def determinar_estructura_datos(operaciones):
    pila = []
    cola = deque()
    cola_prioridad = []
    es_pila = es_cola = es_cola_prioridad = True

    for comando, x in operaciones:
        if comando == 1:  
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x)  
        elif comando == 2:  
            if es_pila:
                if not pila or pila.pop() != x:
                    es_pila = False
            if es_cola:
                if not cola or cola.popleft() != x:
                    es_cola = False
            if es_cola_prioridad:
                if not cola_prioridad or -heapq.heappop(cola_prioridad) != x:
                    es_cola_prioridad = False

    
    posibles = [es_pila, es_cola, es_cola_prioridad]
    if sum(posibles) == 0:
        return "impossible"
    elif sum(posibles) > 1:
        return "not sure"
    elif es_pila:
        return "stack"
    elif es_cola:
        return "queue"
    elif es_cola_prioridad:
        return "priority queue"

def main():
    datos = input().strip().split("\n")
    i = 0
    resultados = []

    while i < len(datos):
        n = int(datos[i])
        i += 1
        operaciones = []
        for _ in range(n):
            comando, x = map(int, datos[i].split())
            operaciones.append((comando, x))
            i += 1
        resultados.append(determinar_estructura_datos(operaciones))
    
    print("\n".join(resultados))

if __name__ == "__main__":
    main()
