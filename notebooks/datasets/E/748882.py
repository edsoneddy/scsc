def adivinar_estructura(operaciones):
    stack = []  # Pila
    queue = []  # Cola
    priority_queue = []  # Cola de prioridad
    es_stack = True
    es_queue = True
    es_priority_queue = True

    for op in operaciones:
        if op[0] == 1:  # Inserción
            value = op[1]
            if es_stack:
                stack.append(value)
            if es_queue:
                queue.append(value)
            if es_priority_queue:
                priority_queue.append(value)
                priority_queue.sort()  # Mantener la cola de prioridad ordenada
        elif op[0] == 2:  # Extracción
            value = op[1]
            # Verificar stack
            if es_stack:
                if stack and stack[-1] == value:
                    stack.pop()
                else:
                    es_stack = False  # Invalida

            # Verificar queue
            if es_queue:
                if queue and queue[0] == value:
                    queue.pop(0)
                else:
                    es_queue = False  # Invalida

            # Verificar priority queue
            if es_priority_queue:
                if priority_queue and priority_queue[-1] == value:
                    priority_queue.pop()
                else:
                    es_priority_queue = False  # Invalida

    resultados = []
    if es_stack:
        resultados.append("stack")
    if es_queue:
        resultados.append("queue")
    if es_priority_queue:
        resultados.append("priority queue")

    if len(resultados) == 0:
        return "impossible"
    elif len(resultados) > 1:
        return "not sure"
    else:
        return resultados[0]

# Código sin mensajes adicionales
def main():
    while True:
        try:
            n = int(input().strip())
            operaciones = []
            for _ in range(n):
                comando = list(map(int, input().strip().split()))
                operaciones.append(comando)
            resultado = adivinar_estructura(operaciones)
            print(resultado)
        except EOFError:
            break  # Termina la ejecución al final del archivo

# Ejecutar la función principal
if __name__ == "__main__":
    main()
