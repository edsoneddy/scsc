import sys
import heapq

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    results = []
    
    while index < len(data):
        n = int(data[index])
        index += 1
        
        is_stack = True
        is_queue = True
        is_pq = True
        
        stack = []
        queue = []
        pq = []
        
        for _ in range(n):
            command = int(data[index])
            x = int(data[index + 1])
            index += 2
            
            if command == 1:
                if is_stack:
                    stack.append(x)
                if is_queue:
                    queue.append(x)
                if is_pq:
                    heapq.heappush(pq, -x)  # Use negative to simulate max-heap
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
                if is_pq:
                    if pq and -heapq.heappop(pq) == x:
                        pass
                    else:
                        is_pq = False
        
        if is_stack and not is_queue and not is_pq:
            results.append("stack")
        elif not is_stack and is_queue and not is_pq:
            results.append("queue")
        elif not is_stack and not is_queue and is_pq:
            results.append("priority queue")
        elif not is_stack and not is_queue and not is_pq:
            results.append("impossible")
        else:
            results.append("not sure")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
