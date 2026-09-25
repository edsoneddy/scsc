import heapq
import sys

def main():
    max_heap = []
    
    input = sys.stdin.read().split()
    index = 0
    
    while index < len(input):
        operation = input[index]
        index += 1
        
        if operation == "T":
            break
        elif operation == "S":
            num = int(input[index])
            index += 1
            heapq.heappush(max_heap, -num)
        elif operation == "A":
            if max_heap:
                print(-max_heap[0])
            else:
                print("Error")
        elif operation == "R":
            if max_heap:
                heapq.heappop(max_heap)
            else:
                print("Error")
        elif operation == "I":
            increment = int(input[index])
            index += 1
            if max_heap:
                max_val = -heapq.heappop(max_heap)
                max_val += increment
                heapq.heappush(max_heap, -max_val)
            else:
                print("Error")
        elif operation == "D":
            decrement = int(input[index])
            index += 1
            if max_heap:
                max_val = -heapq.heappop(max_heap)
                max_val -= decrement
                heapq.heappush(max_heap, -max_val)
            else:
                print("Error")

if __name__ == "__main__":
    main()
