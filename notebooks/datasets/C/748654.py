import heapq
from collections import Counter

class NumberCollection:
    def __init__(self):
        self.heap = []  # Max heap (we'll use negative numbers for max heap behavior)
        self.counter = Counter()  # To handle duplicates
        
    def store(self, x):
        # Store negative for max heap behavior
        heapq.heappush(self.heap, -x)
        self.counter[x] += 1
        
    def print_max(self):
        if not self.heap:
            print("Error")
            return
        # Print the actual (positive) number
        print(-self.heap[0])
        
    def remove_max(self):
        if not self.heap:
            print("Error")
            return
            
        max_num = -heapq.heappop(self.heap)
        self.counter[max_num] -= 1
        if self.counter[max_num] == 0:
            del self.counter[max_num]
            
    def increment(self, x):
        if not self.heap:
            print("Error")
            return
            
        # Remove old max
        old_max = -heapq.heappop(self.heap)
        self.counter[old_max] -= 1
        if self.counter[old_max] == 0:
            del self.counter[old_max]
            
        # Add incremented value
        new_max = old_max + x
        heapq.heappush(self.heap, -new_max)
        self.counter[new_max] += 1
        
    def decrement(self, x):
        if not self.heap:
            print("Error")
            return
            
        # Remove old max
        old_max = -heapq.heappop(self.heap)
        self.counter[old_max] -= 1
        if self.counter[old_max] == 0:
            del self.counter[old_max]
            
        # Add decremented value
        new_max = old_max - x
        heapq.heappush(self.heap, -new_max)
        self.counter[new_max] += 1

def main():
    collection = NumberCollection()
    
    while True:
        try:
            command = input().strip()
            if command == 'T':
                break
                
            parts = command.split()
            operation = parts[0]
            
            if operation == 'S':
                collection.store(int(parts[1]))
            elif operation == 'A':
                collection.print_max()
            elif operation == 'R':
                collection.remove_max()
            elif operation == 'I':
                collection.increment(int(parts[1]))
            elif operation == 'D':
                collection.decrement(int(parts[1]))
                
        except EOFError:
            break

if __name__ == "__main__":
    main()