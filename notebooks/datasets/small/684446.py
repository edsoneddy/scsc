import heapq
import sys

def process_operations(operations):
    max_heap = []
    results = []

    for operation in operations:
        if operation[0] == 'S':
            x = int(operation[1])
            heapq.heappush(max_heap, -x)
        elif operation[0] == 'A':
            if max_heap:
                results.append(-max_heap[0])
            else:
                results.append('Error')
        elif operation[0] == 'R':
            if max_heap:
                heapq.heappop(max_heap)
            else:
                results.append('Error')
        elif operation[0] == 'I':
            if max_heap:
                x = int(operation[1])
                largest = -heapq.heappop(max_heap)
                largest += x
                heapq.heappush(max_heap, -largest)
            else:
                results.append('Error')
        elif operation[0] == 'D':
            if max_heap:
                x = int(operation[1])
                largest = -heapq.heappop(max_heap)
                largest -= x
                heapq.heappush(max_heap, -largest)
            else:
                results.append('Error')
        elif operation[0] == 'T':
            break

    return results

def main():
    operations = []
    while True:
        try:
            line = input().strip()
            if line:
                operations.append(line.split())
            if line == 'T':
                break
        except EOFError:
            break

    results = process_operations(operations)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
