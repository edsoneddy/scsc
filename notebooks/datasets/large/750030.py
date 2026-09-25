from collections import deque
import heapq

def detectar_estructura():
    n = int(input())
    
    pila = []
    cola = deque()
    cola_prioridad = []
    
    es_pila = True
    es_cola = True
    es_cola_prioridad = True
    
    operaciones = []
    for _ in range(n):
        tipo, x = map(int, input().split())
        operaciones.append((tipo, x))
        
        if tipo == 1:
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x) 
        else: 
            if es_pila:
                if len(pila) == 0 or pila.pop() != x:
                    es_pila = False

            if es_cola:
                if len(cola) == 0 or cola.popleft() != x:
                    es_cola = False

            if es_cola_prioridad:
                if len(cola_prioridad) == 0 or -heapq.heappop(cola_prioridad) != x:
                    es_cola_prioridad = False
    
    estructuras_posibles = []
    if es_pila:
        estructuras_posibles.append("stack")
    if es_cola:
        estructuras_posibles.append("queue")
    if es_cola_prioridad:
        estructuras_posibles.append("priority queue")
    
    if len(estructuras_posibles) == 0:
        return "impossible"
    elif len(estructuras_posibles) == 1:
        return estructuras_posibles[0]
    else:
        return "not sure"

def main():
    while True:
        try:
            resultado = detectar_estructura()
            print(resultado)
        except EOFError:
            break

if __name__ == "__main__": 
    main()
