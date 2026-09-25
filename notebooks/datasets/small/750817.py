import heapq
import sys

max_heap = []
results = []

while True:
    line = input().strip()
    if line == "T":
        break

    command = line.split()
    operation = command[0]

    if operation == "S":
        x = int(command[1])
        heapq.heappush(max_heap, -x)

    elif operation == "A":
        if max_heap:
            results.append(-max_heap[0])
        else:
            results.append("Error")

    elif operation == "R":

        if max_heap:
            heapq.heappop(max_heap)
        else:
            results.append("Error")

    elif operation == "I":
        if max_heap:
            x = int(command[1])
            max_value = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -(max_value + x))
        else:
            results.append("Error")

    elif operation == "D":
        if max_heap:
            x = int(command[1])
            max_value = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -(max_value - x))
        else:
            results.append("Error")


for result in results:
    print(result)

