import heapq

max_heap = []  
resultados = []
    
while True:
    instruccion = input().strip()  
    partes = instruccion.split()
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
            x = int(partes[1])
            maximo = -heapq.heappop(max_heap)
            nuevo_valor = maximo + x
            heapq.heappush(max_heap, -nuevo_valor)
        else:
            resultados.append("Error")
        
    elif comando == 'D':
        if max_heap:
            x = int(partes[1])
            maximo = -heapq.heappop(max_heap)
            nuevo_valor = maximo - x
            heapq.heappush(max_heap, -nuevo_valor)
        else:
            resultados.append("Error")
        
    elif comando == 'T':
        break

for resultado in resultados:
    print(resultado)


