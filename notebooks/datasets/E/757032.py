import heapq

def resolver_caso_prueba(operaciones):
    pila = []
    cola = []
    cola_prioridad = []
    
    es_pila = True
    es_cola = True
    es_cola_prioridad = True
    
    for op in operaciones:
        tipo, x = op
        
        if tipo == 1:  # Inserción
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x)  # Usamos -x para simular una cola de prioridad descendente
        elif tipo == 2:  # Extracción
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

    if (es_pila + es_cola + es_cola_prioridad) > 1:
        return "not sure"
    elif es_pila:
        return "stack"
    elif es_cola:
        return "queue"
    elif es_cola_prioridad:
        return "priority queue"
    else:
        return "impossible"


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    i = 0
    while i < len(data):
        n = int(data[i])
        i += 1
        operaciones = []
        
        for j in range(n):
            tipo, x = map(int, data[i+j].split())
            operaciones.append((tipo, x))
        
        print(resolver_caso_prueba(operaciones))
        i += n


if __name__ == "__main__":
    main()
