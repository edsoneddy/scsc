import sys
import heapq

def determine_structure(commands):
    stack = []
    queue = []
    priority_queue = []

    possible_stack = True
    possible_queue = True
    possible_priority_queue = True

    for command in commands:
        op, x = command
        if op == 1:
            stack.append(x)
            queue.append(x)
            heapq.heappush(priority_queue, -x)  # Usamos -x para simular una cola de prioridad max-heap
        elif op == 2:
            if possible_stack:
                if stack and stack[-1] == x:
                    stack.pop()
                else:
                    possible_stack = False
            if possible_queue:
                if queue and queue[0] == x:
                    queue.pop(0)
                else:
                    possible_queue = False
            if possible_priority_queue:
                if priority_queue and -priority_queue[0] == x:
                    heapq.heappop(priority_queue)
                else:
                    possible_priority_queue = False

    if possible_stack and not (possible_queue or possible_priority_queue):
        return "stack"
    if possible_queue and not (possible_stack or possible_priority_queue):
        return "queue"
    if possible_priority_queue and not (possible_stack or possible_queue):
        return "priority queue"
    if possible_stack or possible_queue or possible_priority_queue:
        return "not sure"
    return "impossible"

def main():
    input = sys.stdin.read
    data = input().strip().split()
    i = 0

    while i < len(data):
        n = int(data[i])
        i += 1
        commands = []
        for _ in range(n):
            op = int(data[i])
            x = int(data[i+1])
            commands.append((op, x))
            i += 2
        print(determine_structure(commands))

if __name__ == "__main__":
    main()
