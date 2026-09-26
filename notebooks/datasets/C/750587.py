import heapq

def procesar_instrucciones():
    heap = []
    resultados = []

    while True:
        # Leer instrucción del usuario
        instruccion = input().strip()
        
        # Dividimos la instrucción en partes
        partes = instruccion.split()
        operacion = partes[0]
        
        if operacion == "S":
            # Guardar número en la cola (como valor negativo para simular max-heap)
            numero = int(partes[1])
            heapq.heappush(heap, -numero)
        
        elif operacion == "A":
            # Imprimir el número más grande
            if heap:
                maximo = -heap[0]
                resultados.append(maximo)
                print(maximo)
            else:
                resultados.append("Error")
                print("Error")
        
        elif operacion == "R":
            # Remover el número más grande
            if heap:
                heapq.heappop(heap)
            else:
                resultados.append("Error")
                print("Error")
        
        elif operacion == "I":
            # Incrementar el número más grande en x
            if heap:
                incremento = int(partes[1])
                maximo = -heapq.heappop(heap)
                heapq.heappush(heap, -(maximo + incremento))
            else:
                resultados.append("Error")
                print("Error")
        
        elif operacion == "D":
            # Decrementar el número más grande en x
            if heap:
                decremento = int(partes[1])
                maximo = -heapq.heappop(heap)
                heapq.heappush(heap, -(maximo - decremento))
            else:
                resultados.append("Error")
                print("Error")
        
        elif operacion == "T":
            # Terminar la entrada
            break

    return resultados

# Ejecutar la función para procesar las instrucciones introducidas por el usuario
procesar_instrucciones()
