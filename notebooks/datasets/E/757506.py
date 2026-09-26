from collections import deque
import heapq

def evaluar_caso(operaciones):
    pila = []
    cola = deque()
    prioridad = []
    posible_pila = True
    posible_cola = True
    posible_cola_prioridad = True
    
    for operacion in operaciones:
        comando, x = operacion
        
        if comando == 1:
            # Insertar en las tres estructuras
            pila.append(x)
            cola.append(x)
            heapq.heappush(prioridad, -x)  # Para simular una cola de prioridad
        elif comando == 2:
            # Sacar de cada estructura y verificar si corresponde al valor esperado
            if posible_pila:
                if not pila or pila[-1] != x:
                    posible_pila = False
                else:
                    pila.pop()
            
            if posible_cola:
                if not cola or cola.popleft() != x:
                    posible_cola = False
            
            if posible_cola_prioridad:
                if not prioridad or -heapq.heappop(prioridad) != x:
                    posible_cola_prioridad = False
    
    if posible_pila + posible_cola + posible_cola_prioridad > 1:
        return "not sure"
    elif posible_pila:
        return "stack"
    elif posible_cola:
        return "queue"
    elif posible_cola_prioridad:
        return "priority queue"
    else:
        return "impossible"

# Leer entrada
try:
    while True:
        n = int(input())
        operaciones = []
        for _ in range(n):
            comando, x = map(int, input().split())
            operaciones.append((comando, x))
        print(evaluar_caso(operaciones))
except EOFError:
    pass
