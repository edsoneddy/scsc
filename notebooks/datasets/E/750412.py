from collections import deque
import heapq

def test_stack(operations):
    stack = []
    for op, val in operations:
        if op == 1:
            stack.append(val)
        else:
            if not stack:
                return False
            if stack.pop() != val:
                return False
    return True

def test_queue(operations):
    queue = deque()
    for op, val in operations:
        if op == 1:
            queue.append(val)
        else:
            if not queue:
                return False
            if queue.popleft() != val:
                return False
    return True

def test_priority_queue(operations):
    pq = []
    for op, val in operations:
        if op == 1:
            heapq.heappush(pq, -val)  # Negative for max heap
        else:
            if not pq:
                return False
            if -heapq.heappop(pq) != val:
                return False
    return True

def determine_structure(operations):
    is_stack = test_stack(operations)
    is_queue = test_queue(operations)
    is_pq = test_priority_queue(operations)
    
    possible_structures = [x for x in [is_stack, is_queue, is_pq] if x]
    
    if len(possible_structures) == 0:
        return "impossible"
    elif len(possible_structures) > 1:
        return "not sure"
    else:
        if is_stack:
            return "stack"
        elif is_queue:
            return "queue"
        else:
            return "priority queue"

# Process input until EOF
while True:
    try:
        n = int(input())
        operations = []
        
        # Read n operations
        for _ in range(n):
            op_type, value = map(int, input().split())
            operations.append((op_type, value))
            
        # Print result
        print(determine_structure(operations))
        
    except EOFError:
        break