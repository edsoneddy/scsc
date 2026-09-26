from collections import deque
import heapq

def simulate_operations(operations):
    """
    Simula las operaciones en las tres estructuras de datos y compara resultados
    """
    # Inicializar estructuras
    stack = []  # Pila
    queue = deque()  # Cola
    pq = []  # Cola de prioridad
    
    # Almacenar resultados de operaciones tipo 2
    actual_outputs = []
    stack_outputs = []
    queue_outputs = []
    pq_outputs = []
    
    # Procesar cada operación
    for op_type, x in operations:
        if op_type == 1:  # Insertar
            stack.append(x)
            queue.append(x)
            heapq.heappush(pq, -x)  # Negativo para convertir min-heap en max-heap
        else:  # Sacar
            actual_outputs.append(x)
            
            if stack:
                stack_outputs.append(stack.pop())
            if queue:
                queue_outputs.append(queue.popleft())
            if pq:
                pq_outputs.append(-heapq.heappop(pq))
    
    # Verificar qué estructuras coinciden con los resultados
    is_stack = actual_outputs == stack_outputs
    is_queue = actual_outputs == queue_outputs
    is_pq = actual_outputs == pq_outputs
    
    # Determinar la respuesta
    matches = []
    if is_stack:
        matches.append("stack")
    if is_queue:
        matches.append("queue")
    if is_pq:
        matches.append("priority queue")
    
    if len(matches) == 0:
        return "impossible"
    elif len(matches) == 1:
        return matches[0]
    else:
        return "not sure"

def process_test_case():
    """
    Procesa un caso de prueba
    """
    n = int(input())
    operations = []
    
    # Leer operaciones
    for _ in range(n):
        op_type, x = map(int, input().split())
        operations.append((op_type, x))
    
    # Determinar e imprimir el resultado
    result = simulate_operations(operations)
    print(result)

# Procesar todos los casos de prueba
while True:
    try:
        process_test_case()
    except EOFError:
        break