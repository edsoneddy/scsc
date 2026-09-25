import sys
from collections import deque
import heapq

def determinar_estructura(comandos):
    stack = []
    queue = deque()
    priority_queue = []

    es_stack = True
    es_queue = True
    es_priority_queue = True

    for comando in comandos:
        tipo, x = comando
        if tipo == 1:
            stack.append(x)
            queue.append(x)
            heapq.heappush(priority_queue, -x)  

        elif tipo == 2:
            if es_stack:
                if not stack or stack.pop() != x:
                    es_stack = False

            if es_queue:
                if not queue or queue.popleft() != x:
                    es_queue = False

            if es_priority_queue:
                if not priority_queue or -heapq.heappop(priority_queue) != x:
                    es_priority_queue = False
    posibles = sum([es_stack, es_queue, es_priority_queue])
    if posibles > 1:
        return "not sure"
    elif es_stack:
        return "stack"
    elif es_queue:
        return "queue"
    elif es_priority_queue:
        return "priority queue"
    else:
        return "impossible"

entrada = sys.stdin.read().strip().split("\n")
i = 0
resultados = []

while i < len(entrada):
    n = int(entrada[i])
    i += 1
    comandos = []
    
    for _ in range(n):
        tipo, x = map(int, entrada[i].split())
        comandos.append((tipo, x))
        i += 1
    resultado = determinar_estructura(comandos)
    resultados.append(resultado)

print("\n".join(resultados))
