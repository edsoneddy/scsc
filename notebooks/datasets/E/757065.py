import sys
from collections import deque
import heapq

def identificar_estructura(comandos):
    es_pila = True
    es_cola = True
    es_cola_prioridad = True
    
    pila = []
    cola = deque()
    cola_prioridad = []
    
    for comando in comandos:
        tipo, x = comando
        
        if tipo == 1:
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x)
        
        elif tipo == 2:
            if pila:
                if pila.pop() != x:
                    es_pila = False
            else:
                es_pila = False
            
            if cola:
                if cola.popleft() != x:
                    es_cola = False
            else:
                es_cola = False
            
            if cola_prioridad:
                if -heapq.heappop(cola_prioridad) != x:
                    es_cola_prioridad = False
            else:
                es_cola_prioridad = False
    
    posibles = sum([es_pila, es_cola, es_cola_prioridad])
    if posibles == 0:
        return "impossible"
    elif posibles > 1:
        return "not sure"
    elif es_pila:
        return "stack"
    elif es_cola:
        return "queue"
    elif es_cola_prioridad:
        return "priority queue"

def main():
    input = sys.stdin.read
    datos = input().strip().split("\n")
    
    i = 0
    resultados = []
    while i < len(datos):
        n = int(datos[i])
        i += 1
        comandos = []
        for _ in range(n):
            tipo, x = map(int, datos[i].split())
            comandos.append((tipo, x))
            i += 1
        resultados.append(identificar_estructura(comandos))
    
    print("\n".join(resultados))

if __name__ == "__main__":
    main()
