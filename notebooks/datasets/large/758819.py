import sys
from collections import deque

def process_operations(n, operations):
    stack = []
    queue = deque()
    priority_queue = []
    
    is_stack = True
    is_queue = True
    is_priority_queue = True

    for op in operations:
        cmd, x = op[0], op[1]
        if cmd == 1:
            stack.append(x)
            queue.append(x)
            priority_queue.append(x)
        elif cmd == 2:
            if not stack or not queue or not priority_queue:
                return "impossible"
            if is_stack:
                if stack.pop() != x:
                    is_stack = False
            if is_queue:
                if queue.popleft() != x:
                    is_queue = False
            if is_priority_queue:
                if max(priority_queue) != x:
                    is_priority_queue = False
                else:
                    priority_queue.remove(x)

    if is_stack and not is_queue and not is_priority_queue:
        return "stack"
    if is_queue and not is_stack and not is_priority_queue:
        return "queue"
    if is_priority_queue and not is_stack and not is_queue:
        return "priority queue"
    if is_stack or is_queue or is_priority_queue:
        return "not sure"
    return "impossible"

input = sys.stdin.read
data = input().splitlines()
i = 0
result = []

while i < len(data):
    n = int(data[i])
    i += 1
    operations = []
    for j in range(n):
        op = list(map(int, data[i + j].split()))
        operations.append(op)
    i += n
    result.append(process_operations(n, operations))

for res in result:
    print(res)
