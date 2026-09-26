import sys
import heapq
from collections import deque

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0

    while idx < len(data):
        n = int(data[idx])
        idx += 1

        pila = []
        cola = deque()
        cola_prioridad = []
        es_pila = True
        es_cola = True
        es_cola_prioridad = True

        for _ in range(n):
            comando = int(data[idx])
            x = int(data[idx + 1])
            idx += 2

            if comando == 1:
                pila.append(x)
                cola.append(x)
                heapq.heappush(cola_prioridad, -x)
            elif comando == 2:
                if es_pila:
                    if not pila or pila.pop() != x:
                        es_pila = False

                if es_cola:
                    if not cola or cola.popleft() != x:
                        es_cola = False

                if es_cola_prioridad:
                    if not cola_prioridad or -heapq.heappop(cola_prioridad) != x:
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
