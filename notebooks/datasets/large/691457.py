import sys
import heapq

input = sys.stdin.read
data = input().split()

index = 0

while index < len(data):
    n = int(data[index])
    index += 1

    is_stack = True
    is_queue = True
    is_priority_queue = True

    stack = []
    queue = []
    priority_queue = []

    for _ in range(n):
        operation_type = int(data[index])
        x = int(data[index + 1])
        index += 2

        if operation_type == 1:
            if is_stack:
                stack.append(x)
            if is_queue:
                queue.append(x)
            if is_priority_queue:
                heapq.heappush(priority_queue, -x)
        elif operation_type == 2:
            if is_stack:
                if not stack or stack.pop() != x:
                    is_stack = False
            if is_queue:
                if not queue or queue.pop(0) != x:
                    is_queue = False
            if is_priority_queue:
                if not priority_queue or -heapq.heappop(priority_queue) != x:
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
