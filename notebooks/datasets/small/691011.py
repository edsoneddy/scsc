import heapq

def process_operations(operations):
    heap = []
    for operation in operations:
        if operation[0] == 'S':
            heapq.heappush(heap, -int(operation[2:]))
        elif operation == 'A':
            if not heap:
                print("Error")
            else:
                print(-heap[0])
        elif operation == 'R':
            if not heap:
                print("Error")
            else:
                heapq.heappop(heap)
        elif operation[0] == 'I':
            if not heap:
                print("Error")
            else:
                increment_value = int(operation[2:])
                heapq.heapreplace(heap, -(-heap[0] + increment_value))
        elif operation[0] == 'D':
            if not heap:
                print("Error")
            else:
                decrement_value = int(operation[2:])
                heapq.heapreplace(heap, -(-heap[0] - decrement_value))
        elif operation == 'T':
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
