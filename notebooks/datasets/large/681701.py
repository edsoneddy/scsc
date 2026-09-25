import heapq

def detect_data_structure(commands):
    stack = []
    queue = []
    priority_queue = []
    is_stack = True
    is_queue = True
    is_priority_queue = True

    for command, x in commands:
        if command == 1:  # Insertar elemento
            stack.append(x)
            queue.append(x)
            heapq.heappush(priority_queue, -x)  # Usamos negativos para simular una cola de máximos
        elif command == 2:  # Sacar elemento
            if is_stack:
                if not stack or stack.pop() != x:
                    is_stack = False
            if is_queue:
                if not queue or queue.pop(0) != x:
                    is_queue = False
            if is_priority_queue:
                if not priority_queue or -heapq.heappop(priority_queue) != x:
                    is_priority_queue = False

    # Determinación del tipo de estructura de datos
    possible = [is_stack, is_queue, is_priority_queue].count(True)
    if possible > 1:
        return "not sure"
    elif possible == 0:
        return "impossible"
    else:
        if is_stack:
            return "stack"
        elif is_queue:
            return "queue"
        elif is_priority_queue:
            return "priority queue"

def main():
    print( end="")
    for line in sys.stdin:
        n = int(line.strip())
        commands = []
        for _ in range(n):
            print(end="")
            op, x = map(int, input().strip().split())
            commands.append((op, x))
        result = detect_data_structure(commands)
        print(result)
        print(end="")

if __name__ == "__main__":
    import sys
    main()
