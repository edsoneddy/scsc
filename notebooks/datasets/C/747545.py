import heapq

def procesar_instrucciones(instrucciones):
    heap = []
    resultados = []

    for instruccion in instrucciones:
        operacion = instruccion.split()
        comando = operacion[0]

        if comando == 'S':
            heapq.heappush(heap, -int(operacion[1]))

        elif comando == 'A':
            resultados.append(-heap[0] if heap else "Error")

        elif comando == 'R':
            if heap:
                heapq.heappop(heap)
            else:
                resultados.append("Error")

        elif comando in ('I', 'D'):
            if heap:
                x = int(operacion[1])
                max_val = -heapq.heappop(heap)
                max_val = max_val + x if comando == 'I' else max_val - x
                heapq.heappush(heap, -max_val)
            else:
                resultados.append("Error")

        elif comando == 'T':
            break

    return resultados

instrucciones = []
while True:
    instruccion = input().strip()
    instrucciones.append(instruccion)
    if instruccion == 'T':
        break

resultado = procesar_instrucciones(instrucciones)

print("\n".join(map(str, resultado)))
