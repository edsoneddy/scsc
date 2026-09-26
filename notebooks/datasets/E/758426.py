from collections import deque
import heapq

def determinar_estructura(operaciones):
    pila = []
    cola = deque()
    cola_prioridad = []
    
    es_pila = True
    es_cola = True
    es_cola_prioridad = True
    
    for comando, x in operaciones:
        if comando == 1:  # Insertar
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x)  # Usamos valores negativos para simular max-heap
        elif comando == 2:  # Sacar
            if es_pila:
                if not pila or pila.pop() != x:
                    es_pila = False
            if es_cola:
                if not cola or cola.popleft() != x:
                    es_cola = False
            if es_cola_prioridad:
                if not cola_prioridad or -heapq.heappop(cola_prioridad) != x:
                    es_cola_prioridad = False
    
    # Determinar resultado
    posibles = sum([es_pila, es_cola, es_cola_prioridad])
    if posibles > 1:
        return "not sure"
    elif posibles == 1:
        if es_pila:
            return "stack"
        if es_cola:
            return "queue"
        if es_cola_prioridad:
            return "priority queue"
    else:
        return "impossible"

def main():
    import sys
    input = sys.stdin.read
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
        resultados.append(determinar_estructura(operaciones))
    
    # Imprimir resultados
    print("\n".join(resultados))

if __name__ == "__main__":
    main()
