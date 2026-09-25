from collections import deque
import heapq

def detectar_estructura():
    n = int(input())  # Leer número de operaciones
    operaciones = [tuple(map(int, input().split())) for _ in range(n)]
    
    pila, cola, cola_prioridad = [], deque(), []
    es_pila, es_cola, es_cola_prioridad = True, True, True
    
    for tipo, x in operaciones:
        if tipo == 1:  # Insertar
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x)  # Negativo para simular max-heap
        else:  # tipo == 2, extraer
            if es_pila:
                es_pila = pila and pila.pop() == x
            if es_cola:
                es_cola = cola and cola.popleft() == x
            if es_cola_prioridad:
                es_cola_prioridad = cola_prioridad and -heapq.heappop(cola_prioridad) == x
    
    estructuras_posibles = [
        estructura for estructura, flag in [
            ("stack", es_pila),
            ("queue", es_cola),
            ("priority queue", es_cola_prioridad)
        ] if flag
    ]
    
    return "impossible" if not estructuras_posibles else (
        estructuras_posibles[0] if len(estructuras_posibles) == 1 else "not sure"
    )

def main():
    while True:
        try:
            print(detectar_estructura())
        except EOFError:
            break

if __name__ == "__main__":
    main()