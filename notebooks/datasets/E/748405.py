from collections import deque
import heapq
import sys
def determine_structure(n, operations):
    stack = []
    queue = deque()
    priority_queue = []
    is_stack = True
    is_queue = True
    is_priority_queue = True
    for op in operations:
        command, value = map(int, op.split())
        if command == 1:
            stack.append(value)
            queue.append(value)
            heapq.heappush(priority_queue, -value)  
        elif command == 2:
            if is_stack:
                if stack and stack[-1] == value:
                    stack.pop()
                else:
                    is_stack = False        
            if is_queue:
                if queue and queue[0] == value:
                    queue.popleft()
                else:
                    is_queue = False 
            if is_priority_queue:
                if priority_queue and -priority_queue[0] == value:
                    heapq.heappop(priority_queue)
                else:
                    is_priority_queue = False
    if is_stack + is_queue + is_priority_queue > 1:
        return "not sure"
    elif is_stack:
        return "stack"
    elif is_queue:
        return "queue"
    elif is_priority_queue:
        return "priority queue"
    else:
        return "impossible"
def main():
    input_data = sys.stdin.read().strip().splitlines()
    index = 0
    while index < len(input_data):
        n = int(input_data[index])
        index += 1
        operations = input_data[index:index + n]
        index += n
        result = determine_structure(n, operations)
        print(result)
if __name__ == "__main__":
    main()