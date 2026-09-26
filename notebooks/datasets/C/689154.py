import heapq

def process_operations(operations):
    heap = []
    for op in operations:
        if op == 'A':
            if not heap:
                print("Error")
            else:
                print(-heap[0])
        elif op == 'R':
            if not heap:
                print("Error")
            else:
                heapq.heappop(heap)
        elif op[0] == 'S':
            heapq.heappush(heap, -int(op[2:]))
        elif op[0] == 'I':
            if not heap:
                print("Error")
            else:
                value = int(op[2:])
                heapq.heapreplace(heap, -(-heap[0] + value))
        elif op[0] == 'D':
            if not heap:
                print("Error")
            else:
                value = int(op[2:])
                heapq.heapreplace(heap, -(-heap[0] - value))
        elif op == 'T':
            break


operations = []
while True:
    try:
        operation = input().strip()
        if operation == 'T':
            break
        operations.append(operation)
    except EOFError:
        break

process_operations(operations)
