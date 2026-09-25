import heapq
import sys

def process_operations(operations):
    max_heap = []
    results = []

    for operation in operations:
        if operation[0] == 'S':
            # Guardar el número en el heap
            x = int(operation[1])
            heapq.heappush(max_heap, -x)
        elif operation[0] == 'A':
            # Imprimir el número más grande
            if max_heap:
                results.append(-max_heap[0])
            else:
                results.append("Error")
        elif operation[0] == 'R':
            # Extraer el número más grande
            if max_heap:
                heapq.heappop(max_heap)
            else:
                results.append("Error")
        elif operation[0] == 'I':
            # Incrementar el número más grande
            if max_heap:
                x = int(operation[1])
                max_value = -heapq.heappop(max_heap)
                heapq.heappush(max_heap, -(max_value + x))
            else:
                results.append("Error")
        elif operation[0] == 'D':
            # Decrementar el número más grande
            if max_heap:
                x = int(operation[1])
                max_value = -heapq.heappop(max_heap)
                heapq.heappush(max_heap, -(max_value - x))
            else:
                results.append("Error")
        elif operation[0] == 'T':
            # Terminar la entrada
            break

    return results

def main():
    operations = []
    for line in sys.stdin:
        if line.strip() == 'T':
            operations.append(['T'])
            break
        operations.append(line.strip().split())

    results = process_operations(operations)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
