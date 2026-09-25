from collections import deque
import heapq
 
def guess_structure(operations):
    stack = []
    queue = deque()
    pq = [] 

    could_be_stack = True
    could_be_queue = True
    could_be_pq = True
    
    actual_outputs = [] 
    
    for op, x in operations:
        if op == 1:  
            stack.append(x)
            queue.append(x)
            heapq.heappush(pq, -x)
        else: 
            actual_outputs.append(x)

            if stack and stack[-1] != x:
                could_be_stack = False
            if stack:
                stack.pop()

            if queue and queue[0] != x:
                could_be_queue = False
            if queue:
                queue.popleft()
                
            if pq and -heapq.heappop(pq) != x:
                could_be_pq = False
    
    possible_structures = sum([could_be_stack, could_be_queue, could_be_pq])
    
    if possible_structures == 0:
        return "impossible"
    elif possible_structures > 1:
        return "not sure"
    else:
        if could_be_stack:
            return "stack"
        if could_be_queue:
            return "queue"
        if could_be_pq:
            return "priority queue"
 
def solve():
    try:
        while True:
            n = int(input())
            operations = []
            for _ in range(n):
                op, x = map(int, input().split())
                operations.append((op, x))
            print(guess_structure(operations))
    except EOFError:
        pass
 
if __name__ == "__main__":
    solve()