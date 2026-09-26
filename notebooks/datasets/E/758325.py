from collections import deque
import heapq
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    i = 0
    while i < len(data):
        n = int(data[i])
        i += 1

        stack = []
        queue = deque()
        priority_queue = []
        is_stack = True
        is_queue = True
        is_priority_queue = True

        for _ in range(n):
            command, value = map(int, data[i].split())
            i += 1

            if command == 1:
                stack.append(value)
                queue.append(value)
                heapq.heappush(priority_queue, -value)  
            elif command == 2:
                if is_stack:
                    if stack and stack.pop() == value:
                        pass
                    else:
                        is_stack = False
                
                if is_queue:
                    if queue and queue.popleft() == value:
                        pass
                    else:
                        is_queue = False
                
                if is_priority_queue:
                    if priority_queue and -heapq.heappop(priority_queue) == value:
                        pass
                    else:
                        is_priority_queue = False
        count = sum([is_stack, is_queue, is_priority_queue])

        if count > 1:
            print("not sure")
        elif count == 0:
            print("impossible")
        elif is_stack:
            print("stack")
        elif is_queue:
            print("queue")
        elif is_priority_queue:
            print("priority queue")

if __name__ == "__main__":
    main()
