from collections import deque
import heapq
 
def identify_data_structure(operations):
    stack = []
    queue = deque()
    priority_queue = []
    is_stack = is_queue = is_priority_queue = True
 
    for op_type, x in operations:
        if op_type == 1:
            stack.append(x)
            queue.append(x)
            heapq.heappush(priority_queue, -x)
        elif op_type == 2:
            if stack and stack.pop() != x:
                is_stack = False
            if queue and queue.popleft() != x:
                is_queue = False
            if priority_queue and -heapq.heappop(priority_queue) != x:
                is_priority_queue = False
 
    if is_stack and not is_queue and not is_priority_queue:
        return "stack"
    elif not is_stack and is_queue and not is_priority_queue:
        return "queue"
    elif not is_stack and not is_queue and is_priority_queue:
        return "priority queue"
    elif not is_stack and not is_queue and not is_priority_queue:
        return "impossible"
    else:
        return "not sure"
 
# Ejemplo de uso
while True:
    try:
        n = int(input())
        operations = []
        for _ in range(n):
            operation = list(map(int, input().split()))
            operations.append(tuple(operation))
 
        print(identify_data_structure(operations))
    except EOFError:
        break
 


#la complejidad del código es O(n log n) 
#debido a las operaciones de inserción y eliminación en el priority_queue gestionado por heapq.