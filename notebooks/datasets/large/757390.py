def adivina_estructura():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    i = 0
    while i < len(data):
        n = int(data[i])
        i += 1
        comandos = []
        for _ in range(n):
            comandos.append(tuple(map(int, data[i].split())))
            i += 1
        
        pila, cola, cola_prioridad = [], [], []
        es_pila, es_cola, es_cola_prioridad = True, True, True

        for op, x in comandos:
            if op == 1:
                pila.append(x)
                cola.append(x)
                cola_prioridad.append(x)
                cola_prioridad.sort(reverse=True)
            elif op == 2:
                if pila:
                    es_pila &= (pila.pop() == x)
                else:
                    es_pila = False

                if cola:
                    es_cola &= (cola.pop(0) == x)
                else:
                    es_cola = False

                if cola_prioridad:
                    es_cola_prioridad &= (cola_prioridad.pop(0) == x)
                else:
                    es_cola_prioridad = False

        if es_pila + es_cola + es_cola_prioridad > 1:
            print("not sure")
        elif es_pila:
            print("stack")
        elif es_cola:
            print("queue")
        elif es_cola_prioridad:
            print("priority queue")
        else:
            print("impossible")

adivina_estructura()
