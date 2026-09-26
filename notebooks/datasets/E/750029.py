import sys
import heapq

def adivina_la_estructura(operaciones):
    # Estructuras de datos simuladas
    stack = []
    queue = []
    priority_queue = []
    
    # Banderas para determinar qué estructura es válida
    is_stack = True
    is_queue = True
    is_priority_queue = True
    
    for operacion in operaciones:
        tipo, x = operacion
        
        if tipo == 1:
            # Operación de inserción en las tres estructuras
            stack.append(x)
            queue.append(x)
            heapq.heappush(priority_queue, -x)  # Insertamos como negativo para simular max-heap
            
        elif tipo == 2:
            # Si cualquiera de las estructuras está vacía, ya no puede ser esa estructura
            if is_stack:
                if not stack or stack.pop() != x:
                    is_stack = False
            if is_queue:
                if not queue or queue.pop(0) != x:
                    is_queue = False
            if is_priority_queue:
                if not priority_queue or -heapq.heappop(priority_queue) != x:
                    is_priority_queue = False
    
    # Determinamos el resultado final
    posibles = sum([is_stack, is_queue, is_priority_queue])
    if posibles > 1:
        return "not sure"
    elif posibles == 1:
        if is_stack:
            return "stack"
        elif is_queue:
            return "queue"
        elif is_priority_queue:
            return "priority queue"
    else:
        return "impossible"

# Procesamiento de la entrada
input = sys.stdin.read().strip().splitlines()
i = 0
resultados = []
while i < len(input):
    n = int(input[i])
    i += 1
    operaciones = []
    for _ in range(n):
        operacion = list(map(int, input[i].split()))
        operaciones.append(operacion)
        i += 1
    # Almacenar el resultado para el caso actual
    resultados.append(adivina_la_estructura(operaciones))

# Imprimir todos los resultados de los casos de prueba
for resultado in resultados:
    print(resultado)
