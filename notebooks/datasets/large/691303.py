from sys import stdin
import heapq

def main():
    input = stdin.read
    data = input().strip().split()
    
    index = 0
    while index < len(data):
        n = int(data[index])
        index += 1
        
        stack = []
        queue = []
        priority_queue = []
        is_stack = True
        is_queue = True
        is_priority_queue = True
        
        for _ in range(n):
            type_ = int(data[index])
            value = int(data[index + 1])
            index += 2
            
            if type_ == 1:
                stack.append(value)
                queue.append(value)
                heapq.heappush(priority_queue, -value)
            else:
                if stack:
                    if stack.pop() != value:
                        is_stack = False
                else:
                    is_stack = False
                
                if queue:
                    if queue.pop(0) != value:
                        is_queue = False
                else:
                    is_queue = False
                
                if priority_queue:
                    if -heapq.heappop(priority_queue) != value:
                        is_priority_queue = False
                else:
                    is_priority_queue = False
        
        if (is_stack and is_queue) or (is_stack and is_priority_queue) or (is_queue and is_priority_queue):
            print("not sure")
        elif is_stack:
            print("stack")
        elif is_queue:
            print("queue")
        elif is_priority_queue:
            print("priority queue")
        else:
            print("impossible")

if __name__ == "__main__":
    main()
