import sys
import heapq

def main():
    input = sys.stdin.read
    data = input().split()
    
    i = 0
    while i < len(data):
        n = int(data[i])
        i += 1
        stack = []
        queue = []
        priority_queue = []
        
        is_stack = True
        is_queue = True
        is_priority_queue = True
        
        for _ in range(n):
            command = int(data[i])
            x = int(data[i + 1])
            i += 2
            
            if command == 1:
                stack.append(x)
                queue.append(x)
                heapq.heappush(priority_queue, -x)
            elif command == 2:
                if is_stack:
                    if stack and stack[-1] == x:
                        stack.pop()
                    else:
                        is_stack = False
                if is_queue:
                    if queue and queue[0] == x:
                        queue.pop(0)
                    else:
                        is_queue = False
                if is_priority_queue:
                    if priority_queue and -priority_queue[0] == x:
                        heapq.heappop(priority_queue)
                    else:
                        is_priority_queue = False
        
        if is_stack + is_queue + is_priority_queue == 0:
            print("impossible")
        elif is_stack + is_queue + is_priority_queue > 1:
            print("not sure")
        else:
            if is_stack:
                print("stack")
            elif is_queue:
                print("queue")
            elif is_priority_queue:
                print("priority queue")

if __name__ == "__main__":
    main()

