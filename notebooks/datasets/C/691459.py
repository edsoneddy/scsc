import heapq

def process_operations(operations):
    max_heap = []
    for operation in operations:
        if operation[0] == 'S':
            heapq.heappush(max_heap, -int(operation[2:]))
        elif operation == 'A':
            if not max_heap:
                print("Error")
            else:
                print(-max_heap[0])
        elif operation == 'R':
            if not max_heap:
                print("Error")
            else:
                heapq.heappop(max_heap)
        elif operation[0] == 'I':
            if not max_heap:
                print("Error")
            else:
                increment = int(operation[2:])
                heapq.heapreplace(max_heap, -(-max_heap[0] + increment))
        elif operation[0] == 'D':
            if not max_heap:
                print("Error")
            else:
                decrement = int(operation[2:])
                heapq.heapreplace(max_heap, -(-max_heap[0] - decrement))
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
