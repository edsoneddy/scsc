import heapq
import sys

def process_commands(commands):
    max_heap = []
    results = []
    
    for command in commands:
        parts = command.split()
        op = parts[0]
        
        if op == 'S':
            x = int(parts[1])
            heapq.heappush(max_heap, -x)
        elif op == 'A':
            if max_heap:
                results.append(-max_heap[0])
            else:
                results.append('Error')
        elif op == 'R':
            if max_heap:
                heapq.heappop(max_heap)
            else:
                results.append('Error')
        elif op == 'I':
            if max_heap:
                x = int(parts[1])
                max_value = -heapq.heappop(max_heap)
                max_value += x
                heapq.heappush(max_heap, -max_value)
            else:
                results.append('Error')
        elif op == 'D':
            if max_heap:
                x = int(parts[1])
                max_value = -heapq.heappop(max_heap)
                max_value -= x
                heapq.heappush(max_heap, -max_value)
            else:
                results.append('Error')
        elif op == 'T':
            break
    
    return results

input = sys.stdin.read
data = input().splitlines()

results = process_commands(data)

for result in results:
    print(result)
