import sys
import heapq

def adivina_la_estructura():
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    i = 0
    results = []
    while i < len(data):
        n = int(data[i])
        i += 1
        
        stack = []
        queue = []
        priority_queue = []
        
        is_stack = True
        is_queue = True
        is_priority_queue = True
        
        for _ in range(n):
            operation = data[i].split()
            i += 1
            
            if operation[0] == '1':
                x = int(operation[1])
                if is_stack:
                    stack.append(x)
                if is_queue:
                    queue.append(x)
                if is_priority_queue:
                    heapq.heappush(priority_queue, -x)
            
            elif operation[0] == '2':
                x = int(operation[1])
                if is_stack:
                    if stack and stack[-1] == x:
                        stack.pop()
                    else:
                        is_stack = False
                if is_queue:
                    if queue and queue[0] == x:
                        queue.pop(0)
                    else:
                        is_queue = False
                if is_priority_queue:
                    if priority_queue and -priority_queue[0] == x:
                        heapq.heappop(priority_queue)
                    else:
                        is_priority_queue = False
        
        possible_structures = []
        if is_stack:
            possible_structures.append("stack")
        if is_queue:
            possible_structures.append("queue")
        if is_priority_queue:
            possible_structures.append("priority queue")
        
        if len(possible_structures) == 1:
            results.append(possible_structures[0])
        elif len(possible_structures) > 1:
            results.append("not sure")
        else:
            results.append("impossible")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    adivina_la_estructura()
