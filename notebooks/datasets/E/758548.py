import sys
import heapq
 
def main():
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    index = 0
    results = []
    
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
            command = data[index].split()
            index += 1
            op = int(command[0])
            if op == 1:
                x = int(command[1])
                stack.append(x)
                queue.append(x)
                heapq.heappush(priority_queue, -x)
            elif op == 2:
                x = int(command[1])
                
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
        
        count_valid = is_stack + is_queue + is_priority_queue
        
        if count_valid == 0:
            results.append("impossible")
        elif count_valid > 1:
            results.append("not sure")
        else:
            if is_stack:
                results.append("stack")
            elif is_queue:
                results.append("queue")
            elif is_priority_queue:
                results.append("priority queue")
    
    for result in results:
        print(result)
 
if __name__ == "__main__":
    main()