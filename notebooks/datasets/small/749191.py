import heapq
import sys
input = sys.stdin.read

def process_commands(commands):
    max_heap = []
    results = []

    for command in commands:
        parts = command.split()
        op = parts[0]
        
        if op == "S":
            # S x: guarda una copia de un número x
            x = int(parts[1])
            heapq.heappush(max_heap, -x)
        
        elif op == "A":
            # A: imprime el número más grande
            if max_heap:
                results.append(-max_heap[0])
            else:
                results.append("Error")
        
        elif op == "R":
            # R: extrae el número más grande
            if max_heap:
                heapq.heappop(max_heap)
            else:
                results.append("Error")
        
        elif op == "I":
            # I x: incrementa el número más grande en x
            if max_heap:
                x = int(parts[1])
                largest = -heapq.heappop(max_heap)
                largest += x
                heapq.heappush(max_heap, -largest)
            else:
                results.append("Error")
        
        elif op == "D":
            # D x: decrementa el número más grande en x
            if max_heap:
                x = int(parts[1])
                largest = -heapq.heappop(max_heap)
                largest -= x
                heapq.heappush(max_heap, -largest)
            else:
                results.append("Error")
        
        elif op == "T":
            # T: termina la entrada
            break

    return results

# Leer entrada y procesar
commands = input().strip().splitlines()
output = process_commands(commands)
print("\n".join(map(str, output)))

