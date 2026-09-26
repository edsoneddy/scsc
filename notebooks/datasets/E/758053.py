import sys
from collections import deque
import heapq

def identify_structure(commands):
    # Simular las estructuras de datos
    stack = []
    queue = deque()
    priority_queue = []

    # Indicadores para cada estructura
    is_stack = True
    is_queue = True
    is_priority_queue = True

    for command, x in commands:
        if command == 1:
            # Operación de inserción
            stack.append(x)
            queue.append(x)
            heapq.heappush(priority_queue, -x)  # Usamos valores negativos para simular una cola de prioridad máxima
        elif command == 2:
            # Operación de extracción
            if is_stack:
                if not stack or stack.pop() != x:
                    is_stack = False
            if is_queue:
                if not queue or queue.popleft() != x:
                    is_queue = False
            if is_priority_queue:
                if not priority_queue or -heapq.heappop(priority_queue) != x:
                    is_priority_queue = False

    # Determinar el resultado basado en los indicadores
    results = []
    if is_stack:
        results.append("stack")
    if is_queue:
        results.append("queue")
    if is_priority_queue:
        results.append("priority queue")

    if len(results) == 0:
        return "impossible"
    elif len(results) > 1:
        return "not sure"
    else:
        return results[0]


def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    results = []

    while index < len(data):
        n = int(data[index])
        index += 1

        commands = []
        for _ in range(n):
            command, x = map(int, data[index].split())
            commands.append((command, x))
            index += 1

        results.append(identify_structure(commands))

    print("\n".join(results))

if __name__ == "__main__":
    main()
