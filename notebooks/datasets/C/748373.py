import heapq
import sys
input = sys.stdin.read
data = input().strip().splitlines()
max_heap = []
results = []

for line in data:
    if line.startswith('S'):
        _, x = line.split()
        x = int(x)
        heapq.heappush(max_heap, -x)
    elif line == 'A':
        if max_heap:
            results.append(-max_heap[0])
        else:
            results.append("Error")
    elif line == 'R':
        if max_heap:
            heapq.heappop(max_heap)
        else:
            results.append("Error")
    elif line.startswith('I'):
        _, x = line.split()
        x = int(x)
        if max_heap:
            max_val = -heapq.heappop(max_heap) + x
            heapq.heappush(max_heap, -max_val)
        else:
            results.append("Error")
    elif line.startswith('D'):
        _, x = line.split()
        x = int(x)
        if max_heap:
            max_val = -heapq.heappop(max_heap) - x
            heapq.heappush(max_heap, -max_val)
        else:
            results.append("Error")
    elif line == 'T':
        break
print('\n'.join(map(str, results)))