import heapq

def procesar_operaciones():
    max_heap = []
    resultados = []
    
    while True:
        operacion = input().strip()
        partes = operacion.split()
        comando = partes[0]
        
        if comando == 'S':
            x = int(partes[1])
            heapq.heappush(max_heap, -x)
        
        elif comando == 'A':
            if max_heap:
                resultados.append(-max_heap[0])
            else:
                resultados.append("Error")
        
        elif comando == 'R':
            if max_heap:
                heapq.heappop(max_heap)
            else:
                resultados.append("Error")
        
        elif comando == 'I':
            if max_heap:
                incremento = int(partes[1])
                valor_mas_grande = -heapq.heappop(max_heap)
                nuevo_valor = valor_mas_grande + incremento
                heapq.heappush(max_heap, -nuevo_valor)
            else:
                resultados.append("Error")
        
        elif comando == 'D':
            if max_heap:
                decremento = int(partes[1])
                valor_mas_grande = -heapq.heappop(max_heap)
                nuevo_valor = valor_mas_grande - decremento
                heapq.heappush(max_heap, -nuevo_valor)
            else:
                resultados.append("Error")
        
        elif comando == 'T':
            break
    
    for resultado in resultados:
        print(resultado)

procesar_operaciones()
