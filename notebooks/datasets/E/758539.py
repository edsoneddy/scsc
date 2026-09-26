import sys
import heapq

def determinar_estructura(comandos):
    pila = []
    cola = []
    cola_prioridad = []
    
    es_pila = True
    es_cola = True
    es_cola_prioridad = True

    for comando in comandos:
        tipo, x = comando
        
        if tipo == 1:  
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x) 
        
        elif tipo == 2:  
            if es_pila:
                if not pila or pila.pop() != x:
                    es_pila = False
            if es_cola:
                if not cola or cola.pop(0) != x:
                    es_cola = False
            if es_cola_prioridad:
                if not cola_prioridad or -heapq.heappop(cola_prioridad) != x:
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
entrada = sys.stdin.read().strip().split("\n")
i = 0
resultados = []

while i < len(entrada):
    n = int(entrada[i])
    i += 1
    comandos = []
    for _ in range(n):
        linea = list(map(int, entrada[i].split()))
        comandos.append(linea)
        i += 1
    resultados.append(determinar_estructura(comandos))
print("\n".join(resultados))