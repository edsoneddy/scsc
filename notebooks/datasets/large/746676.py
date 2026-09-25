def determinar_estructura(operaciones):
    from collections import deque
    import heapq
    pila = []
    cola = deque()
    cola_prioridad = []
    
    es_pila = True
    es_cola = True
    es_cola_prioridad = True
    
    for operacion in operaciones:
        tipo, x = operacion
        
        if tipo == 1:
            if es_pila:
                pila.append(x)
            if es_cola:
                cola.append(x)
            if es_cola_prioridad:
                heapq.heappush(cola_prioridad, -x) 
        elif tipo == 2:
            if es_pila:
                if pila and pila[-1] == x:
                    pila.pop()
                else:
                    es_pila = False
            if es_cola:
                if cola and cola[0] == x:
                    cola.popleft()
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
def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    index = 0
    while index < len(data):
        if data[index].strip().isdigit():
            n = int(data[index].strip())
            index += 1
            operaciones = []
            for _ in range(n):
                tipo, x = map(int, data[index].split())
                operaciones.append((tipo, x))
                index += 1
            print(determinar_estructura(operaciones))
        else:
            print(f"Valor inválido en data[{index}]: '{data[index]}'")
            index += 1
 
if __name__ == "__main__":
    main()