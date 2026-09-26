import sys
from collections import deque
import heapq

def main():
    input = sys.stdin.read
    data = input().splitlines()
    index = 0
    results = []

    while index < len(data):
        n = int(data[index])
        index += 1
        operations = data[index:index + n]
        index += n

        stack = []
        queue = deque()
        priority_queue = []

        is_stack = True
        is_queue = True
        is_pq = True

        for operation in operations:
            op_type, x = map(int, operation.split())

            if op_type == 1:
                
                stack.append(x)
                queue.append(x)
                heapq.heappush(priority_queue, -x)  
            elif op_type == 2:
              
                if is_stack:
                    if stack and stack[-1] == x:
                        stack.pop()
                    else:
                        is_stack = False

                if is_queue:
                    if queue and queue[0] == x:
                        queue.popleft()
                    else:
                        is_queue = False

                if is_pq:
                    if priority_queue and -priority_queue[0] == x:
                        heapq.heappop(priority_queue)
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
