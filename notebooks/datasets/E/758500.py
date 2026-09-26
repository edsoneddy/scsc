import sys
import heapq
from collections import deque

def determine_structure(operations):
    stack, queue, priority_queue = [], deque(), []
    is_stack, is_queue, is_pq = True, True, True

    for operation in operations:
        op_type, x = map(int, operation.split())
        if op_type == 1:
            stack.append(x)
            queue.append(x)
            heapq.heappush(priority_queue, -x)
        elif op_type == 2:
            if is_stack:
                is_stack = stack and stack.pop() == x
            if is_queue:
                is_queue = queue and queue.popleft() == x
            if is_pq:
                is_pq = priority_queue and -heapq.heappop(priority_queue) == x

    if is_stack + is_queue + is_pq > 1:
        return "not sure"
    if is_stack:
        return "stack"
    if is_queue:
        return "queue"
    if is_pq:
        return "priority queue"
    return "impossible"

def main():
    input = sys.stdin.read
    data = input().splitlines()
    index = 0
    results = []

    while index < len(data):
        n = int(data[index])
        index += 1
        operations = data[index:index + n]
        index += n
        results.append(determine_structure(operations))

    print("\n".join(results))

if __name__ == "__main__":
    main()
