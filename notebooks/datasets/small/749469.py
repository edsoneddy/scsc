import heapq
import sys

def procesar_operaciones(operaciones):
    heap = []
    resultados = []

    for operacion in operaciones:
        if operacion[0] == 'S':
            # Guardar el número en la heap como negativo
            _, x = operacion.split()
            x = int(x)
            heapq.heappush(heap, -x)

        elif operacion[0] == 'A':
            # Imprimir el número más grande
            if heap:
                resultados.append(-heap[0])  # El mayor es el mínimo en la min-heap de negativos
            else:
                resultados.append("Error")

        elif operacion[0] == 'R':
            # Extraer el número más grande
            if heap:
                heapq.heappop(heap)
            else:
                resultados.append("Error")

        elif operacion[0] == 'I':
            # Incrementar el número más grande
            if heap:
                _, x = operacion.split()
                x = int(x)
                maximo_actual = -heapq.heappop(heap)  # Sacamos el mayor
                maximo_actual += x
                heapq.heappush(heap, -maximo_actual)  # Lo reinserta incrementado
            else:
                resultados.append("Error")

        elif operacion[0] == 'D':
            # Decrementar el número más grande
            if heap:
                _, x = operacion.split()
                x = int(x)
                maximo_actual = -heapq.heappop(heap)  # Sacamos el mayor
                maximo_actual -= x
                heapq.heappush(heap, -maximo_actual)  # Lo reinserta decrementado
            else:
                resultados.append("Error")

        elif operacion[0] == 'T':
            # Terminar la entrada
            break

    return resultados

# Leer las operaciones de entrada
entrada = sys.stdin.read().strip().splitlines()
resultados = procesar_operaciones(entrada)

# Imprimir cada resultado en una línea
for resultado in resultados:
    print(resultado)
