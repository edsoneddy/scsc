from collections import deque
import heapq

def guess_structure(operations):
    # Simularemos las tres estructuras simultáneamente
    stack = []
    queue = deque()
    pq = []  # priority queue
    
    # Banderas para cada estructura
    could_be_stack = True
    could_be_queue = True
    could_be_pq = True
    
    # Procesar cada operación
    actual_outputs = []  # Guardar las salidas reales
    
    for op, x in operations:
        if op == 1:  # insertar
            stack.append(x)
            queue.append(x)
            heapq.heappush(pq, -x)  # Negativo para hacer max-heap
        else:  # op == 2, extraer
            actual_outputs.append(x)
            
            # Verificar stack
            if stack and stack[-1] != x:
                could_be_stack = False
            if stack:
                stack.pop()
                
            # Verificar queue
            if queue and queue[0] != x:
                could_be_queue = False
            if queue:
                queue.popleft()
                
            # Verificar priority queue
            if pq and -heapq.heappop(pq) != x:
                could_be_pq = False
    
    # Contar cuántas estructuras coinciden
    possible_structures = sum([could_be_stack, could_be_queue, could_be_pq])
    
    if possible_structures == 0:
        return "impossible"
    elif possible_structures > 1:
        return "not sure"
    else:
        if could_be_stack:
            return "stack"
        if could_be_queue:
            return "queue"
        if could_be_pq:
            return "priority queue"

def solve():
    try:
        while True:
            n = int(input())
            operations = []
            for _ in range(n):
                op, x = map(int, input().split())
                operations.append((op, x))
            print(guess_structure(operations))
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
    