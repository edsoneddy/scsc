from queue import PriorityQueue
def determine_structure(n, ope):
    stack_structure = True
    queue_structure = True
    priority_queue_structure = True
    stack = []
    queue = []
    priority_queue = PriorityQueue()
    for op in ope:
        op_type, value = op.split()
        if op_type == '1':
            value = int(value)
            stack.append(value)
            queue.append(value)
            priority_queue.put(-value)
        elif op_type == '2':
            value = int(value)
            if not stack or stack.pop() != value:
                stack_structure = False
            if not queue or queue.pop(0) != value:
                queue_structure = False
            if not priority_queue.empty() and -priority_queue.get() != value:
                priority_queue_structure = False

    # Determinar la estructura de datos
    if stack_structure and not queue_structure and not priority_queue_structure:
        return "stack"
    elif not stack_structure and queue_structure and not priority_queue_structure:
        return "queue"
    elif not stack_structure and not queue_structure and priority_queue_structure:
        return "priority queue"
    elif not stack_structure and not queue_structure and not priority_queue_structure:
        return "impossible"
    else:
        return "not sure"
while True:
    try:
        n = int(input())
        ope = [input() for _ in range(n)]
        print(determine_structure(n, ope))
    except EOFError:
        break
