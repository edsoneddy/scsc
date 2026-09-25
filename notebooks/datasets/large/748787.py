from collections import deque
import heapq

def determinar_estructura(n, operaciones):
    es_pila = True
    es_cola = True
    es_cola_prioridad = True

    pila = []  # Para simular la pila
    cola = deque()  # Para simular la cola
    cola_prioridad = []  # Para simular la cola de prioridad

    for tipo, valor in operaciones:
        if tipo == 1:  # Inserta el elemento
            pila.append(valor)
            cola.append(valor)
            heapq.heappush(cola_prioridad, -valor)  # Usar valor negativo para la cola de prioridad
        elif tipo == 2:  # Extrae el elemento
            if es_pila:
                if not pila or pila[-1] != valor:
                    es_pila = False
                else:
                    pila.pop()
            if es_cola:
                if not cola or cola[0] != valor:
                    es_cola = False
                else:
                    cola.popleft()
            if es_cola_prioridad:
                if not cola_prioridad or -cola_prioridad[0] != valor:
                    es_cola_prioridad = False
                else:
                    heapq.heappop(cola_prioridad)

    # Determinar cuál estructura es la correcta
    estructuras_posibles = es_pila + es_cola + es_cola_prioridad

    if estructuras_posibles == 0:
        return "impossible"
    elif estructuras_posibles > 1:
        return "not sure"
    elif es_pila:
        return "stack"
    elif es_cola:
        return "queue"
    elif es_cola_prioridad:
        return "priority queue"

# Lectura de entrada
import sys

input_data = sys.stdin.read().strip().splitlines()
i = 0

while i < len(input_data):
    try:
        n = int(input_data[i].strip())
        operaciones = []
        for j in range(1, n + 1):
            operaciones.append(tuple(map(int, input_data[i + j].strip().split())))
        resultado = determinar_estructura(n, operaciones)
        print(resultado)
        i += n + 1
    except EOFError:
        break
    except ValueError:
        break