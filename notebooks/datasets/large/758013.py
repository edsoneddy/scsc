import sys
import heapq


input = sys.stdin.read
data = input().strip().splitlines()
    
index = 0
results = []
    
while index < len(data):
    n = int(data[index])
    index += 1
        
    stack = []
    queue = []
    priority_queue = []
    possible_stack = True
    possible_queue = True
    possible_priority_queue = True
        
    for _ in range(n):
        command = data[index].strip().split()
        index += 1
        cmd_type = int(command[0])
        if cmd_type == 1:  # Inserción
            x = int(command[1])
            if possible_stack:
                stack.append(x)  # Pila (LIFO)
            if possible_queue:
                queue.append(x)  # Cola (FIFO)
            if possible_priority_queue:
                heapq.heappush(priority_queue, -x)  # Cola de prioridad (max-heap)
        elif cmd_type == 2:  # Extracción
            x = int(command[1])
            if possible_stack:
                if stack and stack[-1] == x:
                    stack.pop()  # Sacar de pila
                else:
                    possible_stack = False

            if possible_queue:
                if queue and queue[0] == x:
                    queue.pop(0)  # Sacar de cola
                else:
                    possible_queue = False

            if possible_priority_queue:
                if priority_queue and -priority_queue[0] == x:
                    heapq.heappop(priority_queue)  # Sacar de cola de prioridad
                else:
                    possible_priority_queue = False

    # Determinación de la estructura de datos
    count_true = sum([possible_stack, possible_queue, possible_priority_queue])
    
    if count_true == 0:
        results.append("impossible")
    elif count_true > 1:
        results.append("not sure")
    elif possible_stack:
        results.append("stack")
    elif possible_queue:
        results.append("queue")
    elif possible_priority_queue:
        results.append("priority queue")

# Salida de resultados
for result in results:
    print(result)

