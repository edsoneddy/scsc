from collections import deque
import heapq

def process_case(n, operations):
    stack = []
    queue = deque()
    priority_queue = []
    is_stack = True
    is_queue = True
    is_pq = True
    
    for op in operations:
        cmd, x = op
        if cmd == 1:
            stack.append(x)
            queue.append(x)
            heapq.heappush(priority_queue, -x)
        elif cmd == 2:
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
    
    if is_stack + is_queue + is_pq > 1:
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
    data = input().splitlines()
    
    idx = 0
    while idx < len(data):
        n = int(data[idx])
        idx += 1
        operations = []
        for _ in range(n):
            cmd, x = map(int, data[idx].split())
            operations.append((cmd, x))
            idx += 1
        print(process_case(n, operations))


if __name__ == "__main__":
    main()