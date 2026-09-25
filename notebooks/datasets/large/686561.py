import sys
import heapq

def detectar_estructura_de_datos(comandos):
    pila = []
    cola = []
    cola_prioridad = []
    es_pila = True
    es_cola = True
    es_cola_prioridad = True

    for comando, x in comandos:
        if comando == 1:
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x)
        elif comando == 2:
            if es_pila:
                if not pila or pila.pop() != x:
                    es_pila = False
            if es_cola:
                if not cola or cola.pop(0) != x:
                    es_cola = False
            if es_cola_prioridad:
                if not cola_prioridad or -heapq.heappop(cola_prioridad) != x:
                    es_cola_prioridad = False

    posibles = [es_pila, es_cola, es_cola_prioridad].count(True)
    if posibles > 1:
        return "not sure"
    elif posibles == 0:
        return "impossible"
    else:
        if es_pila:
            return "stack"
        elif es_cola:
            return "queue"
        elif es_cola_prioridad:
            return "priority queue"

def main():
    for linea in sys.stdin:
        n = int(linea.strip())
        comandos = []
        for _ in range(n):
            op, x = map(int, input().strip().split())
            comandos.append((op, x))
        resultado = detectar_estructura_de_datos(comandos)
        print(resultado)

if __name__ == "__main__":
    main()


#O(n)