def main():
    import sys
    from collections import deque
 
    for line in sys.stdin:
        operaciones = int(line.strip())
        pila = []
        cola = deque()
        cola_prioridad = []
 
        es_pila = True
        es_cola = True
        es_cola_prioridad = True
 
        for _ in range(operaciones):
            comando, valor = map(int, sys.stdin.readline().strip().split())
 
            if comando == 1:
                pila.append(valor)
                cola.append(valor)
                cola_prioridad.append(valor)
                cola_prioridad.sort(reverse=True)
            elif comando == 2:
                if es_pila:
                    if not pila or pila.pop() != valor:
                        es_pila = False
                if es_cola:
                    if not cola or cola.popleft() != valor:
                        es_cola = False
                if es_cola_prioridad:
                    if not cola_prioridad or cola_prioridad.pop(0) != valor:
                        es_cola_prioridad = False
 
        if es_pila and not es_cola and not es_cola_prioridad:
            print("stack")
        elif not es_pila and es_cola and not es_cola_prioridad:
            print("queue")
        elif not es_pila and not es_cola and es_cola_prioridad:
            print("priority queue")
        elif not es_pila and not es_cola and not es_cola_prioridad:
            print("impossible")
        else:
            print("not sure")
 
if __name__ == "__main__":
    main()