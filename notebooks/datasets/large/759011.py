from collections import deque
import heapq
import sys

def procesar_caso(operaciones):
    pila = []
    cola = deque()
    cola_prioridad = []
    
    es_pila, es_cola, es_cola_prioridad = True, True, True
    
    for comando, valor in operaciones:
        if comando == 1:  # Insertar
            pila.append(valor)
            cola.append(valor)
            heapq.heappush(cola_prioridad, -valor)  # Invertimos para simular una max-heap
        elif comando == 2:  # Sacar
            if es_pila:
                if not pila or pila.pop() != valor:
                    es_pila = False
            if es_cola:
                if not cola or cola.popleft() != valor:
                    es_cola = False
            if es_cola_prioridad:
                if not cola_prioridad or -heapq.heappop(cola_prioridad) != valor:
                    es_cola_prioridad = False

    # Decidir el resultado
    posibles = sum([es_pila, es_cola, es_cola_prioridad])
    if posibles == 0:
        return "impossible"
    elif posibles > 1:
        return "not sure"
    elif es_pila:
        return "stack"
    elif es_cola:
        return "queue"
    elif es_cola_prioridad:
        return "priority queue"

# Leer entrada
def procesar_entrada():
    input = sys.stdin.read
    datos = input().strip().split("\n")
    
    i = 0
    resultados = []
    while i < len(datos):
        n = int(datos[i])
        i += 1
        operaciones = []
        for _ in range(n):
            comando, valor = map(int, datos[i].split())
            operaciones.append((comando, valor))
            i += 1
        resultados.append(procesar_caso(operaciones))
    
    print("\n".join(resultados))

# Ejecutar el programa
procesar_entrada()
