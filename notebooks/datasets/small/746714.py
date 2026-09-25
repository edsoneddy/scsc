import heapq

def procesar_instrucciones():
    heap = []  # Usamos un max-heap simulando con valores negativos
    resultados = []

    while True:
        operacion = input()  # Leer la operación del usuario

        if not operacion:  # Si no hay entrada, romper el bucle
            break

        instruccion = operacion[0]

        if instruccion == 'S':
            # Guardar el número `x` en el heap
            _, x = operacion.split()
            x = int(x)
            heapq.heappush(heap, -x)  # Insertar el valor negativo

        elif instruccion == 'A':
            # Mostrar el número más grande
            if heap:
                resultados.append(-heap[0])  # Devolver el valor positivo
            else:
                resultados.append("Error")

        elif instruccion == 'R':
            # Extraer el número más grande
            if heap:
                heapq.heappop(heap)  # Extraemos el mayor
            else:
                resultados.append("Error")

        elif instruccion == 'I':
            # Incrementar el número más grande
            if heap:
                _, x = operacion.split()
                x = int(x)
                max_value = -heapq.heappop(heap)  # Extraemos y convertimos a positivo
                max_value += x
                heapq.heappush(heap, -max_value)  # Volvemos a insertar
            else:
                resultados.append("Error")

        elif instruccion == 'D':
            # Decrementar el número más grande
            if heap:
                _, x = operacion.split()
                x = int(x)
                max_value = -heapq.heappop(heap)  # Extraemos y convertimos a positivo
                max_value -= x
                heapq.heappush(heap, -max_value)  # Volvemos a insertar
            else:
                resultados.append("Error")

        elif instruccion == 'T':
            # Terminar la ejecución
            break

    return resultados

# Ejemplo de uso
salida = procesar_instrucciones()
for resultado in salida:
    print(resultado)
