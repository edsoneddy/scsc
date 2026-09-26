import sys
import heapq
def procesar(entrada):
    max_heap = []
    resultados = []
    for linea in entrada.splitlines():
        if linea.startswith("S"):
            _, x = linea.split()
            x = int(x)
            heapq.heappush(max_heap, -x)
        elif linea == "A":
            if max_heap:
                resultados.append(-max_heap[0])
            else:
                resultados.append("Error")
        elif linea == "R":
            if max_heap:
                heapq.heappop(max_heap)
            else:
                resultados.append("Error")
        elif linea.startswith("I"):
            _, x = linea.split()
            x = int(x)
            if max_heap:
                max_val = -heapq.heappop(max_heap)
                max_val += x
                heapq.heappush(max_heap, -max_val)
            else:
                resultados.append("Error")
        elif linea.startswith("D"):
            _, x = linea.split()
            x = int(x)
            if max_heap:
                max_val = -heapq.heappop(max_heap)
                max_val -= x
                heapq.heappush(max_heap, -max_val)
            else:
                resultados.append("Error")
        elif linea == "T":
            break
    return resultados
def main():
    entrada = sys.stdin.read()
    resultados = procesar(entrada)
    for resultado in resultados:
        print(resultado)
if __name__ == "__main__":
    main()
