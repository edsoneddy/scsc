import sys
from collections import deque
import heapq

def main():
    results = []
    
    while True:
        try:
            # Leer el número de operaciones
            n_line = input().strip()
            if not n_line:
                break
            n = int(n_line)
            
            # Inicializar estructuras de datos y banderas
            stack = []
            queue = deque()
            priority_queue = []
            
            is_stack = True
            is_queue = True
            is_priority_queue = True
            
            # Procesar las operaciones
            for _ in range(n):
                operation, x = map(int, input().strip().split())
                if operation == 1:  # Insertar
                    stack.append(x)
                    queue.append(x)
                    heapq.heappush(priority_queue, -x)  # Max-heap
                elif operation == 2:  # Eliminar
                    if stack:
                        stack_pop = stack.pop()
                    else:
                        stack_pop = None
                    if queue:
                        queue_pop = queue.popleft()
                    else:
                        queue_pop = None
                    if priority_queue:
                        priority_pop = -heapq.heappop(priority_queue)
                    else:
                        priority_pop = None
                    
                    if stack_pop != x:
                        is_stack = False
                    if queue_pop != x:
                        is_queue = False
                    if priority_pop != x:
                        is_priority_queue = False
            
            # Determinar el resultado
            if is_stack + is_queue + is_priority_queue > 1:
                results.append("not sure")
            elif is_stack:
                results.append("stack")
            elif is_queue:
                results.append("queue")
            elif is_priority_queue:
                results.append("priority queue")
            else:
                results.append("impossible")
        except EOFError:
            break
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
