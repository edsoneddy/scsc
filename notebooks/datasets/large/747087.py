import sys
from collections import deque
import heapq

def identificar_estructura_datos(n, operaciones):
  
    stack = []
    queue = deque()
    priority_queue = []
    
    es_stack = True
    es_queue = True
    es_priority_queue = True
    
    for comando, x in operaciones:
        if comando == 1:  
            stack.append(x)
            queue.append(x)
            heapq.heappush(priority_queue, -x)  
        elif comando == 2:  
           
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

   
    posibles_estructuras = sum([es_stack, es_queue, es_priority_queue])
    if posibles_estructuras > 1:
        return "not sure"
    elif es_stack:
        return "stack"
    elif es_queue:
        return "queue"
    elif es_priority_queue:
        return "priority queue"
    else:
        return "impossible"

def main():
    input = sys.stdin.read().strip().splitlines()
    idx = 0
    resultados = []
    
    while idx < len(input):
        n = int(input[idx])
        idx += 1
        operaciones = []
        
        for _ in range(n):
            comando, x = map(int, input[idx].split())
            operaciones.append((comando, x))
            idx += 1
        
        resultado = identificar_estructura_datos(n, operaciones)
        resultados.append(resultado)
    
    print("\n".join(resultados))

if __name__ == "__main__":
    main()
