import sys
from collections import deque
import heapq
 
def determinar_estructura(n, operaciones):
    stack = []
    queue = deque()
    priority_queue = []
    es_stack = True
    es_queue = True
    es_priority_queue = True
    
    for operacion in operaciones:
        tipo, x = operacion
        if tipo == 1:
           
            if es_stack:
                stack.append(x)
            if es_queue:
                queue.append(x)
            if es_priority_queue:
                heapq.heappush(priority_queue, -x) 
        elif tipo == 2:
            if es_stack:
                if stack and stack[-1] == x:
                    stack.pop()
                else:
                    es_stack = False
            if es_queue:
                if queue and queue[0] == x:
                    queue.popleft()
                else:
                    es_queue = False
            if es_priority_queue:
                if priority_queue and -priority_queue[0] == x:
                    heapq.heappop(priority_queue)
                else:
                    es_priority_queue = False
    
    
    posible = sum([es_stack, es_queue, es_priority_queue])
    
    if posible == 0:
        return "impossible"
    elif posible > 1:
        return "not sure"
    elif es_stack:
        return "stack"
    elif es_queue:
        return "queue"
    elif es_priority_queue:
        return "priority queue"
 
def procesar_entrada():
    input = sys.stdin.read
    datos = input().strip().split()
    
    indice = 0
    resultados = []
    
    while indice < len(datos):
        n = int(datos[indice])
        indice += 1
        operaciones = []
        for _ in range(n):
            tipo = int(datos[indice])
            x = int(datos[indice + 1])
            operaciones.append((tipo, x))
            indice += 2
        
        resultado = determinar_estructura(n, operaciones)
        resultados.append(resultado)
    
    for resultado in resultados:
        print(resultado)
 
 
procesar_entrada()
#O(n*logn)