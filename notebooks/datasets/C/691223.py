import heapq

def process_instructions():
    max_heap = []  # Use a max-heap to efficiently track the largest number

    while True:
        instruction = input().split()
        operation = instruction[0]

        if operation == "S":
            num = int(instruction[1])
            heapq.heappush(max_heap, -num)  # Store as negative for max-heap behavior
        elif operation == "A":
            if not max_heap:
                print("Error")  # Empty heap
            else:
                print(-max_heap[0])  # Print the largest (negated)
        elif operation == "R":
            if not max_heap:
                print("Error")
            else:
                heapq.heappop(max_heap)  # Remove the largest
        elif operation == "I" or operation == "D":
            if not max_heap:
                print("Error")
            else:
                num = int(instruction[1])
                largest = -heapq.heappop(max_heap)
                if operation == "I":
                    largest += num
                else:
                    largest -= num
                heapq.heappush(max_heap, -largest)  # Push back the modified largest
        elif operation == "T":
            break  # Terminate input

if __name__ == "__main__":
    process_instructions()
