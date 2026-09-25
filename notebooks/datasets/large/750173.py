from collections import deque
import heapq

def process_operations(n, operations):
    stack = []
    queue = deque()
    priority_queue = []
    is_stack = True
    is_queue = True
    is_pq = True
    
    for operation in operations:
        op, x = operation
        if op == 1:  # Insert operation
            stack.append(x)
            queue.append(x)
            heapq.heappush(priority_queue, -x)  # max heap by inserting negative values
        elif op == 2:  # Remove operation
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
            if is_pq:
                if priority_queue and -priority_queue[0] == x:
                    heapq.heappop(priority_queue)
                else:
                    is_pq = False
    
    if sum([is_stack, is_queue, is_pq]) > 1:
        return "not sure"
    elif is_stack:
        return "stack"
    elif is_queue:
        return "queue"
    elif is_pq:
        return "priority queue"
    else:
        return "impossible"

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    idx = 0
    while idx < len(data):
        n = int(data[idx])
        idx += 1
        operations = []
        for i in range(n):
            op, x = map(int, data[idx].split())
            operations.append((op, x))
            idx += 1
        print(process_operations(n, operations))

if __name__ == "__main__":
    main()
