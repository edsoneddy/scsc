from collections import deque
import heapq

def main():
    while True:
        try:
            n = int(input())
            
            stack = []
            queue = deque()
            priority_queue = []
            is_stack = True
            is_queue = True
            is_priority_queue = True
            
            for _ in range(n):
                command, value = map(int, input().split())
                
                if command == 1: 
                    stack.append(value)
                    queue.append(value)
                    heapq.heappush(priority_queue, -value) 
                elif command == 2: 
                    if not stack and not queue and not priority_queue:
                        is_stack = is_queue = is_priority_queue = False
                        continue
    
                    if is_stack and stack and stack[-1] != value:
                        is_stack = False
                    if is_queue and queue and queue[0] != value:
                        is_queue = False
                    if is_priority_queue and priority_queue and -priority_queue[0] != value:
                        is_priority_queue = False
                 
                    if is_stack and stack and stack[-1] == value:
                        stack.pop()
                    if is_queue and queue and queue[0] == value:
                        queue.popleft()
                    if is_priority_queue and priority_queue and -priority_queue[0] == value:
                        heapq.heappop(priority_queue)
            
            if is_stack and not is_queue and not is_priority_queue:
                print("stack")
            elif not is_stack and is_queue and not is_priority_queue:
                print("queue")
            elif not is_stack and not is_queue and is_priority_queue:
                print("priority queue")
            elif not is_stack and not is_queue and not is_priority_queue:
                print("impossible")
            else:
                print("not sure")
        except EOFError:
            break

if __name__ == "__main__":
    main()
