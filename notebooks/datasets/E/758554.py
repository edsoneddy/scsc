import heapq

while True:
    try:
        # leer entrada
        entrada = input().strip()
        
        # Si no hay entrada, salir del bucle -> si no hay datos por consola, fin!!!
        if not entrada:
            break
        
        n = int(entrada)
        
        # Inicializar estructuras de datos
        pila = []
        cola = []
        cola_prioridad = []

        # sw para determinar si son las estructuras correctas
        es_pila = True
        es_cola = True
        es_cola_prioridad = True
        
        for _ in range(n):
            operacion, x = map(int, input().strip().split())
            
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
                    if cola_prioridad and -heapq.heappop(cola_prioridad) == x:
                        pass
                    else:
                        es_cola_prioridad = False
        
        
        supuestos = sum([es_pila, es_cola, es_cola_prioridad])

        if supuestos > 1:
            print("not sure")
        elif supuestos == 0:
            print("impossible")
        else:
            if es_pila:
                print("stack")
            elif es_cola:
                print("queue")
            elif es_cola_prioridad:
                print("priority queue")
    except EOFError:
        break
