import sys
from collections import deque
import heapq

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    i = 0
    while i < len(data):
        n = int(data[i])
        i += 1
        
        stack = []
        queue = deque()
        priority_queue = []
        
        is_stack = True
        is_queue = True
        is_priority_queue = True
        
        for _ in range(n):
            command = data[i].split()
            op_type = int(command[0])
            x = int(command[1])
            i += 1
            
            if op_type == 1:
                if is_stack:
                    stack.append(x)
                if is_queue:
                    queue.append(x)
                if is_priority_queue:
                    heapq.heappush(priority_queue, -x)
            elif op_type == 2:
                if is_stack:
                    if stack and stack[-1] == x:
                        stack.pop()
                    else:
                        is_stack = False
                if is_queue:
                    if queue and queue[0] == x:
                        queue.popleft()
                    else:
                        is_queue = False
                if is_priority_queue:
                    if priority_queue and -priority_queue[0] == x:
                        heapq.heappop(priority_queue)
                    else:
                        is_priority_queue = False
        
        if is_stack and not is_queue and not is_priority_queue:
            print("stack")
        elif not is_stack and is_queue and not is_priority_queue:
            print("queue")
        elif not is_stack and not is_queue and is_priority_queue:
            print("priority queue")
        elif not is_stack and not is_queue and not is_priority_queue:
            print("impossible")
        else:
            print("not sure")

if __name__ == "__main__":
    main()

#Complejidad: O(n)
