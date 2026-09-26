from collections import deque
import heapq

def guess_structure(operations):
    # Simularemos las tres estructuras simultáneamente
    stack = []
    queue = deque()
    pq = []  # priority queue

    # Banderas para cada estructura
    could_be_stack = True
    could_be_queue = True
    could_be_pq = True

    # Procesar cada operación
    for op, x in operations:
        if op == 1:  # insertar
            stack.append(x)
            queue.append(x)
            heapq.heappush(pq, -x)  # Negativo para hacer max-heap
        else:  # op == 2, extraer
            # Verificar stack
            if could_be_stack:
                if not stack or stack[-1] != x:
                    could_be_stack = False
                else:
                    stack.pop()

            # Verificar queue
            if could_be_queue:
                if not queue or queue[0] != x:
                    could_be_queue = False
                else:
                    queue.popleft()

            # Verificar priority queue
            if could_be_pq:
                if not pq or -pq[0] != x:
                    could_be_pq = False
                else:
                    heapq.heappop(pq)

    # Contar cuántas estructuras coinciden
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
            n = int(input())  # Número de operaciones
            operations = []
            for _ in range(n):
                op, x = map(int, input().split())  # Leer operación e integer
                operations.append((op, x))
            print(guess_structure(operations))  # Llamar a la función para determinar la estructura
    except EOFError:
        pass


if __name__ == "__main__":  # Corregir el nombre del bloque principal
    solve()
