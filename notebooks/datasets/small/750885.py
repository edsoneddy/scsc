import heapq

def procesar_instrucciones():
    max_heap = []

    while True:
        try:
            instruccion = input().strip().split()
            operacion = instruccion[0]

            if operacion == "S" and len(instruccion) == 2:
                # Guardar un número
                x = int(instruccion[1])
                heapq.heappush(max_heap, -x)  # Insertar como negativo para simular max-heap

            elif operacion == "A":
                # Imprimir el máximo
                if max_heap:
                    print(-max_heap[0])  # Mostrar el número más grande
                else:
                    print("Error")

            elif operacion == "R":
                # Extraer el máximo
                if max_heap:
                    heapq.heappop(max_heap)  # Extraer el más grande
                else:
                    print("Error")

            elif operacion == "I" and len(instruccion) == 2:
                # Incrementar el máximo
                if max_heap:
                    x = int(instruccion[1])
                    max_valor = -heapq.heappop(max_heap)  # Extraer el más grande
                    nuevo_valor = max_valor + x
                    heapq.heappush(max_heap, -nuevo_valor)  # Insertar el valor incrementado
                else:
                    print("Error")

            elif operacion == "D" and len(instruccion) == 2:
                # Decrementar el máximo
                if max_heap:
                    x = int(instruccion[1])
                    max_valor = -heapq.heappop(max_heap)  # Extraer el más grande
                    nuevo_valor = max_valor - x
                    heapq.heappush(max_heap, -nuevo_valor)  # Insertar el valor decrementado
                else:
                    print("Error")

            elif operacion == "T":
                # Terminar inmediatamente
                break

            # Ignorar cualquier otra instrucción no válida
        except (ValueError, IndexError):
            continue

# Llamada a la función principal
procesar_instrucciones()
