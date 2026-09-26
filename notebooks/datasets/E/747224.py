import sys
import heapq

def identificar_estructura(n, operaciones):
    es_pila = True
    es_cola = True
    es_cola_prioridad = True
    
    pila = []
    cola = []
    cola_prioridad = []
    
    for operacion, x in operaciones:
        if operacion == 1:
            
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x)  
        elif operacion == 2:
            
            if es_pila:
                if pila and pila[-1] == x:
                    pila.pop()
                else:
                    es_pila = False
            if es_cola:
                if cola and cola[0] == x:
                    cola.pop(0)
                else:
                    es_cola = False
            if es_cola_prioridad:
                if cola_prioridad and -cola_prioridad[0] == x:
                    heapq.heappop(cola_prioridad)
                else:
                    es_cola_prioridad = False

    
    if es_pila and not es_cola and not es_cola_prioridad:
        return "stack"
    elif not es_pila and es_cola and not es_cola_prioridad:
        return "queue"
    elif not es_pila and not es_cola and es_cola_prioridad:
        return "priority queue"
    elif not es_pila and not es_cola and not es_cola_prioridad:
        return "impossible"
    else:
        return "not sure"


entrada = sys.stdin.read().splitlines()
i = 0
salida = []
while i < len(entrada):
    n = int(entrada[i].strip())
    i += 1
    operaciones = []
    for _ in range(n):
        linea = entrada[i].strip().split()
        operacion = int(linea[0])
        x = int(linea[1])
        operaciones.append((operacion, x))
        i += 1
    salida.append(identificar_estructura(n, operaciones))


for resultado in salida:
    print(resultado)
