import heapq
 
def identificar_estructura(n, v):
    stack = []
    queue = []
    priority_queue = []
    es_stack = True
    es_queue = True
    es_priority_queue = True
 
    for operacion in v:
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
            v = []
            for _ in range(n):
                t, x = map(int, input().strip().split())
                v.append((t, x))
            print(identificar_estructura(n, v))
        except EOFError:
            break
 
if __name__ == "__main__":
    main()
