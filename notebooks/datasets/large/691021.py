import heapq
from collections import deque

def identify_structure_operations(operations):
    is_stack = True
    is_queue = True
    is_priority_queue = True
    stack = []
    queue = deque()
    priority_queue = []

    for operation, value in operations:
        if operation == 1:
            stack.append(value)
            queue.append(value)
            heapq.heappush(priority_queue, -value)
        elif operation == 2:
            if not stack or stack.pop() != value:
                is_stack = False
            if not queue or queue.popleft() != value:
                is_queue = False
            if not priority_queue or -heapq.heappop(priority_queue) != value:
                is_priority_queue = False

    possibilities = [is_stack, is_queue, is_priority_queue]
    if sum(possibilities) == 0:
        return "impossible"
    elif sum(possibilities) > 1:
        return "not sure"
    elif is_stack:
        return "stack"
    elif is_queue:
        return "queue"
    elif is_priority_queue:
        return "priority queue"

while True:
    try:
        n = int(input().strip())
        operations = []
        for _ in range(n):
            operation, value = map(int, input().strip().split())
            operations.append((operation, value))

        result = identify_structure_operations(operations)
        print(result)
    except EOFError:
        break
    except ValueError:
        print("Invalid input. Please enter integers.")
