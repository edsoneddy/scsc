from collections import deque
import heapq
import sys

def adivine_la_estructura():
    while True:
        try:
            n = int(input().strip())
            comandos = [input().strip() for _ in range(n)]

            es_pila = True
            es_cola = True
            es_cola_prioridad = True

            pila = []
            cola = deque()
            cola_prioridad = []

            for comando in comandos:
                tipo, x = map(int, comando.split())
                if tipo == 1:
                    pila.append(x)
                    cola.append(x)
                    heapq.heappush(cola_prioridad, -x)
                elif tipo == 2:
                    if pila:
                        if pila.pop() != x:
                            es_pila = False
                    else:
                        es_pila = False

                    if cola:
                        if cola.popleft() != x:
                            es_cola = False
                    else:
                        es_cola = False

                    if cola_prioridad:
                        if -heapq.heappop(cola_prioridad) != x:
                            es_cola_prioridad = False
                    else:
                        es_cola_prioridad = False

            posibles = sum([es_pila, es_cola, es_cola_prioridad])
            if posibles == 0:
                print("impossible")
            elif posibles > 1:
                print("not sure")
            elif es_pila:
                print("stack")
            elif es_cola:
                print("queue")
            elif es_cola_prioridad:
                print("priority queue")
        except EOFError:
            break

adivine_la_estructura()

