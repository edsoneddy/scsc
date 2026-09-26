import heapq

def identificar_estructura(n, operaciones):
    stack = []
    queue = []
    priority_queue = []
    es_stack = True
    es_queue = True
    es_priority_queue = True

    for operacion in operaciones:
        tipo, x = operacion
        if tipo == 1:
            stack.append(x)
            queue.append(x)
            heapq.heappush(priority_queue, -x)
        elif tipo == 2:
            if es_stack:
                if not stack or stack.pop() != x:
                    es_stack = False
            if es_queue:
                if not queue or queue.pop(0) != x:
                    es_queue = False
            if es_priority_queue:
                if not priority_queue or -heapq.heappop(priority_queue) != x:
                    es_priority_queue = False

    if es_stack and not es_queue and not es_priority_queue:
        return "stack"
    elif not es_stack and es_queue and not es_priority_queue:
        return "queue"
    elif not es_stack and not es_queue and es_priority_queue:
        return "priority queue"
    elif not es_stack and not es_queue and not es_priority_queue:
        return "impossible"
    else:
        return "not sure"

def main():
    while True:
        try:
            n = int(input().strip())
            operaciones = []
            for _ in range(n):
                tipo, x = map(int, input().strip().split())
                operaciones.append((tipo, x))
            print(identificar_estructura(n, operaciones))
        except EOFError:
            break

if __name__ == "__main__":
    main()
