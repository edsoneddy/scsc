import heapq

def guess_structure(operaciones):
    stack_posible = True
    queue_posible = True
    pq_posible = True

    stack = []
    queue = []
    pq = []
    for op, num in operaciones:
        if op == 1:
            stack.append(num)
            queue.append(num)
            heapq.heappush(pq, -num) 
        else:
            if not stack or stack.pop() != num:
                stack_posible = False
            if not queue or queue.pop(0) != num:
                queue_posible = False
            if not pq or -heapq.heappop(pq) != num:
                pq_posible = False

    if stack_posible and not queue_posible and not pq_posible:
        return "stack"
    elif not stack_posible and queue_posible and not pq_posible:
        return "queue"
    elif not stack_posible and not queue_posible and pq_posible:
        return "priority queue"
    elif not stack_posible and not queue_posible and not pq_posible:
        return "impossible"
    else:
        return "not sure"

while True:
    try:
        n = int(input())
        operaciones = [list(map(int, input().split())) for _ in range(n)]
        resultado = guess_structure(operaciones)
        print(resultado)
    except EOFError:
        break

# La complejidad del código es O(n)