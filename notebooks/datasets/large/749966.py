import heapq

def identificar_estructura(n, operaciones):
    es_pila = True
    es_cola = True
    es_cola_prioridad = True
    
    pila = []
    cola = []
    cola_prioridad = []
    
    for operacion in operaciones:
        tipo, x = operacion
        if tipo == 1:  
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x)  
        elif tipo == 2:  
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

while True:
    try:
        n = int(input())
        operaciones = []
        for _ in range(n):
            tipo, x = map(int, input().split())
            operaciones.append((tipo, x))
        resultado = identificar_estructura(n, operaciones)
        print(resultado)
    except EOFError:
        break