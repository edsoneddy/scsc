import heapq
import sys

def procesar_instrucciones(instrucciones):
    heap = []
    resultados = []
    
    for instruccion in instrucciones:
        if instruccion[0] == 'S':
            _, x = instruccion.split()
            x = int(x)
            heapq.heappush(heap, -x)
        elif instruccion[0] == 'A':
            if heap:
                resultados.append(-heap[0])
            else:
                resultados.append("Error")
        elif instruccion[0] == 'R':
            if heap:
                heapq.heappop(heap)
            else:
                resultados.append("Error")
        elif instruccion[0] == 'I':
            _, x = instruccion.split()
            x = int(x)
            if heap:
                max_val = -heapq.heappop(heap)
                heapq.heappush(heap, -(max_val + x))
            else:
                resultados.append("Error")
        elif instruccion[0] == 'D':
            _, x = instruccion.split()
            x = int(x)
            if heap:
                max_val = -heapq.heappop(heap)
                heapq.heappush(heap, -(max_val - x))
            else:
                resultados.append("Error")
        elif instruccion[0] == 'T':
            break
    
    return resultados

def main():
    instrucciones = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            instrucciones.append(line)
    
    resultados = procesar_instrucciones(instrucciones)
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()
