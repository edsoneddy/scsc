import sys
from collections import deque
import heapq

input = sys.stdin.read
data = [line.strip() for line in input().splitlines() if line.strip()]

i = 0
resultados = []

while i < len(data):
    try:
        n = int(data[i])
    except ValueError:
        break  # Termina si hay un fin de archivo inesperado o línea inválida
    i += 1

    stack = []
    queue = deque()
    priority_queue = []
    is_stack = is_queue = is_priority_queue = True

    for _ in range(n):
        operacion, x = map(int, data[i].split())
        i += 1

        if operacion == 1:
            stack.append(x)
            queue.append(x)
            heapq.heappush(priority_queue, -x)
        elif operacion == 2:
            if is_stack:
                if not stack or stack.pop() != x:
                    is_stack = False
            if is_queue:
                if not queue or queue.popleft() != x:
                    is_queue = False
            if is_priority_queue:
                if not priority_queue or -heapq.heappop(priority_queue) != x:
                    is_priority_queue = False

    if is_stack + is_queue + is_priority_queue > 1:
        resultados.append("not sure")
    elif is_stack:
        resultados.append("stack")
    elif is_queue:
        resultados.append("queue")
    elif is_priority_queue:
        resultados.append("priority queue")
    else:
        resultados.append("impossible")

for resultado in resultados:
    print(resultado)
