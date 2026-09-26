import sys
from collections import deque
import heapq

for linea in sys.stdin:
    n = int(linea)
    stack = []
    queue = deque()
    priority_queue = []
    is_stack = True
    is_queue = True
    is_pq = True
    for _ in range(n):
        tipo, valor = map(int,sys.stdin.readline().split())
        if tipo == 1:
            stack.append(valor)
            queue.append(valor)
            heapq.heappush(priority_queue, -valor)
        else:
            if stack:
                p1 = stack.pop()
                is_stack &= (p1 == valor)
            if queue:
                p1 = queue.popleft()
                is_queue &= (p1 == valor)
            if priority_queue:
                p1 = -heapq.heappop(priority_queue)
                is_pq &= (p1 == valor)
    p = 1 if is_stack else 0
    c = 1 if is_queue else 0
    cp1 = 1 if is_pq else 0
    suma = p + c + cp1    
    if suma == 0:
        print("impossible")
    elif suma == 1:
        if p == 1:
            print("stack")
        elif c == 1:
            print("queue")
        else:
            print("priority queue")
    else:
        print("not sure")