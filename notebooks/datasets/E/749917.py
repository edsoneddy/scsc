import sys
import heapq

def identificar_estructura(comandos):
    pila = []
    cola = []
    cola_prioridad = []
    es_pila = es_cola = es_cola_prioridad = True

    for comando, x in comandos:
        if comando == 1:  # Inserción en las tres estructuras
            if es_pila:
                pila.append(x)
            if es_cola:
                cola.append(x)
            if es_cola_prioridad:
                heapq.heappush(cola_prioridad, -x)  # Insertamos en el max-heap
        elif comando == 2:  # Extracción en las tres estructuras
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

    # Determinamos el resultado basado en cuáles estructuras son posibles
    posibles = sum([es_pila, es_cola, es_cola_prioridad])
    if posibles == 0:
        return "impossible"
    elif posibles > 1:
        return "not sure"
    else:
        if es_pila:
            return "stack"
        elif es_cola:
            return "queue"
        elif es_cola_prioridad:
            return "priority queue"

# Lectura de entrada
input = sys.stdin.read
data = input().strip().splitlines()
i = 0

while i < len(data):
    n = int(data[i])
    comandos = []
    i += 1
    for _ in range(n):
        comando, x = map(int, data[i].split())
        comandos.append((comando, x))
        i += 1
    print(identificar_estructura(comandos))
