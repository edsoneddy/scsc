import heapq

def detectar_estructura_comando(comandos):
    es_pila = True
    es_cola = True
    es_cola_prioridad = True
    pila = []
    cola = []
    cola_prioridad = []
    
    for tipo, valor in comandos:
        if tipo == 1:
            pila.append(valor)
            cola.append(valor)
            heapq.heappush(cola_prioridad, -valor)
        elif tipo == 2:
            if not pila or pila.pop() != valor:
                es_pila = False
            if not cola or cola.pop(0) != valor:
                es_cola = False
            if not cola_prioridad or -heapq.heappop(cola_prioridad) != valor:
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
    while True:
        try:
            n = int(input())
            comandos = []
            for _ in range(n):
                tipo, valor = map(int, input().split())
                comandos.append((tipo, valor))
            print(detectar_estructura_comando(comandos))
        except EOFError:
            break

if __name__ == "__main__":
    main()
