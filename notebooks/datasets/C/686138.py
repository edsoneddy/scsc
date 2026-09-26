import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, x):
        heapq.heappush(self.heap, -x)
    
    def pop(self):
        if self.heap:
            return -heapq.heappop(self.heap)
        else:
            return "Error"
    
    def top(self):
        if self.heap:
            return -self.heap[0]
        else:
            return "Error"
    
    def increment(self, x):
        if self.heap:
            max_elem = -heapq.heappop(self.heap)
            max_elem += x
            heapq.heappush(self.heap, -max_elem)
        else:
            return "Error"
    
    def decrement(self, x):
        if self.heap:
            max_elem = -heapq.heappop(self.heap)
            max_elem -= x
            heapq.heappush(self.heap, -max_elem)
        else:
            return "Error"

import sys
input = sys.stdin.read

def process_commands():
    max_heap = MaxHeap()
    commands = input().strip().split("\n")
    results = []
    
    for command in commands:
        parts = command.split()
        cmd = parts[0]
        if cmd == 'S':
            x = int(parts[1])
            max_heap.push(x)
        elif cmd == 'A':
            result = max_heap.top()
            if result == "Error":
                results.append("Error")
            else:
                results.append(result)
        elif cmd == 'R':
            result = max_heap.pop()
            if result == "Error":
                results.append("Error")
        elif cmd == 'I':
            x = int(parts[1])
            result = max_heap.increment(x)
            if result == "Error":
                results.append("Error")
        elif cmd == 'D':
            x = int(parts[1])
            result = max_heap.decrement(x)
            if result == "Error":
                results.append("Error")
        elif cmd == 'T':
            break
    
    for res in results:
        print(res)

if __name__ == "__main__":
    process_commands()
