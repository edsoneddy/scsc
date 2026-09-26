from collections import deque
import heapq

def simular_operaciones(n, operaciones):
    pila = []
    cola = deque()
    cola_prioridad = [] 
    salidas_reales = []
    elementos_pila = []
    elementos_cola = []
    elementos_prioridad = []
    for tipo, valor in operaciones:
        if tipo == 1:  
            pila.append(valor)
            cola.append(valor)
            heapq.heappush(cola_prioridad, -valor) 
        else: 
            if not pila or not cola or not cola_prioridad:
                return "impossible"
            elementos_pila.append(pila.pop())
            elementos_cola.append(cola.popleft())
            elementos_prioridad.append(-heapq.heappop(cola_prioridad))
            salidas_reales.append(valor)
    es_pila = elementos_pila == salidas_reales
    es_cola = elementos_cola == salidas_reales
    es_prioridad = elementos_prioridad == salidas_reales
    estructuras_posibles = sum([es_pila, es_cola, es_prioridad])
    
    if estructuras_posibles == 0:
        return "impossible"
    elif estructuras_posibles > 1:
        return "not sure"
    else:
        if es_pila:
            return "stack"
        if es_cola:
            return "queue"
        if es_prioridad:
            return "priority queue"

def main():
    while True:
        try:
            n = int(input())
            operaciones = []
            for _ in range(n):
                tipo, valor = map(int, input().split())
                operaciones.append((tipo, valor))
            resultado = simular_operaciones(n, operaciones)
            print(resultado)
            
        except EOFError:
            break

if __name__ == "__main__":
    main()
