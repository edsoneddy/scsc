import heapq

def procesar_operaciones(operaciones):
    max_heap = []
    resultados = []
    
    for operacion in operaciones:
        if operacion[0] == 'S':
            _, x = operacion
            x = int(x)
            heapq.heappush(max_heap, -x)
        elif operacion[0] == 'A':
            if max_heap:
                resultados.append(-max_heap[0])
            else:
                resultados.append('Error')
        elif operacion[0] == 'R':
            if max_heap:
                heapq.heappop(max_heap)
            else:
                resultados.append('Error')
        elif operacion[0] == 'I':
            if max_heap:
                x = int(operacion[1])
                max_element = -heapq.heappop(max_heap)
                max_element += x
                heapq.heappush(max_heap, -max_element)
            else:
                resultados.append('Error')
        elif operacion[0] == 'D':
            if max_heap:
                x = int(operacion[1])
                max_element = -heapq.heappop(max_heap)
                max_element -= x
                heapq.heappush(max_heap, -max_element)
            else:
                resultados.append('Error')
        elif operacion[0] == 'T':
            break
    
    return resultados

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    operaciones = [line.split() for line in data]
    
    resultados = procesar_operaciones(operaciones)
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()
